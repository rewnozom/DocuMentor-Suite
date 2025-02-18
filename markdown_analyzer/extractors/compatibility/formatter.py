# markdown_analyzer/extractors/compatibility/formatter.py
from typing import List, Dict
from .models import (
    CompatibilityRelation, RelationType,
    TechnicalRequirement, CompatibilityCondition
)

class CompatibilityFormatter:
    """
    Formaterar kompatibilitetsinformation för träningsdata.
    """
    
    def format_relations(self, relations: List[CompatibilityRelation]) -> str:
        """
        Formaterar en samling kompatibilitetsrelationer till markdown.
        """
        if not relations:
            return "Ingen kompatibilitetsinformation tillgänglig."
        
        relations_by_type = self._group_relations(relations)
        output_parts = []
        
        for rel_type, rels in relations_by_type.items():
            section_title = self._get_section_title(rel_type)
            output_parts.append(f"\n## {section_title}")
            
            sorted_rels = sorted(rels, key=lambda x: x.confidence, reverse=True)
            for relation in sorted_rels:
                output_parts.extend(self._format_relation(relation))
        
        return "\n".join(output_parts)

    def _group_relations(self, relations: List[CompatibilityRelation]
                         ) -> Dict[RelationType, List[CompatibilityRelation]]:
        """Grupperar relationer efter typ"""
        grouped = {}
        for relation in relations:
            grouped.setdefault(relation.relation_type, []).append(relation)
        return grouped

    def _get_section_title(self, rel_type: RelationType) -> str:
        """Returnerar lämplig rubrik för en relationstyp"""
        titles = {
            RelationType.DIRECT: "Passar till",
            RelationType.CONDITIONAL: "Passar till (med villkor)",
            RelationType.CERTIFIED: "Certifierad kompatibilitet",
            RelationType.REQUIRES: "Kräver",
            RelationType.REPLACES: "Ersätter",
            RelationType.REPLACED_BY: "Ersätts av",
            RelationType.ACCESSORY: "Tillbehör"
        }
        return titles.get(rel_type, str(rel_type).title())

    def _format_relation(self, relation: CompatibilityRelation) -> List[str]:
        """Formaterar en enskild relation"""
        output = []
        
        base_info = f"- {relation.target_product.name}"
        if relation.target_product.article_number:
            base_info += f" (Art.nr: {relation.target_product.article_number})"
        output.append(base_info)
        
        if relation.target_product.series:
            output.append(f"  Serie: {relation.target_product.series}")
        if relation.target_product.variant:
            output.append(f"  Variant: {relation.target_product.variant}")
        
        if relation.technical_requirements:
            output.append("  Tekniska krav:")
            for req in relation.technical_requirements:
                output.append(self._format_technical_requirement(req))
        
        if relation.conditions:
            output.append("  Villkor:")
            for condition in relation.conditions:
                output.append(self._format_condition(condition))
        
        if relation.certification:
            output.append(f"  Certifiering: {relation.certification}")
        
        if relation.compatibility_notes:
            output.append(f"  Notering: {relation.compatibility_notes}")
        
        return [line.rstrip() for line in output]

    def _format_technical_requirement(self, req: TechnicalRequirement) -> str:
        """Formaterar ett tekniskt krav"""
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
        return f"    - {req.category}: {value_str}{unit_str}{description}"

    def _format_condition(self, condition: CompatibilityCondition) -> str:
        """Formaterar ett villkor"""
        output = [f"    - {condition.description}"]
        if condition.requirements:
            for req in condition.requirements:
                output.append(self._format_technical_requirement(req))
        if condition.notes:
            output.append(f"      Not: {condition.notes}")
        return "\n".join(output)

    def format_for_training(self, relations: List[CompatibilityRelation]) -> Dict:
        """
        Formaterar kompatibilitetsrelationer för träningsdata.
        """
        formatted_text = self.format_relations(relations)
        if relations:
            article_number = relations[0].source_product.article_number
            if article_number:
                return {
                    "user_input": f"-c {article_number}",
                    "ai_output": formatted_text
                }
        return None
