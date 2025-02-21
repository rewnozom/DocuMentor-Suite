# create_trainingdata.py

import os
import logging
import json
import csv
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set, Optional
import pandas as pd
from tqdm import tqdm
from dataclasses import dataclass, field

from compatibility.extractor import CompatibilityExtractor
from compatibility.formatter import CompatibilityFormatter
from compatibility.models import (
    TrainingExample, TrainingMetadata, 
    ProductReference, CompatibilityRelation,
    RelationType
)

@dataclass
class CommandRelation:
    """Representerar en kommandorelation för översikten"""
    source: str                   # Källproduktens namn
    target: str                   # Målproduktens namn
    relation_type: str           # Typ av relation
    confidence: float = 1.0      # Konfidensnivå
    metadata: Dict[str, str] = field(default_factory=dict)  # Extra metadata som artikelnummer

# Konfigurera loggning
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [%(name)s] %(message)s',
    handlers=[
        logging.FileHandler('training_generator.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class CompatibilityTrainingGenerator:
    """
    Huvudklass för att generera träningsdata för kompatibilitetskommandot (-c).
    Läser preprocessade markdown-filer och genererar strukturerad träningsdata.
    """
    
    def __init__(self, source_dir: str):
        self.source_dir = Path(source_dir)
        self.output_dir = Path("./Compatibility_Trainingdata")
        self.extractor = CompatibilityExtractor()
        self.formatter = CompatibilityFormatter()
        self.metadata = TrainingMetadata()
        
        # Använd dictionaries för att hantera unik data
        self.product_relations: Dict[str, Dict[str, List[CompatibilityRelation]]] = {}
        self.training_data: List[TrainingExample] = []
        self.command_relations: Dict[str, List[CommandRelation]] = {}
        
        # Skapa output-katalog
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def process_files(self):
        """Processerar alla markdown-filer"""
        markdown_files = list(self.source_dir.rglob("*.md"))
        self.metadata.total_files_processed = len(markdown_files)
        logger.info(f"Hittade {len(markdown_files)} markdown-filer")
        
        for file_path in tqdm(markdown_files, desc="Processerar filer"):
            try:
                self._process_single_file(file_path)
            except Exception as e:
                logger.error(f"Fel vid processning av {file_path}: {str(e)}")
                self.metadata.add_error(str(file_path))

    def _process_single_file(self, file_path: Path):
        """Processar en enskild fil"""
        content = self._read_file(file_path)
        if not content:
            return

        # Extrahera relationer
        relations = self.extractor.extract(content, str(file_path))
        if not relations:
            return

        self.metadata.total_relations_found += len(relations)
        
        # Gruppera relationer per källprodukt
        for relation in relations:
            product_key = self._get_product_key(relation.source_product)
            
            if product_key not in self.product_relations:
                self.product_relations[product_key] = {
                    "basic": [],
                    "tech": [],
                    "requirements": []
                }
            
            # Kategorisera relationen
            if relation.relation_type in [RelationType.DIRECT, RelationType.ACCESSORY]:
                self.product_relations[product_key]["basic"].append(relation)
            elif relation.conditions:
                self.product_relations[product_key]["requirements"].append(relation)
            else:
                self.product_relations[product_key]["tech"].append(relation)

    def _get_product_key(self, product: ProductReference) -> str:
        """Skapar en unik nyckel för en produkt"""
        if product.article_number:
            return f"art_{product.article_number}"
        return f"name_{product.name}"

    def generate_training_data(self):
        """Huvudprocess för att generera träningsdata"""
        start_time = datetime.now()
        logger.info(f"Startar generering av träningsdata från {self.source_dir}")
        
        try:
            # Processera filer
            self.process_files()
            
            # Generera träningsexempel
            self._generate_training_examples()
            
            # Spara resultat
            self._save_training_data()
            self._save_metadata()
            self._generate_summary()
            self._generate_command_overview()
            
            # Logga sammanfattning
            duration = datetime.now() - start_time
            logger.info(f"Träningsdatagenerering slutförd på {duration.total_seconds():.2f} sekunder")
            self._log_summary()
            
        except Exception as e:
            logger.error(f"Oväntat fel under generering: {str(e)}")
            raise

    def _generate_training_examples(self):
        """Genererar unika träningsexempel från samlade relationer"""
        unique_examples = {}  # För att spåra unika exempel
        
        for product_key, relation_groups in self.product_relations.items():
            # Verifiera att vi har några relationer
            if not any(relation_groups.values()):
                continue
                
            # Använd första tillgängliga relationen för källproduktinfo
            source_product = None
            max_confidence = 0.0
            
            for group in relation_groups.values():
                if group:
                    source_product = group[0].source_product
                    max_confidence = max(max_confidence, max(rel.confidence for rel in group))
            
            if not source_product:
                continue
            
            # Skapa formaterat svar
            response = self.formatter._format_clean_markdown(relation_groups)
            
            # Skapa unika exempel
            if source_product.article_number:
                key = f"art_{source_product.article_number}"
                unique_examples[key] = TrainingExample(
                    user_input=f"-c {source_product.article_number}",
                    ai_output=response,
                    source=source_product.name,
                    confidence=max_confidence
                )
            
            if source_product.name and not source_product.name.startswith("Produkt "):
                key = f"name_{source_product.name}"
                unique_examples[key] = TrainingExample(
                    user_input=f'-c "{source_product.name}"',
                    ai_output=response,
                    source=source_product.name,
                    confidence=max_confidence * 0.9
                )
            
            # Uppdatera command_relations för översikten
            self._update_command_relations(product_key, relation_groups)
            
        # Konvertera till lista och uppdatera statistik
        self.training_data = list(unique_examples.values())
        self.metadata.total_examples_generated = len(self.training_data)

    def _update_command_relations(self, product_key: str, relation_groups: Dict):
        """Uppdaterar command_relations för översikten"""
        cmd = "-c"  # Vi har bara ett kommando för närvarande
        if cmd not in self.command_relations:
            self.command_relations[cmd] = []
        
        # Samla alla unika relationer
        source_product = None
        seen_targets = set()
        
        for group in relation_groups.values():
            for relation in group:
                if not source_product:
                    source_product = relation.source_product
                
                target_key = f"{relation.target_product.name}:{relation.relation_type.value}"
                if target_key in seen_targets:
                    continue
                
                seen_targets.add(target_key)
                self.command_relations[cmd].append(
                    CommandRelation(
                        source=relation.source_product.name,
                        target=relation.target_product.name,
                        relation_type=relation.relation_type.value,
                        confidence=relation.confidence,
                        metadata={
                            "article_number": relation.source_product.article_number
                        } if relation.source_product.article_number else {}
                    )
                )

    def _read_file(self, file_path: Path) -> Optional[str]:
        """Läser innehållet från en fil med förbättrad felhantering"""
        encodings = ['utf-8', 'latin-1', 'windows-1252']
        
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    return f.read()
            except UnicodeDecodeError:
                continue
            except Exception as e:
                logger.error(f"Kunde inte läsa {file_path}: {str(e)}")
                break
        
        self.metadata.add_error(str(file_path))
        return None

    def _save_training_data(self):
        """Sparar träningsdata i olika format med förbättrad felhantering"""
        logger.info("Sparar träningsdata...")
        
        if not self.training_data:
            logger.warning("Inga träningsexempel att spara!")
            return
        
        try:
            # Konvertera till DataFrame
            df_data = [
                {
                    "user_input": ex.user_input,
                    "ai_output": ex.ai_output,
                    "confidence": ex.confidence,
                    "source": ex.source
                }
                for ex in self.training_data
            ]
            
            df = pd.DataFrame(df_data)
            
            # Spara i olika format
            json_path = self.output_dir / "compatibility_training.json"
            csv_path = self.output_dir / "compatibility_training.csv"
            parquet_path = self.output_dir / "compatibility_training.parquet"
            
            # JSON med pretty printing
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(
                    [ex.__dict__ for ex in self.training_data],
                    f,
                    ensure_ascii=False,
                    indent=2
                )
            
            # CSV med korrekt escape-hantering
            df.to_csv(
                csv_path, 
                index=False, 
                encoding='utf-8',
                quoting=csv.QUOTE_ALL,
                escapechar='\\'
            )
            
            # Parquet för effektiv lagring
            df.to_parquet(parquet_path, index=False)
            
            logger.info(f"Sparade {len(df)} träningsexempel i alla format")
            
        except Exception as e:
            logger.error(f"Fel vid sparande av data: {str(e)}")
            raise


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


    def _generate_command_overview(self):
        """Genererar strukturerad markdown-översikt över kommandon"""
        if not self.command_relations:
            logger.warning("Inga kommandorelationer att dokumentera!")
            return
            
        overview_path = self.output_dir / "command_overview.md"
        content = ["# Kommandoöversikt\n"]
        
        for command, relations in self.command_relations.items():
            content.append(f"## {command}")
            content.append("Används för att hitta produktkompatibilitet i Copiax sortiment.\n")
            
            # Gruppera efter källprodukt
            by_source = {}
            for rel in relations:
                if rel.source not in by_source:
                    by_source[rel.source] = {
                        "types": {},
                        "metadata": rel.metadata
                    }
                
                if rel.relation_type not in by_source[rel.source]["types"]:
                    by_source[rel.source]["types"][rel.relation_type] = set()
                
                by_source[rel.source]["types"][rel.relation_type].add(rel.target)
            
            # Skriv ut strukturerad information
            for source, info in sorted(by_source.items()):
                content.extend([
                    f"\n### {source}",
                    *(f"Artikelnummer: {info['metadata']['article_number']}\n"
                      if 'article_number' in info['metadata'] else []),
                    *(f"#### {rel_type}:\n" + "\n".join(f"* {target}" 
                      for target in sorted(targets)) + "\n"
                      for rel_type, targets in sorted(info["types"].items()))
                ])
        
        with open(overview_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(content))
        
        logger.info(f"Kommandoöversikt genererad: {overview_path}")

    def _generate_summary(self):
        """Genererar detaljerad sammanfattning av träningsdatan"""
        summary_path = self.output_dir / "training_summary.md"
        
        content = [
            "# Sammanfattning av Träningsdata",
            f"\nGenererad: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "\n## Statistik",
            f"- Processade filer: {self.metadata.total_files_processed}",
            f"- Extraherade relationer: {self.metadata.total_relations_found}",
            f"- Genererade exempel: {self.metadata.total_examples_generated}",
            f"- Filer med fel: {len(self.metadata.files_with_errors)}",
            "\n## Distribution av Exempel"
        ]
        
        # Analys av distribution
        command_types = {}
        confidence_ranges = {
            "Hög (>0.9)": 0,
            "Medium (0.7-0.9)": 0,
            "Låg (<0.7)": 0
        }
        
        for example in self.training_data:
            cmd = example.user_input.split()[0]
            command_types[cmd] = command_types.get(cmd, 0) + 1
            
            if example.confidence > 0.9:
                confidence_ranges["Hög (>0.9)"] += 1
            elif example.confidence > 0.7:
                confidence_ranges["Medium (0.7-0.9)"] += 1
            else:
                confidence_ranges["Låg (<0.7)"] += 1
        
        # Lägg till statistik
        content.extend([
            "\n### Kommandotyper",
            *(f"- {cmd}: {count} exempel"
              for cmd, count in command_types.items()),
            "\n### Konfidensfördelning",
            *(f"- {range_name}: {count} exempel"
              for range_name, count in confidence_ranges.items())
        ])
        
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(content))
        
        logger.info(f"Sammanfattning genererad: {summary_path}")

    def _log_summary(self):
        """Loggar detaljerad sammanfattning av genereringen"""
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
    """Huvudfunktion för att köra generatorn"""
    source_dir = "./converted_docs"
    
    try:
        generator = CompatibilityTrainingGenerator(source_dir)
        generator.generate_training_data()
    except Exception as e:
        logger.error(f"Fel vid generering av träningsdata: {str(e)}")
        raise

if __name__ == "__main__":
    main()

