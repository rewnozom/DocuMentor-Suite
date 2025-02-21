"""
models.py – Modelldefinitioner för kompatibilitetsdata

Denna modul samlar alla dataklasser och enums som används för att representera
kompatibilitetsrelationer, produktreferenser, tekniska krav, villkor, produktfamiljer samt
utökad information för AI-träningsdata.

Den inkluderar modeller från både V1 och V2 av din kodbas.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Set
from enum import Enum

# =============================================================================
# Enum & Grundläggande Produktreferens
# =============================================================================

class RelationType(Enum):
    """
    Enum för de olika typerna av kompatibilitetsrelationer.
    """
    DIRECT = "direct"                # Direkt kompatibel
    CONDITIONAL = "conditional"      # Kompatibel under vissa villkor
    CERTIFIED = "certified"          # Certifierad kompatibilitet
    REQUIRES = "requires"            # Kräver denna produkt
    REPLACES = "replaces"            # Ersätter denna produkt
    REPLACED_BY = "replaced_by"      # Ersätts av denna produkt
    ACCESSORY = "accessory"          # Tillbehör till produkt

@dataclass(frozen=True)
class ProductReference:
    """
    Referens till en produkt.

    Klassen är oföränderlig (immutable) vilket gör den säker att använda som nyckel i mängder och dictionaries.
    """
    name: str
    article_number: Optional[str] = None
    series: Optional[str] = None
    variant: Optional[str] = None
    manufacturer: Optional[str] = None

    def __hash__(self):
        return hash((self.name, self.article_number, self.series, self.variant, self.manufacturer))

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

# =============================================================================
# Tekniska Krav, Villkor och Kompatibilitetsrelationer
# =============================================================================

@dataclass
class TechnicalRequirement:
    """
    Tekniska krav för kompatibilitet.
    
    Exempel: "voltage", "dimensions", "protocol" med eventuella min/max-värden, exakt värde, enhet och beskrivning.
    """
    category: str
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    exact_value: Optional[str] = None
    unit: Optional[str] = None
    description: Optional[str] = None

@dataclass
class CompatibilityCondition:
    """
    Villkor för kompatibilitet.
    
    Inkluderar en typ (t.ex. "installation", "environment", "configuration"), en beskrivning, eventuella tekniska krav
    och ytterligare noteringar.
    """
    condition_type: str
    description: str
    requirements: List[TechnicalRequirement] = field(default_factory=list)
    notes: Optional[str] = None

@dataclass
class CompatibilityRelation:
    """
    Detaljerad kompatibilitetsrelation mellan produkter.
    
    Inkluderar käll- och målprodukt, relationstyp, eventuella villkor och tekniska krav,
    certifiering, noteringar, referens till dokumentation, en konfidensnivå och kontext.
    """
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

# =============================================================================
# Produktfamilj
# =============================================================================

@dataclass
class ProductFamily:
    """
    Information om en produktfamilj eller serie.
    
    Innehåller namn, en valfri beskrivning, medlemmar (artikelnummer), gemensam kompatibilitet
    samt en versionshistorik.
    """
    name: str
    description: Optional[str] = None
    members: Set[str] = field(default_factory=set)
    common_compatibility: List[CompatibilityRelation] = field(default_factory=list)
    version_history: Dict[str, str] = field(default_factory=dict)

# =============================================================================
# Utökad Produktreferens
# =============================================================================

@dataclass
class EnhancedProductReference:
    """
    Utökad produktreferens med ytterligare identifierare.
    
    Innehåller standardfält samt extra fält som:
      - copiax_article: Huvudartikelnummer (ex. Copiax)
      - supplier_article: Leverantörens artikelnummer
      - ean: EAN-kod
      - additional_info: Ytterligare metadata om produkten
    """
    name: str
    copiax_article: Optional[str] = None
    supplier_article: Optional[str] = None
    ean: Optional[str] = None
    series: Optional[str] = None
    variant: Optional[str] = None
    additional_info: Dict[str, str] = field(default_factory=dict)

    def to_basic_reference(self) -> ProductReference:
        """
        Konverterar denna EnhancedProductReference till en grundläggande ProductReference.
        """
        return ProductReference(
            name=self.name,
            article_number=self.copiax_article,
            series=self.series,
            variant=self.variant,
            manufacturer=self.additional_info.get("manufacturer")
        )

# =============================================================================
# Träningsdata- och Kommandomodeller
# =============================================================================

@dataclass
class TrainingExample:
    """
    Representerar ett träningsdataexempel för AI-modellering.
    
    Innehåller användarinput, förväntat AI-svar, en valfri källa samt en konfidensnivå.
    """
    user_input: str
    ai_output: str
    source: Optional[str] = None
    confidence: float = 1.0

@dataclass
class CommandRelation:
    """
    Representerar en relation i ett kommandobaserat gränssnitt.
    
    Innehåller källa, mål, relationstyp, kontext, konfidens och extra metadata.
    """
    source: str
    target: str
    relation_type: str
    context: Optional[str] = None
    confidence: float = 1.0
    metadata: Dict[str, str] = field(default_factory=dict)

# =============================================================================
# Metadata för Träningsdatagenerering
# =============================================================================

@dataclass
class TrainingMetadata:
    """
    Metadata för generering av träningsdata.
    
    Samlar statistik som:
      - Totalt antal processade filer
      - Totalt antal funna relationer
      - Totalt antal genererade träningsdataexempel
      - Lista på filer som gett fel
      - Övriga bearbetningsstatistik
    """
    total_files_processed: int = 0
    total_relations_found: int = 0
    total_examples_generated: int = 0
    files_with_errors: Set[str] = field(default_factory=set)
    processing_stats: Dict[str, int] = field(default_factory=dict)

    def add_error(self, filename: str):
        """Lägger till en fil i error-listan."""
        self.files_with_errors.add(filename)

    def increment_stat(self, stat_name: str, value: int = 1):
        """Ökar en statistik-räknare."""
        self.processing_stats[stat_name] = self.processing_stats.get(stat_name, 0) + value

    def get_summary(self) -> Dict[str, any]:
        """Returnerar en sammanfattning av den insamlade metadatan."""
        return {
            "total_files": self.total_files_processed,
            "total_relations": self.total_relations_found,
            "total_examples": self.total_examples_generated,
            "error_files": len(self.files_with_errors),
            "stats": self.processing_stats
        }
