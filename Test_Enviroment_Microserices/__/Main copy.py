import os
import shutil
import logging
from pathlib import Path
from typing import Dict, Set, List

from compatibility.extractor import CompatibilityExtractor
from compatibility.models import CompatibilityRelation, ProductReference
from compatibility.formatter import CompatibilityFormatter

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
                # Simulera sections dictionary som extractor förväntar sig
                sections = {"Compatibility": content}  # Förenkla genom att behandla hela innehållet som kompatibilitetssektion
                
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
                # Lägg till både käll- och målprodukter
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
            related_products = set()
            
            # Samla alla relaterade produkter
            for relation in relations:
                self._add_related_products(related_products, relation)
            
            # Lägg till alla filer relaterade till dessa produkter
            for product_ref in related_products:
                if product_ref.article_number:
                    current_group.update(
                        product_to_files.get(product_ref.article_number, set())
                    )
                if product_ref.name:
                    current_group.update(
                        product_to_files.get(product_ref.name, set())
                    )
            
            if current_group:
                group_dir = self._create_group_directory(group_counter, current_group)
                group_counter += 1
                processed_files.update(current_group)

    def _create_group_directory(self, group_number: int, files: Set[str]) -> Path:
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
        
        # Skapa README
        self._create_group_readme(group_dir, files)
        
        return group_dir

    def _create_group_readme(self, group_dir: Path, files: Set[str]):
        """Skapar en README-fil för gruppen med formaterad kompatibilitetsinformation"""
        readme_content = ["# Kompatibilitetsgrupp\n\n## Inkluderade filer:\n"]
        
        for file_path in sorted(files):
            file_name = Path(file_path).name
            relations = self.relations_by_file.get(file_path, [])
            
            if relations:
                readme_content.append(f"\n### {file_name}")
                formatted_content = self.formatter.format_relations(relations)
                readme_content.append(formatted_content)
        
        with open(group_dir / "README.md", 'w', encoding='utf-8') as f:
            f.write("\n".join(readme_content))

    def _add_to_product_mapping(self, mapping: Dict[str, Set[str]], 
                              product: ProductReference, file_path: str):
        """Lägger till en produkt i product -> files mappningen"""
        if product.article_number:
            mapping.setdefault(product.article_number, set()).add(file_path)
        if product.name:
            mapping.setdefault(product.name, set()).add(file_path)

    def _add_related_products(self, product_set: Set[ProductReference], 
                            relation: CompatibilityRelation):
        """Lägger till relaterade produkter från en relation i en set"""
        product_set.add(relation.source_product)
        product_set.add(relation.target_product)

    def _log_results(self):
        """Loggar resultat av organiseringen"""
        logger.info("\n=== Resultat ===")
        logger.info(f"Processade filer med relationer: {len(self.relations_by_file)}")
        logger.info(f"Saknade filer: {len(self.missing_files)}")
        
        if self.missing_files:
            logger.warning("\nSaknade filer:")
            for file in sorted(self.missing_files):
                logger.warning(f"- {file}")

def main():
    # Konfigurera sökvägar
    source_dir = "./converted_docs"  # Ändra till din källkatalog
    output_dir = "./Compatibility_Documents"
    
    # Skapa och kör organiseraren
    organizer = EnhancedCompatibilityOrganizer(source_dir, output_dir)
    organizer.scan_and_organize()

if __name__ == "__main__":
    main()