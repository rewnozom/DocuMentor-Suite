"""
content_analyzer.py – Modul för att analysera och strukturera markdown-innehåll

Detta modul delas upp i två huvudsakliga ansvarsområden:
  1. Definiera datamodeller för sektioner och relationer samt en enum för sektionstyper.
  2. En PatternMatcher som använder regex-mönster (från patterns.py) för att extrahera produktinformation, 
     artikelnummer och relationer.
  3. En ContentAnalyzer som bygger på PatternMatcher för att dela upp innehållet i sektioner, filtrera relevanta
     sektioner och sammanfoga relaterade sektioner.
"""

import re
import logging
from enum import Enum, auto
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Set, Tuple

# Importera mönster från vår patterns-modul
from .patterns import (
    ARTICLE_NUMBER_PATTERNS,
    BASIC_COMPATIBILITY_PATTERNS,
    COMPATIBILITY_RELATIONSHIPS,
    CONDITION_PATTERNS,
    TECHNICAL_PATTERNS,
)

# --- Datamodeller och Enum ---
class SectionType(Enum):
    PRODUCT_INFO = auto()
    COMPATIBILITY = auto()
    TECHNICAL = auto()
    INSTALLATION = auto()
    MAINTENANCE = auto()
    UNKNOWN = auto()

@dataclass
class Section:
    type: SectionType
    content: str
    start_line: int
    end_line: int
    confidence: float
    related_sections: Set[int] = field(default_factory=set)

@dataclass
class RelationInfo:
    source_product: str
    target_product: str
    relation_type: str
    confidence: float
    context: str = ""

# --- PatternMatcher – extraherar information med regex ---
class PatternMatcher:
    """
    Hanterar regex-baserad extraktion.
    Ansvarsområden:
      • Identifiera sektionstyp (PRODUCT_INFO eller COMPATIBILITY) med en konfidensbedömning.
      • Extrahera artikelnummer.
      • Extrahera produktrelationer med kontext.
    """
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self._compile_patterns()

    def _compile_patterns(self):
        # Kompilera mönster för sektionstyper
        self.product_info_patterns = [re.compile(p, re.MULTILINE) for p in ARTICLE_NUMBER_PATTERNS]  # Använd artikelmönster som en del av produktinfo
        self.compatibility_patterns = [re.compile(p, re.MULTILINE) for p in BASIC_COMPATIBILITY_PATTERNS]
        # Kompilera mönster för relationer – vi använder mönster från COMPATIBILITY_RELATIONSHIPS
        self.relation_patterns = {}
        for key, patterns in COMPATIBILITY_RELATIONSHIPS.items():
            self.relation_patterns[key] = [re.compile(p, re.MULTILINE) for p in patterns]

    def get_section_type(self, text: str, context: Optional[str] = None) -> Tuple[SectionType, float]:
        """
        Bestämmer sektionstypen utifrån texten.
        Returnerar en tuple (SectionType, confidence).
        """
        scores = {SectionType.PRODUCT_INFO: 0.0, SectionType.COMPATIBILITY: 0.0}
        # En förenklad poängsättning baserad på om vissa nyckelord finns
        if re.search(r'(?i)Art(?:ikel)?\s*nr', text):
            scores[SectionType.PRODUCT_INFO] += 0.2
        if re.search(r'(?i)passar\s+med|kompatibel\s+med', text):
            scores[SectionType.COMPATIBILITY] += 0.2
        # Extra bonus om texten är kort och börjar med rubrik
        if text.strip().startswith('#'):
            header_bonus = 0.1 / max(1, len(re.match(r'^#+', text).group()))
            for st in scores:
                scores[st] += header_bonus

        max_score = max(scores.values())
        if max_score == 0.0:
            return SectionType.UNKNOWN, 0.0
        chosen_type = max(scores.items(), key=lambda x: x[1])[0]
        return chosen_type, max_score

    def extract_article_numbers(self, text: str) -> List[str]:
        """Extraherar artikelnummer med hjälp av definierade mönster."""
        article_numbers = set()
        for pattern in ARTICLE_NUMBER_PATTERNS:
            for match in re.finditer(pattern, text, re.MULTILINE):
                number = match.group(1).strip()
                if number.isdigit() and 5 <= len(number) <= 8:
                    article_numbers.add(number)
        return sorted(list(article_numbers))

    def extract_relations(self, text: str, context_lines: int = 3) -> List[RelationInfo]:
        """
        Extraherar produktrelationer med kontext.
        Går igenom texten rad för rad och söker i varje rad (och omgivande rader) efter mönster.
        """
        relations = []
        product_info = self._extract_product_info(text)
        lines = text.split('\n')
        for i, line in enumerate(lines):
            context = '\n'.join(lines[max(0, i - context_lines): min(len(lines), i + context_lines + 1)])
            # Testa varje typ av relationsmönster
            for rel_type, patterns in self.relation_patterns.items():
                for pattern in patterns:
                    match = pattern.search(line)
                    if match:
                        target = match.group(1).strip() if match.groups() else ""
                        if target:
                            confidence = self._calculate_relation_confidence(line, context, product_info)
                            if confidence > 0.5:
                                determined_type = self._determine_relation_type(line)
                                relations.append(RelationInfo(
                                    source_product=product_info.get('name', ''),
                                    target_product=target,
                                    relation_type=determined_type,
                                    confidence=confidence,
                                    context=context
                                ))
        return relations

    def _extract_product_info(self, text: str) -> Dict[str, str]:
        """Extraherar grundläggande produktinformation (namn och artikelnummer)."""
        info = {}
        # Försök hitta ett produktnamn i en rubrik
        header_match = re.search(r'^#+\s*(.+)', text, re.MULTILINE)
        if header_match:
            name = header_match.group(1).strip()
            if name and not name.isdigit():
                info['name'] = name
        articles = self.extract_article_numbers(text)
        if articles:
            info['article_number'] = articles[0]
        return info

    def _determine_relation_type(self, text: str) -> str:
        """Avgör relationstypen baserat på textens innehåll."""
        if re.search(r'(?i)ersätter|uppgraderar|efterträder', text):
            return 'replacement'
        elif re.search(r'(?i)kräver|måste\s+ha|förutsätter', text):
            return 'requires'
        elif re.search(r'(?i)rekommenderas', text):
            return 'recommended'
        elif re.search(r'(?i)passar\s+(?:till|med)', text):
            return 'compatibility'
        elif re.search(r'(?i)integreras|kommunicerar', text):
            return 'integration'
        return 'general'

    def _calculate_relation_confidence(self, line: str, context: str, product_info: Dict[str, str]) -> float:
        """Enkel modell för att beräkna konfidensnivå för en relation."""
        confidence = 0.5
        for pattern_str in BASIC_COMPATIBILITY_PATTERNS:
            if re.search(pattern_str, line) or re.search(pattern_str, context):
                confidence += 0.05
        if re.search(r'(?i)passar\s+till', line):
            confidence += 0.1
        if re.search(r'(?i)kräver', line):
            confidence += 0.05
        if product_info.get('article_number'):
            confidence += 0.1
        if product_info.get('name'):
            confidence += 0.05
        if re.search(r'(?i)(kan|möjligen|eventuellt|kanske)', line):
            confidence -= 0.05
        return min(1.0, max(0.0, confidence))

    def has_table(self, text: str) -> bool:
        """Kontrollerar om text innehåller en Markdown-tabell."""
        return bool(re.search(r'\|.*\|', text))


