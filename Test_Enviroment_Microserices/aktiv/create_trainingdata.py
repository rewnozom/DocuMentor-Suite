"""
create_trainingdata.py – Träningsdatagenerator

Denna modul skannar igenom en angiven källkatalog med markdown-filer, 
extraherar kompatibilitetsrelationer med hjälp av CompatibilityExtractor och 
en EnhancedCompatibilityFormatter, och genererar ett träningsdataset för AI-modellering.

Utdata sparas i flera format (JSON, CSV, Parquet) samt en översikt (command overview)
och metadata om processen. Alla inställningar styrs via en YAML-konfigurationsfil.
"""

import os
import json
import csv
import logging
from pathlib import Path
from typing import Dict, List, Set, Optional
from datetime import datetime

import pandas as pd
from tqdm import tqdm
import yaml

# Importera nödvändiga klasser från dina moduler
from Extra.extractor import CompatibilityExtractor
from Formatter.formatter import EnhancedCompatibilityFormatter
from Models.models import TrainingExample, CommandRelation, TrainingMetadata

# ---------------------------------------------------
# YAML-konfigurationsladdare
# ---------------------------------------------------
def load_config(path: str = "trainingdata_config.yaml") -> Dict:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    else:
        # Standardinställningar om konfigfilen inte hittas
        return {
            "source_directory": "./converted_docs",
            "output_directory": "./Compatibility_Trainingdata",
            "output_formats": ["json", "csv", "parquet"],
            "json_filename": "compatibility_training.json",
            "csv_filename": "compatibility_training.csv",
            "parquet_filename": "compatibility_training.parquet",
            "command_overview_filename": "command_overview.md",
            "metadata_filename": "generation_metadata.json",
            "log_level": "INFO"
        }

CONFIG = load_config()

