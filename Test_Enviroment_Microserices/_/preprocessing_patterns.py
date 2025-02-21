# preprocessing_patterns.py

from typing import List, Dict, Optional, Tuple, Set
import re
import logging
from dataclasses import dataclass
from enum import Enum, auto

# --- KONFIGURATION ---
BASE_CONFIDENCE = 0.5
MIN_CONFIDENCE_TO_INCLUDE = 0.7
BASIC_BONUS = 0.05
DIRECT_BONUS = 0.1
REQUIRES_BONUS = 0.05
RECOMMENDED_BONUS = 0.05
PRODUCT_ARTICLE_BONUS = 0.1
PRODUCT_NAME_BONUS = 0.05
UNCERTAINTY_PENALTY = 0.05
SHORT_LINE_PENALTY = 0.05
LONG_LINE_BONUS = 0.05
# ----------------------

# Grundläggande kompatibilitetsmönster (BASIC)
BASIC_COMPATIBILITY_PATTERNS = [
    r'(?i)passar\s+(?:till|med|för)\s+([^\.]+)',
    r'(?i)passar\s+(?:på|i)?\s*([^\.]+)',
    r'(?i)kompatibel\s+med\s+([^\.]+)',
    r'(?i)compatible\s+with\s+([^\.]+)',
    r'(?i)kan\s+användas\s+(?:till|med)\s+([^\.]+)',
    r'(?i)(?:monteras|installeras)\s+tillsammans\s+med\s+([^\.]+)',
    r'(?i)fungerar\s+(?:med|tillsammans\s+med)\s+([^\.]+)',
    r'(?i)(?:godkänd|certifierad)\s+för\s+(?:användning\s+med)?\s+([^\.]+)',
    r'(?i)anpassad\s+för\s+([^\.]+)',
    r'(?i)avsedd\s+för\s+([^\.]+)',
    r'(?i)lämplig\s+(?:till|för)\s+([^\.]+)',
    r'(?i)tillbehör\s+till\s+([^\.]+)',
    r'(?i)rekommenderas?\s+(?:till|med|för)\s+([^\.]+)'
]

# Detaljerade kompatibilitetsrelationer
COMPATIBILITY_RELATIONSHIPS = {
    'direct': [
        r'(?i)kompatibel\s+med\s+([^\.]+)',
        r'(?i)compatible\s+with\s+([^\.]+)',
        r'(?i)fungerar\s+med\s+([^\.]+)',
        r'(?i)works\s+with\s+([^\.]+)',
        r'(?i)(?:kan|can)\s+användas\s+med\s+([^\.]+)',
        r'(?i)kan\s+kopplas\s+till\s+([^\.]+)',
        r'(?i)ansluts\s+till\s+([^\.]+)'
    ],
    'requires': [
        r'(?i)kräver\s+([^\.]+)',
        r'(?i)requires\s+([^\.]+)',
        r'(?i)måste\s+ha\s+([^\.]+)',
        r'(?i)förutsätter\s+([^\.]+)',
        r'(?i)beroende\s+av\s+([^\.]+)'
    ],
    'recommended': [
        r'(?i)rekommenderas?\s+(?:till|med|för)\s+([^\.]+)',
        r'(?i)recommended\s+(?:for|with)\s+([^\.]+)',
        r'(?i)(?:bäst|optimal)\s+(?:med|för)\s+([^\.]+)',
        r'(?i)(?:lämplig|suitable)\s+(?:för|for)\s+([^\.]+)'
    ]
}

# Sammanlagda kompatibilitetsmönster – kombinerar rubrikbaserade uttryck med de BASIC-uttrycken
COMPATIBILITY_PATTERNS = [
    # Rubrikbaserade uttryck:
    r'(?i)^#+\s*(?:Passar\s+(?:till|med|för)|Kompatibel\s+med)',
    r'(?i)^#+\s*Användningsområde',
    r'(?i).*\|\s*Passar\s+(?:till|med|för)\s*\|',
    r'(?i)(?:är\s+avsedd\s+för|kan\s+användas\s+(?:till|med|för)|passar\s+(?:till|med|för))',
    r'(?i)(?:kompatibel\s+med|fungerar\s+tillsammans\s+med)',
    r'(?i)(?:kräver|förutsätter|måste\s+ha)\s+([^\.]+)',
    r'(?i)(?:ersätter|kompletterar|integreras\s+med)\s+([^\.]+)',
    # Lägg in BASIC-kompatibilitetsmönster:
    *BASIC_COMPATIBILITY_PATTERNS
]

