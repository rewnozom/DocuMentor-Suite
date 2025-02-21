# markdown_analyzer/core/document.py

from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import List, Dict, Any, Optional

# Grundläggande komponenter

@dataclass
class ProductImage:
    """Information om produktbild"""
    image_ref: str
    page_num: int
    image_num: int
    mapped_path: str

@dataclass
class Compatibility:
    """Information om kompatibilitet mellan produkter"""
    type: str  # t.ex. 'fits', 'requires', 'replaces', 'accessory'
    target_article: str
    description: str
    source_section: str
    confidence: float
    context: str = ""
    source_file: str = ""

@dataclass
class TechnicalSpec:
    """Teknisk specifikation för en produkt"""
    category: str
    value: str
    unit: Optional[str]
    source: str
    confidence: float = 1.0

@dataclass
class InstallationInfo:
    """Installationsinformation och krav"""
    requirements: List[str]
    steps: List[str]
    warnings: List[str]
    tools_needed: List[str]
    related_products: List[str] = field(default_factory=list)
    source_sections: List[str] = field(default_factory=list)

@dataclass
class TableInfo:
    """Information extraherad från tabeller"""
    headers: List[str]
    rows: List[List[str]]
    context: str
    type: str = ""

@dataclass
class CrossReference:
    """Referens till andra produkter"""
    source_article: str
    referenced_article: str
    context: str
    reference_type: str
    location: str
    confidence: float = 1.0

# Utökad metadata och kompletterande information

@dataclass
class DocumentMetadata:
    """Utökad metadata-information."""
    created_date: Optional[datetime] = None
    last_modified: Optional[datetime] = None
    version: str = "1.0"
    language: str = "sv"
    author: Optional[str] = None
    department: Optional[str] = None
    status: str = "active"

@dataclass
class MaintenanceInfo:
    """Underhållskrav och scheman."""
    cleaning_instructions: List[str] = field(default_factory=list)
    inspection_intervals: List[str] = field(default_factory=list)
    required_tools: List[str] = field(default_factory=list)
    spare_parts: List[str] = field(default_factory=list)
    service_contacts: List[str] = field(default_factory=list)

@dataclass
class EnvironmentalRequirements:
    """Miljökrav och gränsvärden."""
    temperature_range: Optional[str] = None
    humidity_range: Optional[str] = None
    ip_rating: Optional[str] = None
    altitude_limits: Optional[str] = None
    noise_level: Optional[str] = None

@dataclass
class SafetyInfo:
    """Säkerhetsinformation och certifieringar."""
    warnings: List[str] = field(default_factory=list)
    certifications: List[str] = field(default_factory=list)
    protection_class: Optional[str] = None
    risk_class: Optional[str] = None
    safety_features: List[str] = field(default_factory=list)

@dataclass
class DocumentSection:
    """Utökad sektioninformation."""
    title: str
    content: str
    level: int
    order: int
    subsections: List['DocumentSection'] = field(default_factory=list)
    attributes: Dict[str, Any] = field(default_factory=dict)

# Den utökade dokumentstrukturen

