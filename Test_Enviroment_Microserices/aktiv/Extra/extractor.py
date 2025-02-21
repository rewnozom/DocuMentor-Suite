"""
extractor.py – Extraherar kompatibilitetsinformation från dokumenttext

Denna modul kombinerar en modern pattern-baserad extraktion med ursprunglig logik för att
extrahera:
  • Grundläggande kompatibilitetsrelationer med hjälp av BASIC och alternativa regex.
  • Ersättningsrelationer.
  • Teknisk information och villkor som berikar varje relation.
  • Produktfamiljsinformation och applicerar familjerelaterad kompatibilitet.
  • Slutgiltig konfidensberäkning och validering av extraherade relationer.

Alla fel hanteras genom anpassade undantag (ExtractionError).
"""

import re
import logging
from typing import List, Dict, Optional
from dataclasses import dataclass

# Importera modeller och mönster
from ..Models.models import (
    RelationType, TechnicalRequirement, CompatibilityCondition,
    ProductReference, CompatibilityRelation, ProductFamily
)
from ..Patterns.patterns import (
    BASIC_COMPATIBILITY_PATTERNS, REPLACEMENT_PATTERNS, CONDITION_PATTERNS,
    FAMILY_PATTERNS, TECHNICAL_REQUIREMENT_PATTERNS, CERTIFICATION_PATTERNS,
    ARTICLE_NUMBER_PATTERNS
)
from .errors import ExtractionError


