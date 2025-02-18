# markdown_analyzer/extractors/images.py

import re
from typing import List
from .base import BaseExtractor
from ..core.document import ProductImage

class ImageExtractor(BaseExtractor):
    """Extraherar och hanterar produktbilder"""
    
    def extract(self, content: str, article_number: str = "") -> List[ProductImage]:
        """
        Extraherar produktbilder från markdown-innehållet.
        Om flera bilder hittas, används den andra bilden; annars används den första.
        """
        images = []
        # Uppdaterat regex: tillåter valfri text (inklusive tom) inom klamrarna
        image_pattern = r'!\[.*?\]\((_page_(\d+)_(?:Picture|Figure)_(\d+)\.jpeg)\)'
        matches = list(re.finditer(image_pattern, content))
        if matches:
            chosen_match = matches[1] if len(matches) >= 2 else matches[0]
            image_ref, page_num, image_num = chosen_match.groups()
            mapped_path = f"./{article_number}/{image_ref}" if article_number else ""
            images.append(ProductImage(
                image_ref=image_ref,
                page_num=int(page_num),
                image_num=int(image_num),
                mapped_path=mapped_path
            ))
        return images