@dataclass
class DocumentStructure:
    """Utökad dokumentstruktur."""
    # Grundläggande information
    filename: str
    article_number: str
    document_type: str
    product_name: str
    description: str
    manufacturer: Optional[str] = None

    # Metadata
    metadata: DocumentMetadata = field(default_factory=DocumentMetadata)
    
    # Innehållskomponenter
    product_images: List[ProductImage] = field(default_factory=list)
    compatibility: List[Compatibility] = field(default_factory=list)
    accessories: List[str] = field(default_factory=list)
    spare_parts: List[str] = field(default_factory=list)
    cross_references: List[CrossReference] = field(default_factory=list)
    technical_specs: List[TechnicalSpec] = field(default_factory=list)
    
    # Utökad information
    environmental_reqs: EnvironmentalRequirements = field(default_factory=EnvironmentalRequirements)
    safety_info: SafetyInfo = field(default_factory=SafetyInfo)
    maintenance_info: MaintenanceInfo = field(default_factory=MaintenanceInfo)
    
    # Dokumentstruktur
    sections: Dict[str, DocumentSection] = field(default_factory=dict)
    tables: List[TableInfo] = field(default_factory=list)
    warnings: List[Dict[str, Any]] = field(default_factory=list)
    
    # Validering och bearbetning
    last_updated: str = field(default_factory=lambda: datetime.now().isoformat())
    processing_errors: List[str] = field(default_factory=list)
    confidence_score: float = 1.0
    validation_status: Dict[str, bool] = field(default_factory=dict)
    
    # Versionskontroll
    version_history: List[Dict[str, Any]] = field(default_factory=list)
    related_documents: List[str] = field(default_factory=list)
    
    def add_version(self, version: str, changes: str, author: str):
        """Lägg till en ny version i versionshistoriken."""
        self.version_history.append({
            'version': version,
            'changes': changes,
            'author': author,
            'timestamp': datetime.now().isoformat()
        })
    
    def add_section(self, title: str, content: str, level: int = 1) -> DocumentSection:
        """Lägg till en ny sektion i dokumentet."""
        order = len(self.sections)
        section = DocumentSection(title=title, content=content, level=level, order=order)
        self.sections[title] = section
        return section
    
    def add_warning(self, warning: str, severity: str = "normal"):
        """Lägg till en varning med allvarlighetsgrad."""
        self.warnings.append({
            'message': warning,
            'severity': severity,
            'timestamp': datetime.now().isoformat()
        })
    
    def get_section_tree(self) -> Dict[str, List[DocumentSection]]:
        """Returnera en hierarkisk struktur av sektioner."""
        tree = {}
        for section in self.sections.values():
            tree.setdefault(section.level, []).append(section)
        return tree
    
    def update_confidence(self, component: str, score: float):
        """Uppdatera förtroendepoängen för en specifik komponent."""
        self.validation_status[component] = score
        self.confidence_score = sum(self.validation_status.values()) / len(self.validation_status)
    
    def validate_structure(self) -> List[str]:
        """Validera dokumentstrukturen och returnera en lista med felmeddelanden."""
        errors = []
        if not self.article_number:
            errors.append("Missing article number")
        if not self.product_name:
            errors.append("Missing product name")
        if self.technical_specs:
            for spec in self.technical_specs:
                if not spec.category or not spec.value:
                    errors.append(f"Invalid technical specification: {spec}")
        if self.compatibility:
            for comp in self.compatibility:
                if not comp.type or not comp.description:
                    errors.append(f"Invalid compatibility information: {comp}")
        if not self.sections:
            errors.append("Document has no sections")
        return errors
    
    def export_metadata(self) -> Dict[str, Any]:
        """Exportera dokumentets metadata."""
        return {
            'filename': self.filename,
            'article_number': self.article_number,
            'document_type': self.document_type,
            'product_name': self.product_name,
            'manufacturer': self.manufacturer,
            'metadata': asdict(self.metadata),
            'last_updated': self.last_updated,
            'confidence_score': self.confidence_score,
            'validation_status': self.validation_status,
            'version_history': self.version_history
        }
    
    def merge_document(self, other: 'DocumentStructure') -> None:
        """Slå ihop ett annat dokument med detta."""
        if self.article_number != other.article_number:
            raise ValueError("Cannot merge documents with different article numbers")
        for title, section in other.sections.items():
            if title not in self.sections:
                self.sections[title] = section
            else:
                self.sections[title].content += f"\n\n{section.content}"
        self.technical_specs.extend(other.technical_specs)
        self.compatibility.extend(other.compatibility)
        self.metadata.last_modified = datetime.now()
        self.add_version(
            version=str(float(self.metadata.version) + 0.1),
            changes=f"Merged with document {other.filename}",
            author="system"
        )
    
    def __post_init__(self):
        # Vid initiering valideras strukturen och eventuella fel sparas i processing_errors
        errors = self.validate_structure()
        if errors:
            self.processing_errors.extend(errors)
