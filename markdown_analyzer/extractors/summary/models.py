# markdown_analyzer/extractors/summary/models.py

from dataclasses import dataclass, field
from typing import List, Optional
from ...extractors.technical.models import TechnicalSpecification

@dataclass

class SummarySection:
    """En sektion i en produktsammanfattning"""
    title: str
    content: List[str]
    importance: float
    category: str

@dataclass
class ProductSummary:
    """Komplett produktsammanfattning"""
    article_number: str
    product_name: str
    main_image: Optional[str]
    key_features: List[str]
    technical_highlights: List[TechnicalSpecification]
    compatibility_info: List[str]
    sections: List[SummarySection]
    documentation_links: List[str] = field(default_factory=list)