import os
import re
import shutil
import logging
from typing import List, Dict, Set, Tuple
from pathlib import Path
from dataclasses import dataclass

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

@dataclass
class CompatibilityMatch:
    source_file: str
    matched_products: Set[str]
    context: str

class CompatibilityOrganizer:
    def __init__(self, source_dir: str, output_dir: str):
        self.source_dir = Path(source_dir)
        self.output_dir = Path(output_dir)
        self.compatibility_patterns = [
            r'(?i)passar\s+(?:till|med|för)\s+([^\.]+)',
            r'(?i)kompatibel\s+med\s+([^\.]+)',
            r'(?i)kan\s+användas\s+(?:till|med)\s+([^\.]+)',
            r'(?i)(?:monteras|installeras)\s+tillsammans\s+med\s+([^\.]+)',
            r'(?i)fungerar\s+(?:med|tillsammans\s+med)\s+([^\.]+)',
            r'(?i)(?:godkänd|certifierad)\s+för\s+(?:användning\s+med)?\s+([^\.]+)',
            r'(?i)anpassad\s+för\s+([^\.]+)'
        ]
        self.product_patterns = {
            'artikelnummer': r'(?i)(?:art(?:ikel)?\.?\s*(?:nr|number)?:?\s*)?(\d{5,8})',
            'product_name': r'(?i)(?:BB\s+\d+V\s+\d+A\s+FLX\s+[SML])',
            'model': r'(?i)(?:PRO[123](?:\s+v\d)?)'
        }
        self.files_processed: Dict[str, CompatibilityMatch] = {}
        self.missing_files: Set[str] = set()

    def scan_and_organize(self):
        """Huvudfunktion för att skanna och organisera kompatibilitetsdokument"""
        logger.info(f"Startar skanning av {self.source_dir}")
        
        # Skapa output-katalogen om den inte finns
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Skanna alla markdown-filer
        for file_path in self.source_dir.rglob("*.md"):
            self._process_file(file_path)
        
        # Organisera filer baserat på kompatibilitet
        self._organize_files()
        
        # Logga resultat
        self._log_results()

    def _process_file(self, file_path: Path):
        """Processar en enskild fil och extraherar kompatibilitetsinformation"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            matched_products = set()
            context = ""
            
            # Leta efter kompatibilitetsmatchningar
            for pattern in self.compatibility_patterns:
                matches = re.finditer(pattern, content, re.MULTILINE)
                for match in matches:
                    # Extrahera kontext (100 tecken före och efter matchningen)
                    start = max(0, match.start() - 100)
                    end = min(len(content), match.end() + 100)
                    context = content[start:end].strip()
                    
                    # Extrahera produktreferenser från matchningen
                    products = self._extract_product_references(match.group(1))
                    matched_products.update(products)
            
            if matched_products:
                self.files_processed[str(file_path)] = CompatibilityMatch(
                    source_file=str(file_path),
                    matched_products=matched_products,
                    context=context
                )
                logger.info(f"Hittade kompatibilitet i {file_path.name} med {len(matched_products)} produkter")
            
        except Exception as e:
            logger.error(f"Fel vid processning av {file_path}: {str(e)}")

    def _extract_product_references(self, text: str) -> Set[str]:
        """Extraherar produktreferenser från en text"""
        products = set()
        
        # Kolla efter olika typer av produktreferenser
        for pattern_type, pattern in self.product_patterns.items():
            matches = re.finditer(pattern, text)
            for match in matches:
                products.add(match.group(0))
        
        # Hantera tabellrader
        if '|' in text:
            # Splitta på | och rensa whitespace
            parts = [p.strip() for p in text.split('|')]
            for part in parts:
                # Kolla varje del efter produktreferenser
                for pattern_type, pattern in self.product_patterns.items():
                    if matches := re.finditer(pattern, part):
                        for match in matches:
                            products.add(match.group(0))
        
        return products

    def _organize_files(self):
        """Organiserar filer i kompatibilitetsgrupper"""
        # Skapa en mapping mellan produkter och filer
        product_to_files: Dict[str, Set[str]] = {}
        
        # Bygg produkt -> filer mapping
        for file_path, match_info in self.files_processed.items():
            for product in match_info.matched_products:
                if product not in product_to_files:
                    product_to_files[product] = set()
                product_to_files[product].add(file_path)
        
        # Skapa kompatibilitetsgrupper
        groups: List[Set[str]] = []
        processed_files = set()
        
        for file_path, match_info in self.files_processed.items():
            if file_path in processed_files:
                continue
            
            # Skapa en ny grupp som börjar med denna fil
            current_group = {file_path}
            related_products = match_info.matched_products
            
            # Lägg till alla filer som är relaterade till dessa produkter
            for product in related_products:
                current_group.update(product_to_files.get(product, set()))
            
            groups.append(current_group)
            processed_files.update(current_group)
        
        # Kopiera filer till sina respektive grupper
        for i, group in enumerate(groups, 1):
            group_dir = self.output_dir / f"compatibility_group_{i}"
            group_dir.mkdir(exist_ok=True)
            
            for file_path in group:
                try:
                    source_path = Path(file_path)
                    if source_path.exists():
                        shutil.copy2(source_path, group_dir)
                    else:
                        self.missing_files.add(str(file_path))
                        logger.warning(f"Fil saknas: {file_path}")
                except Exception as e:
                    logger.error(f"Fel vid kopiering av {file_path}: {str(e)}")
            
            # Skapa en README för gruppen
            self._create_group_readme(group_dir, group)

    def _create_group_readme(self, group_dir: Path, files: Set[str]):
        """Skapar en README-fil för en kompatibilitetsgrupp"""
        readme_content = ["# Kompatibilitetsgrupp\n\n## Inkluderade filer:\n"]
        
        for file_path in sorted(files):
            file_name = Path(file_path).name
            match_info = self.files_processed.get(file_path)
            
            readme_content.append(f"\n### {file_name}")
            if match_info:
                readme_content.append("\nKompatibel med:")
                for product in sorted(match_info.matched_products):
                    readme_content.append(f"- {product}")
                readme_content.append(f"\nKontext:\n```\n{match_info.context}\n```\n")
        
        with open(group_dir / "README.md", 'w', encoding='utf-8') as f:
            f.write("\n".join(readme_content))

    def _log_results(self):
        """Loggar resultatet av organiseringen"""
        logger.info("\n=== Resultat ===")
        logger.info(f"Processade filer: {len(self.files_processed)}")
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
    organizer = CompatibilityOrganizer(source_dir, output_dir)
    organizer.scan_and_organize()

if __name__ == "__main__":
    main()