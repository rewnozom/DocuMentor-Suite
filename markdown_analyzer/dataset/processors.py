# markdown_analyzer/dataset/processors.py
import re
import logging
from typing import Dict, List, Optional, Set, Any
from pathlib import Path

from ..core.document import DocumentStructure
from ..extractors.base import BaseExtractor
from ..core.patterns import (
    ARTICLE_NUMBER_PATTERNS,
    COMPATIBILITY_PATTERNS,
    TECHNICAL_PATTERNS
)


class DocumentProcessor:
    """
    Hanterar processering av individuella dokument för att extrahera strukturerad information.
    
    Integrerade förändringar:
      - Om inget artikelnummer hittas, genereras ett temporärt artikelnummer.
      - Konstruktor accepterar valfritt en lista med extraherare samt en logger.
    """
    def __init__(self, extractors: List[BaseExtractor] = None, logger: Optional[logging.Logger] = None):
        self.extractors = extractors if extractors is not None else []
        self.logger = logger or logging.getLogger(__name__)

    def process_document(self, filepath: Path) -> Optional[DocumentStructure]:
        """
        Bearbetar ett dokument och extraherar all relevant information.
        Om inget artikelnummer hittas, genereras ett temporärt artikelnummer.
        """
        try:
            content = self._read_file_content(filepath)
            if not content:
                return None

            # Extrahera grundläggande metadata
            article_number = self._extract_article_number(filepath.name, content)
            if not article_number:
                article_number = f"TEMP_{abs(hash(filepath.name))}"[:20]
                self.logger.warning(f"Generated temporary article number for {filepath}: {article_number}")

            # Skapa dokumentstruktur
            doc = DocumentStructure(
                filename=filepath.name,
                article_number=article_number,
                document_type=self._determine_document_type(filepath.name),
                product_name=self._extract_product_name(content) or "Unknown Product",
                description=self._extract_description(content) or "No description available"
            )

            # Kör alla extraherare
            for extractor in self.extractors:
                try:
                    result = extractor.extract(content)
                    self._apply_extraction_result(doc, result, extractor.__class__.__name__)
                except Exception as e:
                    self.logger.error(f"Error in extraction with {extractor.__class__.__name__}: {str(e)}")

            return doc

        except Exception as e:
            self.logger.error(f"Error processing {filepath}: {str(e)}")
            return None

    def _read_file_content(self, filepath: Path) -> Optional[str]:
        """Läser filinnehåll med olika teckenkodningar."""
        encodings = ['utf-8', 'latin-1', 'utf-16', 'cp1252']
        for encoding in encodings:
            try:
                return filepath.read_text(encoding=encoding)
            except UnicodeDecodeError:
                continue
            except Exception as e:
                self.logger.error(f"Error reading {filepath}: {str(e)}")
                break
        return None

    def _extract_article_number(self, filename: str, content: str) -> Optional[str]:
        """Extraherar artikelnummer från filnamn och innehåll."""
        # Försök först i filnamnet
        for pattern in ARTICLE_NUMBER_PATTERNS:
            if match := re.search(pattern, filename):
                return match.group(1)
        # Sedan i innehållet
        for pattern in ARTICLE_NUMBER_PATTERNS:
            if matches := list(re.finditer(pattern, content)):
                return matches[0].group(1)
        return None

    def _determine_document_type(self, filename: str) -> str:
        """
        Bestämmer dokumenttypen baserat på filnamnets suffix.
        
        Kollar efter följande suffix (oavsett stora eller små bokstäver):
          - _pro / _PRO            -> "produktinfo"
          - _produktblad          -> "produktblad"
          - _tek / _TEK           -> "teknisk_specifikation"
          - _sak                  -> "säkerhetsinformation"
          - _man / _MAN           -> "manual"
          - _ins / _INs           -> "installationer"
          - _cert / _CERT         -> "certifieringar"
          - _bro / _BRO           -> "broschyr"
          - _mdek                 -> "ospecificerad"
          - _pre / _PRE           -> "ospecificerad"
        
        Om inget matchar returneras "ospecificerad".
        """
        fname = filename.lower()
        mapping = {
            "pro": "produktinfo",
            "produktblad": "produktblad",
            "tek": "teknisk_specifikation",
            "sak": "säkerhetsinformation",
            "man": "manual",
            "ins": "installationer",
            "cert": "certifieringar",
            "bro": "broschyr",
            "mdek": "ospecificerad",
            "pre": "ospecificerad"
        }
        for suffix, doc_type in mapping.items():
            if f"_{suffix}" in fname:
                return doc_type
        return "ospecificerad"

    def _extract_product_name(self, content: str) -> Optional[str]:
        """Extraherar produktnamnet från innehållet."""
        m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if m:
            return m.group(1).strip()
        return None

    def _extract_description(self, content: str) -> Optional[str]:
        """Extraherar en kort beskrivning från innehållet."""
        lines = content.splitlines()
        if len(lines) >= 2:
            return " ".join(lines[1:3]).strip()
        return None

    def _apply_extraction_result(self, doc: DocumentStructure, result: Dict, extractor_name: str) -> None:
        """Applicerar extraherad information på dokumentstrukturen."""
        field_mapping = {
            'ImageExtractor': 'product_images',
            'CompatibilityExtractor': 'compatibility',
            'TechnicalExtractor': 'technical_specs',
            'PackagingExtractor': 'packaging_info'
        }
        if field_name := field_mapping.get(extractor_name):
            setattr(doc, field_name, result)


