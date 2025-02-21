import os
import yaml
from typing import List, Dict, Optional
from dataclasses import dataclass
from ..Models.models import (
    CompatibilityRelation, RelationType,
    TechnicalRequirement, CompatibilityCondition
)

# Ladda konfiguration från YAML-fil
def load_config(path: str = "formatter_config.yaml") -> Dict:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    else:
        # Standardinställningar om konfigfil inte hittas
        return {
            "include_article_number": True,
            "include_ean": True,
            "include_supplier_article": True,
            "include_technical_requirements": True,
            "include_conditions": True,
            "include_certification": True,
            "include_compatibility_notes": True,
            "confidence_multipliers": {
                "no_article_number": 0.9,
                "conditions": 0.95,
                "technical_requirements": 0.98,
                "certification": 1.1,
                "max_confidence": 1.0
            },
            "relation_titles": {
                "DIRECT": "Passar till",
                "CONDITIONAL": "Passar till (med villkor)",
                "CERTIFIED": "Certifierad kompatibilitet",
                "REQUIRES": "Kräver",
                "REPLACES": "Ersätter",
                "REPLACED_BY": "Ersätts av",
                "ACCESSORY": "Tillbehör"
            },
            "training_examples": {
                "article_number": True,
                "ean": True,
                "supplier_article": True,
                "product_name": True,
                "product_name_confidence_factor": 0.9
            }
        }

CONFIG = load_config()

@dataclass
class TrainingExample:
    """Representerar ett träningsexempel."""
    user_input: str
    ai_output: str
    confidence: float = 1.0

