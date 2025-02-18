# markdown_analyzer/extractors/summary/formatter.py
from typing import Dict
from ...extractors.summary.models import ProductSummary
from ...extractors.technical.models import TechnicalValue

class SummaryFormatter:
    """
    Formaterar produktsammanfattningar för träningsdata.
    """
    
    def format_summary(self, summary: ProductSummary) -> str:
        """Formaterar en produktsammanfattning till markdown"""
        output_parts = []
        
        # Lägg till rubrik och bild
        output_parts.append(f"# {summary.product_name}")
        if summary.main_image:
            output_parts.append(f"\n{summary.main_image}")
        
        # Lägg till viktiga funktioner
        if summary.key_features:
            output_parts.append("\n## Viktiga egenskaper")
            for feature in summary.key_features:
                output_parts.append(f"- {feature}")
        
        # Lägg till tekniska höjdpunkter
        if summary.technical_highlights:
            output_parts.append("\n## Tekniska specifikationer")
            for spec in summary.technical_highlights:
                value = self._format_technical_value(spec.value)
                output_parts.append(f"- {spec.name}: {value}")
        
        # Lägg till kompatibilitetsinformation
        if summary.compatibility_info:
            output_parts.append("\n## Kompatibilitet")
            for info in summary.compatibility_info:
                output_parts.append(f"- {info}")
        
        # Lägg till ytterligare sektioner
        for section in summary.sections:
            if section.content:
                output_parts.append(f"\n## {section.title}")
                for line in section.content:
                    output_parts.append(line)
        
        return "\n".join(output_parts)

    def _format_technical_value(self, value: TechnicalValue) -> str:
        """Formaterar ett tekniskt värde med enhet"""
        if value.min_value is not None and value.max_value is not None:
            return (f"{value.min_value:.{value.precision}f} - "
                   f"{value.max_value:.{value.precision}f} "
                   f"{value.unit.name}")
        
        base_str = f"{value.value:.{value.precision}f} {value.unit.name}"
        if value.tolerance:
            base_str += f" ±{value.tolerance:.{value.precision}f}"
        if value.typical:
            base_str += " (typiskt)"
            
        return base_str

    def create_training_example(self, summary: ProductSummary) -> Dict:
        """Skapar ett träningsexempel från en sammanfattning"""
        return {
            "user_input": f"-s {summary.article_number}",
            "ai_output": self.format_summary(summary)
        }