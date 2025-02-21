
# errors.py
"""Anpassade felklasser för markdown-analysatorn"""


from typing import Any, Dict, Optional

class MarkdownAnalyzerError(Exception):
    """Basfel för Markdown Analyzer."""
    def __init__(self, message: str, details: Optional[Dict] = None):
        self.message = message
        self.details = details or {}
        super().__init__(self.message)

class ExtractionError(MarkdownAnalyzerError):
    """Fel vid informationsutvinning."""
    def __init__(self, message: str, extractor_name: str, source: str):
        details = {'extractor': extractor_name, 'source': source}
        super().__init__(f"Extraction error in {extractor_name}: {message}", details)