class CompatibilityFormatter:
    """
    Grundläggande formatter för kompatibilitetsinformation.
    
    Styr vilka fält som inkluderas (t.ex. artikelnummer, tekniska krav, villkor m.m.)
    baserat på YAML-konfigurationen.
    """

    def format_relations(self, relations: List[CompatibilityRelation]) -> str:
        """
        Formaterar en samling kompatibilitetsrelationer till Markdown.
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

    def format_for_training(self, relation: CompatibilityRelation) -> List[TrainingExample]:
        """
        Formaterar en kompatibilitetsrelation för träningsdata.
        Skapar träningsdataexempel baserade på de identifierare som är aktiverade i konfigurationen.
        """
        examples = []
        response = self._format_compatibility_response(relation)
        confidence = self._calculate_confidence(relation)
        # Exempel med artikelnummer
        if (CONFIG.get("training_examples", {}).get("article_number", True)
                and relation.source_product.article_number):
            examples.append(TrainingExample(
                user_input=f"-c {relation.source_product.article_number}",
                ai_output=response,
                confidence=confidence
            ))
        # Exempel med produktnamn
        if CONFIG.get("training_examples", {}).get("product_name", True):
            factor = CONFIG.get("training_examples", {}).get("product_name_confidence_factor", 0.9)
            examples.append(TrainingExample(
                user_input=f'-c "{relation.source_product.name}"',
                ai_output=response,
                confidence=round(confidence * factor, 3)
            ))
        return examples

    def _format_compatibility_response(self, relation: CompatibilityRelation) -> str:
        """Formaterar ett detaljerat svar för träningsdata."""
        parts = [f"Här är kompatibilitetsinformation för {relation.source_product.name}:"]
        # Källproduktens detaljer
        if CONFIG.get("include_article_number", True) and relation.source_product.article_number:
            parts.append(f"Copiax artikelnummer: {relation.source_product.article_number}")
        if CONFIG.get("include_ean", True) and hasattr(relation.source_product, 'ean') and relation.source_product.ean:
            parts.append(f"EAN: {relation.source_product.ean}")
        if CONFIG.get("include_supplier_article", True) and hasattr(relation.source_product, 'supplier_article') and relation.source_product.supplier_article:
            parts.append(f"Leverantörens artikelnummer: {relation.source_product.supplier_article}")
        parts.append("")  # tom rad
        # Relationstyp och målprodukt
        parts.append(f"{self._get_section_title(relation.relation_type)}:")
        parts.append("")
        target_info = [f"* {relation.target_product.name}"]
        if CONFIG.get("include_article_number", True) and relation.target_product.article_number:
            target_info.append(f"  Copiax artikelnummer: {relation.target_product.article_number}")
        if CONFIG.get("include_ean", True) and hasattr(relation.target_product, 'ean') and relation.target_product.ean:
            target_info.append(f"  EAN: {relation.target_product.ean}")
        if CONFIG.get("include_supplier_article", True) and hasattr(relation.target_product, 'supplier_article') and relation.target_product.supplier_article:
            target_info.append(f"  Leverantörens artikelnummer: {relation.target_product.supplier_article}")
        if getattr(relation.target_product, 'series', None):
            target_info.append(f"  Serie: {relation.target_product.series}")
        if getattr(relation.target_product, 'variant', None):
            target_info.append(f"  Variant: {relation.target_product.variant}")
        parts.extend(target_info)
        # Tekniska krav
        if CONFIG.get("include_technical_requirements", True) and relation.technical_requirements:
            parts.append("")
            parts.append("Tekniska krav:")
            for req in relation.technical_requirements:
                parts.append(self._format_technical_requirement(req))
        # Villkor
        if CONFIG.get("include_conditions", True) and relation.conditions:
            parts.append("")
            parts.append("Villkor:")
            for condition in relation.conditions:
                parts.append(self._format_condition(condition))
        # Certifiering och noteringar
        if CONFIG.get("include_certification", True) and relation.certification:
            parts.append("")
            parts.append(f"Certifiering: {relation.certification}")
        if CONFIG.get("include_compatibility_notes", True) and relation.compatibility_notes:
            parts.append("")
            parts.append(f"Notering: {relation.compatibility_notes}")
        return "\n".join(parts)

    def _calculate_confidence(self, relation: CompatibilityRelation) -> float:
        """Beräknar konfidensnivå för en relation enligt multiplikatorer från konfig."""
        conf = 1.0
        multipliers = CONFIG.get("confidence_multipliers", {})
        if not relation.source_product.article_number:
            conf *= multipliers.get("no_article_number", 0.9)
        if relation.conditions:
            conf *= multipliers.get("conditions", 0.95)
        if relation.technical_requirements:
            conf *= multipliers.get("technical_requirements", 0.98)
        if relation.certification:
            conf = min(multipliers.get("max_confidence", 1.0), conf * multipliers.get("certification", 1.1))
        return round(conf, 3)

    def _group_relations(self, relations: List[CompatibilityRelation]) -> Dict[RelationType, List[CompatibilityRelation]]:
        """Grupperar relationer efter relationstyp."""
        grouped: Dict[RelationType, List[CompatibilityRelation]] = {}
        for relation in relations:
            grouped.setdefault(relation.relation_type, []).append(relation)
        return grouped

    def _get_section_title(self, rel_type: RelationType) -> str:
        """Returnerar en rubrik baserat på relationstyp, med titlar från konfig."""
        relation_titles = CONFIG.get("relation_titles", {})
        key = rel_type.name if hasattr(rel_type, "name") else str(rel_type)
        return relation_titles.get(key, str(rel_type).title())

    def _format_relation(self, relation: CompatibilityRelation) -> List[str]:
        """Formaterar en enskild relation som en Markdown-lista."""
        output = []
        base_info = f"- {relation.target_product.name}"
        if CONFIG.get("include_article_number", True) and relation.target_product.article_number:
            base_info += f" (Art.nr: {relation.target_product.article_number})"
        output.append(base_info)
        if getattr(relation.target_product, 'series', None):
            output.append(f"  Serie: {relation.target_product.series}")
        if getattr(relation.target_product, 'variant', None):
            output.append(f"  Variant: {relation.target_product.variant}")
        if CONFIG.get("include_technical_requirements", True) and relation.technical_requirements:
            output.append("  Tekniska krav:")
            for req in relation.technical_requirements:
                output.append(self._format_technical_requirement(req))
        if CONFIG.get("include_conditions", True) and relation.conditions:
            output.append("  Villkor:")
            for condition in relation.conditions:
                output.append(self._format_condition(condition))
        if CONFIG.get("include_certification", True) and relation.certification:
            output.append(f"  Certifiering: {relation.certification}")
        if CONFIG.get("include_compatibility_notes", True) and relation.compatibility_notes:
            output.append(f"  Notering: {relation.compatibility_notes}")
        return [line.rstrip() for line in output]

    def _format_technical_requirement(self, req: TechnicalRequirement) -> str:
        """Formaterar ett tekniskt krav."""
        if req.exact_value:
            value_str = f"{req.exact_value}"
        else:
            parts = []
            if req.min_value is not None:
                parts.append(f"min {req.min_value}")
            if req.max_value is not None:
                parts.append(f"max {req.max_value}")
            value_str = ", ".join(parts)
        unit_str = f" {req.unit}" if req.unit else ""
        description = f" ({req.description})" if req.description else ""
        return f"    - {req.category}: {value_str}{unit_str}{description}"

    def _format_condition(self, condition: CompatibilityCondition) -> str:
        """Formaterar ett villkor."""
        lines = [f"    - {condition.description}"]
        if condition.requirements:
            for req in condition.requirements:
                lines.append(self._format_technical_requirement(req))
        if condition.notes:
            lines.append(f"      Not: {condition.notes}")
        return "\n".join(lines)


class EnhancedCompatibilityFormatter(CompatibilityFormatter):
    """
    Utökad formatter som bygger vidare på CompatibilityFormatter.
    
    Denna version genererar träningsdataexempel för ytterligare identifierare (t.ex. EAN och leverantörsartikel)
    och anpassar utskriften med extra detaljer om dessa fält – allt styrt av YAML-konfigurationen.
    """

    def format_for_training(self, relation: CompatibilityRelation) -> List[TrainingExample]:
        """
        Skapar träningsdataexempel för en kompatibilitetsrelation med utökade identifierare.
        """
        examples = []
        response = self._format_compatibility_response(relation)
        confidence = self._calculate_confidence(relation)
        # Artikelnummer
        if (CONFIG.get("training_examples", {}).get("article_number", True)
                and relation.source_product.article_number):
            examples.append(TrainingExample(
                user_input=f"-c {relation.source_product.article_number}",
                ai_output=response,
                confidence=confidence
            ))
        # EAN
        if (CONFIG.get("training_examples", {}).get("ean", True)
                and hasattr(relation.source_product, 'ean')
                and relation.source_product.ean):
            examples.append(TrainingExample(
                user_input=f"-c {relation.source_product.ean}",
                ai_output=response,
                confidence=confidence
            ))
        # Leverantörsartikel
        if (CONFIG.get("training_examples", {}).get("supplier_article", True)
                and hasattr(relation.source_product, 'supplier_article')
                and relation.source_product.supplier_article):
            examples.append(TrainingExample(
                user_input=f"-c {relation.source_product.supplier_article}",
                ai_output=response,
                confidence=confidence
            ))
        # Produktnamn (alltid med lägre konfidens)
        if CONFIG.get("training_examples", {}).get("product_name", True):
            factor = CONFIG.get("training_examples", {}).get("product_name_confidence_factor", 0.9)
            examples.append(TrainingExample(
                user_input=f'-c "{relation.source_product.name}"',
                ai_output=response,
                confidence=round(confidence * factor, 3)
            ))
        return examples

    def _format_compatibility_response(self, relation: CompatibilityRelation) -> str:
        """
        Skapar ett ännu mer detaljerat svar för träningsdata med utökad information.
        Här inkluderas även extra fält (EAN, leverantörsartikel) om de finns och är aktiverade.
        """
        parts = [f"Här är kompatibilitetsinformation för {relation.source_product.name}:"]
        if CONFIG.get("include_article_number", True) and relation.source_product.article_number:
            parts.append(f"Copiax artikelnummer: {relation.source_product.article_number}")
        if CONFIG.get("include_ean", True) and hasattr(relation.source_product, 'ean') and relation.source_product.ean:
            parts.append(f"EAN: {relation.source_product.ean}")
        if CONFIG.get("include_supplier_article", True) and hasattr(relation.source_product, 'supplier_article') and relation.source_product.supplier_article:
            parts.append(f"Leverantörens artikelnummer: {relation.source_product.supplier_article}")
        parts.append("")
        # Relationstyp och målprodukt
        relation_type_text = self._get_section_title(relation.relation_type)
        parts.append(f"{relation_type_text}:")
        parts.append("")
        target_info = [f"* {relation.target_product.name}"]
        if CONFIG.get("include_article_number", True) and relation.target_product.article_number:
            target_info.append(f"  Copiax artikelnummer: {relation.target_product.article_number}")
        if CONFIG.get("include_ean", True) and hasattr(relation.target_product, 'ean') and relation.target_product.ean:
            target_info.append(f"  EAN: {relation.target_product.ean}")
        if CONFIG.get("include_supplier_article", True) and hasattr(relation.target_product, 'supplier_article') and relation.target_product.supplier_article:
            target_info.append(f"  Leverantörens artikelnummer: {relation.target_product.supplier_article}")
        if getattr(relation.target_product, 'series', None):
            target_info.append(f"  Serie: {relation.target_product.series}")
        if getattr(relation.target_product, 'variant', None):
            target_info.append(f"  Variant: {relation.target_product.variant}")
        parts.extend(target_info)
        # Tekniska krav
        if CONFIG.get("include_technical_requirements", True) and relation.technical_requirements:
            parts.append("")
            parts.append("Tekniska krav:")
            for req in relation.technical_requirements:
                parts.append(self._format_technical_requirement(req))
        # Villkor
        if CONFIG.get("include_conditions", True) and relation.conditions:
            parts.append("")
            parts.append("Villkor:")
            for condition in relation.conditions:
                parts.append(self._format_condition(condition))
        # Certifiering och noteringar
        if CONFIG.get("include_certification", True) and relation.certification:
            parts.append("")
            parts.append(f"Certifiering: {relation.certification}")
        if CONFIG.get("include_compatibility_notes", True) and relation.compatibility_notes:
            parts.append("")
            parts.append(f"Notering: {relation.compatibility_notes}")
        return "\n".join(parts)
