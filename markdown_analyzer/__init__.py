# markdown_analyzer/__init__.py

# 1) Import from top-level modules:
from .analyzer import MarkdownAnalyzer
from .config import settings, Settings
from .validators import (
    CommandValidator,
    FullInfoValidator,
    SummaryValidator,
    TechnicalValidator,
    CompatibilityValidator,
    TrainingDataValidator,
)

# 2) Import from commands:
from .commands.dataset_commands import DatasetCommands

# 3) Import from core:
from .core import (
    DocumentStructure,
    TableInfo,
    ARTICLE_NUMBER_PATTERNS,
    COMPATIBILITY_PATTERNS,
    TECHNICAL_PATTERNS,
    CHARS_PER_SEGMENT,
    FIELD_LIMIT,
    CSV_SPLIT_ROWS,
    SUFFIX_MAP,
    VALID_DOCUMENT_TYPES,
    TECHNICAL_TABLE_HEADERS,
    MarkdownAnalyzerError,
    DocumentParsingError,
    ArticleNumberError,
    ValidationError,
)

# 4) Import from dataset:
from .dataset import (
    DatasetGenerator,
    DocumentProcessor,
    TrainingDataProcessor,
    DatasetValidator,
    DatasetExporter,
    MultiFormatExporter,
)

# 5) Import from extractors:
from .extractors import (
    BaseExtractor,
    MetadataExtractor,
    CompatibilityExtractor,
    TechnicalExtractor,
    ImageExtractor,
    PackagingExtractor,
)

# 5a) Import from extractors.compatibility:
from .extractors.compatibility import (
    CompatibilityFormatter,
    RelationType,
    TechnicalRequirement,
    CompatibilityCondition,
    ProductReference,
    CompatibilityRelation,
    ProductFamily,
    CompatibilityValidator as CompatibilityValidator_Compat,  # to avoid clash in name
    BASIC_COMPATIBILITY_PATTERNS,
    REPLACEMENT_PATTERNS,
    CONDITION_PATTERNS,
    FAMILY_PATTERNS,
    TECHNICAL_REQUIREMENT_PATTERNS,
    CERTIFICATION_PATTERNS,
)

# 5b) Import from extractors.summary:
from .extractors.summary import (
    SummaryFormatter,
    SummarySection,
    ProductSummary,
    SummaryProcessor,
)

# 5c) Import from extractors.technical:
from .extractors.technical import (
    TechnicalSpecification,
    TechnicalValue,
    TechnicalCategory,
    UnitCategory,
    TechnicalUnit,
    TECHNICAL_PATTERNS as TECHNICAL_PATTERNS_2,  # rename to avoid clash
    IMPORTANCE_INDICATORS,
    UNIT_DEFINITIONS,
)

# 6) Import from trainers:
from .trainers import (
    BaseTrainer,
    MarkdownFormatter,
    BasicInfoTrainer,
    SummaryTrainer,
    TechnicalTrainer,
    CompatibilityTrainer,
)

# 7) Import from utils:
from .utils import (
    TextProcessor,
    DataValidator as DataValidator_Utils,  # to avoid confusion with the dataset validator
    setup_logging,
    find_markdown_files,
    ensure_dir,
)

# -----------------------------------------------------------------------------
# AGGREGATE THEM ALL IN __all__:
# -----------------------------------------------------------------------------
__all__ = [
    # Top-level modules:
    "MarkdownAnalyzer",
    "settings",
    "Settings",
    # top-level validators.py
    "CommandValidator",
    "FullInfoValidator",
    "SummaryValidator",
    "TechnicalValidator",
    "CompatibilityValidator",
    "TrainingDataValidator",

    # commands
    "DatasetCommands",

    # core
    "DocumentStructure",
    "TableInfo",
    "ARTICLE_NUMBER_PATTERNS",
    "COMPATIBILITY_PATTERNS",
    "TECHNICAL_PATTERNS",
    "CHARS_PER_SEGMENT",
    "FIELD_LIMIT",
    "CSV_SPLIT_ROWS",
    "SUFFIX_MAP",
    "VALID_DOCUMENT_TYPES",
    "TECHNICAL_TABLE_HEADERS",
    "MarkdownAnalyzerError",
    "DocumentParsingError",
    "ArticleNumberError",
    "ValidationError",

    # dataset
    "DatasetGenerator",
    "DocumentProcessor",
    "TrainingDataProcessor",
    "DatasetValidator",
    "DatasetExporter",
    "MultiFormatExporter",

    # extractors (high-level)
    "BaseExtractor",
    "MetadataExtractor",
    "CompatibilityExtractor",
    "TechnicalExtractor",
    "ImageExtractor",
    "PackagingExtractor",

    # extractors.compatibility
    "CompatibilityFormatter",
    "RelationType",
    "TechnicalRequirement",
    "CompatibilityCondition",
    "ProductReference",
    "CompatibilityRelation",
    "ProductFamily",
    "CompatibilityValidator_Compat",
    "BASIC_COMPATIBILITY_PATTERNS",
    "REPLACEMENT_PATTERNS",
    "CONDITION_PATTERNS",
    "FAMILY_PATTERNS",
    "TECHNICAL_REQUIREMENT_PATTERNS",
    "CERTIFICATION_PATTERNS",

    # extractors.summary
    "SummaryFormatter",
    "SummarySection",
    "ProductSummary",
    "SummaryProcessor",

    # extractors.technical
    "TechnicalSpecification",
    "TechnicalValue",
    "TechnicalCategory",
    "UnitCategory",
    "TechnicalUnit",
    "TECHNICAL_PATTERNS_2",
    "IMPORTANCE_INDICATORS",
    "UNIT_DEFINITIONS",

    # trainers
    "BaseTrainer",
    "MarkdownFormatter",
    "BasicInfoTrainer",
    "SummaryTrainer",
    "TechnicalTrainer",
    "CompatibilityTrainer",

    # utils
    "TextProcessor",
    "DataValidator_Utils",
    "setup_logging",
    "find_markdown_files",
    "ensure_dir",
]
