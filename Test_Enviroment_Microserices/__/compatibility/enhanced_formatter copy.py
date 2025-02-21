# formatters.py
from typing import List, Dict
from compatibility.formatter import CompatibilityFormatter
from compatibility.models import CompatibilityRelation, RelationType

class EnhancedCompatibilityFormatter(CompatibilityFormatter):
    """
    Utökad formatering av kompatibilitetsinformation för träningsdata.
    Inkluderar EAN och leverantörsartiklar.
    """
    
    def format_for_training(self, relation: CompatibilityRelation) -> Dict[str, str]:
        """
        Formaterar en kompatibilitetsrelation för träning.
        Skapar flera träningsexempel baserat på olika identifierare.
        """
        examples = []
        
        # Basformatet för svaret
        response_parts = [
            f"Här är kompatibilitetsinformation för {relation.source_product.name}:"
        ]
        
        # Lägg till källproduktens artikelinformation
        if relation.source_product.article_number:
            response_parts.append(f"\nCopiax artikelnummer: {relation.source_product.article_number}")
        
        # Lägg till EAN om det finns
        if hasattr(relation.source_product, 'ean') and relation.source_product.ean:
            response_parts.append(f"EAN: {relation.source_product.ean}")
            
        # Lägg till leverantörsartikel om det finns
        if hasattr(relation.source_product, 'supplier_article') and relation.source_product.supplier_article:
            response_parts.append(f"Leverantörens artikelnummer: {relation.source_product.supplier_article}")
        
        response_parts.append("\nKompatibel med:")
        
        # Formatera målproduktinformation
        target_parts = self._format_target_product(relation)
        response_parts.extend(target_parts)
        
        # Lägg till tekniska detaljer och villkor
        requirement_parts = self._format_requirements(relation)
        if requirement_parts:
            response_parts.extend(["\nTekniska detaljer:"] + requirement_parts)
        
        condition_parts = self._format_conditions(relation)
        if condition_parts:
            response_parts.extend(["\nVillkor:"] + condition_parts)
        
        response = "\n".join(response_parts)
        
        # Skapa träningsexempel för varje identifierare
        if relation.source_product.article_number:
            examples.append({
                "user_input": f"-c {relation.source_product.article_number}",
                "ai_output": response
            })
            
        if hasattr(relation.source_product, 'ean') and relation.source_product.ean:
            examples.append({
                "user_input": f"-c {relation.source_product.ean}",
                "ai_output": response
            })
            
        if hasattr(relation.source_product, 'supplier_article') and relation.source_product.supplier_article:
            examples.append({
                "user_input": f"-c {relation.source_product.supplier_article}",
                "ai_output": response
            })
            
        # Alltid inkludera produktnamn som ett alternativ
        examples.append({
            "user_input": f"-c {relation.source_product.name}",
            "ai_output": response
        })
        
        return examples

    def _format_target_product(self, relation: CompatibilityRelation) -> List[str]:
        """Formaterar målproduktinformation"""
        parts = [f"* {relation.target_product.name}"]
        
        if relation.target_product.article_number:
            parts.append(f"  Copiax artikelnummer: {relation.target_product.article_number}")
            
        if hasattr(relation.target_product, 'ean') and relation.target_product.ean:
            parts.append(f"  EAN: {relation.target_product.ean}")
            
        if hasattr(relation.target_product, 'supplier_article') and relation.target_product.supplier_article:
            parts.append(f"  Leverantörens artikelnummer: {relation.target_product.supplier_article}")
            
        return parts

    def _format_requirements(self, relation: CompatibilityRelation) -> List[str]:
        """Formaterar tekniska krav"""
        parts = []
        for req in relation.technical_requirements:
            value = req.exact_value
            if req.unit:
                value = f"{value} {req.unit}"
            parts.append(f"* {req.category}: {value}")
        return parts

    def _format_conditions(self, relation: CompatibilityRelation) -> List[str]:
        """Formaterar villkor"""
        parts = []
        for condition in relation.conditions:
            parts.append(f"* {condition.description}")
            if condition.requirements:
                for req in condition.requirements:
                    parts.append(f"  - {req.category}: {req.exact_value or ''}")
        return parts