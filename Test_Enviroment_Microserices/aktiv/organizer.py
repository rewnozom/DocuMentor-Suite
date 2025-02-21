"""
organizer.py – Modul för att organisera kompatibilitetsdokument

Denna modul ansvarar för att:
  • Skanna igenom en källkatalog med markdown-filer.
  • Extrahera kompatibilitetsrelationer från varje fil med hjälp av CompatibilityExtractor.
  • Gruppera filer baserat på gemensamma produkter (artikelnummer eller namn).
  • Kopiera filerna till nya gruppkataloger och skapa en README-fil för varje grupp med en översikt.
  
Observera att denna modul inte genererar träningsdata, utan fokuserar enbart på att analysera och
organisera dokumenten för en bättre överblick av kompatibilitetsinformationen.
"""

import os
import shutil
import logging
from pathlib import Path
from typing import Dict, Set, List

from Extra.extractor import CompatibilityExtractor
from Formatter.formatter import CompatibilityFormatter
from Models.models import CompatibilityRelation, ProductReference

# Konfigurera loggning
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('compatibility_organizer.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class EnhancedCompatibilityOrganizer:
    def __init__(self, source_dir: str, output_dir: str):
        """
        Initierar organisatören med en källa och en output-katalog.
        
        Args:
            source_dir (str): Källkatalog med markdown-filer.
            output_dir (str): Målkatalog där organiserade grupper skapas.
        """
        self.source_dir = Path(source_dir)
        self.output_dir = Path(output_dir)
        self.extractor = CompatibilityExtractor()
        self.formatter = CompatibilityFormatter()
        self.relations_by_file: Dict[str, List[CompatibilityRelation]] = {}
        self.missing_files: Set[str] = set()

    def scan_and_organize(self):
        """Huvudmetod för att skanna och organisera kompatibilitetsdokument."""
        logger.info(f"Startar skanning av {self.source_dir}")
        
        # Skapa output-katalogen
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Processera alla markdown-filer
        self._process_documents()
        
        # Organisera filerna i grupper baserat på gemensamma produkter
        self._organize_files()
        
        # Logga en sammanfattning av resultatet
        self._log_results()

    def _process_documents(self):
        """Processar alla markdown-filer och extraherar kompatibilitetsrelationer."""
        for file_path in self.source_dir.rglob("*.md"):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                # Här behandlar vi hela dokumentet som en "Compatibility"-sektion
                sections = {"Compatibility": content}
                relations = self.extractor.extract(content, sections)
                if relations:
                    self.relations_by_file[str(file_path)] = relations
                    logger.info(f"Hittade {len(relations)} kompatibilitetsrelationer i {file_path.name}")
            except Exception as e:
                logger.error(f"Fel vid processning av {file_path}: {str(e)}")

    def _organize_files(self):
        """
        Organiserar filer baserat på kompatibilitetsrelationer.
        Skapar en mapping mellan produkter och filer, grupperar filer med gemensam produktreferens,
        och skapar en ny gruppkatalog för varje grupp.
        """
        product_to_files: Dict[str, Set[str]] = {}
        
        # Bygg produkt -> filer mapping
        for file_path, relations in self.relations_by_file.items():
            for relation in relations:
                self._add_to_product_mapping(product_to_files, relation.source_product, file_path)
                self._add_to_product_mapping(product_to_files, relation.target_product, file_path)
        
        processed_files = set()
        group_counter = 1
        
        # Skapa grupper baserat på relationerna
        for file_path, relations in self.relations_by_file.items():
            if file_path in processed_files:
                continue
            
            current_group = {file_path}
            related_products = set()
            for relation in relations:
                related_products.add(relation.source_product)
                related_products.add(relation.target_product)
            
            for product in related_products:
                if product.article_number:
                    current_group.update(product_to_files.get(product.article_number, set()))
                if product.name:
                    current_group.update(product_to_files.get(product.name, set()))
            
            if current_group:
                group_dir = self._create_group_directory(group_counter, current_group, relations)
                group_counter += 1
                processed_files.update(current_group)

    def _add_to_product_mapping(self, mapping: Dict[str, Set[str]], product: ProductReference, file_path: str):
        """Lägger till en produkt i mappningen mellan produkter och filer."""
        if product.article_number:
            mapping.setdefault(product.article_number, set()).add(file_path)
        if product.name:
            mapping.setdefault(product.name, set()).add(file_path)

    def _create_group_directory(self, group_number: int, files: Set[str], relations: List[CompatibilityRelation]) -> Path:
        """
        Skapar en gruppkatalog för en grupp av filer och kopierar dessa filer.
        Skapar även en README-fil med en översikt över de extraherade relationerna.
        """
        group_dir = self.output_dir / f"compatibility_group_{group_number}"
        group_dir.mkdir(exist_ok=True)
        
        for file_path in files:
            try:
                source_path = Path(file_path)
                if source_path.exists():
                    shutil.copy2(source_path, group_dir)
                else:
                    self.missing_files.add(file_path)
                    logger.warning(f"Fil saknas: {file_path}")
            except Exception as e:
                logger.error(f"Fel vid kopiering av {file_path}: {str(e)}")
        
        self._create_group_readme(group_dir, files, relations)
        return group_dir

    def _create_group_readme(self, group_dir: Path, files: Set[str], relations: List[CompatibilityRelation]):
        """
        Skapar en README.md för gruppen med en lista på ingående filer och en översikt över
        de kompatibilitetsrelationer som extraherats från dessa filer.
        """
        readme_content = ["# Kompatibilitetsgrupp\n\n## Inkluderade filer:\n"]
        for file_path in sorted(files):
            file_name = Path(file_path).name
            readme_content.append(f"\n### {file_name}")
            file_relations = self.relations_by_file.get(file_path, [])
            if file_relations:
                formatted = self.formatter.format_relations(file_relations)
                readme_content.append(formatted)
        readme_file = group_dir / "README.md"
        with open(readme_file, 'w', encoding='utf-8') as f:
            f.write("\n".join(readme_content))
        logger.info(f"README skapad för grupp: {readme_file}")

    def _log_results(self):
        """Loggar en sammanfattning av organiseringsprocessen."""
        logger.info("\n=== Organiseringssammanfattning ===")
        logger.info(f"Antal filer med extraherade relationer: {len(self.relations_by_file)}")
        logger.info(f"Saknade filer: {len(self.missing_files)}")
        if self.missing_files:
            logger.warning("Följande filer saknades:")
            for file in sorted(self.missing_files):
                logger.warning(f"- {file}")

def main():
    # Justera dessa sökvägar efter dina behov
    source_dir = "./converted_docs"
    output_dir = "./Compatibility_Organized"
    
    organizer = EnhancedCompatibilityOrganizer(source_dir, output_dir)
    organizer.scan_and_organize()

if __name__ == "__main__":
    main()