class CompatibilityExtractor:
    """
    Extraherar kompatibilitetsinformation från dokumenttext.

    Denna klass kombinerar:
      - Extraktion med grundläggande och alternativa regex-mönster.
      - Skapande av produktreferenser från textutdrag.
      - Extraktion av ersättningsrelationer.
      - Berikning av relationer med tekniska krav, villkor och certifieringar.
      - Extraktion av produktfamiljsinformation och tillägg av familjerelaterad kompatibilitet.
      - Validering och konfidensberäkning.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.product_families: Dict[str, ProductFamily] = {}

    def extract(self, content: str, sections: Dict[str, str], file_path: Optional[str] = None) -> List[CompatibilityRelation]:
        """
        Huvudmetod för att extrahera kompatibilitetsrelationer från ett dokument.

        Args:
            content: Hela dokumentets innehåll.
            sections: En dictionary med sektioner (t.ex. {"Compatibility": "<text>"}).
            file_path: Sökväg till dokumentfilen (valfritt).

        Returns:
            En lista med CompatibilityRelation-objekt.
        """
        try:
            relations: List[CompatibilityRelation] = []

            # Försök använda dedikerad "Compatibility"-sektion, annars hela innehållet
            compat_section = sections.get("Compatibility", "") or content

            # Hämta källproduktinformation
            source_product = self._get_source_product(content, file_path)

            # Extrahera grundläggande kompatibilitet med primära mönster
            for pattern in self._get_basic_patterns():
                for match in re.finditer(pattern, compat_section, re.IGNORECASE):
                    target_info = match.group(1).strip()
                    target_product = self._create_product_reference(target_info)
                    if not target_product:
                        continue
                    relation_type = self._determine_relation_type(match.group(0))
                    relation = CompatibilityRelation(
                        source_product=source_product,
                        target_product=target_product,
                        relation_type=relation_type,
                        confidence=0.9,
                        context=self._extract_context(compat_section, match)
                    )
                    relations.append(relation)

            # Om inga relationer hittats, använd alternativa mönster
            if not relations:
                for pattern in self._get_alternative_patterns():
                    for match in re.finditer(pattern, content, re.IGNORECASE):
                        target_info = match.group(1).strip()
                        target_product = self._create_product_reference(target_info)
                        if target_product:
                            relation = CompatibilityRelation(
                                source_product=source_product,
                                target_product=target_product,
                                relation_type=RelationType.DIRECT,
                                confidence=0.8,
                                context=self._extract_context(content, match)
                            )
                            relations.append(relation)

            # Extrahera ersättningsrelationer
            relations.extend(self._extract_replacements(content, source_product))

            # Berika relationerna med tekniska krav, villkor och certifieringsinfo
            self._enrich_relations_with_requirements(relations, content)

            # Extrahera produktfamilj (om någon finns) och lägg till familjerelaterad kompatibilitet
            product_family = self._extract_product_family(content)
            if product_family:
                self._add_family_compatibility(relations, product_family)

            # Validera relationerna
            validated_relations = [rel for rel in relations if self._validate_relation(rel)]

            # Uppdatera konfidensen baserat på kontext och innehåll
            for relation in validated_relations:
                relation.confidence = self._calculate_confidence(relation)

            return validated_relations

        except Exception as e:
            self.logger.error(f"Fel vid kompatibilitetsextraktion: {str(e)}")
            raise ExtractionError(f"Kompatibilitetsextraktion misslyckades: {str(e)}")

    def _get_basic_patterns(self) -> List[str]:
        """Returnerar en lista med grundläggande regex för kompatibilitet."""
        return [
            r'(?i)kompatibel\s+med\s+([^\.]+)',
            r'(?i)compatible\s+with\s+([^\.]+)',
            r'(?i)fungerar\s+med\s+([^\.]+)',
            r'(?i)works\s+with\s+([^\.]+)',
            r'(?i)(?:kan|can)\s+användas\s+med\s+([^\.]+)',
            r'(?i)kan\s+kopplas\s+till\s+([^\.]+)',
            r'(?i)ansluts\s+till\s+([^\.]+)'
        ]

    def _get_alternative_patterns(self) -> List[str]:
        """Returnerar en lista med alternativa regex för kompatibilitet."""
        return [
            r'(?i)kräver\s+([^\.]+)',
            r'(?i)requires\s+([^\.]+)',
            r'(?i)måste\s+ha\s+([^\.]+)',
            r'(?i)förutsätter\s+([^\.]+)',
            r'(?i)beroende\s+av\s+([^\.]+)'
        ]

    def _determine_relation_type(self, text: str) -> RelationType:
        """Bestämmer relationsriktningen baserat på textinnehållet."""
        text_lower = text.lower()
        if "requires" in text_lower or "needs" in text_lower:
            return RelationType.REQUIRES
        elif "replaces" in text_lower or "replacement" in text_lower:
            return RelationType.REPLACES
        elif "replaced by" in text_lower or "superseded by" in text_lower:
            return RelationType.REPLACED_BY
        elif "accessory" in text_lower or "tillbehör" in text_lower:
            return RelationType.ACCESSORY
        else:
            return RelationType.DIRECT

    def _extract_context(self, content: str, match) -> str:
        """Extraherar en kontextsträng runt en matchning."""
        start = max(0, match.start() - 100)
        end = min(len(content), match.end() + 100)
        return content[start:end].strip()

    def _create_product_reference(self, text: str) -> Optional[ProductReference]:
        """Skapar en produktreferens från en given text."""
        article_match = re.search(r'(?:art(?:ikel)?\.?\s*(?:nr|number)?:?\s*)?(\d{5,8})', text)
        series_match = re.search(r'(?:serie|series):\s*([A-Za-z0-9\-]+)', text)
        variant_match = re.search(r'(?:variant|version|typ):\s*([A-Za-z0-9\-]+)', text)
        
        # Rensa bort parenteser med extrainformation samt eventuella artikelnummer
        name = re.sub(r'\(.*?\)', '', text).strip()
        name = re.sub(r'art(?:ikel)?\.?\s*(?:nr|number)?:?\s*\d+', '', name).strip()
        
        return ProductReference(
            name=name,
            article_number=article_match.group(1) if article_match else None,
            series=series_match.group(1) if series_match else None,
            variant=variant_match.group(1) if variant_match else None
        )

    def _get_source_product(self, content: str, file_path: Optional[str] = None) -> ProductReference:
        """
        Hämtar källproduktinformation från dokumentets inledande text eller filnamn.
        Om inget namn hittas används artikelnummeret som namn.
        """
        first_paragraph = content.split('\n\n')[0]
        name_match = re.search(r'^#\s+(.+)$', first_paragraph, re.MULTILINE)
        article_match = re.search(r'(?:art(?:ikel)?\.?\s*(?:nr|number)?:?\s*)?(\d{5,8})', content)
        file_article_number = None
        if file_path:
            file_article_match = re.search(r'(\d{8})', file_path)
            if file_article_match:
                file_article_number = file_article_match.group(1)
        article_number = article_match.group(1) if article_match else file_article_number
        if not name_match and article_number:
            name = f"Produkt {article_number}"
        else:
            name = name_match.group(1) if name_match else "Unknown Product"
        return ProductReference(name=name, article_number=article_number)

    def _extract_replacements(self, content: str, source_product: ProductReference) -> List[CompatibilityRelation]:
        """Extraherar ersättningsrelationer."""
        relations = []
        for pattern in REPLACEMENT_PATTERNS:
            for match in re.finditer(pattern, content):
                target_info = match.group(1).strip()
                context = self._extract_context(content, match)
                target_product = self._create_product_reference(target_info)
                if not target_product:
                    continue
                if "ersätts av" in match.group(0).lower():
                    relation_type = RelationType.REPLACED_BY
                else:
                    relation_type = RelationType.REPLACES
                relation = CompatibilityRelation(
                    source_product=source_product,
                    target_product=target_product,
                    relation_type=relation_type,
                    context=context
                )
                relation.confidence = self._calculate_confidence(relation)
                relations.append(relation)
        return relations

    def _extract_product_family(self, content: str) -> Optional[ProductFamily]:
        """Extraherar information om produktfamilj."""
        for pattern in FAMILY_PATTERNS:
            if match := re.search(pattern, content):
                family_name = match.group(1).strip()
                if family_name not in self.product_families:
                    self.product_families[family_name] = ProductFamily(name=family_name)
                family = self.product_families[family_name]
                description_match = re.search(fr'(?i){family_name}\s*:\s*([^\.]+)', content)
                if description_match:
                    family.description = description_match.group(1).strip()
                return family
        return None

    def _enrich_relations_with_requirements(self, relations: List[CompatibilityRelation], content: str) -> None:
        """Berikar relationerna med tekniska krav, villkor och certifieringar."""
        for relation in relations:
            requirements = self._extract_technical_requirements(content, relation.context)
            relation.technical_requirements.extend(requirements)
            conditions = self._extract_conditions(content, relation.context)
            relation.conditions.extend(conditions)
            if conditions:
                relation.relation_type = RelationType.CONDITIONAL
            certification = self._extract_certification(content, relation.context)
            if certification:
                relation.certification = certification
                relation.relation_type = RelationType.CERTIFIED

    def _extract_technical_requirements(self, content: str, context: Optional[str]) -> List[TechnicalRequirement]:
        """Extraherar tekniska krav från text."""
        requirements = []
        search_text = context or content
        for category, patterns in TECHNICAL_REQUIREMENT_PATTERNS.items():
            if isinstance(patterns, dict):
                for subcategory, subpatterns in patterns.items():
                    for pattern in subpatterns:
                        for match in re.finditer(pattern, search_text):
                            if category == 'dimensions' and len(match.groups()) >= 3:
                                requirements.append(TechnicalRequirement(
                                    category=f"{category}.{subcategory}",
                                    exact_value=f"{match.group(1)}x{match.group(2)}x{match.group(3)}",
                                    unit="mm"
                                ))
                            else:
                                value = match.group(1)
                                unit = self._extract_unit(value)
                                if unit:
                                    value = value.replace(unit, '').strip()
                                try:
                                    float(value)
                                    requirements.append(TechnicalRequirement(
                                        category=f"{category}.{subcategory}",
                                        exact_value=value,
                                        unit=unit
                                    ))
                                except ValueError:
                                    requirements.append(TechnicalRequirement(
                                        category=f"{category}.{subcategory}",
                                        exact_value=value,
                                        description=match.group(0)
                                    ))
            else:
                for pattern in patterns:
                    for match in re.finditer(pattern, search_text):
                        if category == 'dimensions' and len(match.groups()) >= 3:
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
                                float(value)
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

    def _extract_conditions(self, content: str, context: Optional[str]) -> List[CompatibilityCondition]:
        """Extraherar villkor för kompatibilitet."""
        conditions = []
        search_text = context or content
        for pattern in CONDITION_PATTERNS:
            for match in re.finditer(pattern, search_text):
                condition_text = match.group(1).strip()
                condition_type = self._determine_condition_type(condition_text)
                reqs = self._extract_technical_requirements(condition_text, None)
                conditions.append(CompatibilityCondition(
                    condition_type=condition_type,
                    description=condition_text,
                    requirements=reqs
                ))
        return conditions

    def _extract_certification(self, content: str, context: Optional[str]) -> Optional[str]:
        """Extraherar certifieringsinformation från text."""
        search_text = context or content
        for pattern in CERTIFICATION_PATTERNS:
            if match := re.search(pattern, search_text):
                return match.group(1).strip()
        return None

    def _determine_condition_type(self, condition_text: str) -> str:
        """Bestämmer typ av villkor baserat på text."""
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

    def _extract_unit(self, text: str) -> Optional[str]:
        """Extraherar en enhet från text."""
        unit_match = re.search(r'(V|mm|cm|m)', text)
        return unit_match.group(1) if unit_match else None

    def _calculate_confidence(self, relation: CompatibilityRelation) -> float:
        """Beräknar konfidensnivå för en relation baserat på dess attribut."""
        confidence = 1.0
        if not relation.target_product.article_number:
            confidence *= 0.8
        if relation.conditions:
            confidence *= 0.9
        if relation.certification:
            confidence = min(1.0, confidence * 1.2)
        if relation.context:
            context_quality = self._assess_context_quality(relation.context)
            confidence *= context_quality
        return round(confidence, 2)

    def _assess_context_quality(self, context: str) -> float:
        """Bedömer kontextens kvalitet."""
        quality = 1.0
        if len(context) < 100:
            quality *= 0.9
        uncertainty_indicators = ['kanske', 'möjligen', 'troligen', 'bör', 'eventuellt']
        if any(ind in context.lower() for ind in uncertainty_indicators):
            quality *= 0.8
        if re.search(r'\d+(?:\.\d+)?\s*(?:mm|cm|V|A|W)', context):
            quality = min(1.0, quality * 1.1)
        return quality

    def _validate_relation(self, relation: CompatibilityRelation) -> bool:
        """Validerar att en kompatibilitetsrelation är komplett och logiskt korrekt."""
        if not relation.source_product.name:
            return False
        if not relation.target_product.name:
            return False
        if (relation.source_product.article_number and relation.target_product.article_number and 
            relation.source_product.article_number == relation.target_product.article_number):
            return False
        if relation.conditions:
            for condition in relation.conditions:
                if not condition.description:
                    return False
        if relation.technical_requirements:
            for req in relation.technical_requirements:
                if not (req.exact_value or (req.min_value is not None or req.max_value is not None)):
                    return False
        return True

    def _add_family_compatibility(self, relations: List[CompatibilityRelation], family: ProductFamily) -> None:
        """Lägger till familjerelaterad kompatibilitetsinformation till relationerna."""
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
                    technical_requirements=common_relation.technical_requirements.copy(),
                    certification=common_relation.certification,
                    compatibility_notes=f"Medlem av produktfamilj: {family.name}",
                    confidence=round(common_relation.confidence * 0.9, 2)
                )
                relations.append(member_relation)
