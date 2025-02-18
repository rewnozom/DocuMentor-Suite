# markdown_analyzer/extractors/compatibility/models.py
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Set
from enum import Enum

class RelationType(Enum):
    DIRECT = "direct"                # Direkt kompatibel
    CONDITIONAL = "conditional"      # Kompatibel under vissa villkor
    CERTIFIED = "certified"          # Certifierad kompatibilitet
    REQUIRES = "requires"            # Kräver denna produkt
    REPLACES = "replaces"            # Ersätter denna produkt
    REPLACED_BY = "replaced_by"      # Ersätts av denna produkt
    ACCESSORY = "accessory"         # Tillbehör till produkt

@dataclass
class TechnicalRequirement:
    """Tekniska krav för kompatibilitet"""
    category: str          # t.ex. "voltage", "dimensions", "protocol"
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    exact_value: Optional[str] = None
    unit: Optional[str] = None
    description: Optional[str] = None

@dataclass
class CompatibilityCondition:
    """Villkor för kompatibilitet"""
    condition_type: str    # t.ex. "installation", "environment", "configuration"
    description: str
    requirements: List[TechnicalRequirement] = field(default_factory=list)
    notes: Optional[str] = None

@dataclass
class ProductReference:
    """Referens till en produkt"""
    name: str
    article_number: Optional[str] = None
    series: Optional[str] = None
    variant: Optional[str] = None
    manufacturer: Optional[str] = None

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
    members: Set[str] = field(default_factory=set)  # artikelnummer
    common_compatibility: List[CompatibilityRelation] = field(default_factory=list)
    version_history: Dict[str, str] = field(default_factory=dict)  # version -> artikelnummer
