# Metadata

import re
from .base import BaseExtractor
from ..core.patterns import ARTICLE_NUMBER_PATTERNS
from ..core.constants import VALID_DOCUMENT_TYPES

class MetadataExtractor(BaseExtractor):
    """Extraherar grundläggande metadata från dokument"""

    def extract_article_number(self, filename: str, content: str) -> str:
        filename = filename.replace('_', ' ')
        for pattern in ARTICLE_NUMBER_PATTERNS:
            match = re.search(pattern, filename)
            if match:
                self.logger.debug(f"Hittade artikelnummer i filnamn: {match.group(1)}")
                return match.group(1)
        content_start = content[:1000]
        for pattern in ARTICLE_NUMBER_PATTERNS:
            matches = list(re.finditer(pattern, content_start))
            if matches:
                return matches[0].group(1)
        temp_id = f"TEMP_{abs(hash(filename + content[:100]))}"[:20]
        self.logger.warning(f"Inget artikelnummer hittat, genererar: {temp_id}")
        return temp_id

    def extract_document_type(self, filename: str) -> str:
        parts = filename.lower().split('_')
        if len(parts) > 1:
            suffix = parts[-1].split('.')[0]
            if suffix in VALID_DOCUMENT_TYPES:
                return VALID_DOCUMENT_TYPES[suffix]
        for suffix, doc_type in VALID_DOCUMENT_TYPES.items():
            if suffix in filename.lower():
                return doc_type
        return "ospecificerad"

    def extract_product_name(self, content: str) -> str:
        """Extracts product name from markdown content"""
        if match := re.search(r'^#\s+([^(\n]+)', content, re.MULTILINE):
            return match.group(1).strip()
        self.logger.warning("No product name found in content")
        return "Unknown Product"

    def extract_description(self, content: str) -> str:
        """En enkel extraktion av en kort beskrivning från innehållet"""
        lines = content.splitlines()
        if len(lines) >= 2:
            return " ".join(lines[1:3]).strip()
        return ""