# Produktidentifieringsmönster
PRODUCT_PATTERNS = [
    r'(?i)^#+\s*(?:[A-Z0-9-]+\s+)?(?:SAFETRON|ASSA|ABLOY|SOLID|STEP|RCO|KABA|DORMA)',
    r'(?i)^#+\s*Art(?:ikel)?\.?\s*nr\.?:?\s*\d+',
    r'(?i)^#+\s*Produkt(?:information|beskrivning)',
    r'(?i)^#+\s*[A-Z0-9-]+(?:\s+[A-Z0-9-]+){1,3}\s*$',
    r'(?i)(?:E-nummer|RSK-nummer|Art\.?\s*nr\.?):\s*(\d{5,12})',
    r'(?i)^#+\s*(?:Serie|Produktserie|Variant):\s*([A-Z0-9-]+)'
]

# Relationsmönster – med ett specialfall för att fånga hela raden vid "NoKey-..."
RELATION_PATTERNS = [
    r'(?i)(NoKey-\d+\s*/\s*\d+\s+KG\d+\s+passar\s+för\s+montering\s+.+)',
    r'(?i)(?:kopplas\s+till|ansluts\s+till|sammankopplas\s+med)\s+([^\.]+)',
    r'(?i)(?:behöver|kräver|måste\s+ha)\s+([^\.]+)',
    r'(?i)(?:ersätter|uppgraderar|efterträder)\s+([^\.]+)',
    r'(?i)(?:integreras\s+med|fungerar\s+med|kommunicerar\s+med)\s+([^\.]+)'
]

# Använder en förenklad enum för sektionstyper (endast de typer vi behöver)
class SectionTypeExtended(Enum):
    PRODUCT_INFO = auto()
    COMPATIBILITY = auto()
    UNKNOWN = auto()

SectionType = SectionTypeExtended

@dataclass
class Section:
    type: SectionType
    content: str
    start_line: int
    end_line: int
    confidence: float
    related_sections: Set[int] = None

@dataclass
class RelationInfo:
    source_product: str
    target_product: str
    relation_type: str
    confidence: float
    context: str = ""

