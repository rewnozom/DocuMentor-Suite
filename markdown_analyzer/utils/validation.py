# markdown_analyzer/utils/validation.py
from typing import List, Dict, Any
from ..core.document import DocumentStructure

class DataValidator:
    """Validerar extraherad data"""
    
    @staticmethod
    def validate_document(doc: DocumentStructure) -> List[str]:
        """Validerar ett helt dokumentobjekt"""
        errors = []
        
        # Kontrollera obligatoriska fält
        if not doc.article_number:
            errors.append("Saknar artikelnummer")
        elif doc.article_number.startswith("TEMP_"):
            errors.append("Använder temporärt artikelnummer")
        
        if not doc.product_name:
            errors.append("Saknar produktnamn")
        
        # Kontrollera bilder
        if not doc.product_images:
            errors.append("Saknar produktbilder")
        
        # Kontrollera kompatibilitet
        for comp in doc.compatibility:
            if not comp.target_article and comp.confidence > 0.7:
                errors.append(f"Hög konfidens ({comp.confidence}) för kompatibilitet utan artikelnummer")
        
        return errors
    
    @staticmethod
    def validate_technical_specs(specs: List[Dict[str, Any]]) -> List[str]:
        """Validerar tekniska specifikationer"""
        errors = []
        
        for spec in specs:
            if not spec.get('value'):
                errors.append(f"Teknisk spec saknar värde: {spec}")
            if spec.get('confidence', 0) > 0.9 and not spec.get('unit'):
                errors.append(f"Hög konfidens utan enhet: {spec}")
        
        return errors
