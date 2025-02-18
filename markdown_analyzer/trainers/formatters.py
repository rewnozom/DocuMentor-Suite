# markdown_analyzer/trainers/formatters.py
from typing import List
class MarkdownFormatter:
    """Hanterar formattering av markdown-output"""
    
    def format_heading(self, text: str, level: int = 1) -> str:
        """Formaterar en rubrik"""
        return f"{'#' * level} {text}\n\n"
    
    def format_image(self, image_ref: str, alt_text: str = "") -> str:
        """Formaterar en bildreferens"""
        return f"![{alt_text}]{image_ref}\n\n"
    
    def format_list(self, items: List[str], ordered: bool = False) -> str:
        """Formaterar en lista"""
        formatted = []
        for i, item in enumerate(items, 1):
            prefix = f"{i}. " if ordered else "- "
            formatted.append(f"{prefix}{item}")
        return "\n".join(formatted) + "\n\n"
    
    def format_table(self, headers: List[str], rows: List[List[str]]) -> str:
        """Formaterar en tabell"""
        table = []
        # Lägg till rubriker
        table.append("| " + " | ".join(headers) + " |")
        # Lägg till separator
        table.append("| " + " | ".join(["---"] * len(headers)) + " |")
        # Lägg till rader
        for row in rows:
            table.append("| " + " | ".join(row) + " |")
        return "\n".join(table) + "\n\n"