# markdown_analyzer/extractors/summary/processor.py

from typing import List
import re
from collections import defaultdict
from ...extractors.technical.patterns import IMPORTANCE_INDICATORS
from ...core.document import DocumentStructure
from ...extractors import MetadataExtractor
from ...core.enums import TechnicalCategory, UnitCategory
from ...extractors.summary.models import ProductSummary
from ...extractors.compatibility.models import (
    RelationType, TechnicalRequirement, CompatibilityCondition,
    ProductReference, CompatibilityRelation, ProductFamily
)

from ...extractors.technical.models import TechnicalSpecification, TechnicalUnit, TechnicalValue

class SummaryProcessor:
    """
    Processar och prioriterar information för produktsammanfattningar.
    """
    
    def __init__(self, max_highlights: int = 5):
        self.max_highlights = max_highlights

    def create_summary(self, doc: DocumentStructure) -> ProductSummary:
        """Skapar en strukturerad sammanfattning"""
        # Samla grundläggande information
        summary = ProductSummary(
            article_number=doc.article_number,
            product_name=doc.product_name,
            main_image=self._get_main_image(doc),
            key_features=self._extract_key_features(doc),
            technical_highlights=self._select_technical_highlights(doc),
            compatibility_info=self._summarize_compatibility(doc),
            sections=[]
        )
        
        # Lägg till relevanta sektioner
        summary.sections.extend(self._create_sections(doc))
        
        return summary

    def _select_technical_highlights(self, 
                                   doc: DocumentStructure
                                   ) -> List[TechnicalSpecification]:
        """Väljer ut de viktigaste tekniska specifikationerna"""
        if not doc.technical_specs:
            return []
            
        # Beräkna viktighet för varje spec
        rated_specs = []
        for spec in doc.technical_specs:
            importance = self._calculate_spec_importance(spec)
            rated_specs.append((spec, importance))
        
        # Sortera och välj top specs
        rated_specs.sort(key=lambda x: x[1], reverse=True)
        return [spec for spec, _ in rated_specs[:self.max_highlights]]

    def _calculate_spec_importance(self, spec: TechnicalSpecification) -> float:
        """Beräknar hur viktig en specifikation är för sammanfattningen"""
        importance = spec.importance
        
        # Öka för vissa kategorier
        category_weights = {
            TechnicalCategory.ELECTRICAL: 1.2,
            TechnicalCategory.DIMENSIONS: 1.1,
            TechnicalCategory.PERFORMANCE: 1.3
        }
        importance *= category_weights.get(spec.category, 1.0)
        
        # Kontrollera efter viktiga nyckelord i beskrivningen
        if spec.description:
            for pattern in IMPORTANCE_INDICATORS['high']:
                if re.search(pattern, spec.description):
                    importance *= 1.3
                    break
            for pattern in IMPORTANCE_INDICATORS['medium']:
                if re.search(pattern, spec.description):
                    importance *= 1.1
                    break
        
        return importance

    def _summarize_compatibility(self, doc: DocumentStructure) -> List[str]:
        """Skapar en sammanfattning av kompatibilitetsinformation"""
        if not doc.compatibility:
            return []
            
        summary = []
        
        # Gruppera efter typ
        by_type = defaultdict(list)
        for comp in doc.compatibility:
            by_type[comp.type].append(comp)
        
        # Skapa sammanfattningar för varje typ
        for comp_type, comps in by_type.items():
            if comp_type == RelationType.DIRECT:
                summary.append(
                    f"Passar direkt till {len(comps)} produkter"
                )
            elif comp_type == RelationType.REQUIRES:
                summary.append(
                    f"Kräver {len(comps)} andra komponenter"
                )
            elif comp_type == RelationType.REPLACES:
                summary.append(
                    f"Ersätter {len(comps)} äldre modeller"
                )
        
        return summary