class PatternMatcher:
    """Hanterar regex-logik för att extrahera produktinformation och kompatibilitetsrelationer."""
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self._compile_patterns()
    
    def _compile_patterns(self):
        """Kompilerar de använda regex-mönstren."""
        self.patterns = {
            SectionType.PRODUCT_INFO: [re.compile(p, re.MULTILINE) for p in PRODUCT_PATTERNS],
            SectionType.COMPATIBILITY: [re.compile(p, re.MULTILINE) for p in COMPATIBILITY_PATTERNS]
        }
        self.relation_patterns = [re.compile(p, re.MULTILINE) for p in RELATION_PATTERNS]

    def get_section_type(self, text: str, context: Optional[str] = None) -> Tuple[SectionType, float]:
        """
        Identifierar om texten huvudsakligen innehåller produktinformation eller 
        kompatibilitetsinformation, och returnerar en konfidensnivå.
        """
        scores = {
            SectionType.PRODUCT_INFO: 0.0,
            SectionType.COMPATIBILITY: 0.0
        }
        for section_type, patterns in self.patterns.items():
            for pattern in patterns:
                for match in pattern.finditer(text):
                    base_score = BASE_CONFIDENCE
                    if match.start() < len(text) * 0.2:
                        base_score += 0.1
                    if text.startswith('#'):
                        header_level = len(re.match(r'^#+', text).group())
                        base_score += (0.1 / header_level)
                    if context:
                        context_score = self._calculate_context_score(match.group(), context)
                        base_score += context_score
                    scores[section_type] = max(scores[section_type], base_score)
        max_score = max(scores.values())
        if max_score == 0.0:
            return SectionType.UNKNOWN, 0.0
        section_type = max(scores.items(), key=lambda x: x[1])[0]
        return section_type, max_score

    def _calculate_context_score(self, match_text: str, context: str) -> float:
        """Beräknar en enkel kontextbaserad poäng."""
        score = 0.0
        if re.search(r'\d{5,8}', context):
            score += 0.1
        return score

    def extract_article_numbers(self, text: str) -> List[str]:
        """Extraherar artikelnummer från text."""
        article_patterns = [
            r'(?i)art(?:ikel)?\.?\s*nr\.?:?\s*(\d{5,8})',
            r'(?i)(\d{5,8})\s*(?:\(art(?:ikel)?\.?\s*nr\.?\))',
            r'(?i)^.*\|\s*(\d{5,8})\s*\|',
            r'(?i)(?:E-nr|RSK)\.?\s*:?\s*(\d{5,8})',
            r'(?i)(?<=\s)(\d{5,8})(?=\s)'
        ]
        article_numbers = set()
        for pattern in article_patterns:
            for match in re.finditer(pattern, text, re.MULTILINE):
                number = match.group(1).strip()
                if self._validate_article_number(number):
                    article_numbers.add(number)
        return sorted(list(article_numbers))

    def _validate_article_number(self, number: str) -> bool:
        """Validerar ett artikelnummer."""
        return number.isdigit() and 5 <= len(number) <= 8

    def extract_relations(self, text: str, context_lines: int = 3) -> List[RelationInfo]:
        """
        Extraherar produktrelationer från texten med enkel kontexthantering.
        """
        relations = []
        product_info = self._extract_product_info(text)
        lines = text.split('\n')
        for i, line in enumerate(lines):
            context_start = max(0, i - context_lines)
            context_end = min(len(lines), i + context_lines + 1)
            context = '\n'.join(lines[context_start:context_end])
            for pattern in self.relation_patterns:
                for match in pattern.finditer(line):
                    # Specialfall: om "NoKey-" ingår, ta hela raden
                    if "NoKey-" in match.group(0):
                        target_product = line.strip()
                    else:
                        target_product = match.group(1).strip() if match.groups() else ""
                    if target_product:
                        confidence = self._calculate_relation_confidence(line, context, product_info)
                        if confidence > 0.5:
                            relation_type = self._determine_relation_type(line)
                            relations.append(RelationInfo(
                                source_product=product_info.get('name', ''),
                                target_product=target_product,
                                relation_type=relation_type,
                                confidence=confidence,
                                context=context
                            ))
        return relations

    def _extract_product_info(self, text: str) -> Dict[str, str]:
        """Extraherar grundläggande produktinformation."""
        info = {}
        for pattern in self.patterns[SectionType.PRODUCT_INFO]:
            match = pattern.search(text)
            if match:
                name = match.group(0).strip('#').strip()
                if name and not name.isdigit():
                    info['name'] = name
                    break
        articles = self.extract_article_numbers(text)
        if articles:
            info['article_number'] = articles[0]
        return info

    def _determine_relation_type(self, text: str) -> str:
        """Avgör typ av relation baserat på texten."""
        if re.search(r'(?i)ersätter|uppgraderar|efterträder', text):
            return 'replacement'
        elif re.search(r'(?i)kräver|måste\s+ha|förutsätter', text):
            return 'requires'
        elif re.search(r'(?i)rekommenderas?', text):
            return 'recommended'
        elif re.search(r'(?i)passar\s+(?:till|med|för)', text):
            return 'compatibility'
        elif re.search(r'(?i)integreras|kommunicerar', text):
            return 'integration'
        return 'general'

    def _calculate_relation_confidence(self, line: str, context: str, product_info: Dict[str, str]) -> float:
        """
        Beräknar konfidensnivå för en relation med fokus på kompatibilitetsinformation.
        - Basvärde + bonus från BASIC_COMPATIBILITY_PATTERNS.
        - Bonus från 'direct', 'requires' och 'recommended' mönster.
        - Om kompatibilitetsnyckelord finns i raden/kontexten adderas produktinfo-bonus.
        - Osäkerhetsord sänker konfidensen.
        """
        confidence = BASE_CONFIDENCE
        
        for pattern_str in BASIC_COMPATIBILITY_PATTERNS:
            regex = re.compile(pattern_str)
            if regex.search(line) or regex.search(context):
                confidence += BASIC_BONUS
        
        for pattern_str in COMPATIBILITY_RELATIONSHIPS.get('direct', []):
            regex = re.compile(pattern_str, re.MULTILINE)
            if regex.search(line):
                confidence += DIRECT_BONUS
        
        for pattern_str in COMPATIBILITY_RELATIONSHIPS.get('requires', []):
            regex = re.compile(pattern_str, re.MULTILINE)
            if regex.search(line):
                confidence += REQUIRES_BONUS
        
        for pattern_str in COMPATIBILITY_RELATIONSHIPS.get('recommended', []):
            regex = re.compile(pattern_str, re.MULTILINE)
            if regex.search(line):
                confidence += RECOMMENDED_BONUS
        
        if re.search(r'(?i)(passar\s+(?:till|med|för)|kompatibel\s+med|användningsområde)', line + " " + context):
            if product_info.get('article_number'):
                confidence += PRODUCT_ARTICLE_BONUS
            if product_info.get('name'):
                confidence += PRODUCT_NAME_BONUS
        
        if re.search(r'(?i)(kan|möjligen|eventuellt|kanske)', line):
            confidence -= UNCERTAINTY_PENALTY
        if re.search(r'(?i)(om|när|under\s+förutsättning)', context):
            confidence -= UNCERTAINTY_PENALTY
        
        line_length = len(line.strip())
        if line_length < 20:
            confidence -= SHORT_LINE_PENALTY
        elif line_length > 100:
            confidence += LONG_LINE_BONUS
        
        confidence = min(1.0, max(0.0, confidence))
        return round(confidence, 3)

    def has_table(self, text: str) -> bool:
        """Kontrollerar om texten innehåller en tabell."""
        return bool(re.search(r'\|.*\|', text))

    def is_related_section(self, section1: Section, section2: Section) -> bool:
        """Avgör om två sektioner är relaterade."""
        if abs(section1.end_line - section2.start_line) <= 2:
            return True
        articles1 = set(self.extract_article_numbers(section1.content))
        articles2 = set(self.extract_article_numbers(section2.content))
        if articles1 and articles2 and articles1.intersection(articles2):
            return True
        relations1 = self.extract_relations(section1.content)
        relations2 = self.extract_relations(section2.content)
        if relations1 and relations2:
            products1 = {r.source_product for r in relations1} | {r.target_product for r in relations1}
            products2 = {r.source_product for r in relations2} | {r.target_product for r in relations2}
            if products1.intersection(products2):
                return True
        return False


