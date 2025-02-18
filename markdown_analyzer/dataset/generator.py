# markdown_analyzer/dataset/generator.py
import os
import json
import csv
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from multiprocessing import Manager
from tqdm import tqdm

# Relativa importer (anpassa beroende på din mappstruktur)
from ..config import Settings
from ..core.document import DocumentStructure
from ..core.training_data import TrainingDataExporter
from ..extractors import (
    MetadataExtractor,
    CompatibilityExtractor,
    TechnicalExtractor,
    ImageExtractor
)
try:
    from ..utils.html_logger import HTMLLogHandler
except ImportError:
    HTMLLogHandler = None

from ..trainers import TrainerRegistry
from ..dataset.validators import DatasetValidator, ValidationPipeline
from ..utils import TextProcessor, MarkdownFormatter


class ParallelProcessor:
    """
    Hanterar parallell bearbetning av dokument med avancerad load balancing.
    Använder både processer (ProcessPoolExecutor) och trådar (ThreadPoolExecutor)
    för att optimera filbearbetningen.
    """
    def __init__(self, num_processes: int = None, num_threads_per_process: int = 4):
        self.num_processes = num_processes or os.cpu_count()
        self.num_threads_per_process = num_threads_per_process
        self.manager = Manager()
        self.shared_data = self.manager.dict()
        self.lock = self.manager.Lock()

    def process_files(self, 
                      files: List[Path], 
                      processor_func: callable, 
                      chunk_size: int = 10,
                      show_progress: bool = True) -> List[Dict]:
        """
        Processera filer parallellt med både processer och trådar.

        Args:
            files: Lista med filer att bearbeta.
            processor_func: Funktion för att bearbeta varje fil.
            chunk_size: Antal filer per chunk.
            show_progress: Om progressbar ska visas.
        """
        results = []
        chunks = self._create_chunks(files, chunk_size)
        
        with ProcessPoolExecutor(max_workers=self.num_processes) as process_executor:
            futures = []
            for chunk in chunks:
                future = process_executor.submit(
                    self._process_chunk,
                    chunk,
                    processor_func
                )
                futures.append(future)
            
            if show_progress:
                with tqdm(total=len(files), desc="Processing files") as pbar:
                    for future in as_completed(futures):
                        chunk_results = future.result()
                        results.extend(chunk_results)
                        pbar.update(len(chunk_results))
            else:
                for future in as_completed(futures):
                    results.extend(future.result())
        
        return results

    def _create_chunks(self, files: List[Path], chunk_size: int) -> List[List[Path]]:
        """Dela upp listan med filer i mindre chunks."""
        return [files[i:i + chunk_size] for i in range(0, len(files), chunk_size)]

    def _process_chunk(self, 
                      chunk: List[Path], 
                      processor_func: callable) -> List[Dict]:
        """Bearbeta ett chunk med filer med hjälp av trådar."""
        chunk_results = []
        
        with ThreadPoolExecutor(max_workers=self.num_threads_per_process) as thread_executor:
            futures = [
                thread_executor.submit(processor_func, file)
                for file in chunk
            ]
            
            for future in as_completed(futures):
                try:
                    result = future.result()
                    if result:
                        chunk_results.append(result)
                except Exception as e:
                    with self.lock:
                        self.shared_data['errors'] = self.shared_data.get('errors', [])
                        self.shared_data['errors'].append(str(e))
        
        return chunk_results


