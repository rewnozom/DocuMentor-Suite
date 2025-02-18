# markdown_analyzer/trainers/commands.py

from typing import List, Dict
from trainers.base import BaseTrainer  # Förutsätter att BaseTrainer är definierad
from trainers.formatters import MarkdownFormatter  # Exempelimport för formatering
from core.document import DocumentStructure


class BasicInfoTrainer(BaseTrainer):
    """Genererar träningsdata för grundläggande information (-f)."""
    
    def create_training_data(self, doc: DocumentStructure) -> List[Dict]:
        if not doc.article_number or doc.article_number.startswith("TEMP_"):
            return []
        
        output_parts = []
        # Lägg till produktnamn som rubrik
        output_parts.append(self.formatter.format_heading(doc.product_name))
        
        # Lägg till produktbild om tillgänglig
        if doc.product_images:
            output_parts.append(
                self.formatter.format_image(doc.product_images[0].image_ref, doc.article_number)
            )
        
        # Lägg till beskrivning
        if doc.description:
            output_parts.append(doc.description + "\n\n")
        
        example = {
            "command": "f",
            "article_number": doc.article_number,
            "input_text": f"-f {doc.article_number}",
            "output_text": "".join(output_parts),
            "confidence": 1.0
        }
        
        return [example] if self.validate_example(example) else []
    
    def validate_example(self, example: Dict) -> bool:
        return bool(example.get("output_text"))


class SummaryTrainer(BaseTrainer):
    """Genererar träningsdata för sammanfattningar (-s)."""
    
    def create_training_data(self, doc: DocumentStructure) -> List[Dict]:
        if not (doc.compatibility or doc.technical_specs):
            return []
        
        output_parts = []
        
        # Lägg till produktbild om tillgänglig
        if doc.product_images:
            output_parts.append(
                self.formatter.format_image(doc.product_images[0].image_ref, doc.article_number)
            )
        
        # Lägg till kompatibilitetsinformation
        if doc.compatibility:
            output_parts.append(self.formatter.format_heading("Kompatibilitet", 2))
            compat_items = []
            for comp in doc.compatibility:
                if hasattr(comp, 'target_article') and comp.target_article:
                    compat_items.append(f"{comp.description} (Art.nr: {comp.target_article})")
                else:
                    compat_items.append(comp.description)
            output_parts.append(self.formatter.format_list(compat_items))
        
        # Lägg till tekniska höjdpunkter
        if doc.technical_specs:
            output_parts.append(self.formatter.format_heading("Tekniska Specifikationer", 2))
            tech_items = []
            for spec in doc.technical_specs:
                if hasattr(spec.value, 'format_value'):
                    value_str = spec.value.format_value()
                else:
                    value_str = f"{spec.value} {spec.unit or ''}"
                tech_items.append(f"{spec.category}: {value_str}")
            output_parts.append(self.formatter.format_list(tech_items))
        
        example = {
            "command": "s",
            "article_number": doc.article_number,
            "input_text": f"-s {doc.article_number}",
            "output_text": "".join(output_parts),
            "confidence": 1.0
        }
        
        return [example] if self.validate_example(example) else []
    
    def validate_example(self, example: Dict) -> bool:
        # Enkel validering: output_text måste finnas
        return bool(example.get("output_text"))


class TechnicalTrainer(BaseTrainer):
    """Genererar träningsdata för teknisk information (-t)."""
    
    def create_training_data(self, doc: DocumentStructure) -> List[Dict]:
        if not doc.technical_specs:
            return []
        
        specs_by_category = {}
        for spec in doc.technical_specs:
            specs_by_category.setdefault(spec.category, []).append(spec)
        
        output_parts = []
        # Skapa formaterad output per kategori
        for category, specs in specs_by_category.items():
            output_parts.append(self.formatter.format_heading(category.title(), 2))
            for spec in specs:
                if hasattr(spec.value, 'format_value'):
                    value_str = spec.value.format_value()
                else:
                    value_str = f"{spec.value} {spec.unit or ''}"
                output_parts.append(f"- {value_str}\n")
        
        example = {
            "command": "t",
            "article_number": doc.article_number,
            "input_text": f"-t {doc.article_number}",
            "output_text": "".join(output_parts),
            "confidence": 1.0
        }
        
        return [example] if self.validate_example(example) else []
    
    def validate_example(self, example: Dict) -> bool:
        return bool(example.get("output_text"))


class CompatibilityTrainer(BaseTrainer):
    """Genererar träningsdata för kompatibilitetsinformation (-c)."""
    
    def create_training_data(self, doc: DocumentStructure) -> List[Dict]:
        if not doc.compatibility:
            return []
        
        by_type = {}
        for comp in doc.compatibility:
            by_type.setdefault(comp.type, []).append(comp)
        
        output_parts = []
        # Skapa formaterad output per kompatibilitetstyp
        for comp_type, comps in by_type.items():
            title = {
                'fits': 'Passar till',
                'requires': 'Kräver',
                'replaces': 'Ersätter',
                'accessory': 'Tillbehör'
            }.get(comp_type, comp_type.title())
            
            output_parts.append(self.formatter.format_heading(title, 2))
            compat_items = []
            for comp in comps:
                if hasattr(comp, 'target_article') and comp.target_article:
                    compat_items.append(f"{comp.description} (Art.nr: {comp.target_article})")
                else:
                    compat_items.append(comp.description)
            output_parts.append(self.formatter.format_list(compat_items))
        
        example = {
            "command": "c",
            "article_number": doc.article_number,
            "input_text": f"-c {doc.article_number}",
            "output_text": "".join(output_parts),
            "confidence": 1.0
        }
        
        return [example] if self.validate_example(example) else []
    
    def validate_example(self, example: Dict) -> bool:
        return bool(example.get("output_text"))
