# compatibility/extractor.py

import re
import logging
from typing import List, Dict, Optional, Set
from dataclasses import dataclass

from .models import (
    RelationType, CompatibilityCondition,
    ProductReference, CompatibilityRelation, ProductFamily
)

from .patterns import (
    BASIC_COMPATIBILITY_PATTERNS,
    REPLACEMENT_PATTERNS,
    CONDITION_PATTERNS,
    FAMILY_PATTERNS,
    ARTICLE_NUMBER_PATTERNS,
    COMPATIBILITY_RELATIONSHIPS
)

from .errors import ExtractionError

class CompatibilityExtractor:
    """
    Extraherar kompatibilitetsinformation från markdown-dokument.
    Fokuserar på att identifiera och extrahera produktrelationer för -c kommandot.
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.product_families: Dict[str, ProductFamily] = {}

    def extract(self, content: str, file_path: Optional[str] = None) -> List[CompatibilityRelation]:
        """
        Extraherar kompatibilitetsinformation från dokumentinnehåll.

        Args:
            content: Dokumentets innehåll
            file_path: Sökväg till dokumentfilen (optional)

        Returns:
            Lista med CompatibilityRelation-objekt
        """
        try:
            relations: List[CompatibilityRelation] = []
            
            # Identifiera källprodukt
            source_product = self._get_source_product(content, file_path)
            if not source_product:
                self.logger.warning(f"Kunde inte identifiera källprodukt i {file_path}")
                return []

            # Extrahera grundläggande kompatibilitet
            basic_relations = self._extract_basic_compatibility(content, source_product)
            relations.extend(basic_relations)

            # Extrahera ersättningsrelationer
            replacement_relations = self._extract_replacements(content, source_product)
            relations.extend(replacement_relations)

            # Extrahera produktfamilj och familjerelaterad kompatibilitet
            product_family = self._extract_product_family(content)
            if product_family:
                self._add_family_compatibility(relations, product_family)

            # Berika relationerna med villkor
            self._enrich_relations_with_conditions(relations, content)

            # Validera och filtrera relationerna
            validated_relations = [rel for rel in relations if self._validate_relation(rel)]
            
            # Uppdatera konfidens baserat på kontexten
            for relation in validated_relations:
                relation.confidence = self._calculate_confidence(relation)

            return validated_relations

        except Exception as e:
            self.logger.error(f"Fel vid kompatibilitetsextraktion: {str(e)}")
            raise ExtractionError(
                message=f"Kompatibilitetsextraktion misslyckades: {str(e)}", 
                extractor_name="CompatibilityExtractor",
                source=str(file_path)
            )

    def _get_source_product(self, content: str, file_path: Optional[str] = None) -> Optional[ProductReference]:
        """Identifierar källprodukten från dokumentet"""
        # Försök hitta produktnamn i första stycket
        first_paragraph = content.split('\n\n')[0]
        name_match = re.search(r'^#\s+(.+)$', first_paragraph, re.MULTILINE)
        
        # Extrahera artikelnummer
        article_number = None
        for pattern in ARTICLE_NUMBER_PATTERNS:
            if match := re.search(pattern, content):
                article_number = match.group(1)
                break
                
        # Använd filnamn som backup
        if not article_number and file_path:
            file_article_match = re.search(r'(\d{8})', str(file_path))
            if file_article_match:
                article_number = file_article_match.group(1)

        # Skapa produktreferens
        if name_match:
            name = name_match.group(1).strip()
        elif article_number:
            name = f"Produkt {article_number}"
        else:
            return None

        return ProductReference(
            name=name,
            article_number=article_number
        )

    def _extract_basic_compatibility(self, content: str, source_product: ProductReference) -> List[CompatibilityRelation]:
        """Extraherar grundläggande kompatibilitetsrelationer"""
        relations = []
        
        # Kombinera alla kompatibilitetsmönster
        all_patterns = (
            BASIC_COMPATIBILITY_PATTERNS +
            COMPATIBILITY_RELATIONSHIPS['direct'] +
            COMPATIBILITY_RELATIONSHIPS['requires']
        )

        for pattern in all_patterns:
            for match in re.finditer(pattern, content, re.IGNORECASE):
                target_info = match.group(1).strip()
                target_product = self._create_product_reference(target_info)
                
                if not target_product:
                    continue

                # Bestäm relationstyp
                relation_type = self._determine_relation_type(match.group(0))
                
                # Skapa relation
                relation = CompatibilityRelation(
                    source_product=source_product,
                    target_product=target_product,
                    relation_type=relation_type,
                    confidence=0.9,
                    context=self._extract_context(content, match)
                )
                relations.append(relation)

        return relations




    def _create_product_reference(self, text: str) -> Optional[ProductReference]:
        """Skapar en produktreferens från text"""
        # Extrahera artikelnummer
        article_match = re.search(r'(?:art(?:ikel)?\.?\s*(?:nr|number)?:?\s*)?(\d{5,8})', text)
        
        # Extrahera serie och variant
        series_match = re.search(r'(?:serie|series):\s*([A-Za-z0-9\-]+)', text)
        variant_match = re.search(r'(?:variant|version|typ):\s*([A-Za-z0-9\-]+)', text)
        
        # Rensa produktnamn
        name = re.sub(r'\(.*?\)', '', text).strip()  # Ta bort parenteser
        name = re.sub(r'art(?:ikel)?\.?\s*(?:nr|number)?:?\s*\d+', '', name).strip()  # Ta bort artikelnummer
        
        if not name:  # Om inget namn finns, returnera None
            return None
            
        return ProductReference(
            name=name,
            article_number=article_match.group(1) if article_match else None,
            series=series_match.group(1) if series_match else None,
            variant=variant_match.group(1) if variant_match else None
        )

    def _extract_replacements(self, content: str, source_product: ProductReference) -> List[CompatibilityRelation]:
        """Extraherar ersättningsrelationer"""
        relations = []
        for pattern in REPLACEMENT_PATTERNS:
            for match in re.finditer(pattern, content):
                target_info = match.group(1).strip()
                target_product = self._create_product_reference(target_info)
                
                if not target_product:
                    continue
                    
                # Bestäm om produkten ersätter eller ersätts
                relation_type = (RelationType.REPLACED_BY 
                               if "ersätts av" in match.group(0).lower() 
                               else RelationType.REPLACES)
                
                relation = CompatibilityRelation(
                    source_product=source_product,
                    target_product=target_product,
                    relation_type=relation_type,
                    context=self._extract_context(content, match)
                )
                relations.append(relation)
                
        return relations

    def _extract_product_family(self, content: str) -> Optional[ProductFamily]:
        """Extraherar information om produktfamilj"""
        for pattern in FAMILY_PATTERNS:
            if match := re.search(pattern, content):
                family_name = match.group(1).strip()
                
                if family_name not in self.product_families:
                    self.product_families[family_name] = ProductFamily(name=family_name)
                    
                family = self.product_families[family_name]
                
                # Försök hitta beskrivning
                description_match = re.search(
                    fr'(?i){family_name}\s*:\s*([^\.]+)', 
                    content
                )
                if description_match:
                    family.description = description_match.group(1).strip()
                    
                return family
                
        return None

    def _determine_relation_type(self, text: str) -> RelationType:
        """Bestämmer relationstyp baserat på text"""
        text = text.lower()
        if "kräver" in text or "requires" in text or "måste ha" in text:
            return RelationType.REQUIRES
        elif "ersätter" in text or "replaces" in text:
            return RelationType.REPLACES
        elif "ersätts av" in text or "replaced by" in text:
            return RelationType.REPLACED_BY
        elif "tillbehör" in text or "accessory" in text:
            return RelationType.ACCESSORY
        else:
            return RelationType.DIRECT

    def _extract_context(self, content: str, match) -> str:
        """Extraherar kontext runt en matchning"""
        start = max(0, match.start() - 100)
        end = min(len(content), match.end() + 100)
        return content[start:end].strip()

    def _enrich_relations_with_conditions(self, relations: List[CompatibilityRelation], content: str) -> None:
        """Berikar relationer med villkor"""
        for relation in relations:
            conditions = self._extract_conditions(content, relation.context)
            relation.conditions.extend(conditions)
            if conditions:
                relation.relation_type = RelationType.CONDITIONAL

    def _extract_conditions(self, content: str, context: Optional[str]) -> List[CompatibilityCondition]:
        """Extraherar villkor för kompatibilitet"""
        conditions = []
        search_text = context or content
        
        for pattern in CONDITION_PATTERNS:
            for match in re.finditer(pattern, search_text):
                condition_text = match.group(1).strip()
                condition_type = self._determine_condition_type(condition_text)
                
                conditions.append(CompatibilityCondition(
                    condition_type=condition_type,
                    description=condition_text
                ))
                
        return conditions

    def _determine_condition_type(self, condition_text: str) -> str:
        """Bestämmer typ av villkor"""
        type_indicators = {
            'installation': ['montering', 'installation', 'monteras'],
            'configuration': ['inställning', 'konfiguration', 'programmering'],
            'operation': ['drift', 'användning', 'hantering']
        }
        
        condition_lower = condition_text.lower()
        for condition_type, indicators in type_indicators.items():
            if any(indicator in condition_lower for indicator in indicators):
                return condition_type
                
        return 'other'

    def _validate_relation(self, relation: CompatibilityRelation) -> bool:
        """Validerar en kompatibilitetsrelation"""
        if not relation.source_product.name or not relation.target_product.name:
            return False
            
        if (relation.source_product.article_number and 
            relation.target_product.article_number and 
            relation.source_product.article_number == relation.target_product.article_number):
            return False
            
        return True

    def _calculate_confidence(self, relation: CompatibilityRelation) -> float:
        """Beräknar konfidensnivå för en relation"""
        confidence = 1.0
        
        # Justera baserat på tillgänglig information
        if not relation.target_product.article_number:
            confidence *= 0.8
        if relation.conditions:
            confidence *= 0.9
        if relation.context:
            context_quality = self._assess_context_quality(relation.context)
            confidence *= context_quality
            
        return round(confidence, 2)

    def _assess_context_quality(self, context: str) -> float:
        """Bedömer kvaliteten på kontext"""
        quality = 1.0
        
        # Kortare kontext ger lägre kvalitet
        if len(context) < 100:
            quality *= 0.9
            
        # Osäkerhetsmarkörer sänker kvaliteten
        uncertainty_indicators = ['kanske', 'möjligen', 'troligen', 'eventuellt']
        if any(ind in context.lower() for ind in uncertainty_indicators):
            quality *= 0.8
            
        return quality

    def _add_family_compatibility(self, relations: List[CompatibilityRelation], family: ProductFamily) -> None:
        """Lägger till familjerelaterad kompatibilitet"""
        for member_article in family.members:
            for common_relation in family.common_compatibility:
                member_relation = CompatibilityRelation(
                    source_product=ProductReference(
                        name=family.name,
                        article_number=member_article
                    ),
                    target_product=common_relation.target_product,
                    relation_type=common_relation.relation_type,
                    conditions=common_relation.conditions.copy(),
                    compatibility_notes=f"Medlem av produktfamilj: {family.name}",
                    confidence=round(common_relation.confidence * 0.9, 2)
                )
                relations.append(member_relation)






