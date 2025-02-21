# markdown_analyzer/extractors/compatibility/__init__.py
from .extractor import CompatibilityExtractor
from .formatter import CompatibilityFormatter
from .models import (
    RelationType, TechnicalRequirement, CompatibilityCondition,
    ProductReference, CompatibilityRelation, ProductFamily
)
from .validator import CompatibilityValidator
from .patterns import (
    BASIC_COMPATIBILITY_PATTERNS, REPLACEMENT_PATTERNS,
    CONDITION_PATTERNS, FAMILY_PATTERNS,
    TECHNICAL_REQUIREMENT_PATTERNS, CERTIFICATION_PATTERNS
)

__all__ = [
    'CompatibilityExtractor',
    'CompatibilityFormatter',
    'CompatibilityValidator',
    'RelationType',
    'TechnicalRequirement',
    'CompatibilityCondition',
    'ProductReference',
    'CompatibilityRelation',
    'ProductFamily',
    'BASIC_COMPATIBILITY_PATTERNS',
    'REPLACEMENT_PATTERNS',
    'CONDITION_PATTERNS',
    'FAMILY_PATTERNS',
    'TECHNICAL_REQUIREMENT_PATTERNS',
    'CERTIFICATION_PATTERNS'
]
