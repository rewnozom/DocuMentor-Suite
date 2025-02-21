from typing import List
from compatibility.formatter import CompatibilityFormatter
from compatibility.models import (
    CompatibilityRelation, RelationType, TrainingExample,
    TechnicalRequirement, CompatibilityCondition
)

class EnhancedCompatibilityFormatter(CompatibilityFormatter):
    """
    Utökad formatering av kompatibilitetsinformation för träningsdata.
    Denna version kombinerar funktionaliteten från tidigare versioner:
      - Inkluderar EAN och leverantörsartiklar (om tillgängliga)
      - Formaterar tekniska krav och villkor i detalj
      - Skapar flera tränings-exempel med olika identifierare
    """

    def format_for_training(self, relation: CompatibilityRelation) -> List[TrainingExample]:
        """
        Formaterar en kompatibilitetsrelation för träningsdata.
        Skapar flera träningsexempel baserat på olika identifierare från källprodukten.
        """
        response = self._format_response(relation)
        confidence = self._calculate_confidence(relation)
        examples: List[TrainingExample] = []
        
        # Exempel med artikelnummer (full konfidens)
        if relation.source_product.article_number:
            examples.append(TrainingExample(
                user_input=f"-c {relation.source_product.article_number}",
                ai_output=response,
                source=relation.source_product.name,
                confidence=confidence
            ))
        
        # Exempel med EAN
        if hasattr(relation.source_product, 'ean') and relation.source_product.ean:
            examples.append(TrainingExample(
                user_input=f"-c {relation.source_product.ean}",
                ai_output=response,
                source=relation.source_product.name,
                confidence=confidence
            ))
        
        # Exempel med leverantörsartikel
        if hasattr(relation.source_product, 'supplier_article') and relation.source_product.supplier_article:
            examples.append(TrainingExample(
                user_input=f"-c {relation.source_product.supplier_article}",
                ai_output=response,
                source=relation.source_product.name,
                confidence=confidence
            ))
        
        # Exempel med produktnamn (något lägre konfidens)
        examples.append(TrainingExample(
            user_input=f'-c "{relation.source_product.name}"',
            ai_output=response,
            source=relation.source_product.name,
            confidence=round(confidence * 0.9, 3)
        ))
        
        return examples

    def _format_response(self, relation: CompatibilityRelation) -> str:
        """Formaterar ett detaljerat svar för träningsdata."""
        parts = []
        
        # Rubrik med källproduktens namn
        parts.append(f"Här är kompatibilitetsinformation för {relation.source_product.name}:")
        
        # Källproduktens detaljer
        if relation.source_product.article_number:
            parts.append(f"Copiax artikelnummer: {relation.source_product.article_number}")
        if hasattr(relation.source_product, 'ean') and relation.source_product.ean:
            parts.append(f"EAN: {relation.source_product.ean}")
        if hasattr(relation.source_product, 'supplier_article') and relation.source_product.supplier_article:
            parts.append(f"Leverantörens artikelnummer: {relation.source_product.supplier_article}")
        
        parts.append("")  # tom rad
        
        # Relationstyp och målproduktinformation
        relation_type_text = self._get_relation_type_text(relation.relation_type)
        parts.append(f"{relation_type_text}:")
        
        # Målproduktens detaljer
        parts.append(f"* {relation.target_product.name}")
        if relation.target_product.article_number:
            parts.append(f"  Copiax artikelnummer: {relation.target_product.article_number}")
        if hasattr(relation.target_product, 'ean') and relation.target_product.ean:
            parts.append(f"  EAN: {relation.target_product.ean}")
        if hasattr(relation.target_product, 'supplier_article') and relation.target_product.supplier_article:
            parts.append(f"  Leverantörens artikelnummer: {relation.target_product.supplier_article}")
        if getattr(relation.target_product, 'series', None):
            parts.append(f"  Serie: {relation.target_product.series}")
        if getattr(relation.target_product, 'variant', None):
            parts.append(f"  Variant: {relation.target_product.variant}")
        
        # Tekniska krav
        if relation.technical_requirements:
            parts.append("")
            parts.append("Tekniska krav:")
            for req in relation.technical_requirements:
                parts.append(self._format_technical_requirement(req))
        
        # Villkor
        if relation.conditions:
            parts.append("")
            parts.append("Villkor:")
            for condition in relation.conditions:
                parts.append(self._format_condition(condition))
        
        # Certifiering
        if getattr(relation, 'certification', None):
            parts.append("")
            parts.append(f"Certifiering: {relation.certification}")
        
        # Kompatibilitetsnoteringar
        if getattr(relation, 'compatibility_notes', None):
            parts.append("")
            parts.append(f"Notering: {relation.compatibility_notes}")
        
        return "\n".join(parts)

    def _get_relation_type_text(self, rel_type: RelationType) -> str:
        """Returnerar lämplig rubrik för en relationstyp."""
        type_texts = {
            RelationType.DIRECT: "Passar till",
            RelationType.CONDITIONAL: "Passar till (med villkor)",
            RelationType.CERTIFIED: "Certifierad kompatibilitet",
            RelationType.REQUIRES: "Kräver",
            RelationType.REPLACES: "Ersätter",
            RelationType.REPLACED_BY: "Ersätts av",
            RelationType.ACCESSORY: "Tillbehör"
        }
        return type_texts.get(rel_type, str(rel_type).title())

    def _format_technical_requirement(self, req: TechnicalRequirement) -> str:
        """Formaterar ett tekniskt krav."""
        if req.exact_value:
            value_str = f"{req.exact_value}"
        else:
            value_parts = []
            if req.min_value is not None:
                value_parts.append(f"min {req.min_value}")
            if req.max_value is not None:
                value_parts.append(f"max {req.max_value}")
            value_str = ", ".join(value_parts)
        
        unit_str = f" {req.unit}" if req.unit else ""
        description = f" ({req.description})" if req.description else ""
        return f"  * {req.category}: {value_str}{unit_str}{description}"

    def _format_condition(self, condition: CompatibilityCondition) -> str:
        """Formaterar ett villkor."""
        parts = [f"  * {condition.description}"]
        
        if condition.requirements:
            for req in condition.requirements:
                # Ta bort onödig indragning från det tekniska kravet
                parts.append(f"    - {self._format_technical_requirement(req).strip()}")
                
        if condition.notes:
            parts.append(f"    Not: {condition.notes}")
            
        return "\n".join(parts)

    def _calculate_confidence(self, relation: CompatibilityRelation) -> float:
        """Beräknar konfidensnivå för en relation."""
        confidence = 1.0
        
        # Justera baserat på tillgänglig information
        if not relation.source_product.article_number:
            confidence *= 0.9
        if relation.conditions:
            confidence *= 0.95
        if relation.technical_requirements:
            confidence *= 0.98
        if getattr(relation, 'certification', None):
            confidence = min(1.0, confidence * 1.1)
            
        return round(confidence, 3)
