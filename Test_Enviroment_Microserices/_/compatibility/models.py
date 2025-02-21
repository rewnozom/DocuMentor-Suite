# compatibility/models.py

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Set
from enum import Enum

class RelationType(Enum):
    """Definierar typer av relationer mellan produkter"""
    DIRECT = "direct"             # Direkt kompatibilitet
    CONDITIONAL = "conditional"   # Kompatibel under vissa villkor
    REQUIRES = "requires"         # Kräver denna produkt
    REPLACES = "replaces"        # Ersätter en annan produkt
    REPLACED_BY = "replaced_by"   # Ersätts av en annan produkt
    ACCESSORY = "accessory"       # Tillbehör till produkt

@dataclass(frozen=True)
class ProductReference:
    """Referens till en produkt"""
    name: str
    article_number: Optional[str] = None
    series: Optional[str] = None
    variant: Optional[str] = None

    def __hash__(self):
        return hash((
            self.name,
            self.article_number,
            self.series,
            self.variant
        ))

@dataclass
class CompatibilityCondition:
    """Villkor för kompatibilitet"""
    condition_type: str
    description: str
    notes: Optional[str] = None

@dataclass
class CompatibilityRelation:
    """Kompatibilitetsrelation mellan produkter"""
    source_product: ProductReference
    target_product: ProductReference
    relation_type: RelationType
    conditions: List[CompatibilityCondition] = field(default_factory=list)
    compatibility_notes: Optional[str] = None
    confidence: float = 1.0
    context: Optional[str] = None

@dataclass
class ProductFamily:
    """Information om produktfamilj/serie"""
    name: str
    description: Optional[str] = None
    members: Set[str] = field(default_factory=set)
    common_compatibility: List[CompatibilityRelation] = field(default_factory=list)

@dataclass
class TrainingExample:
    """Träningsexempel för LLM"""
    user_input: str           # Input från användaren (-c kommando)
    ai_output: str           # Formaterat svar
    source: Optional[str] = None  # Källdokument
    confidence: float = 1.0   # Konfidensnivå för exemplet

@dataclass
class TrainingMetadata:
    """Metadata för träningsdatagenerering"""
    total_files_processed: int = 0
    total_relations_found: int = 0
    total_examples_generated: int = 0
    files_with_errors: Set[str] = field(default_factory=set)
    processing_stats: Dict[str, int] = field(default_factory=dict)

    def add_error(self, filename: str):
        """Lägger till en fil i error-listan"""
        self.files_with_errors.add(filename)

    def get_summary(self) -> Dict[str, any]:
        """Returnerar en sammanfattning av metadatan"""
        return {
            "total_files": self.total_files_processed,
            "total_relations": self.total_relations_found,
            "total_examples": self.total_examples_generated,
            "error_files": len(self.files_with_errors),
            "stats": self.processing_stats
        }