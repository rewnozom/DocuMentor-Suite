# markdown_analyzer/analyzer.py
from typing import List, Dict, Optional
from pathlib import Path
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

from .core.document import DocumentStructure
from .extractors import (
    MetadataExtractor,
    CompatibilityExtractor,
    TechnicalExtractor,
    ImageExtractor,
    PackagingExtractor
)
from .trainers import (
    BasicInfoTrainer,
    SummaryTrainer,
    TechnicalTrainer,
    CompatibilityTrainer
)
from .utils import (
    TextProcessor,
    DataValidator,
    setup_logging,
    find_markdown_files
)

class MarkdownAnalyzer:
    """
    Huvudklass som koordinerar analysen av markdown-dokument och generering av träningsdata.
    """
    
    def __init__(self, debug: bool = False):
        # Konfigurera loggning
        setup_logging(debug)
        self.logger = logging.getLogger(__name__)
        
        # Initiera extraktorer
        self.metadata_extractor = MetadataExtractor()
        self.compatibility_extractor = CompatibilityExtractor()
        self.technical_extractor = TechnicalExtractor()
        self.image_extractor = ImageExtractor()
        self.packaging_extractor = PackagingExtractor()
        
        # Initiera trainers
        self.trainers = {
            'f': BasicInfoTrainer(),
            's': SummaryTrainer(),
            't': TechnicalTrainer(),
            'c': CompatibilityTrainer()
        }
        
        # Status och resultat
        self.documents: List[DocumentStructure] = []
        self.errors: List[str] = []
        self.processed_files: set = set()
        
        # Hjälpklasser
        self.text_processor = TextProcessor()
        self.validator = DataValidator()

    def process_directory(self, input_dir: str, num_workers: int = 4) -> None:
        """
        Processar alla markdown-filer i en katalog och dess underkataloger.
        """
        self.logger.info(f"Börjar processera katalog: {input_dir}")
        
        # Hitta alla markdown-filer
        files = find_markdown_files([input_dir])
        if not files:
            self.logger.warning("Inga markdown-filer hittades")
            return
        
        self.logger.info(f"Hittade {len(files)} markdown-filer")
        
        # Processa filer parallellt
        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            future_to_file = {
                executor.submit(self.process_file, file): file 
                for file in files
            }
            
            with tqdm(total=len(files), desc="Processerar filer") as pbar:
                for future in as_completed(future_to_file):
                    file = future_to_file[future]
                    try:
                        result = future.result()
                        if result:
                            self.documents.append(result)
                    except Exception as e:
                        self.logger.error(f"Fel vid processering av {file}: {str(e)}")
                        self.errors.append(f"Fil: {file}, Fel: {str(e)}")
                    finally:
                        pbar.update(1)
        
        self.logger.info(f"Processering klar. {len(self.documents)} dokument analyserade.")
        if self.errors:
            self.logger.warning(f"Påträffade {len(self.errors)} fel under processering.")

    def process_file(self, filepath: Path) -> Optional[DocumentStructure]:
        """
        Processar en enskild markdown-fil och extraherar all relevant information.
        """
        if str(filepath) in self.processed_files:
            self.logger.debug(f"Fil redan processerad: {filepath}")
            return None
        
        try:
            self.logger.debug(f"Börjar processera fil: {filepath}")
            
            # Läs filinnehåll
            content = filepath.read_text(encoding='utf-8')
            
            # Extrahera grundläggande metadata
            article_number = self.metadata_extractor.extract_article_number(
                filepath.name, content
            )
            product_name = self.metadata_extractor.extract_product_name(content)
            document_type = self.metadata_extractor.extract_document_type(filepath.name)
            
            # Dela upp innehållet i sektioner
            sections = self.text_processor.extract_sections(content)
            
            # Skapa grundläggande dokumentstruktur
            doc = DocumentStructure(
                filename=filepath.name,
                article_number=article_number,
                document_type=document_type,
                product_name=product_name,
                description=self.metadata_extractor.extract_description(content),
                manufacturer=self.metadata_extractor.extract_manufacturer(content)
            )
            
            # Extrahera all information
            doc.product_images = self.image_extractor.extract(content, article_number)
            doc.compatibility = self.compatibility_extractor.extract(content, sections)
            doc.technical_specs = self.technical_extractor.extract(content, doc.tables)
            doc.sections = sections
            
            # Validera dokumentet
            validation_errors = self.validator.validate_document(doc)
            if validation_errors:
                for error in validation_errors:
                    self.logger.warning(f"Validieringsfel för {filepath.name}: {error}")
                doc.processing_errors.extend(validation_errors)
            
            # Markera som processerad
            self.processed_files.add(str(filepath))
            
            return doc
            
        except Exception as e:
            self.logger.error(f"Fel vid processering av {filepath}: {str(e)}")
            self.errors.append(f"Fil: {filepath}, Fel: {str(e)}")
            return None

    def generate_training_data(self, output_dir: str, commands: List[str] = None) -> None:
        """
        Genererar träningsdata för specificerade kommandon.
        """
        if commands is None:
            commands = list(self.trainers.keys())
        
        self.logger.info(f"Genererar träningsdata för kommandon: {commands}")
        
        all_examples = []
        
        # Generera träningsexempel för varje dokument och kommando
        for doc in self.documents:
            for cmd in commands:
                if cmd in self.trainers:
                    trainer = self.trainers[cmd]
                    examples = trainer.create_training_data(doc)
                    if examples:
                        all_examples.extend(examples)
        
        # Validera alla exempel
        for example in all_examples:
            if not self.trainers[example.command].validate_example(example):
                self.logger.warning(
                    f"Ogiltigt träningsexempel för {example.article_number}"
                )
        
        # Spara träningsdata
        if all_examples:
            from .trainers.utils import save_training_data
            save_training_data(all_examples, output_dir)
            self.logger.info(
                f"Sparade {len(all_examples)} träningsexempel i {output_dir}"
            )
        else:
            self.logger.warning("Inga träningsexempel genererades")

    def get_statistics(self) -> Dict:
        """
        Returnerar statistik om analyserade dokument.
        """
        stats = {
            'total_documents': len(self.documents),
            'documents_with_errors': len([d for d in self.documents if d.processing_errors]),
            'temp_article_numbers': len([d for d in self.documents if d.article_number.startswith("TEMP_")]),
            'compatibility_info': len([d for d in self.documents if d.compatibility]),
            'technical_specs': len([d for d in self.documents if d.technical_specs]),
            'with_images': len([d for d in self.documents if d.product_images]),
            'document_types': {},
            'processing_errors': len(self.errors)
        }
        
        # Räkna dokumenttyper
        for doc in self.documents:
            if doc.document_type not in stats['document_types']:
                stats['document_types'][doc.document_type] = 0
            stats['document_types'][doc.document_type] += 1
        
        return stats

    def print_summary(self) -> None:
        """
        Skriver ut en sammanfattning av analysen.
        """
        stats = self.get_statistics()
        
        print("\n=== Analyssammanfattning ===")
        print(f"Totalt antal dokument: {stats['total_documents']}")
        print(f"Dokument med fel: {stats['documents_with_errors']}")
        print(f"Temporära artikelnummer: {stats['temp_article_numbers']}")
        print("\nDokument med:")
        print(f"- Kompatibilitetsinformation: {stats['compatibility_info']}")
        print(f"- Tekniska specifikationer: {stats['technical_specs']}")
        print(f"- Produktbilder: {stats['with_images']}")
        
        print("\nDokumenttyper:")
        for doc_type, count in stats['document_types'].items():
            print(f"- {doc_type}: {count}")
        
        if self.errors:
            print(f"\nAntal processeringsfel: {stats['processing_errors']}")