# --- ContentAnalyzer – bearbetar hela dokumentets struktur ---
class ContentAnalyzer:
    """
    Analyserar ett markdown-dokument och delar upp det i sektioner.
    Ansvarsområden:
      • Dela upp innehållet rad för rad.
      • Bestämma sektionstyp och konfidens.
      • Extrahera och logga relationer.
      • Sammanfoga relaterade sektioner för att skapa ett renare dokument.
    """
    def __init__(self):
        self.matcher = PatternMatcher()
        self.logger = logging.getLogger(__name__)

    def analyze_content(self, content: str) -> List[Section]:
        """Dela upp innehållet i sektioner baserat på radbrytningar och kontext."""
        lines = content.split('\n')
        sections = []
        current_section = None
        buffer = []
        for i, line in enumerate(lines):
            context = '\n'.join(lines[max(0, i-2): min(len(lines), i+3)])
            section_type, conf = self.matcher.get_section_type(line, context=context)
            if conf > 0.7 and (current_section is None or section_type != current_section.type):
                if current_section:
                    current_section.content = "\n".join(buffer)
                    sections.append(current_section)
                    buffer = []
                current_section = Section(type=section_type, content="", start_line=i, end_line=i, confidence=conf)
            if current_section:
                buffer.append(line)
                current_section.end_line = i
        if current_section and buffer:
            current_section.content = "\n".join(buffer)
            sections.append(current_section)
        self._analyze_section_relations(sections)
        self._log_section_analysis(sections)
        return sections

    def _analyze_section_relations(self, sections: List[Section]) -> None:
        """Bestämmer vilka sektioner som är relaterade (t.ex. om de delar artikelnummer)."""
        for i, sec in enumerate(sections):
            sec.related_sections = set()
            for j, other in enumerate(sections):
                if i != j and self.matcher.is_related_section(sec, other):
                    sec.related_sections.add(j)

    def _log_section_analysis(self, sections: List[Section]) -> None:
        """Loggar en sammanfattning av de identifierade sektionerna."""
        self.logger.info("Sektionsanalys slutförd:")
        for i, sec in enumerate(sections):
            self.logger.info(
                f"Sektion {i+1}: Typ={sec.type.name}, Rader={sec.start_line}-{sec.end_line}, "
                f"Konfidens={sec.confidence:.2f}, Relaterade={sec.related_sections or 'Inga'}"
            )

    def merge_related_sections(self, sections: List[Section]) -> str:
        """
        Sammanfogar relaterade sektioner till ett enhetligt dokument.
        T.ex. att slå ihop produktinformation med relaterade kompatibilitetssektioner.
        """
        merged = []
        processed = set()
        for i, sec in enumerate(sections):
            if sec.type == SectionType.PRODUCT_INFO:
                group = [sec]
                processed.add(i)
                for j in sec.related_sections:
                    if j not in processed and sections[j].type in {SectionType.COMPATIBILITY, SectionType.TECHNICAL}:
                        group.append(sections[j])
                        processed.add(j)
                group.sort(key=lambda s: s.start_line)
                for s in group:
                    merged.append(s.content)
                merged.append("")  # tom rad mellan grupper
        # Lägg till övriga sektioner
        for i, sec in enumerate(sections):
            if i not in processed and sec.type in {SectionType.COMPATIBILITY, SectionType.TECHNICAL}:
                merged.append(sec.content)
                merged.append("")
        return "\n".join(merged).strip()
