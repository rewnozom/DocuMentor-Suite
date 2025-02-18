# markdown_analyzer/extractors/compatibility/extractor.py
import re
import logging
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass

from .models import (
    RelationType, TechnicalRequirement, CompatibilityCondition,
    ProductReference, CompatibilityRelation, ProductFamily
)
from .patterns import (
    BASIC_COMPATIBILITY_PATTERNS, REPLACEMENT_PATTERNS,
    CONDITION_PATTERNS, FAMILY_PATTERNS,
    TECHNICAL_REQUIREMENT_PATTERNS, CERTIFICATION_PATTERNS
)
from ...core.errors import ExtractionError

class CompatibilityExtractor:
    """
    Extraherar kompatibilitetsinformation från dokumenttext.
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.product_families: Dict[str, ProductFamily] = {}

    def extract(self, content: str, sections: Dict[str, str]) -> List[CompatibilityRelation]:
        """
        Huvudmetod för att extrahera kompatibilitetsinformation.
        
        Args:
            content: Hela dokumentets innehåll
            sections: Dokumentet uppdelat i sektioner
            
        Returns:
            Lista med CompatibilityRelation-objekt
        """
        try:
            relations = []
            
            # Extrahera produktfamilj först
            product_family = self._extract_product_family(content)
            
            # Processa varje sektion
            for section_name, section_content in sections.items():
                # Grundläggande kompatibilitet
                relations.extend(self._extract_basic_compatibility(
                    section_content, section_name
                ))
                
                # Ersättningsinformation
                relations.extend(self._extract_replacements(
                    section_content, section_name
                ))
                
                # Tekniska krav och villkor
                self._enrich_relations_with_requirements(
                    relations, section_content
                )
            
            # Lägg till familjeinformation om tillgänglig
            if product_family:
                self._add_family_compatibility(relations, product_family)
            
            # Validera och filtrera relationer
            validated_relations = [
                rel for rel in relations 
                if self._validate_relation(rel)
            ]
            
            return validated_relations
            
        except Exception as e:
            self.logger.error(f"Fel vid kompatibilitetsextraktion: {str(e)}")
            raise ExtractionError(f"Kompatibilitetsextraktion misslyckades: {str(e)}")

    def _extract_basic_compatibility(self, content: str, 
                                   section_name: str) -> List[CompatibilityRelation]:
        """Extraherar grundläggande kompatibilitetsinformation"""
        relations = []
        
        for pattern in BASIC_COMPATIBILITY_PATTERNS:
            for match in re.finditer(pattern, content):
                target_info = match.group(1).strip()
                context = self._extract_context(content, match)
                
                # Skapa produktreferenser
                target_product = self._create_product_reference(target_info)
                if not target_product:
                    continue
                
                # Skapa relation
                relation = CompatibilityRelation(
                    source_product=self._get_source_product(content),
                    target_product=target_product,
                    relation_type=RelationType.DIRECT,
                    context=context
                )
                
                # Justera konfidens baserat på kontext
                relation.confidence = self._calculate_confidence(relation)
                
                relations.append(relation)
        
        return relations

    def _extract_replacements(self, content: str, 
                            section_name: str) -> List[CompatibilityRelation]:
        """Extraherar information om ersättningsprodukter"""
        relations = []
        
        for pattern in REPLACEMENT_PATTERNS:
            for match in re.finditer(pattern, content):
                target_info = match.group(1).strip()
                context = self._extract_context(content, match)
                
                target_product = self._create_product_reference(target_info)
                if not target_product:
                    continue
                
                # Bestäm relationsriktning
                if "ersätts av" in match.group(0).lower():
                    relation_type = RelationType.REPLACED_BY
                else:
                    relation_type = RelationType.REPLACES
                
                relation = CompatibilityRelation(
                    source_product=self._get_source_product(content),
                    target_product=target_product,
                    relation_type=relation_type,
                    context=context
                )
                
                relation.confidence = self._calculate_confidence(relation)
                relations.append(relation)
        
        return relations

    def _extract_product_family(self, content: str) -> Optional[ProductFamily]:
        """Extraherar information om produktfamilj"""
        for pattern in FAMILY_PATTERNS:
            if match := re.search(pattern, content):
                family_name = match.group(1).strip()
                
                # Skapa eller hämta existerande familj
                if family_name not in self.product_families:
                    self.product_families[family_name] = ProductFamily(
                        name=family_name
                    )
                
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

    def _enrich_relations_with_requirements(self, relations: List[CompatibilityRelation],
                                          content: str) -> None:
        """Berikar relationer med tekniska krav och villkor"""
        for relation in relations:
            # Extrahera tekniska krav
            requirements = self._extract_technical_requirements(
                content, relation.context
            )
            relation.technical_requirements.extend(requirements)
            
            # Extrahera villkor
            conditions = self._extract_conditions(
                content, relation.context
            )
            relation.conditions.extend(conditions)
            
            # Uppdatera relationstyp om villkor hittades
            if conditions:
                relation.relation_type = RelationType.CONDITIONAL
            
            # Leta efter certifieringar
            certification = self._extract_certification(
                content, relation.context
            )
            if certification:
                relation.certification = certification
                relation.relation_type = RelationType.CERTIFIED

    def _extract_technical_requirements(self, content: str,
                                      context: Optional[str]) -> List[TechnicalRequirement]:
        """Extraherar tekniska krav från text"""
        requirements = []
        search_text = context or content
        
        for category, patterns in TECHNICAL_REQUIREMENT_PATTERNS.items():
            for pattern in patterns:
                for match in re.finditer(pattern, search_text):
                    if category == 'dimensions':
                        requirements.append(TechnicalRequirement(
                            category=category,
                            exact_value=f"{match.group(1)}x{match.group(2)}x{match.group(3)}",
                            unit="mm"
                        ))
                    else:
                        value = match.group(1)
                        unit = self._extract_unit(value)
                        if unit:
                            value = value.replace(unit, '').strip()
                        
                        try:
                            float_value = float(value)
                            requirements.append(TechnicalRequirement(
                                category=category,
                                exact_value=value,
                                unit=unit
                            ))
                        except ValueError:
                            requirements.append(TechnicalRequirement(
                                category=category,
                                exact_value=value,
                                description=match.group(0)
                            ))
        
        return requirements

    def _extract_conditions(self, content: str, 
                          context: Optional[str]) -> List[CompatibilityCondition]:
        """Extraherar villkor för kompatibilitet"""
        conditions = []
        search_text = context or content
        
        for pattern in CONDITION_PATTERNS:
            for match in re.finditer(pattern, search_text):
                condition_text = match.group(1).strip()
                condition_type = self._determine_condition_type(condition_text)
                
                # Leta efter tekniska krav i villkoret
                requirements = self._extract_technical_requirements(condition_text, None)
                
                conditions.append(CompatibilityCondition(
                    condition_type=condition_type,
                    description=condition_text,
                    requirements=requirements
                ))
        
        return conditions

    def _extract_certification(self, content: str, 
                             context: Optional[str]) -> Optional[str]:
        """Extraherar certifieringsinformation"""
        search_text = context or content
        
        for pattern in CERTIFICATION_PATTERNS:
            if match := re.search(pattern, search_text):
                return match.group(1).strip()
        
        return None

    def _determine_condition_type(self, condition_text: str) -> str:
        """Bestämmer typ av villkor baserat på text"""
        type_indicators = {
            'installation': ['montering', 'installation', 'monteras', 'installeras'],
            'environment': ['miljö', 'temperatur', 'fukt', 'utomhus', 'inomhus'],
            'configuration': ['inställning', 'konfiguration', 'setup', 'programmering'],
            'operation': ['drift', 'användning', 'hantering'],
            'maintenance': ['underhåll', 'service', 'rengöring']
        }
        
        condition_lower = condition_text.lower()
        for condition_type, indicators in type_indicators.items():
            if any(indicator in condition_lower for indicator in indicators):
                return condition_type
        
        return 'other'

    def _extract_context(self, content: str, match) -> str:
        """Extraherar relevant kontext runt en matchning"""
        start = max(0, match.start() - 200)
        end = min(len(content), match.end() + 200)
        return content[start:end]

    def _create_product_reference(self, text: str) -> Optional[ProductReference]:
        """Skapar en produktreferens från text"""
        # Leta efter artikelnummer
        article_match = re.search(r'(?:art(?:ikel)?\.?\s*(?:nr|number)?:?\s*)?(\d{5,8})', text)
        
        # Leta efter serienummer/variant
        series_match = re.search(r'(?:serie|series):\s*([A-Za-z0-9\-]+)', text)
        variant_match = re.search(r'(?:variant|version|typ):\s*([A-Za-z0-9\-]+)', text)
        
        # Rensa produktnamn
        name = re.sub(r'\(.*?\)', '', text).strip()  # Ta bort parenteser och innehåll
        name = re.sub(r'art(?:ikel)?\.?\s*(?:nr|number)?:?\s*\d+', '', name).strip()  # Ta bort artikelnummer
        
        return ProductReference(
            name=name,
            article_number=article_match.group(1) if article_match else None,
            series=series_match.group(1) if series_match else None,
            variant=variant_match.group(1) if variant_match else None
        )

    def _get_source_product(self, content: str) -> ProductReference:
        """Hämtar information om källprodukten"""
        # Leta först i dokumentets början
        first_paragraph = content.split('\n\n')[0]
        name_match = re.search(r'^#\s+(.+)$', first_paragraph, re.MULTILINE)
        
        name = name_match.group(1) if name_match else "Unknown Product"
        article_match = re.search(r'(?:art(?:ikel)?\.?\s*(?:nr|number)?:?\s*)?(\d{5,8})', content)
        
        return ProductReference(
            name=name,
            article_number=article_match.group(1) if article_match else None
        )

    def _calculate_confidence(self, relation: CompatibilityRelation) -> float:
        """Beräknar konfidensnivå för en relation"""
        confidence = 1.0
        
        # Minska konfidens om artikelnummer saknas
        if not relation.target_product.article_number:
            confidence *= 0.8
        
        # Minska för villkorlig kompatibilitet
        if relation.conditions:
            confidence *= 0.9
        
        # Öka för certifierad kompatibilitet
        if relation.certification:
            confidence = min(1.0, confidence * 1.2)
        
        # Justera baserat på kontextens kvalitet
        if relation.context:
            context_quality = self._assess_context_quality(relation.context)
            confidence *= context_quality
        
        return round(confidence, 2)

    def _assess_context_quality(self, context: str) -> float:
        """Bedömer kvaliteten på kontexten"""
        quality = 1.0
        
        # Minska om kontexten är kort
        if len(context) < 100:
            quality *= 0.9
        
        # Minska om kontexten innehåller osäkra formuleringar
        uncertainty_indicators = ['kanske', 'möjligen', 'troligen', 'bör', 'eventuellt']
        if any(indicator in context.lower() for indicator in uncertainty_indicators):
            quality *= 0.8
        
        # Öka om kontexten innehåller tekniska detaljer
        if re.search(r'\d+(?:\.\d+)?\s*(?:mm|cm|V|A|W)', context):
            quality = min(1.0, quality * 1.1)
        
        return quality

    def _validate_relation(self, relation: CompatibilityRelation) -> bool:
        """Validerar en kompatibilitetsrelation"""
        # Måste ha källprodukt
        if not relation.source_product.name:
            return False
        
        # Måste ha målprodukt
        if not relation.target_product.name:
            return False
        
        # Kontrollera att källa och mål inte är samma
        if (relation.source_product.article_number and 
            relation.target_product.article_number and 
            relation.source_product.article_number == relation.target_product.article_number):
            return False
        
        # Validera villkor om de finns
        if relation.conditions:
            for condition in relation.conditions:
                if not condition.description:
                    return False
        
        # Validera tekniska krav
        if relation.technical_requirements:
            for req in relation.technical_requirements:
                if not (req.exact_value or (req.min_value is not None or req.max_value is not None)):
                    return False
        
        return True

    def _add_family_compatibility(self, relations: List[CompatibilityRelation],
                                family: ProductFamily) -> None:
        """Lägger till familjerelaterad kompatibilitetsinformation"""
        # Lägg till familjemedlemmar i relationer
        for member_article in family.members:
            for common_relation in family.common_compatibility:
                # Skapa en kopia av relationen för varje medlem
                member_relation = CompatibilityRelation(
                    source_product=ProductReference(
                        name=family.name,
                        article_number=member_article
                    ),
                    target_product=common_relation.target_product,
                    relation_type=common_relation.relation_type,
                    conditions=common_relation.conditions.copy(),
                    technical_requirements=common_relation.technical_requirements.copy(),
                    certification=common_relation.certification,
                    compatibility_notes=f"Medlem av produktfamilj: {family.name}",
                    confidence=common_relation.confidence * 0.9  # Något lägre konfidens för ärvd kompatibilitet
                )
                
                relations.append(member_relation)