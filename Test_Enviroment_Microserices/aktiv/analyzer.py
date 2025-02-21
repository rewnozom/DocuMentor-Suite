# directory_analyzer.py
import logging
from pathlib import Path
from typing import List

# Importera ContentAnalyzer och Section från din content_analyzer-modul
from Patterns.content_analyzer import ContentAnalyzer, Section

class DirectoryMarkdownAnalyzer:
    """
    DirectoryMarkdownAnalyzer

    Denna klass ansvarar för att:
      - Skanna igenom en angiven katalog (och dess undermappar) med markdown‑filer.
      - Analysera varje fil med hjälp av ContentAnalyzer.
      - Skriva ut en översikt över de identifierade sektionerna för varje fil.
    
    Detta liknar organiseraren, men syftet här är att enbart analysera och rapportera filinnehållet.
    """
    def __init__(self, source_dir: str):
        self.source_dir = Path(source_dir)
        self.analyzer = ContentAnalyzer()
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def analyze_directory(self) -> None:
        """
        Skannar igenom källkatalogen och analyserar varje markdown-fil.
        """
        markdown_files = list(self.source_dir.rglob("*.md"))
        self.logger.info(f"Hittade {len(markdown_files)} markdown-filer i {self.source_dir}")
        for file in markdown_files:
            self.logger.info(f"\nAnalyserar fil: {file}")
            try:
                content = file.read_text(encoding="utf-8")
            except Exception as e:
                self.logger.error(f"Fel vid läsning av {file}: {e}")
                continue

            sections = self.analyzer.analyze_content(content)
            self.print_analysis(file, sections)

    def print_analysis(self, file: Path, sections: List[Section]) -> None:
        """
        Skriver ut en översikt över de identifierade sektionerna i en fil.
        """
        print(f"\n=== Analys av fil: {file.name} ===")
        if not sections:
            print("Inga sektioner identifierades.")
            return

        for i, section in enumerate(sections, start=1):
            print(f"\nSektion {i}:")
            print(f"  Typ: {section.type.name}")
            print(f"  Rader: {section.start_line} - {section.end_line}")
            print(f"  Konfidens: {section.confidence:.2f}")
            related = section.related_sections if section.related_sections else "Inga"
            print(f"  Relaterade sektioner: {related}")
            print("  Innehåll:")
            print(section.content)
            print("-" * 40)

def main():
    # Ange din källkatalog här
    source_dir = "./converted_docs"
    analyzer = DirectoryMarkdownAnalyzer(source_dir)
    analyzer.analyze_directory()

if __name__ == "__main__":
    main()