# Ställ in loggning enligt konfiguration
logging.basicConfig(
    level=getattr(logging, CONFIG.get("log_level", "INFO")),
    format='%(asctime)s - %(levelname)s - [%(name)s] %(message)s',
    handlers=[
        logging.FileHandler('training_generator.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------
# Huvudklassen: CompatibilityTrainingGenerator
# ---------------------------------------------------
class CompatibilityTrainingGenerator:
    def __init__(self, source_dir: Optional[str] = None):
        self.source_dir = Path(source_dir or CONFIG.get("source_directory"))
        self.output_dir = Path(CONFIG.get("output_directory"))
        self.extractor = CompatibilityExtractor()
        self.formatter = EnhancedCompatibilityFormatter()
        self.training_data: List[TrainingExample] = []
        self.command_relations: Dict[str, List[CommandRelation]] = {}
        self.metadata = TrainingMetadata()

        # Skapa output-katalogen om den inte finns
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_training_data(self):
        """Huvudfunktion för att generera träningsdata."""
        start_time = datetime.now()
        logger.info(f"Startar generering av träningsdata från {self.source_dir}")

        try:
            markdown_files = list(self.source_dir.rglob("*.md"))
            self.metadata.total_files_processed = len(markdown_files)
            logger.info(f"Hittade {len(markdown_files)} markdown-filer.")

            for file_path in tqdm(markdown_files, desc="Processerar filer"):
                try:
                    self._process_file(file_path)
                except Exception as e:
                    logger.error(f"Fel vid processning av {file_path}: {str(e)}")
                    self.metadata.add_error(str(file_path))

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
        """Processar en fil och extraherar kompatibilitetsrelationer samt genererar träningsdata."""
        logger.debug(f"Processar fil: {file_path}")
        try:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                with open(file_path, 'r', encoding='latin-1') as f:
                    content = f.read()
        except Exception as e:
            logger.error(f"Kunde inte läsa {file_path}: {str(e)}")
            self.metadata.add_error(str(file_path))
            return

        # Skapa en sections-dictionary där vi behandlar hela innehållet som "Compatibility"
        sections = {"Compatibility": content}
        relations = self.extractor.extract(content, sections, str(file_path))

        if relations:
            self.metadata.total_relations_found += len(relations)
            logger.info(f"Hittade {len(relations)} kompatibilitetsrelationer i {file_path.name}")

            for relation in relations:
                try:
                    examples = self.formatter.format_for_training(relation)
                    if not examples:
                        continue
                    self.training_data.extend(examples)
                    self.metadata.total_examples_generated += len(examples)

                    # Skapa kommandorelationer
                    for example in examples:
                        cmd = example.user_input.split()[0]  # Exempelvis "-c"
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
                except Exception as e:
                    logger.error(f"Fel vid generering av träningsexempel för {file_path}: {str(e)}")
                    self.metadata.add_error(str(file_path))

    def _save_training_data(self):
        """Sparar träningsdata i de format som anges i konfigurationen."""
        logger.info("Sparar träningsdata...")
        if not self.training_data:
            logger.warning("Inga träningsexempel att spara!")
            return

        try:
            valid_examples = [ex for ex in self.training_data if isinstance(ex, TrainingExample)]
            if not valid_examples:
                logger.error("Inga giltiga träningsexempel hittades!")
                return

            df_data = [{
                "user_input": ex.user_input,
                "ai_output": ex.ai_output,
                "confidence": ex.confidence,
                "source": ex.source
            } for ex in valid_examples]

            df = pd.DataFrame(df_data)

            # Spara utdata enligt de format som anges i konfigurationen
            if "json" in CONFIG.get("output_formats", []):
                json_path = self.output_dir / CONFIG.get("json_filename", "compatibility_training.json")
                with open(json_path, 'w', encoding='utf-8') as f:
                    json.dump([ex.__dict__ for ex in valid_examples], f, ensure_ascii=False, indent=2)
                logger.debug(f"JSON sparad: {json_path}")

            if "csv" in CONFIG.get("output_formats", []):
                csv_path = self.output_dir / CONFIG.get("csv_filename", "compatibility_training.csv")
                df.to_csv(csv_path, index=False, encoding='utf-8', quoting=csv.QUOTE_ALL, escapechar='\\')
                logger.debug(f"CSV sparad: {csv_path}")

            if "parquet" in CONFIG.get("output_formats", []):
                parquet_path = self.output_dir / CONFIG.get("parquet_filename", "compatibility_training.parquet")
                df.to_parquet(parquet_path, index=False)
                logger.debug(f"Parquet sparad: {parquet_path}")

            logger.info(f"Sparade {len(df)} träningsexempel i angivna format.")
        except Exception as e:
            logger.error(f"Fel vid sparande av träningsdata: {str(e)}")
            raise

    def _generate_command_overview(self):
        """Genererar en markdown-översikt över kommandon."""
        logger.info("Genererar kommandoöversikt...")
        overview_path = self.output_dir / CONFIG.get("command_overview_filename", "command_overview.md")
        content = ["# Kommandoöversikt\n"]

        for command, relations in self.command_relations.items():
            content.append(f"\n## {command}")
            content.append("\nAnvänds för att hitta produktkompatibilitet i Copiax sortiment.\n")
            by_source: Dict[str, Dict[str, Set[str]]] = {}
            for rel in relations:
                if rel.source not in by_source:
                    by_source[rel.source] = {"types": {}, "metadata": rel.metadata if hasattr(rel, "metadata") else {}}
                if rel.relation_type not in by_source[rel.source]["types"]:
                    by_source[rel.source]["types"][rel.relation_type] = set()
                by_source[rel.source]["types"][rel.relation_type].add(rel.target)
            for source, info in by_source.items():
                content.append(f"\n### {source}")
                if "article_number" in info["metadata"]:
                    content.append(f"Artikelnummer: {info['metadata']['article_number']}\n")
                for rel_type, targets in info["types"].items():
                    content.append(f"#### {rel_type}:")
                    for target in sorted(targets):
                        content.append(f"* {target}")
                    content.append("")
        with open(overview_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(content))
        logger.info(f"Kommandoöversikt genererad: {overview_path}")

    def _save_metadata(self):
        """Sparar metadata om träningsdatagenereringen."""
        metadata_path = self.output_dir / CONFIG.get("metadata_filename", "generation_metadata.json")
        metadata = {
            "timestamp": datetime.now().isoformat(),
            "source_directory": str(self.source_dir),
            "statistics": self.metadata.get_summary()
        }
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        logger.info(f"Metadata sparad: {metadata_path}")

    def _log_summary(self):
        """Loggar en sammanfattning av träningsdatagenereringen."""
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
    try:
        source_dir = CONFIG.get("source_directory")
        generator = CompatibilityTrainingGenerator(source_dir)
        generator.generate_training_data()
    except Exception as e:
        logger.error(f"Fel vid generering av träningsdata: {str(e)}")
        raise

if __name__ == "__main__":
    main()
