# compatibility/models.py
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Set
from enum import Enum

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set


class RelationType(Enum):
    DIRECT = "direct"
    CONDITIONAL = "conditional"
    CERTIFIED = "certified"
    REQUIRES = "requires"
    REPLACES = "replaces"
    REPLACED_BY = "replaced_by"
    ACCESSORY = "accessory"

@dataclass(frozen=True)  # Make it immutable
class ProductReference:
    """Referens till en produkt"""
    name: str
    article_number: Optional[str] = None
    series: Optional[str] = None
    variant: Optional[str] = None
    manufacturer: Optional[str] = None

    def __hash__(self):
        # Create a unique hash based on immutable attributes
        return hash((
            self.name,
            self.article_number,
            self.series,
            self.variant,
            self.manufacturer
        ))

    def __eq__(self, other):
        if not isinstance(other, ProductReference):
            return False
        return (
            self.name == other.name and
            self.article_number == other.article_number and
            self.series == other.series and
            self.variant == other.variant and
            self.manufacturer == other.manufacturer
        )

@dataclass
class TechnicalRequirement:
    """Tekniska krav för kompatibilitet"""
    category: str
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    exact_value: Optional[str] = None
    unit: Optional[str] = None
    description: Optional[str] = None

@dataclass
class CompatibilityCondition:
    """Villkor för kompatibilitet"""
    condition_type: str
    description: str
    requirements: List[TechnicalRequirement] = field(default_factory=list)
    notes: Optional[str] = None

@dataclass
class CompatibilityRelation:
    """Detaljerad kompatibilitetsrelation mellan produkter"""
    source_product: ProductReference
    target_product: ProductReference
    relation_type: RelationType
    conditions: List[CompatibilityCondition] = field(default_factory=list)
    technical_requirements: List[TechnicalRequirement] = field(default_factory=list)
    certification: Optional[str] = None
    compatibility_notes: Optional[str] = None
    documentation_ref: Optional[str] = None
    confidence: float = 1.0
    context: Optional[str] = None

@dataclass
class ProductFamily:
    """Information om produktfamilj/serie"""
    name: str
    description: Optional[str] = None
    members: Set[str] = field(default_factory=set)
    common_compatibility: List[CompatibilityRelation] = field(default_factory=list)
    version_history: Dict[str, str] = field(default_factory=dict)


@dataclass
class EnhancedProductReference:
    """Utökad produktreferens med fler identifierare"""
    name: str
    copiax_article: Optional[str] = None
    supplier_article: Optional[str] = None
    ean: Optional[str] = None
    series: Optional[str] = None
    variant: Optional[str] = None
    additional_info: Dict[str, str] = field(default_factory=dict)

    def to_basic_reference(self) -> ProductReference:
        """Konverterar till en basic ProductReference"""
        return ProductReference(
            name=self.name,
            article_number=self.copiax_article,
            series=self.series,
            variant=self.variant
        )

@dataclass
class TrainingExample:
    """Representerar ett träningsexempel"""
    user_input: str
    ai_output: str
    source: Optional[str] = None
    confidence: float = 1.0

@dataclass
class CommandRelation:
    """Representerar en kommandorelation"""
    source: str
    target: str
    relation_type: str
    context: Optional[str] = None
    confidence: float = 1.0
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class TrainingMetadata:
    """Metadata för träningsdatagenereringen"""
    total_files_processed: int = 0
    total_relations_found: int = 0
    total_examples_generated: int = 0
    files_with_errors: Set[str] = field(default_factory=set)
    processing_stats: Dict[str, int] = field(default_factory=dict)

    def add_error(self, filename: str):
        """Lägger till en fil i error-listan"""
        self.files_with_errors.add(filename)

    def increment_stat(self, stat_name: str, value: int = 1):
        """Ökar en statistik-räknare"""
        self.processing_stats[stat_name] = self.processing_stats.get(stat_name, 0) + value

    def get_summary(self) -> Dict[str, any]:
        """Returnerar en sammanfattning av metadatan"""
        return {
            "total_files": self.total_files_processed,
            "total_relations": self.total_relations_found,
            "total_examples": self.total_examples_generated,
            "error_files": len(self.files_with_errors),
            "stats": self.processing_stats
        }