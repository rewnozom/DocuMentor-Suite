import os
import shutil
import logging
from pathlib import Path
from typing import Dict, Set, List

from compatibility.extractor import CompatibilityExtractor
from compatibility.formatter import CompatibilityFormatter
from compatibility.models import CompatibilityRelation, ProductReference

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
        self.source_dir = Path(source_dir)
        self.output_dir = Path(output_dir)
        self.extractor = CompatibilityExtractor()
        self.formatter = CompatibilityFormatter()
        self.relations_by_file: Dict[str, List[CompatibilityRelation]] = {}
        self.missing_files: Set[str] = set()

    def scan_and_organize(self):
        """Huvudfunktion för att skanna och organisera kompatibilitetsdokument"""
        logger.info(f"Startar skanning av {self.source_dir}")
        
        # Skapa output-katalogen
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Processera alla markdown-filer
        self._process_documents()
        
        # Organisera filer baserat på kompatibilitetsrelationer
        self._organize_files()
        
        # Logga resultat
        self._log_results()

    def _process_documents(self):
        """Processar alla markdown-dokument och extraherar kompatibilitetsinformation"""
        for file_path in self.source_dir.rglob("*.md"):
            try:
                # Läs dokumentet
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extrahera kompatibilitetsinformation
                sections = {"Compatibility": content}
                
                relations = self.extractor.extract(content, sections)
                
                if relations:
                    self.relations_by_file[str(file_path)] = relations
                    logger.info(f"Hittade {len(relations)} kompatibilitetsrelationer i {file_path.name}")
                
            except UnicodeDecodeError:
                try:
                    # Försök med latin-1 encoding som fallback
                    with open(file_path, 'r', encoding='latin-1') as f:
                        content = f.read()
                    sections = {"Compatibility": content}
                    relations = self.extractor.extract(content, sections)
                    if relations:
                        self.relations_by_file[str(file_path)] = relations
                        logger.info(f"Hittade {len(relations)} kompatibilitetsrelationer i {file_path.name} (latin-1)")
                except Exception as e:
                    logger.error(f"Fel vid processning av {file_path} med latin-1: {str(e)}")
            except Exception as e:
                logger.error(f"Fel vid processning av {file_path}: {str(e)}")

    def _organize_files(self):
        """Organiserar filer baserat på kompatibilitetsrelationer"""
        # Skapa mapping mellan produkter och filer
        product_to_files: Dict[str, Set[str]] = {}
        
        # Bygg produkt -> filer mapping
        for file_path, relations in self.relations_by_file.items():
            for relation in relations:
                # Använd artikelnummer eller namn som nyckel
                self._add_to_product_mapping(product_to_files, relation.source_product, file_path)
                self._add_to_product_mapping(product_to_files, relation.target_product, file_path)
        
        # Skapa kompatibilitetsgrupper
        processed_files = set()
        group_counter = 1
        
        for file_path, relations in self.relations_by_file.items():
            if file_path in processed_files:
                continue
                
            # Skapa en ny grupp
            current_group = {file_path}
            for relation in relations:
                # Lägg till filer för källprodukt
                if relation.source_product.article_number:
                    current_group.update(
                        product_to_files.get(relation.source_product.article_number, set())
                    )
                elif relation.source_product.name:
                    current_group.update(
                        product_to_files.get(relation.source_product.name, set())
                    )
                
                # Lägg till filer för målprodukt
                if relation.target_product.article_number:
                    current_group.update(
                        product_to_files.get(relation.target_product.article_number, set())
                    )
                elif relation.target_product.name:
                    current_group.update(
                        product_to_files.get(relation.target_product.name, set())
                    )
            
            if current_group:
                group_dir = self._create_group_directory(group_counter, current_group, relations)
                group_counter += 1
                processed_files.update(current_group)

    def _add_to_product_mapping(self, mapping: Dict[str, Set[str]], 
                              product: ProductReference, file_path: str):
        """Lägger till en produkt i product -> files mappningen"""
        if product.article_number:
            mapping.setdefault(product.article_number, set()).add(file_path)
        if product.name:
            mapping.setdefault(product.name, set()).add(file_path)

    def _create_group_directory(self, group_number: int, files: Set[str], 
                              relations: List[CompatibilityRelation]) -> Path:
        """Skapar en gruppkatalog och kopierar relevanta filer"""
        group_dir = self.output_dir / f"compatibility_group_{group_number}"
        group_dir.mkdir(exist_ok=True)
        
        # Kopiera filer
        for file_path in files:
            try:
                source_path = Path(file_path)
                if source_path.exists():
                    shutil.copy2(source_path, group_dir)
                else:
                    self.missing_files.add(str(file_path))
                    logger.warning(f"Fil saknas: {file_path}")
            except Exception as e:
                logger.error(f"Fel vid kopiering av {file_path}: {str(e)}")
        
        # Skapa README med relations-information
        self._create_group_readme(group_dir, files, relations)
        
        return group_dir

    def _create_group_readme(self, group_dir: Path, files: Set[str], 
                           relations: List[CompatibilityRelation]):
        """Skapar en README-fil för gruppen med kompatibilitetsinformation"""
        readme_content = ["# Kompatibilitetsgrupp\n\n## Inkluderade filer:\n"]
        
        # Lägg till fillista
        for file_path in sorted(files):
            file_name = Path(file_path).name
            readme_content.append(f"\n### {file_name}")
            
            # Hitta relations för denna fil
            file_relations = [r for r in relations if str(file_path) in str(r.source_product.name)]
            if file_relations:
                formatted_content = self.formatter.format_relations(file_relations)
                readme_content.append(formatted_content)
        
        # Skriv README
        with open(group_dir / "README.md", 'w', encoding='utf-8') as f:
            f.write("\n".join(readme_content))

    def _log_results(self):
        """Loggar resultat av organiseringen"""
        logger.info("\n=== Resultat ===")
        logger.info(f"Processade filer med relationer: {len(self.relations_by_file)}")
        
        total_relations = sum(len(relations) for relations in self.relations_by_file.values())
        logger.info(f"Totalt antal relationer: {total_relations}")
        
        logger.info(f"Saknade filer: {len(self.missing_files)}")
        
        if self.missing_files:
            logger.warning("\nSaknade filer:")
            for file in sorted(self.missing_files):
                logger.warning(f"- {file}")

def main():
    # Konfigurera sökvägar - justera dessa efter behov
    source_dir = "./converted_docs"  # Ändra till din källkatalog
    output_dir = "./Compatibility_Documents"
    
    # Skapa och kör organiseraren
    organizer = EnhancedCompatibilityOrganizer(source_dir, output_dir)
    organizer.scan_and_organize()

if __name__ == "__main__":
    main()