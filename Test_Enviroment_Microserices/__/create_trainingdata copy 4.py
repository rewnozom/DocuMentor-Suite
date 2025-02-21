# training_generator.py
import os
import json
import logging
from pathlib import Path
from typing import Dict, List, Set
from datetime import datetime
import pandas as pd
from tqdm import tqdm

from compatibility.extractor import CompatibilityExtractor
from compatibility.enhanced_formatter import EnhancedCompatibilityFormatter
from compatibility.models import (
    TrainingExample, CommandRelation, TrainingMetadata
)

# Konfigurera loggning
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [%(name)s] %(message)s',
    handlers=[
        logging.FileHandler('training_generator.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class CompatibilityTrainingGenerator:
    def __init__(self, source_dir: str):
        self.source_dir = Path(source_dir)
        self.output_dir = Path("./Compatibility_Trainingdata")
        self.extractor = CompatibilityExtractor()
        self.formatter = EnhancedCompatibilityFormatter()
        self.training_data: List[TrainingExample] = []
        self.command_relations: Dict[str, List[CommandRelation]] = {}
        self.metadata = TrainingMetadata()
        
        # Skapa output-katalog
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_training_data(self):
        """Huvudfunktion för att generera träningsdata"""
        start_time = datetime.now()
        logger.info(f"Startar generering av träningsdata från {self.source_dir}")
        
        try:
            # Skanna källkatalog
            markdown_files = list(self.source_dir.rglob("*.md"))
            self.metadata.total_files_processed = len(markdown_files)
            logger.info(f"Hittade {len(markdown_files)} markdown-filer")
            
            # Processera varje fil med progress bar
            for file_path in tqdm(markdown_files, desc="Processerar filer"):
                try:
                    self._process_file(file_path)
                except Exception as e:
                    logger.error(f"Fel vid processning av {file_path}: {str(e)}")
                    self.metadata.add_error(str(file_path))
            
            # Spara alla resultat
            self._save_training_data()
            self._generate_command_overview()
            self._save_metadata()
            
            duration = datetime.now() - start_time
            logger.info(f"Träningsdatagenerering slutförd på {duration.total_seconds():.2f} sekunder")
            self._log_summary()
            
        except Exception as e:
            logger.error(f"Oväntat fel under generering: {str(e)}")
            raise

    def _process_file(self, file_path: Path):
        """Processar en enskild fil"""
        logger.debug(f"Processar fil: {file_path}")
        
        try:
            # Läs fil med UTF-8
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            # Försök med latin-1 om UTF-8 misslyckas
            try:
                with open(file_path, 'r', encoding='latin-1') as f:
                    content = f.read()
            except Exception as e:
                logger.error(f"Kunde inte läsa {file_path}: {str(e)}")
                self.metadata.add_error(str(file_path))
                return
        
        # Extrahera relationer
        sections = {"Compatibility": content}
        relations = self.extractor.extract(content, sections)
        
        if relations:
            self.metadata.total_relations_found += len(relations)
            logger.info(f"Hittade {len(relations)} relationer i {file_path.name}")
            
            # Skapa träningsexempel och kommandorelationer
            for relation in relations:
                # Generera träningsexempel
                examples = self.formatter.format_for_training(relation)
                self.training_data.extend(examples)
                self.metadata.total_examples_generated += len(examples)
                
                # Spara kommandorelationer
                for example in examples:
                    cmd = example.user_input.split()[0]  # Extrahera kommandot (ex: -c)
                    if cmd not in self.command_relations:
                        self.command_relations[cmd] = []
                    
                    self.command_relations[cmd].append(
                        CommandRelation(
                            source=relation.source_product.name,
                            target=relation.target_product.name,
                            relation_type=relation.relation_type.value,
                            context=str(file_path.name),
                            confidence=example.confidence
                        )
                    )

    def _save_training_data(self):
        """Sparar träningsdata i olika format"""
        logger.info("Sparar träningsdata...")
        
        # Konvertera till DataFrame
        df = pd.DataFrame([{
            "user_input": ex.user_input,
            "ai_output": ex.ai_output,
            "confidence": ex.confidence
        } for ex in self.training_data])
        
        # Spara i olika format
        json_path = self.output_dir / "compatibility_training.json"
        csv_path = self.output_dir / "compatibility_training.csv"
        parquet_path = self.output_dir / "compatibility_training.parquet"
        
        # JSON med formatting
        df.to_json(json_path, orient='records', force_ascii=False, indent=2)
        
        # CSV med korrekt encoding
        df.to_csv(csv_path, index=False, encoding='utf-8')
        
        # Parquet för effektiv lagring
        df.to_parquet(parquet_path, index=False)
        
        logger.info(f"Sparade {len(df)} träningsexempel i JSON, CSV och Parquet format")

    def _generate_command_overview(self):
        """Genererar markdown-översikt över kommandon"""
        logger.info("Genererar kommandoöversikt...")
        
        overview_path = self.output_dir / "command_overview.md"
        content = ["# Compatibility Command Overview\n"]
        
        for command, relations in self.command_relations.items():
            content.append(f"\n## {command}")
            content.append("\nAnvänds för att hitta produktkompatibilitet i Copiax sortiment.\n")
            
            # Gruppera efter källprodukt och relationstyp
            by_source = {}
            for rel in relations:
                if rel.source not in by_source:
                    by_source[rel.source] = {"types": {}, "context": rel.context}
                
                if rel.relation_type not in by_source[rel.source]["types"]:
                    by_source[rel.source]["types"][rel.relation_type] = []
                
                by_source[rel.source]["types"][rel.relation_type].append(rel.target)
            
            # Skriv ut grupperad information
            for source, info in by_source.items():
                content.append(f"\n### {source}")
                content.append(f"Kontext: {info['context']}\n")
                
                for rel_type, targets in info["types"].items():
                    content.append(f"#### {rel_type}:")
                    for target in sorted(set(targets)):
                        content.append(f"* {target}")
                    content.append("")  # Tom rad mellan sektioner
        
        with open(overview_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(content))
        
        logger.info(f"Kommandoöversikt genererad: {overview_path}")

    def _save_metadata(self):
        """Sparar metadata om genereringen"""
        metadata_path = self.output_dir / "generation_metadata.json"
        
        metadata = {
            "timestamp": datetime.now().isoformat(),
            "source_directory": str(self.source_dir),
            "statistics": self.metadata.get_summary()
        }
        
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Metadata sparad: {metadata_path}")

    def _log_summary(self):
        """Loggar en sammanfattning av genereringen"""
        summary = self.metadata.get_summary()
        
        logger.info("\n=== Genereringssammanfattning ===")
        logger.info(f"Processade filer: {summary['total_files']}")
        logger.info(f"Hittade relationer: {summary['total_relations']}")
        logger.info(f"Genererade exempel: {summary['total_examples']}")
        logger.info(f"Filer med fel: {summary['error_files']}")
        
        if self.metadata.files_with_errors:
            logger.info("\nFiler med fel:")
            for file in sorted(self.metadata.files_with_errors):
                logger.info(f"- {file}")

def main():
    # Konfigurera källkatalog
    source_dir = "./converted_docs"
    
    try:
        # Skapa och kör generator
        generator = CompatibilityTrainingGenerator(source_dir)
        generator.generate_training_data()
    except Exception as e:
        logger.error(f"Fel vid generering av träningsdata: {str(e)}")
        raise

if __name__ == "__main__":
    main()