import os
import json
import logging
import pandas as pd
from pathlib import Path
from typing import Dict, List, Set, Optional
from dataclasses import dataclass
from collections import defaultdict
from compatibility.models import CompatibilityRelation, ProductReference

# Konfigurera loggning
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('training_generator.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class TrainingExample:
    user_input: str
    ai_output: str

@dataclass
class CommandRelation:
    source: str
    target: str
    relation_type: str
    context: Optional[str] = None

class CompatibilityTrainingGenerator:
    def __init__(self, compatibility_dir: str):
        self.compatibility_dir = Path(compatibility_dir)
        self.output_dir = Path("./Compatibility_Trainingdata")
        self.training_data: List[TrainingExample] = []
        self.command_relations: Dict[str, List[CommandRelation]] = defaultdict(list)
        
    def generate_training_data(self):
        """Huvudfunktion för att generera träningsdata"""
        logger.info("Startar generering av träningsdata")
        
        # Skapa output-katalogen
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Processa varje kompatibilitetsgrupp
        for group_dir in self.compatibility_dir.glob("compatibility_group_*"):
            self._process_group(group_dir)
        
        # Spara all data
        self._save_training_data()
        self._generate_command_overview()
        
        logger.info(f"Genererat {len(self.training_data)} träningsexempel")

    def _process_group(self, group_dir: Path):
        """Processar en kompatibilitetsgrupp och skapar träningsexempel"""
        readme_path = group_dir / "README.md"
        if not readme_path.exists():
            return

        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()

        relations = self._extract_relations_from_readme(content)
        
        for source_product in relations:
            compatible_products = relations[source_product]
            
            # Skapa träningsexempel
            if source_product.article_number:
                query = f"-c {source_product.article_number}"
                response = self._format_compatibility_response(source_product, compatible_products)
                self.training_data.append(TrainingExample(query, response))
                
                # Spara kommandorelation
                for target in compatible_products:
                    self.command_relations["-c"].append(
                        CommandRelation(
                            source=source_product.article_number,
                            target=target.name,
                            relation_type="compatibility",
                            context=f"Artikel {source_product.article_number} ({source_product.name})"
                        )
                    )
            
            # Fråga med produktnamn
            query = f"-c {source_product.name}"
            response = self._format_compatibility_response(source_product, compatible_products)
            self.training_data.append(TrainingExample(query, response))

    def _save_training_data(self):
        """Sparar träningsdata i JSON, CSV och Parquet format"""
        # Konvertera till DataFrame
        df = pd.DataFrame([{
            "user_input": ex.user_input,
            "ai_output": ex.ai_output
        } for ex in self.training_data])
        
        # Spara JSON
        json_path = self.output_dir / "compatibility_training.json"
        df.to_json(json_path, orient='records', force_ascii=False, indent=2)
        
        # Spara CSV
        csv_path = self.output_dir / "compatibility_training.csv"
        df.to_csv(csv_path, index=False, encoding='utf-8')
        
        # Spara Parquet
        parquet_path = self.output_dir / "compatibility_training.parquet"
        df.to_parquet(parquet_path, index=False)
        
        logger.info(f"Träningsdata sparad i JSON, CSV och Parquet format")

    def _generate_command_overview(self):
        """Genererar en markdown-översikt över alla kommandon och deras relationer"""
        overview_path = self.output_dir / "command_overview.md"
        
        content = ["# Kommandoöversikt\n"]
        
        for command, relations in self.command_relations.items():
            content.append(f"\n## {command}")
            content.append("\nKommandot används för att hitta kompatibilitet mellan produkter.\n")
            
            # Gruppera efter källprodukt
            relations_by_source = defaultdict(list)
            for rel in relations:
                relations_by_source[rel.source].append(rel)
            
            for source, source_relations in relations_by_source.items():
                content.append(f"\n### {source_relations[0].context}\n")
                content.append("Kompatibla produkter:")
                for rel in source_relations:
                    content.append(f"* {rel.target}")
                content.append("")  # Tom rad för separation
        
        with open(overview_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(content))
        
        logger.info(f"Kommandoöversikt genererad: {overview_path}")

    def _extract_relations_from_readme(self, content: str) -> Dict[ProductReference, List[ProductReference]]:
        """Extraherar relationer från README-innehåll"""
        relations: Dict[ProductReference, List[ProductReference]] = {}
        current_product = None
        compatible_products = []

        lines = content.split('\n')
        for line in lines:
            if line.startswith('### '):
                if current_product and compatible_products:
                    relations[current_product] = compatible_products
                
                product_name = line[4:].strip()
                current_product = self._create_product_reference(product_name)
                compatible_products = []
            
            elif line.strip().startswith('- '):
                product_info = line[2:].strip()
                compatible_product = self._create_product_reference(product_info)
                if compatible_product:
                    compatible_products.append(compatible_product)

        if current_product and compatible_products:
            relations[current_product] = compatible_products

        return relations

    def _create_product_reference(self, text: str) -> Optional[ProductReference]:
        """Skapar en ProductReference från text"""
        article_match = None
        if '(Art.nr: ' in text:
            start = text.find('(Art.nr: ') + 9
            end = text.find(')', start)
            if end > start:
                article_match = text[start:end]
                text = text[:start-9].strip()

        return ProductReference(
            name=text,
            article_number=article_match
        )

    def _format_compatibility_response(self, 
                                    source_product: ProductReference,
                                    compatible_products: List[ProductReference]) -> str:
        """Formaterar ett kompatibilitetssvar"""
        if not compatible_products:
            return f"Jag hittar inga kompatibla produkter för {source_product.name} i Copiax sortiment."

        response_lines = [
            f"Här är en lista över produkter som är kompatibla med {source_product.name}"
        ]
        if source_product.article_number:
            response_lines[0] += f" (Copiax artikelnummer: {source_product.article_number})"
        response_lines[0] += ":"
        response_lines.append("")

        for product in compatible_products:
            response_lines.append(product.name)
            if product.article_number:
                response_lines.append(f"Copiax artikelnummer: {product.article_number}")
            response_lines.append("")

        return "\n".join(response_lines).strip()

def main():
    compatibility_dir = "./Compatibility_Documents"
    
    generator = CompatibilityTrainingGenerator(compatibility_dir)
    generator.generate_training_data()

if __name__ == "__main__":
    main()