# Förenklad ContentAnalyzer för att gruppera och filtrera sektioner
class ContentAnalyzer:
    """Analyserar och grupperar innehåll baserat på sammanhang."""
    def __init__(self):
        self.matcher = PatternMatcher()
        self.logger = logging.getLogger(__name__)
    
    def analyze_content(self, content: str) -> List[Section]:
        """
        Analyserar innehållet och identifierar sektioner med enkel kontexthantering.
        """
        lines = content.split('\n')
        sections = []
        current_section = None
        section_buffer = []
        for line_num, line in enumerate(lines):
            context_start = max(0, line_num - 2)
            context_end = min(len(lines), line_num + 3)
            context = '\n'.join(lines[context_start:context_end])
            section_type, confidence = self.matcher.get_section_type(line, context=context)
            if confidence > 0.7 and (not current_section or section_type != current_section.type):
                if current_section:
                    current_section.content = '\n'.join(section_buffer)
                    sections.append(current_section)
                    section_buffer = []
                current_section = Section(
                    type=section_type,
                    content='',
                    start_line=line_num,
                    end_line=line_num,
                    confidence=confidence,
                    related_sections=set()
                )
            if current_section:
                section_buffer.append(line)
                current_section.end_line = line_num
                if self.matcher.has_table(line):
                    current_section.confidence = min(1.0, current_section.confidence + 0.1)
        if current_section and section_buffer:
            current_section.content = '\n'.join(section_buffer)
            sections.append(current_section)
        self._analyze_section_relations(sections)
        self._log_section_analysis(sections)
        return sections
    
    def _analyze_section_relations(self, sections: List[Section]) -> None:
        """Analyserar och etablerar relationer mellan sektioner."""
        for i, section in enumerate(sections):
            section.related_sections = set()
            for j, other in enumerate(sections):
                if i != j and self._are_sections_related(section, other):
                    section.related_sections.add(j)
                    if section.type == SectionType.COMPATIBILITY and other.type == SectionType.PRODUCT_INFO:
                        section.confidence = min(1.0, section.confidence + 0.05)
    
    def _are_sections_related(self, section1: Section, section2: Section) -> bool:
        """Avgör om sektioner är relaterade."""
        if self.matcher.is_related_section(section1, section2):
            return True
        relations1 = self.matcher.extract_relations(section1.content)
        relations2 = self.matcher.extract_relations(section2.content)
        if relations1 and relations2:
            products1 = {r.source_product for r in relations1} | {r.target_product for r in relations1}
            products2 = {r.source_product for r in relations2} | {r.target_product for r in relations2}
            if products1.intersection(products2):
                return True
        articles1 = set(self.matcher.extract_article_numbers(section1.content))
        articles2 = set(self.matcher.extract_article_numbers(section2.content))
        if articles1 and articles2 and articles1.intersection(articles2):
            return True
        return False
    
    def filter_relevant_sections(self, sections: List[Section]) -> List[Section]:
        """
        Filtrerar ut sektioner med typ PRODUCT_INFO och COMPATIBILITY.
        """
        relevant_types = {SectionType.PRODUCT_INFO, SectionType.COMPATIBILITY}
        filtered_sections = [section for section in sections if section.type in relevant_types]
        # Vi kan använda MIN_CONFIDENCE_TO_INCLUDE här för att exkludera sektioner med för låg konfidens.
        filtered_sections = [section for section in filtered_sections if section.confidence >= MIN_CONFIDENCE_TO_INCLUDE]
        return sorted(filtered_sections, key=lambda x: x.start_line)
    
    def merge_related_sections(self, sections: List[Section]) -> str:
        """
        Sammanfogar relaterade sektioner till ett sammanhängande dokument.
        """
        merged_content = []
        processed_sections = set()
        for section in sections:
            if section.type == SectionType.PRODUCT_INFO:
                section_group = [section]
                processed_sections.add(sections.index(section))
                for related_idx in section.related_sections:
                    if related_idx not in processed_sections:
                        related_section = sections[related_idx]
                        if related_section.type == SectionType.COMPATIBILITY:
                            section_group.append(related_section)
                            processed_sections.add(related_idx)
                section_group.sort(key=lambda s: s.start_line)
                for s in section_group:
                    content = self._format_section_content(s)
                    merged_content.append(content)
                merged_content.append('')  # Tom rad mellan grupper
        for idx, section in enumerate(sections):
            if idx not in processed_sections and section.type == SectionType.COMPATIBILITY:
                content = self._format_section_content(section)
                merged_content.append(content)
                merged_content.append('')
        return '\n'.join(merged_content).strip()
    
    def _format_section_content(self, section: Section) -> str:
        """
        Formaterar sektionsinnehållet med enkel struktur.
        """
        lines = section.content.split('\n')
        formatted_lines = []
        for line in lines:
            if line.strip().startswith('#'):
                formatted_lines.append(line)
                continue
            if self.matcher.has_table(line):
                formatted_lines.append(line)
                continue
            if line.strip().startswith(('- ', '* ', '+ ')):
                formatted_lines.append(line)
                continue
            formatted_line = line.strip()
            if formatted_line:
                formatted_lines.append(formatted_line)
        return '\n'.join(formatted_lines)
    
    def _log_section_analysis(self, sections: List[Section]) -> None:
        """Loggar en sammanfattning av de identifierade sektionerna."""
        self.logger.info("Sektionsanalys slutförd:")
        for i, section in enumerate(sections):
            self.logger.info(
                f"Sektion {i+1}:\n"
                f"  Typ: {section.type.name}\n"
                f"  Rader: {section.start_line}-{section.end_line}\n"
                f"  Konfidens: {section.confidence:.2f}\n"
                f"  Relaterade sektioner: {section.related_sections if section.related_sections else 'Inga'}"
            )
