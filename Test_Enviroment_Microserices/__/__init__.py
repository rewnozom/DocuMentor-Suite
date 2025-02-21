# markdown_analyzer/core/__init__.py

from .enums import TechnicalCategory, UnitCategory


from .document import DocumentStructure, TableInfo
from .patterns import (
    ARTICLE_NUMBER_PATTERNS,
    COMPATIBILITY_PATTERNS,  # Add this line
    COMPATIBILITY_RELATIONSHIPS,
    TECHNICAL_PATTERNS
)
from .constants import (
    CHARS_PER_SEGMENT,
    FIELD_LIMIT,
    CSV_SPLIT_ROWS,
    SUFFIX_MAP,
    VALID_DOCUMENT_TYPES,
    TECHNICAL_TABLE_HEADERS
)
from .compatibility.errors import (
    MarkdownAnalyzerError,
    DocumentParsingError,
    ArticleNumberError,
    ValidationError
)

__all__ = [
    'DocumentStructure',
    'TableInfo',
    'ARTICLE_NUMBER_PATTERNS',
    'COMPATIBILITY_PATTERNS',  # Add this line
    'COMPATIBILITY_RELATIONSHIPS',
    'TECHNICAL_PATTERNS',
    'CHARS_PER_SEGMENT',
    'FIELD_LIMIT',
    'CSV_SPLIT_ROWS',
    'SUFFIX_MAP',
    'VALID_DOCUMENT_TYPES',
    'TECHNICAL_TABLE_HEADERS',
    'MarkdownAnalyzerError',
    'DocumentParsingError',
    'ArticleNumberError',
    'ValidationError',
    'TechnicalUnit',
    'TechnicalCategory',
    'TechnicalSpecification',
    'TechnicalValue',
    'UnitCategory'
    
]