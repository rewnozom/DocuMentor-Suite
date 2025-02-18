
# markdown_analyzer/core/errors.py
"""Anpassade felklasser för markdown-analysatorn"""


from typing import Any, Dict, Optional

class MarkdownAnalyzerError(Exception):
    """Basfel för Markdown Analyzer."""
    def __init__(self, message: str, details: Optional[Dict] = None):
        self.message = message
        self.details = details or {}
        super().__init__(self.message)

class DocumentParsingError(MarkdownAnalyzerError):
    """Fel vid dokumentparsning."""
    def __init__(self, message: str, filename: str, line_number: Optional[int] = None):
        details = {'filename': filename, 'line_number': line_number}
        super().__init__(f"Parsing error in {filename}: {message}", details)

class ArticleNumberError(MarkdownAnalyzerError):
    """Fel relaterade till artikelnummer."""
    def __init__(self, message: str, article_number: str, context: str):
        details = {'article_number': article_number, 'context': context}
        super().__init__(f"Article number error ({article_number}): {message}", details)

class ExtractionError(MarkdownAnalyzerError):
    """Fel vid informationsutvinning."""
    def __init__(self, message: str, extractor_name: str, source: str):
        details = {'extractor': extractor_name, 'source': source}
        super().__init__(f"Extraction error in {extractor_name}: {message}", details)

class ValidationError(MarkdownAnalyzerError):
    """Fel vid datavalidering."""
    def __init__(self, message: str, validator_name: str, data: Any):
        details = {'validator': validator_name, 'data': str(data)}
        super().__init__(f"Validation error in {validator_name}: {message}", details)

class ProcessingError(MarkdownAnalyzerError):
    """Fel vid dokumentbearbetning."""
    def __init__(self, message: str, stage: str, document: Optional[str] = None):
        details = {'stage': stage, 'document': document}
        super().__init__(f"Processing error in {stage}: {message}", details)

class DatasetGenerationError(MarkdownAnalyzerError):
    """Fel vid datasetgenerering."""
    def __init__(self, message: str, command: str, details: Dict):
        super().__init__(f"Dataset generation error for command '{command}': {message}", details)
