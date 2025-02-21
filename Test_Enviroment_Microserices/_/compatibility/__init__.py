# compatibility/__init__.py

from .patterns import (
    ARTICLE_NUMBER_PATTERNS,
    BASIC_COMPATIBILITY_PATTERNS,
    COMPATIBILITY_RELATIONSHIPS,
    REPLACEMENT_PATTERNS,
    CONDITION_PATTERNS,
    FAMILY_PATTERNS
)

from .extractor import CompatibilityExtractor
from .formatter import CompatibilityFormatter

from .models import (
    RelationType,
    ProductReference,
    CompatibilityRelation,
    CompatibilityCondition,
    ProductFamily,
    TrainingExample,
    TrainingMetadata
)

__all__ = [
    'CompatibilityExtractor',
    'CompatibilityFormatter',
    'RelationType',
    'ProductReference',
    'CompatibilityRelation',
    'CompatibilityCondition',
    'ProductFamily',
    'TrainingExample',
    'TrainingMetadata'
]