# preprocessing_main.py

import os
import re
import shutil
import logging
from pathlib import Path
from typing import Optional, List, Dict, Tuple
from preprocessing_patterns import ContentAnalyzer, Section, SectionType
import concurrent.futures
import time

# För att dynamiskt kontrollera CPU-användning
try:
    import psutil
except ImportError:
    psutil = None  # Om psutil inte finns, kommer vi inte att dynamiskt övervaka CPU

# Maximal CPU-användning (i procent) innan vi inte skickar in fler trådar
CPU_THRESHOLD = 85

# Max antal retries vid fel
MAX_RETRIES = 1

# Globala listor för rapportering
success_files = []
failure_files = []


class MarkdownPreProcessor:
    """
    Pre-processor för markdown-filer som extraherar produktinformation och kompatibilitetsrelationer och
    strukturerar om filerna enligt den ursprungliga mappstrukturen. Endast dokument med relevant kompatibilitetsinformation
    kopieras till "./1_Prebehandlade_dokument/".
    """
    def __init__(self, source_dir: str = "./converted_docs", 
                 target_dir: str = "./1_Prebehandlade_dokument"):
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir)
        self.analyzer = ContentAnalyzer()
        self.setup_logging()
        
    def setup_logging(self):
        """Konfigurerar loggning."""
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        log_dir = Path("log/1_Prebehandlade_dokument")
        log_dir.mkdir(parents=True, exist_ok=True)
        
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        handlers = {
            'console': logging.StreamHandler(),
            'terminal': logging.FileHandler(log_dir / "terminal.log", encoding='utf-8'),
            'success': logging.FileHandler(log_dir / "success.log", encoding='utf-8'),
            'warning': logging.FileHandler(log_dir / "warnings.log", encoding='utf-8'),
            'error': logging.FileHandler(log_dir / "errors.log", encoding='utf-8')
        }
        
        for handler in handlers.values():
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def _clean_path(self, file_path: Path) -> Path:
        """
        Rensar och standardiserar filnamnet genom att:
          - Ta bort specialtecken och URL-referenser.
          - Extrahera artikelnummer (om möjligt) och lägga till ett eventuellt suffix.
        """
        path_str = str(file_path)
        path_str = re.sub(r'[➊➋➌]', '', path_str)
        path_str = re.sub(
            r'(?i)copiax(?:se)?https?(?:www)?(?:\.)?copiax(?:\.)?se(?:\s+)?(?:images|doc)?', 
            '', 
            path_str
        )
        article_match = re.search(r'(\d{8}|\d{7}|\d{6})', path_str)
        if article_match:
            article_number = article_match.group(1)
            doc_type = ''
            if '_pro' in path_str.lower():
                doc_type = '_pro'
            elif '_man' in path_str.lower():
                doc_type = '_man'
            elif '_sak' in path_str.lower():
                doc_type = '_sak'
            elif '_tek' in path_str.lower():
                doc_type = '_tek'
            new_name = f"{article_number}{doc_type}"
            if file_path.suffix:
                new_name += file_path.suffix
            return Path(new_name)
        clean_name = re.sub(r'[^\w\s-]', '', path_str)
        clean_name = re.sub(r'\s+', '_', clean_name.strip())
        return Path(clean_name)

    def create_directory_structure(self, file_path: Path) -> Tuple[Path, Path]:
        """
        Skapar målstrukturen baserat på den relativa sökvägen från source_dir.
        Filerna placeras i samma undermappstruktur, med mapparna 'behandlade' och 'original'.
        """
        try:
            rel_path = file_path.parent.relative_to(self.source_dir)
        except ValueError:
            rel_path = Path(file_path.parent.name)
        
        treated_dir = self.target_dir / rel_path / "behandlade"
        original_dir = self.target_dir / rel_path / "original"
        treated_dir.mkdir(parents=True, exist_ok=True)
        original_dir.mkdir(parents=True, exist_ok=True)
        return treated_dir, original_dir

    def process_markdown(self, content: str) -> Optional[str]:
        """
        Processar markdown-innehållet, extraherar relevanta sektioner (produktinfo och 
        kompatibilitetsrelationer) och returnerar den sammanslagna texten. Om inga relevanta 
        sektioner eller relationer hittas returneras None.
        """
        try:
            sections = self.analyzer.analyze_content(content)
            if not sections:
                self.logger.warning("Inga sektioner hittades i innehållet")
                return None

            self.log_sections(sections)
            
            relevant_sections = self.analyzer.filter_relevant_sections(sections)
            if not relevant_sections:
                self.logger.warning("Inga relevanta sektioner hittades")
                return None
            
            all_relations = []
            for section in relevant_sections:
                relations = self.analyzer.matcher.extract_relations(section.content)
                if relations:
                    all_relations.extend(relations)
            if not all_relations:
                self.logger.warning("Inga kompatibilitetsrelationer hittades i dokumentet")
                return None
            
            processed_content = self.analyzer.merge_related_sections(relevant_sections)
            if not self.validate_processed_content(processed_content, sections):
                self.logger.warning("Validering av processat innehåll misslyckades")
                return None
                
            return processed_content
        except Exception as e:
            self.logger.error(f"Fel vid processning av markdown: {str(e)}")
            return None

    def log_sections(self, sections: List[Section]):
        """Loggar en översikt över de identifierade sektionerna."""
        self.logger.info("Identifierade sektioner:")
        for i, section in enumerate(sections):
            self.logger.info(
                f"Sektion {i+1}: Typ={section.type.name}, "
                f"Rader={section.start_line}-{section.end_line}, "
                f"Konfidens={section.confidence:.2f}, "
                f"Relaterade sektioner={section.related_sections or 'Inga'}"
            )

    def validate_processed_content(self, processed_content: str, original_sections: List[Section]) -> bool:
        """
        Enkel validering: säkerställer att viss produktinformation (artikelnummer) finns kvar.
        """
        if not processed_content:
            return False
            
        original_articles = set()
        processed_articles = set()
        
        for section in original_sections:
            if section.type in {SectionType.PRODUCT_INFO, SectionType.COMPATIBILITY}:
                original_articles.update(self.analyzer.matcher.extract_article_numbers(section.content))
        processed_articles.update(self.analyzer.matcher.extract_article_numbers(processed_content))
        
        if original_articles and not processed_articles.intersection(original_articles):
            self.logger.warning("Viktiga artikelnummer saknas i processat innehåll")
            return False
            
        return True

    def process_file(self, file_path: Path) -> None:
        """
        Processar en enskild markdown-fil. Endast om filen innehåller relevant kompatibilitetsinformation
        skapas målmappar och filen kopieras.
        Med retry-logik (max 1 retry vid fel).
        """
        retries = 0
        while retries <= MAX_RETRIES:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                processed_content = self.process_markdown(content)
                if processed_content is None:
                    self.logger.warning(f"Ingen relevant information extraherad från {file_path}")
                    failure_files.append((str(file_path), "Ingen kompatibilitetsinformation"))
                    return
                
                cleaned_file_name = self._clean_path(file_path)
                treated_dir, original_dir = self.create_directory_structure(file_path)
                
                treated_file = treated_dir / cleaned_file_name
                with open(treated_file, 'w', encoding='utf-8') as f:
                    f.write(processed_content)
                
                original_file = original_dir / cleaned_file_name
                shutil.copy2(file_path, original_file)
                
                self.logger.info(
                    f"Processad fil: {cleaned_file_name}\n"
                    f"Original: {file_path}\n"
                    f"Ny sökväg: {treated_file}\n"
                    f"Original storlek: {len(content)} tecken\n"
                    f"Processad storlek: {len(processed_content)} tecken"
                )
                success_files.append(str(file_path))
                return
            except Exception as e:
                self.logger.error(f"Fel vid processning av {file_path}: {str(e)}")
                retries += 1
                if retries <= MAX_RETRIES:
                    self.logger.info(f"Retry {retries} för {file_path}")
                else:
                    failure_files.append((str(file_path), str(e)))
                    return

    def process_directory(self, dir_path: Optional[Path] = None) -> None:
        """
        Processar alla markdown-filer i en katalog och dess underkataloger.
        Endast de filer som innehåller relevant kompatibilitetsinformation behandlas.
        Parallellisering sker med ThreadPoolExecutor och CPU-belastning övervakas.
        """
        if dir_path is None:
            dir_path = self.source_dir

        files = list(dir_path.rglob("*.md"))
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = []
            for file in files:
                # Om psutil finns, kontrollera CPU-belastning
                if psutil:
                    while psutil.cpu_percent(interval=0.1) > CPU_THRESHOLD:
                        self.logger.info("CPU-belastningen över 85%, väntar innan ny fil skickas in...")
                        time.sleep(1)
                futures.append(executor.submit(self.process_file, file))
            # Vänta på att alla uppgifter ska slutföras
            concurrent.futures.wait(futures)

    def get_statistics(self) -> Dict:
        """Returnerar statistik över processningen."""
        return {
            "total_files_processed": len(list(self.source_dir.rglob("*.md"))),
            "total_files_generated": len(list(self.target_dir.rglob("*.md"))),
            "source_directory": str(self.source_dir),
            "target_directory": str(self.target_dir),
            "processed_directories": len(list(self.target_dir.rglob("behandlade"))),
            "original_directories": len(list(self.target_dir.rglob("original"))),
            "successful_files": len(success_files),
            "failed_files": len(failure_files)
        }

    def write_summary_report(self):
        """
        Skriver en sammanfattande rapport över processade filer till markdown-filer i loggmappen.
        """
        report_dir = Path("log/1_Prebehandlade_dokument")
        success_report = report_dir / "success_summary.md"
        failure_report = report_dir / "failure_summary.md"
        
        with open(success_report, 'w', encoding='utf-8') as f:
            f.write("# Sammanfattning av lyckade filer\n\n")
            for file in success_files:
                f.write(f"- {file}\n")
        
        with open(failure_report, 'w', encoding='utf-8') as f:
            f.write("# Sammanfattning av misslyckade filer\n\n")
            for file, reason in failure_files:
                f.write(f"- {file} | Orsak: {reason}\n")

    def run(self):
        """Huvudmetod för att köra preprocessorn."""
        from datetime import datetime
        self.logger.info(f"{'='*50}")
        self.logger.info(f"Ny körning startad: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.logger.info(f"{'='*50}")
        
        self.process_directory()
        
        stats = self.get_statistics()
        self.logger.info("Pre-processing slutförd:")
        for key, value in stats.items():
            self.logger.info(f"{key}: {value}")
        
        self.write_summary_report()
        
        self.logger.info(f"{'='*50}\n")

if __name__ == "__main__":
    processor = MarkdownPreProcessor()
    processor.run()
