from typing import Dict
from .base import BaseCommand
from ..core.document import DocumentStructure
from ..extractors.technical.technical_extractor import TechnicalExtractor
from ..extractors.compatibility import CompatibilityExtractor
from ..extractors.summary import SummaryProcessor

class FullInfoCommand(BaseCommand):
    """Command for full product information (-f)"""
    def process(self, doc: DocumentStructure) -> Dict:
        if not doc.article_number or doc.article_number.startswith("TEMP_"):
            return None

        return {
            "user_input": f"-f {doc.article_number}",
            "ai_output": self._format_full_info(doc)
        }

    def _format_full_info(self, doc: DocumentStructure) -> str:
        output_parts = []
        
        # Add product name as heading
        output_parts.append(f"# {doc.product_name}\n")
        
        # Add product image
        if doc.product_images:
            output_parts.append(f"{doc.product_images[0].image_ref}\n")
        
        # Add description
        if doc.description:
            output_parts.append(f"{doc.description}\n")
        
        # Add technical specifications if available
        if doc.technical_specs:
            output_parts.append("\n## Technical Specifications\n")
            for spec in doc.technical_specs:
                output_parts.append(f"- {spec.category}: {spec.value} {spec.unit or ''}\n")
        
        return "\n".join(output_parts)

class SummaryCommand(BaseCommand):
    """Command for product summaries (-s)"""
    def __init__(self):
        super().__init__()
        self.processor = SummaryProcessor()
        
    def process(self, doc: DocumentStructure) -> Dict:
        if not (doc.compatibility or doc.technical_specs):
            return None

        summary = self.processor.create_summary(doc)
        return {
            "user_input": f"-s {doc.article_number}",
            "ai_output": self.processor.formatter.format_summary(summary)
        }

class TechnicalCommand(BaseCommand):
    """Command for technical information (-t)"""
    def __init__(self):
        super().__init__()
        self.extractor = TechnicalExtractor()
        
    def process(self, doc: DocumentStructure) -> Dict:
        if not doc.technical_specs:
            return None

        tech_info = self.extractor.extract(doc.content, doc.tables)
        return {
            "user_input": f"-t {doc.article_number}",
            "ai_output": self.extractor.formatter.format_specifications(tech_info)
        }

class CompatibilityCommand(BaseCommand):
    """Command for compatibility information (-c)"""
    def __init__(self):
        super().__init__()
        self.extractor = CompatibilityExtractor()
        
    def process(self, doc: DocumentStructure) -> Dict:
        if not doc.compatibility:
            return None

        compat_info = self.extractor.extract(doc.content, doc.sections)
        return {
            "user_input": f"-c {doc.article_number}",
            "ai_output": self.extractor.formatter.format_relations(compat_info)
        }