class TrainingDataProcessor:
    """
    Hanterar generering av träningsdata från processade dokument.
    """
    def __init__(self, chars_per_segment: int = 2000):
        self.logger = logging.getLogger(__name__)
        self.seen_examples: Set[str] = set()
        self.chars_per_segment = chars_per_segment

    def create_training_examples(self, doc: DocumentStructure, commands: List[str]) -> List[Dict]:
        """
        Skapar träningsexempel och hanterar segmentering av långa texter.
        """
        examples = []
        for cmd in commands:
            if example := self._create_example_for_command(doc, cmd):
                ai_output = example['ai_output']
                if len(ai_output) > self.chars_per_segment:
                    segments = self._segment_output(ai_output)
                    for i, segment in enumerate(segments, 1):
                        segmented_example = {
                            'user_input': f"{example['user_input']} del{i}",
                            'ai_output': segment
                        }
                        if self._is_unique_example(segmented_example):
                            examples.append(segmented_example)
                else:
                    if self._is_unique_example(example):
                        examples.append(example)
        return examples

    def _segment_output(self, text: str) -> List[str]:
        segments = []
        remaining = text
        while len(remaining) > self.chars_per_segment:
            break_point = remaining[:self.chars_per_segment].rfind('\n\n')
            if break_point == -1:
                break_point = remaining[:self.chars_per_segment].rfind('. ')
            if break_point == -1:
                break_point = self.chars_per_segment
            segments.append(remaining[:break_point].strip())
            remaining = remaining[break_point:].strip()
        if remaining:
            segments.append(remaining)
        return segments

    def _is_unique_example(self, example: Dict) -> bool:
        example_key = f"{example['user_input']}_{example['ai_output'][:100]}"
        if example_key not in self.seen_examples:
            self.seen_examples.add(example_key)
            return True
        return False

    def _create_example_for_command(self, doc: DocumentStructure, command: str) -> Optional[Dict]:
        creation_methods = {
            'f': self._create_full_info_example,
            's': self._create_summary_example,
            't': self._create_technical_example,
            'c': self._create_compatibility_example,
            'p': self._create_packaging_example
        }
        if method := creation_methods.get(command):
            return method(doc)
        else:
            self.logger.warning(f"Okänt kommando: {command}")
            return None

    def _create_full_info_example(self, doc: DocumentStructure) -> Optional[Dict]:
        if not doc.article_number or doc.article_number.startswith("TEMP_"):
            return None
        output_parts = [
            f"# {doc.product_name}\n" if doc.product_name else "",
            next((f"{img.image_ref}\n" for img in doc.product_images), ""),
            f"{doc.description}\n" if doc.description else ""
        ]
        return {"user_input": f"-f {doc.article_number}", "ai_output": "".join(filter(None, output_parts))}

    def _create_summary_example(self, doc: DocumentStructure) -> Optional[Dict]:
        if not (doc.compatibility or doc.technical_specs):
            return None
        output_parts = []
        if doc.product_images:
            output_parts.append(f"{doc.product_images[0].image_ref}\n")
        if doc.technical_specs:
            output_parts.append("## Tekniska Specifikationer\n")
            for spec in doc.technical_specs[:5]:
                output_parts.append(f"- {spec.category}: {spec.value} {spec.unit or ''}\n")
        if doc.compatibility:
            output_parts.append("\n## Kompatibilitet\n")
            for comp in doc.compatibility:
                output_parts.append(f"- {comp.description}\n")
        return {"user_input": f"-s {doc.article_number}", "ai_output": "".join(output_parts)}

    def _create_technical_example(self, doc: DocumentStructure) -> Optional[Dict]:
        if not doc.technical_specs:
            return None
        specs_by_category = {}
        for spec in doc.technical_specs:
            specs_by_category.setdefault(spec.category, []).append(spec)
        output_parts = ["## Tekniska Specifikationer\n"]
        for category, specs in specs_by_category.items():
            output_parts.append(f"\n### {category}\n")
            for spec in specs:
                output_parts.append(f"- {spec.value} {spec.unit or ''}\n")
        return {"user_input": f"-t {doc.article_number}", "ai_output": "".join(output_parts)}

    def _create_compatibility_example(self, doc: DocumentStructure) -> Optional[Dict]:
        if not doc.compatibility:
            return None
        comp_by_type = {}
        for comp in doc.compatibility:
            comp_by_type.setdefault(comp.type, []).append(comp)
        output_parts = []
        for comp_type, comps in comp_by_type.items():
            title = {
                'fits': 'Passar till',
                'requires': 'Kräver',
                'replaces': 'Ersätter',
                'accessory': 'Tillbehör'
            }.get(comp_type, comp_type.title())
            output_parts.append(f"\n## {title}\n")
            for comp in comps:
                if comp.target_article:
                    output_parts.append(f"- {comp.description} (Art.nr: {comp.target_article})\n")
                else:
                    output_parts.append(f"- {comp.description}\n")
        return {"user_input": f"-c {doc.article_number}", "ai_output": "\n".join(output_parts)}

    def _create_packaging_example(self, doc: DocumentStructure) -> Optional[Dict]:
        if not hasattr(doc, 'packaging_info') or not doc.packaging_info:
            return None
        output_parts = ["## Förpackningsinformation\n"]
        info = doc.packaging_info
        details = [
            f"- Typ: {info.package_type}",
            f"- EAN: {info.ean}" if info.ean else None,
            f"- Dimensioner: {info.dimensions}",
            f"- Bruttovikt: {info.weight_gross}",
            f"- Nettovikt: {info.weight_net}" if info.weight_net else None,
            f"- Antal per förpackning: {info.units_per_package}",
            f"- Volym: {info.volume}" if info.volume else None
        ]
        output_parts.extend(filter(None, details))
        return {"user_input": f"-p {doc.article_number}", "ai_output": "\n".join(output_parts)}