class DatasetGenerator:
    """
    Utökad datasetgenerator med parallell bearbetning, validering och
    träningsdataexport. Funktionaliteten inkluderar:
      - Sökning efter markdown-filer i angivna kataloger.
      - Parallell bearbetning med avancerad load balancing.
      - Extrahering av metadata, sektioner, bilder, kompatibilitet och tekniska specifikationer.
      - Validering av dokument och träningsdata.
      - Generering av träningsdata via ett TrainerRegistry.
      - Export av träningsdata i både JSON- och CSV-format.
      - Valfri HTML-loggning (om HTMLLogHandler finns).
    """
    def __init__(self, input_dirs: List[str], output_dir: str, html_logging: bool = True):
        self.input_dirs = input_dirs
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Initiera extraherare
        self.metadata_extractor = MetadataExtractor()
        self.compatibility_extractor = CompatibilityExtractor()
        self.technical_extractor = TechnicalExtractor()
        self.image_extractor = ImageExtractor()
        
        # Initiera hjälpverktyg
        self.text_processor = TextProcessor()
        self.formatter = MarkdownFormatter()
        
        # Initiera parallell processor
        self.parallel_processor = ParallelProcessor()
        
        # Initiera validerare och trainer-registry
        self.validator = DatasetValidator()
        self.validation_pipeline = ValidationPipeline()
        self.trainer_registry = TrainerRegistry()
        
        # Konfigurera loggning
        self.logger = logging.getLogger(__name__)
        
        # Valfri HTML-loggning
        self.html_handler = None
        if html_logging and HTMLLogHandler:
            try:
                html_handler = HTMLLogHandler(
                    log_dir=str(self.output_dir / "logs"),
                    filename_prefix="dataset_generation"
                )
                self.logger.addHandler(html_handler)
                self.html_handler = html_handler
            except Exception as e:
                self.logger.warning(f"Kunde inte aktivera HTML-loggning: {e}")

    def _find_markdown_files(self) -> List[Path]:
        """Sök igenom input-katalogerna efter markdown-filer."""
        files = []
        for input_dir in self.input_dirs:
            p = Path(input_dir)
            files.extend(list(p.rglob("*.md")))
        return files

    def _process_file(self, filepath: Path) -> Optional[DocumentStructure]:
        """Bearbeta en enskild fil med alla extraherare."""
        try:
            content = filepath.read_text(encoding='utf-8')
            
            # Extrahera grundläggande metadata
            article_number = self.metadata_extractor.extract_article_number(filepath.name, content)
            product_name = self.metadata_extractor.extract_product_name(content)
            document_type = self.metadata_extractor.extract_document_type(filepath.name)
            description = self.metadata_extractor.extract_description(content)
            
            # Skapa initial dokumentstruktur
            doc = DocumentStructure(
                filename=filepath.name,
                article_number=article_number,
                document_type=document_type,
                product_name=product_name,
                description=description
            )
            
            # Extrahera sektioner för kontextuell extrahering
            sections = self.text_processor.extract_sections(content)
            
            # Extrahera övriga komponenter
            doc.product_images = self.image_extractor.extract(content, article_number)
            doc.compatibility = self.compatibility_extractor.extract(content, sections)
            doc.technical_specs = self.technical_extractor.extract(content, sections)
            if hasattr(doc, 'sections'):
                doc.sections = sections
            
            # Validera dokumentet
            validation_errors = self.validator.validate_document(doc)
            if validation_errors:
                if not hasattr(doc, 'processing_errors'):
                    doc.processing_errors = []
                doc.processing_errors.extend(validation_errors)
            
            return doc
            
        except Exception as e:
            self.logger.error(f"Error processing {filepath}: {str(e)}")
            return None

    def generate_dataset(self, 
                         commands: Optional[List[str]] = None,
                         chunk_size: int = 10) -> None:
        """
        Generera träningsdataset med parallell bearbetning.

        Args:
            commands: Lista med kommandon att generera data för (exempelvis 'f', 's', 't', 'c').
                      Standard är att använda alla dessa.
            chunk_size: Antal filer att bearbeta per chunk.
        """
        try:
            files = self._find_markdown_files()
            if not files:
                self.logger.warning("No markdown files found")
                return

            # Bearbeta filer parallellt
            documents = self.parallel_processor.process_files(
                files=files,
                processor_func=self._process_file,
                chunk_size=chunk_size
            )

            # Generera träningsdata via trainer-registret
            commands = commands or ['f', 's', 't', 'c']
            training_data = self._generate_training_data(documents, commands)

            # Validera och spara träningsdata
            self._validate_and_save_training_data(training_data)

        except Exception as e:
            self.logger.error(f"Error in dataset generation: {str(e)}")
            raise
        finally:
            if self.html_handler:
                self.html_handler.close()

    def _generate_training_data(self, 
                                documents: List[DocumentStructure],
                                commands: List[str]) -> Dict[str, List[Dict]]:
        """Generera träningsdata med hjälp av trainer-registret."""
        training_data = {}
        
        for command in commands:
            examples = []
            for doc in documents:
                try:
                    new_examples = self.trainer_registry.create_training_data(doc, command)
                    examples.extend(new_examples)
                except Exception as e:
                    self.logger.error(
                        f"Error generating {command} training data for {doc.article_number}: {str(e)}"
                    )
            if examples:
                training_data[command] = examples
        
        return training_data

    def _validate_and_save_training_data(self, training_data: Dict[str, List[Dict]]) -> None:
        """Validera och spara träningsdata för varje kommando."""
        for command, examples in training_data.items():
            valid_examples = []
            
            for example in examples:
                errors = self.validation_pipeline.validate_training_example(example, command)
                if not errors:
                    valid_examples.append(example)
                else:
                    self.logger.warning(f"Invalid example for command {command}: {errors}")
            
            if valid_examples:
                self._save_command_data(command, valid_examples)
            else:
                self.logger.error(f"No valid examples generated for command {command}")

    def _save_command_data(self, command: str, valid_examples: List[Dict]) -> None:
        """Spara träningsdata för ett specifikt kommando i både JSON och CSV."""
        # Spara till JSON
        json_path = self.output_dir / f"training_data_{command}.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(valid_examples, f, ensure_ascii=False, indent=2)
        
        # Spara till CSV
        csv_path = self.output_dir / f"training_data_{command}.csv"
        with open(csv_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['user_input', 'ai_output'])
            writer.writeheader()
            for example in valid_examples:
                writer.writerow(example)
