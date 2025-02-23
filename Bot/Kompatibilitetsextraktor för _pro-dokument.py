#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Förbättrad Kompatibilitetsextraktor för _pro-dokument

Denna avancerade mikroservice:
1. Letar efter _pro-dokument i den angivna katalogstrukturen
2. Extraherar kompatibilitetsrelationer med omfattande regex-mönster
3. Klassificerar relationer i detaljerade kategorier
4. Identifierar potentiella nya relationstyper med NLP-metoder
5. Skapar utförlig dokumentation och analys för varje steg
6. Sparar resultaten i en organiserad katalogstruktur med JSONL-filer
"""

import os
import re
import json
import logging
import random
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple, Set, Counter
from collections import defaultdict, Counter

# Konfigurera loggning
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("enhanced_compatibility_extractor.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Definiera katalogstrukturer
BASE_DIR = Path("./converted_docs")
OUTPUT_DIR = Path("./extracted_data/compatibility")
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

# Skapa struktur för resultatkategorier
RESULTS_STRUCTURE = {
    "matched": OUTPUT_DIR / "matched",
    "unmatched": OUTPUT_DIR / "unmatched",
    "samples": OUTPUT_DIR / "samples",
    "patterns": OUTPUT_DIR / "patterns",
    "reports": OUTPUT_DIR / "reports",
    "discovered": OUTPUT_DIR / "discovered",
    "relations": OUTPUT_DIR / "relations",
    "validation": OUTPUT_DIR / "validation" 
}

# Skapa kataloger
for dir_path in RESULTS_STRUCTURE.values():
    dir_path.mkdir(exist_ok=True, parents=True)

# -----------------------------------------------------------
# UTÖKADE KOMPATIBILITETSMÖNSTER
# -----------------------------------------------------------

# Grundläggande kompatibilitetsmönster
BASIC_COMPATIBILITY_PATTERNS = [
    r'(?i)passar\s+(?:till|med|för)\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)passar\s+(?:på|i)?\s*([^\.;]+)(?:\.|\;|$)',
    r'(?i)kompatibel\s+med\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)compatible\s+with\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)kan\s+användas\s+(?:till|med)\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)(?:monteras|installeras)\s+tillsammans\s+med\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)fungerar\s+(?:med|tillsammans\s+med)\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)(?:godkänd|certifierad)\s+för\s+(?:användning\s+med)?\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)anpassad\s+för\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)avsedd\s+för\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)lämplig\s+(?:till|för)\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)tillbehör\s+till\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)rekommenderas?\s+(?:till|med|för)\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)designed\s+for\s+(?:use\s+with)?\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)(?:tillval|option)\s+(?:till|för)\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)utformad\s+för\s+(?:användning\s+med)?\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)specifically\s+for\s+([^\.;]+)(?:\.|\;|$)',
]

# Detaljerade kompatibilitetsrelationer för olika relationstyper
COMPATIBILITY_RELATIONSHIPS = {
    'direct': [
        r'(?i)kompatibel\s+med\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)compatible\s+with\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)fungerar\s+med\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)works\s+with\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)(?:kan|can)\s+användas\s+med\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)kan\s+kopplas\s+till\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)ansluts\s+till\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)connects\s+(?:to|with)\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)interfaces?\s+with\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)interacts?\s+with\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)är\s+kompatib(?:el|la)\s+med\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)fullt\s+kompatib(?:el|la)\s+med\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)fully\s+compatible\s+with\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)(?:100%|helt)\s+kompatib(?:el|la)\s+med\s+([^\.;]+)(?:\.|\;|$)',
    ],
    'requires': [
        r'(?i)kräver\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)requires\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)måste\s+ha\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)förutsätter\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)beroende\s+av\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)dependent\s+on\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)needs?\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)behöver\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)måste\s+användas?\s+med\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)must\s+be\s+used\s+with\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)fungerar\s+endast\s+med\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)only\s+works\s+with\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)obligatorisk(?:t)?\s+med\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)nödvändig(?:t)?\s+med\s+([^\.;]+)(?:\.|\;|$)',
    ],
    'recommended': [
        r'(?i)rekommenderas?\s+(?:till|med|för)\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)recommended\s+(?:for|with)\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)(?:bäst|optimal)\s+(?:med|för)\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)(?:lämplig|suitable)\s+(?:för|for)\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)passar\s+utmärkt\s+(?:till|med|för)\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)ideally?\s+(?:suited|used)\s+(?:for|with)\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)bästa\s+val(?:et)?\s+för\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)best\s+choice\s+for\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)idealisk(?:t)?\s+för\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)ideal\s+for\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)perfekt\s+för\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)perfect\s+for\s+([^\.;]+)(?:\.|\;|$)',
    ],
    'fits': [
        r'(?i)passar\s+(?:till|med|för)\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)passar\s+(?:på|i)\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)fits\s+(?:on|in|with)\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)(?:can\s+be|är)\s+monterad\s+(?:på|i)\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)(?:can\s+be|är)\s+installerad\s+(?:på|i)\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)designed\s+to\s+fit\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)utformad\s+för\s+att\s+passa\s+(?:till|med|för|på|i)\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)måttanpassad\s+för\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)storleksanpassad\s+för\s+([^\.;]+)(?:\.|\;|$)',
    ],
    'designed_for': [
        r'(?i)speciellt\s+(?:designad|utvecklad|framtagen)\s+för\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)specially\s+designed\s+for\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)specifically\s+(?:designed|developed)\s+for\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)anpassad\s+för\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)tailored\s+for\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)skräddarsydd\s+för\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)optimerad\s+för\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)optimized\s+for\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)utformad\s+(?:specifikt)?\s+för\s+(?:användning\s+med)?\s+([^\.;]+)(?:\.|\;|$)',
    ],
    'accessory': [
        r'(?i)tillbehör\s+(?:till|för)\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)accessor(?:y|ies)\s+for\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)extra\s+(?:utrustning|tillbehör)\s+(?:till|för)\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)additional\s+(?:equipment|accessory)\s+for\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)(?:tillval|option)\s+(?:till|för)\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)add-on\s+(?:for|to)\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)komplement\s+(?:till|för)\s+([^\.;]+)(?:\.|\;|$)',
        r'(?i)kompletterande\s+(?:del|produkt|utrustning)\s+(?:till|för)\s+([^\.;]+)(?:\.|\;|$)',
    ]
}

# Ersättningsmönster
REPLACEMENT_PATTERNS = [
    r'(?i)ersätter\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)ersättning\s+för\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)ersätts\s+av\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)tidigare\s+version:\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)ny\s+version\s+av\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)replaces\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)replacement\s+for\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)efterträdare\s+till\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)successor\s+(?:to|of)\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)upgraded\s+version\s+of\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)uppgraderad\s+version\s+av\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)(?:istället|instead)\s+(?:för|of)\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)alternativ\s+till\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)alternative\s+to\s+([^\.;]+)(?:\.|\;|$)',
]

# Villkorsmönster
CONDITION_PATTERNS = [
    r'(?i)(?:endast|bara)\s+(?:vid|för|med)\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)kräver\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)förutsätter\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)under\s+förutsättning\s+att\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)om\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)när\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)only\s+(?:with|for|when)\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)requires\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)dependent\s+on\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)subject\s+to\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)contingent\s+(?:on|upon)\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)villkorat\s+av\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)prerequisites?:\s*([^\.;]+)(?:\.|\;|$)',
    r'(?i)förut?sättning(?:ar)?:\s*([^\.;]+)(?:\.|\;|$)',
]

# Familjemönster
FAMILY_PATTERNS = [
    r'(?i)(?:ingår\s+i|del\s+av)\s+(?:serie|familj)?\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)tillhör\s+(?:serie|familj)\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)(?:serie|familj):\s*([^\.;]+)(?:\.|\;|$)',
    r'(?i)(?:produktserie|product\s+series):\s*([^\.;]+)(?:\.|\;|$)',
    r'(?i)(?:part|member)\s+of\s+(?:the)?\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)(?:belongs|belongs\s+to)\s+(?:the)?\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)i\s+(?:serien|familjen)\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)ur\s+(?:serien|familjen)\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)from\s+the\s+([^\.;]+)\s+series(?:\.|\;|$)',
    r'(?i)in\s+the\s+([^\.;]+)\s+(?:series|family|range)(?:\.|\;|$)',
    r'(?i)within\s+the\s+([^\.;]+)\s+(?:series|family|range)(?:\.|\;|$)',
]

# Versioner och generationsmönster
VERSION_PATTERNS = [
    r'(?i)version(?:\s+|\:)([^\.;]+)(?:\.|\;|$)',
    r'(?i)generation(?:\s+|\:)([^\.;]+)(?:\.|\;|$)',
    r'(?i)(?:ver|v)(?:\.|:)\s*([^\.;]+)(?:\.|\;|$)',
    r'(?i)(?:gen|g)(?:\.|:)\s*([^\.;]+)(?:\.|\;|$)',
    r'(?i)modell(?:\s+|\:)([^\.;]+)(?:\.|\;|$)',
    r'(?i)model(?:\s+|\:)([^\.;]+)(?:\.|\;|$)',
    r'(?i)typ(?:\s+|\:)([^\.;]+)(?:\.|\;|$)',
    r'(?i)type(?:\s+|\:)([^\.;]+)(?:\.|\;|$)',
    r'(?i)revision(?:\s+|\:)([^\.;]+)(?:\.|\;|$)',
    r'(?i)utgåva(?:\s+|\:)([^\.;]+)(?:\.|\;|$)',
    r'(?i)edition(?:\s+|\:)([^\.;]+)(?:\.|\;|$)',
]

# Negativt kompatibilitetsmönster - vad produkten INTE är kompatibel med
NEGATIVE_COMPATIBILITY_PATTERNS = [
    r'(?i)(?:inte|ej)\s+kompatibel\s+med\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)not\s+compatible\s+with\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)(?:passar|fungerar)\s+(?:inte|ej)\s+(?:till|med|för)\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)does\s+not\s+(?:work|function)\s+with\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)(?:kan|can)(?:not)?\s+(?:inte|ej)\s+användas\s+med\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)incompatible\s+with\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)oförenlig\s+med\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)(?:inte|ej)\s+(?:lämplig|suitable)\s+för\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)unsuitable\s+for\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)(?:inte|ej)\s+avsedd\s+för\s+([^\.;]+)(?:\.|\;|$)',
    r'(?i)not\s+intended\s+for\s+([^\.;]+)(?:\.|\;|$)',
]

# Mönster för att upptäcka specifika artikelnummer i kompatibilitetsförhållanden
ARTICLE_RELATION_PATTERNS = [
    r'(?i)kompatib(?:el|la)\s+med\s+(?:[^\.;]*?)((?:\d{5,8}|E-\s*\d{7})(?:\s*,\s*(?:\d{5,8}|E-\s*\d{7}))*)',
    r'(?i)passar\s+(?:till|med|för)\s+(?:[^\.;]*?)((?:\d{5,8}|E-\s*\d{7})(?:\s*,\s*(?:\d{5,8}|E-\s*\d{7}))*)',
    r'(?i)works\s+with\s+(?:[^\.;]*?)((?:\d{5,8}|E-\s*\d{7})(?:\s*,\s*(?:\d{5,8}|E-\s*\d{7}))*)',
    r'(?i)fungerar\s+med\s+(?:[^\.;]*?)((?:\d{5,8}|E-\s*\d{7})(?:\s*,\s*(?:\d{5,8}|E-\s*\d{7}))*)',
    r'(?i)(?:avsedd|designad)\s+för\s+(?:[^\.;]*?)((?:\d{5,8}|E-\s*\d{7})(?:\s*,\s*(?:\d{5,8}|E-\s*\d{7}))*)',
]

# Listor med artiklar som produkten är kompatibel med
LIST_RELATION_PATTERNS = [
    r'(?i)Kompatibel\s+med(?:\s+följande)?(?:\s+produkter)?(?:\s+artiklar)?:\s*\n*((?:\s*[-•*]\s*[^\n]+\n*)+)',
    r'(?i)Compatible\s+with(?:\s+the\s+following)?(?:\s+products)?(?:\s+articles)?:\s*\n*((?:\s*[-•*]\s*[^\n]+\n*)+)',
    r'(?i)Passar\s+(?:till|för|med)(?:\s+följande)?(?:\s+produkter)?(?:\s+artiklar)?:\s*\n*((?:\s*[-•*]\s*[^\n]+\n*)+)',
    r'(?i)Fits\s+(?:with|to)(?:\s+the\s+following)?(?:\s+products)?(?:\s+articles)?:\s*\n*((?:\s*[-•*]\s*[^\n]+\n*)+)',
    r'(?i)Fungerar\s+med(?:\s+följande)?(?:\s+produkter)?(?:\s+artiklar)?:\s*\n*((?:\s*[-•*]\s*[^\n]+\n*)+)',
    r'(?i)Works\s+with(?:\s+the\s+following)?(?:\s+products)?(?:\s+articles)?:\s*\n*((?:\s*[-•*]\s*[^\n]+\n*)+)',
]

# Sammanfoga alla mönster till en enkel datastruktur för enklare hantering
PATTERN_GROUPS = {
    "basic": BASIC_COMPATIBILITY_PATTERNS,
    "direct": COMPATIBILITY_RELATIONSHIPS["direct"],
    "requires": COMPATIBILITY_RELATIONSHIPS["requires"],
    "recommended": COMPATIBILITY_RELATIONSHIPS["recommended"],
    "fits": COMPATIBILITY_RELATIONSHIPS["fits"],
    "designed_for": COMPATIBILITY_RELATIONSHIPS["designed_for"],
    "accessory": COMPATIBILITY_RELATIONSHIPS["accessory"],
    "replacement": REPLACEMENT_PATTERNS,
    "condition": CONDITION_PATTERNS,
    "family": FAMILY_PATTERNS,
    "version": VERSION_PATTERNS,
    "negative": NEGATIVE_COMPATIBILITY_PATTERNS,
    "article_relation": ARTICLE_RELATION_PATTERNS,
    "list_relation": LIST_RELATION_PATTERNS
}

# Utökad datastruktor för att hålla reda på mönster och resultat
ALL_PATTERNS = []
PATTERN_INDEX_MAP = {}
PATTERN_GROUP_MAP = {}

# Bygg upp datastrukturer för mönsterindexering
pattern_index = 0
for group_name, patterns in PATTERN_GROUPS.items():
    for pattern in patterns:
        ALL_PATTERNS.append(pattern)
        PATTERN_INDEX_MAP[pattern_index] = pattern
        PATTERN_GROUP_MAP[pattern_index] = group_name
        pattern_index += 1



class EnhancedCompatibilityExtractorPro:
    """Förbättrad extraktor för kompatibilitetsinformation från _pro-dokument"""
    
    def __init__(self, base_dir: Path, output_dir: Path):
        self.base_dir = base_dir
        self.output_dir = output_dir
        
        # Statistik och resultatvariabler
        self.document_count = 0
        self.compatibility_count = 0
        self.documents_with_compatibility = 0
        self.documents_without_compatibility = 0
        self.pattern_counts = {group: 0 for group in PATTERN_GROUPS}
        self.individual_pattern_counts = defaultdict(int)
        self.discovered_phrases = []
        self.relation_types = Counter()
        self.pattern_performance = {}
        
        # För automatisk upptäckt av nya mönster
        self.discovered_patterns = []
        self.common_phrases = Counter()
        
        # För mönsteranalys
        self.top_performing_patterns = {}
        self.low_performing_patterns = {}
        
        # Tilldela tidsstämpel för alla filer
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
    def find_documents(self) -> List[Path]:
        """Hitta alla markdown-filer (utom meta-filer)"""
        document_files = []
        for root, _, files in os.walk(self.base_dir):
            for file in files:
                if file.endswith(".md") and not file.endswith("_meta.md"):
                    document_files.append(Path(root) / file)
        return document_files
    
    def extract_product_id(self, filename: str) -> str:
        """Extrahera produktID från filnamnet"""
        match = re.match(r'^([\w\-]+)_pro', filename, re.IGNORECASE)
        if match:
            return match.group(1)
        return filename.split('_')[0]
    
    def preprocess_content(self, content: str) -> str:
        """
        Förbehandla innehållet för bättre matchning:
        1. Normalisera radbrytningar
        2. Ersätt flera mellanslag med ett
        3. Normalisera punktlistor
        """
        # Normalisera radbrytningar
        content = content.replace('\r\n', '\n').replace('\r', '\n')
        
        # Normalisera mellanslag
        content = re.sub(r'\s+', ' ', content)
        
        # Normalisera punktlistor (behåll radbrytningar för listmönster)
        content = re.sub(r'^\s*[•*-]\s*', '\n• ', content, flags=re.MULTILINE)
        
        return content
    
    def clean_match_text(self, text: str) -> str:
        """Rensa matchad text för bättre kvalitet"""
        # Rensa bort punkter, kommatecken etc. i slutet
        text = re.sub(r'[.,;:]+', '', text.strip())
        
        # Ta bort onödiga mellanslag
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Ta bort parenteser om de omsluter hela strängen
        if text.startswith('(') and text.endswith(')'):
            text = text[1:-1].strip()
            
        return text
    
    def extract_list_items(self, list_text: str) -> List[str]:
        """Extrahera enskilda punkter från en punktlista"""
        items = []
        
        # Normalisera listsymboler
        normalized = list_text.replace('\r\n', '\n').replace('\r', '\n')
        
        # Matcha varje listobjekt
        for line in normalized.strip().split('\n'):
            line = line.strip()
            if not line:
                continue
                
            # Ta bort listsymboler och whitespace
            cleaned_line = re.sub(r'^[-*•]?\s*', '', line).strip()
            if cleaned_line:
                items.append(cleaned_line)
        
        return items
    
    def get_context(self, content: str, match_start: int, match_end: int, window_size: int = 100) -> str:
        """Hämta kontext runt en matchning med förbättrad läsbarhet"""
        # Hämta råtext
        start_pos = max(0, match_start - window_size)
        end_pos = min(len(content), match_end + window_size)
        
        # Extrahera och rensa kontexten
        context = content[start_pos:end_pos]
        
        # Rensa för bättre läsbarhet
        context = context.replace('\n', ' ').replace('\r', '')
        context = re.sub(r'\s+', ' ', context).strip()
        
        # Markera den matchade delen med stjärnor för bättre synlighet
        relative_start = match_start - start_pos
        relative_end = match_end - start_pos
        
        if 0 <= relative_start < len(context) and 0 <= relative_end <= len(context):
            context = context[:relative_start] + "**" + context[relative_start:relative_end] + "**" + context[relative_end:]
        
        return context
    
    def identify_potential_patterns(self, content: str) -> List[str]:
        """Identifiera potentiella nya kompatibilitetsmönster med språkbaserad analys"""
        potential_patterns = []
        
        # Dela in i meningar för analys
        sentences = re.split(r'(?<=[.!?])\s+', content)
        
        # Nyckelord som kan indikera kompatibilitetsinformation
        compatibility_keywords = [
            'kompatibel', 'compatible', 'passar', 'fits', 'fungerar',
            'works', 'kan användas', 'can be used', 'designad för',
            'designed for', 'avsedd för', 'intended for', 'lämplig',
            'suitable', 'rekommenderas', 'recommended', 'tillbehör',
            'accessory', 'ersätter', 'replaces', 'kräver', 'requires'
        ]
        
        for sentence in sentences:
            # Kontrollera om någon av nyckelorden finns i meningen
            if any(keyword in sentence.lower() for keyword in compatibility_keywords):
                # Kontrollera att meningen inte redan matchar befintliga mönster
                if not any(re.search(pattern, sentence, re.IGNORECASE) for pattern in ALL_PATTERNS):
                    # Rensa meningen
                    clean_sentence = sentence.strip()
                    if clean_sentence:
                        potential_patterns.append(clean_sentence)
                        # Spara för mönsteranalys
                        self.common_phrases[clean_sentence] += 1
        
        return potential_patterns
    
    def extract_numeric_relations(self, text: str) -> List[str]:
        """Extrahera artikelnummer och andra numeriska identifierare från text"""
        # Mönster för olika typer av produktidentifierare
        id_patterns = [
            r'(?<!\d)(\d{5,8})(?!\d)',  # 5-8 siffror (vanliga artikelnummer)
            r'E-(?:nr\.?|nummer)?\s*:?\s*(\d{7})',  # E-nummer format
            r'(?<!\d)(\d{13})(?!\d)',  # 13 siffror (EAN)
            r'(?<!\d)(\d{12})(?!\d)',  # 12 siffror (UPC)
            r'(?<!\d)(\d{8})(?!\d)',   # 8 siffror (GTIN-8)
        ]
        
        found_ids = []
        
        for pattern in id_patterns:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                id_value = match.group(1).strip()
                if id_value:
                    found_ids.append(id_value)
        
        return found_ids
    
    def extract_compatibility_from_file(self, file_path: Path) -> Dict[str, Any]:
        """Extrahera kompatibilitetsrelationer från en _pro-fil med förbättrade metoder"""
        try:
            # Läs in innehållet
            with open(file_path, 'r', encoding='utf-8') as f:
                raw_content = f.read()
            
            # Förbehandla innehållet
            content = self.preprocess_content(raw_content)
            
            # Extrahera produktidentifierare från filnamnet
            product_id = self.extract_product_id(file_path.name)
            
            # Resultatstruktur
            result = {
                "product_id": product_id,
                "file_path": str(file_path),
                "filename": file_path.name,
                "has_compatibility": False,
                "compatibility": [],
                "discovered_patterns": [],
                "content_sample": content[:1000] if len(content) > 1000 else content  # Exempel på innehållet
            }
            
            # Sök efter kompatibilitetsrelationer med alla mönster
            for pattern_index, pattern in enumerate(ALL_PATTERNS):
                # Identifiera vilken grupp mönstret tillhör
                group_name = PATTERN_GROUP_MAP[pattern_index]
                
                for match in re.finditer(pattern, content, re.IGNORECASE | re.DOTALL):
                    # För listmönster behöver vi särskild hantering
                    if group_name == "list_relation":
                        list_text = match.group(1)
                        list_items = self.extract_list_items(list_text)
                        
                        for item in list_items:
                            # Skapa en matchning för varje punktlista
                            relation_data = {
                                "relation_type": group_name,
                                "related_product": self.clean_match_text(item),
                                "context": f"Från punktlista: {list_text[:100]}...",
                                "pattern_index": pattern_index,
                                "pattern": pattern,
                                "source": "list"
                            }
                            
                            # Extrahera eventuella artikelnummer från listan
                            numeric_ids = self.extract_numeric_relations(item)
                            if numeric_ids:
                                relation_data["numeric_ids"] = numeric_ids
                            
                            result["compatibility"].append(relation_data)
                            self.compatibility_count += 1
                            self.individual_pattern_counts[pattern_index] += 1
                            self.pattern_counts[group_name] += 1
                    else:
                        # Standardhantering för vanliga mönster
                        related_product = match.group(1).strip()
                        
                        # Rensa och validera matchningen
                        cleaned_product = self.clean_match_text(related_product)
                        
                        # Hoppa över tomma eller för korta matchningar
                        if not cleaned_product or len(cleaned_product) < 3:
                            continue
                        
                        # Hämta kontext
                        context = self.get_context(content, match.start(), match.end(), window_size=120)
                        
                        # Skapa matchningsdata
                        relation_data = {
                            "relation_type": group_name,
                            "related_product": cleaned_product,
                            "context": context,
                            "position": match.span(),
                            "pattern_index": pattern_index,
                            "pattern": pattern,
                            "source": "regex"
                        }
                        
                        # Extrahera eventuella artikelnummer från kompatibilitetsbeskrivningen
                        numeric_ids = self.extract_numeric_relations(cleaned_product)
                        if numeric_ids:
                            relation_data["numeric_ids"] = numeric_ids
                        
                        # Lägg till i resultatet
                        result["compatibility"].append(relation_data)
                        
                        # Uppdatera statistik
                        self.compatibility_count += 1
                        self.individual_pattern_counts[pattern_index] += 1
                        self.pattern_counts[group_name] += 1
                        self.relation_types[group_name] += 1
            
            # Identifiera potentiella nya mönster
            potential_patterns = self.identify_potential_patterns(content)
            if potential_patterns:
                result["discovered_patterns"] = potential_patterns
                for pattern in potential_patterns:
                    self.discovered_phrases.append({
                        "product_id": product_id,
                        "phrase": pattern,
                        "file": str(file_path)
                    })
            
            # Uppdatera dokument-status
            if result["compatibility"]:
                result["has_compatibility"] = True
                self.documents_with_compatibility += 1
            else:
                self.documents_without_compatibility += 1
            
            return result
            
        except Exception as e:
            logger.error(f"Fel vid bearbetning av {file_path}: {str(e)}")
            return None



    def analyze_pattern_performance(self):
        """Analysera mönstrens prestanda baserat på matchningsfrekvens"""
        if not self.individual_pattern_counts:
            return {}
        
        # Sortera mönster efter antalet träffar
        sorted_patterns = sorted(
            self.individual_pattern_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        # Skapa mönsterprestationsrapport
        performance = {}
        
        for pattern_index, count in sorted_patterns:
            pattern = PATTERN_INDEX_MAP[pattern_index]
            group = PATTERN_GROUP_MAP[pattern_index]
            
            performance[pattern_index] = {
                "pattern": pattern,
                "count": count,
                "group": group,
                "percentage": (count / self.compatibility_count * 100) if self.compatibility_count > 0 else 0
            }
        
        # Identifiera topp- och bottenprestanda
        top_count = min(10, len(sorted_patterns))
        if top_count > 0:
            self.top_performing_patterns = dict(sorted_patterns[:top_count])
            
        if len(sorted_patterns) > top_count:
            # Endast inkludera mönster med minst en matchning
            bottom_performers = [(idx, count) for idx, count in sorted_patterns if count > 0]
            bottom_count = min(10, len(bottom_performers))
            self.low_performing_patterns = dict(bottom_performers[-bottom_count:])
            
        return performance
    
    def suggest_new_patterns(self) -> List[Dict[str, Any]]:
        """Föreslå nya mönster baserat på upptäckta fraser"""
        suggestions = []
        
        # Analysera frekventa fraser
        if self.common_phrases:
            # Ta de 20 vanligaste fraserna
            common_phrases = self.common_phrases.most_common(20)
            
            for phrase, count in common_phrases:
                # Förbered förslagen
                if count >= 2:  # Minst 2 förekomster
                    # Identifiera nyckelord i frasen
                    keywords = [
                        'kompatibel', 'compatible', 'passar', 'fits', 'fungerar', 
                        'works', 'användas', 'used', 'designad', 'designed', 
                        'avsedd', 'intended', 'lämplig', 'suitable', 'rekommenderas', 
                        'recommended', 'tillbehör', 'accessory'
                    ]
                    
                    # Skapa förslag på mönster baserat på frasen
                    for keyword in keywords:
                        if keyword.lower() in phrase.lower():
                            pattern_suggestion = {}
                            
                            # Försök skapa ett regex-mönster baserat på frasen
                            # Leta efter något som ser ut som en relation
                            if " med " in phrase.lower():
                                parts = phrase.lower().split(" med ", 1)
                                if len(parts) == 2 and keyword in parts[0]:
                                    pattern = f"(?i){parts[0]} med ([^\.;]+)(?:\.|\;|$)"
                                    pattern_suggestion = {
                                        "phrase": phrase,
                                        "keyword": keyword,
                                        "suggested_pattern": pattern,
                                        "occurrences": count,
                                        "relation_type": "direct"
                                    }
                            elif " för " in phrase.lower():
                                parts = phrase.lower().split(" för ", 1)
                                if len(parts) == 2 and keyword in parts[0]:
                                    pattern = f"(?i){parts[0]} för ([^\.;]+)(?:\.|\;|$)"
                                    pattern_suggestion = {
                                        "phrase": phrase,
                                        "keyword": keyword,
                                        "suggested_pattern": pattern,
                                        "occurrences": count,
                                        "relation_type": "designed_for"
                                    }
                            elif " till " in phrase.lower():
                                parts = phrase.lower().split(" till ", 1)
                                if len(parts) == 2 and keyword in parts[0]:
                                    pattern = f"(?i){parts[0]} till ([^\.;]+)(?:\.|\;|$)"
                                    pattern_suggestion = {
                                        "phrase": phrase,
                                        "keyword": keyword,
                                        "suggested_pattern": pattern,
                                        "occurrences": count,
                                        "relation_type": "accessory"
                                    }
                            
                            if pattern_suggestion:
                                suggestions.append(pattern_suggestion)
                                break
        
        # Spara förslagen
        if suggestions:
            suggestions_file = RESULTS_STRUCTURE["discovered"] / f"suggested_patterns_{self.timestamp}.json"
            with open(suggestions_file, 'w', encoding='utf-8') as f:
                json.dump(suggestions, f, ensure_ascii=False, indent=2)
            
            logger.info(f"Sparade {len(suggestions)} förslag på nya mönster till {suggestions_file}")
                
        return suggestions
    
    def cluster_relation_types(self, relations: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        """Gruppera relationer efter typ för bättre organisering"""
        clusters = defaultdict(list)
        
        for relation in relations:
            relation_type = relation.get("relation_type", "unknown")
            clusters[relation_type].append(relation)
            
        return dict(clusters)
    
    def process_documents(self) -> None:
        """Bearbeta alla _pro-dokument och extrahera kompatibilitetsinformation"""
        # Hitta alla _pro-filer
        document_files = self.find_documents()
        total_files = len(document_files)
        logger.info(f"Hittade {total_files} _pro-filer att analysera")
        
        # Skapa utdatakatalog
        self.output_dir.mkdir(exist_ok=True, parents=True)
        
        # Skapa utdatafiler
        compat_file = RESULTS_STRUCTURE["matched"] / f"compatibility_pro_{self.timestamp}.jsonl"
        no_compat_file = RESULTS_STRUCTURE["unmatched"] / f"no_compatibility_pro_{self.timestamp}.jsonl"
        samples_file = RESULTS_STRUCTURE["samples"] / f"samples_without_compatibility_{self.timestamp}.jsonl"
        discovered_file = RESULTS_STRUCTURE["discovered"] / f"discovered_phrases_{self.timestamp}.jsonl"
        
        # Bearbeta varje fil
        with open(compat_file, 'w', encoding='utf-8') as compat_f, \
             open(no_compat_file, 'w', encoding='utf-8') as no_compat_f:
             
            for i, file_path in enumerate(document_files):
                # Extrahera kompatibilitetsrelationer
                result = self.extract_compatibility_from_file(file_path)
                
                if result:
                    # Organisera relationer efter typ
                    if result["has_compatibility"]:
                        # Gruppera relationerna efter typ
                        result["grouped_compatibility"] = self.cluster_relation_types(result["compatibility"])
                        
                        # Skriv till matchningsfil
                        json_line = json.dumps(result, ensure_ascii=False)
                        compat_f.write(json_line + '\n')
                        
                        # Spara också i relationsspecifika filer
                        for relation_type, relations in result["grouped_compatibility"].items():
                            if relations:
                                relation_dir = RESULTS_STRUCTURE["relations"] / relation_type
                                relation_dir.mkdir(exist_ok=True, parents=True)
                                
                                relation_file = relation_dir / f"{relation_type}_{self.timestamp}.jsonl"
                                relation_data = {
                                    "product_id": result["product_id"],
                                    "file_path": result["file_path"],
                                    "filename": result["filename"],
                                    "relations": relations
                                }
                                
                                # Append-mode för att samla alla relationer av samma typ
                                with open(relation_file, 'a', encoding='utf-8') as rel_f:
                                    rel_f.write(json.dumps(relation_data, ensure_ascii=False) + '\n')
                    else:
                        # För filer utan kompatibilitetsinfo, behåll bara grundläggande info
                        no_compat_record = {
                            "product_id": result["product_id"],
                            "file_path": result["file_path"],
                            "filename": result["filename"],
                            "content_sample": result["content_sample"]
                        }
                        json_line = json.dumps(no_compat_record, ensure_ascii=False)
                        no_compat_f.write(json_line + '\n')
                    
                    # Spara potentiellt upptäckta mönster
                    if result.get("discovered_patterns"):
                        with open(discovered_file, 'a', encoding='utf-8') as disc_f:
                            for pattern in result["discovered_patterns"]:
                                discovered_data = {
                                    "product_id": result["product_id"],
                                    "file_path": result["file_path"],
                                    "filename": result["filename"],
                                    "discovered_pattern": pattern
                                }
                                disc_f.write(json.dumps(discovered_data, ensure_ascii=False) + '\n')
                
                self.document_count += 1
                
                # Logga framsteg
                if (i+1) % 100 == 0 or i+1 == total_files:
                    logger.info(f"Bearbetade {i+1}/{total_files} filer ({(i+1)/total_files*100:.1f}%)")
        
        # Exportera slumpmässiga exempel från dokument utan kompatibilitet för analys
        if self.documents_without_compatibility > 0:
            no_compat_records = []
            with open(no_compat_file, 'r', encoding='utf-8') as f:
                for line in f:
                    no_compat_records.append(json.loads(line))
            
            sample_size = min(50, len(no_compat_records))
            samples = random.sample(no_compat_records, sample_size)
            
            with open(samples_file, 'w', encoding='utf-8') as f:
                for sample in samples:
                    f.write(json.dumps(sample, ensure_ascii=False) + '\n')
            
            logger.info(f"Exporterade {sample_size} slumpmässiga exempel utan kompatibilitet till {samples_file}")
        
        # Analysera mönsterprestanda
        pattern_performance = self.analyze_pattern_performance()
        
        # Föreslå nya mönster baserat på upptäckta fraser
        suggested_patterns = self.suggest_new_patterns()
        
        # Generera detaljerade rapporter
        self.generate_reports(
            total_files=total_files,
            compat_file=compat_file,
            no_compat_file=no_compat_file,
            samples_file=samples_file,
            discovered_file=discovered_file,
            pattern_performance=pattern_performance,
            suggested_patterns=suggested_patterns
        )

    def generate_reports(self, total_files: int, compat_file: Path, no_compat_file: Path, 
                        samples_file: Path, discovered_file: Path, pattern_performance: Dict,
                        suggested_patterns: List) -> None:
        """Generera detaljerade rapporter och sammanfattningar"""
        
        # 1. Skapa en detaljerad sammanfattningsfil (JSON)
        summary = {
            "timestamp": self.timestamp,
            "total_pro_files": total_files,
            "total_files_processed": self.document_count,
            "documents_with_compatibility": self.documents_with_compatibility,
            "documents_without_compatibility": self.documents_without_compatibility,
            "compatibility_coverage_percentage": (self.documents_with_compatibility / total_files * 100) if total_files > 0 else 0,
            "total_compatibility_relations_found": self.compatibility_count,
            "average_relations_per_document": (self.compatibility_count / self.documents_with_compatibility) if self.documents_with_compatibility > 0 else 0,
            "pattern_group_counts": self.pattern_counts,
            "relation_type_distribution": dict(self.relation_types),
            "pattern_performance_summary": {
                "top_patterns": [
                    {
                        "pattern_index": idx,
                        "pattern": PATTERN_INDEX_MAP[idx],
                        "group": PATTERN_GROUP_MAP[idx],
                        "matches": count
                    }
                    for idx, count in sorted(self.top_performing_patterns.items(), key=lambda x: x[1], reverse=True)
                ],
                "low_performing_patterns": [
                    {
                        "pattern_index": idx,
                        "pattern": PATTERN_INDEX_MAP[idx],
                        "group": PATTERN_GROUP_MAP[idx],
                        "matches": count
                    }
                    for idx, count in sorted(self.low_performing_patterns.items(), key=lambda x: x[1])
                ]
            },
            "suggested_patterns_count": len(suggested_patterns),
            "discovered_phrases_count": len(self.discovered_phrases)
        }
        
        summary_file = RESULTS_STRUCTURE["reports"] / f"compatibility_pro_summary_{self.timestamp}.json"
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)
        
        # 2. Skapa en detaljerad mönsterprestationsrapport (JSON)
        pattern_report = {
            "timestamp": self.timestamp,
            "total_patterns": len(ALL_PATTERNS),
            "patterns_with_matches": len(self.individual_pattern_counts),
            "individual_pattern_performance": pattern_performance,
            "pattern_group_performance": {
                group: {
                    "total_matches": count,
                    "percentage_of_all_matches": (count / self.compatibility_count * 100) if self.compatibility_count > 0 else 0
                }
                for group, count in self.pattern_counts.items() if count > 0
            }
        }
        
        pattern_report_file = RESULTS_STRUCTURE["patterns"] / f"pattern_performance_{self.timestamp}.json"
        with open(pattern_report_file, 'w', encoding='utf-8') as f:
            json.dump(pattern_report, f, ensure_ascii=False, indent=2)
        
        # 3. Skapa en omfattande markdown-rapport
        self.generate_markdown_report(
            total_files=total_files,
            summary=summary,
            pattern_report=pattern_report,
            compat_file=compat_file,
            no_compat_file=no_compat_file,
            samples_file=samples_file,
            discovered_file=discovered_file,
            suggested_patterns=suggested_patterns
        )
    
    def generate_reports(self, total_files: int, compat_file: Path, no_compat_file: Path, 
                        samples_file: Path, discovered_file: Path, pattern_performance: Dict,
                        suggested_patterns: List) -> None:
        """Generera detaljerade rapporter och sammanfattningar"""
        
        # 1. Skapa en detaljerad sammanfattningsfil (JSON)
        summary = {
            "timestamp": self.timestamp,
            "total_pro_files": total_files,
            "total_files_processed": self.document_count,
            "documents_with_compatibility": self.documents_with_compatibility,
            "documents_without_compatibility": self.documents_without_compatibility,
            "compatibility_coverage_percentage": (self.documents_with_compatibility / total_files * 100) if total_files > 0 else 0,
            "total_compatibility_relations_found": self.compatibility_count,
            "average_relations_per_document": (self.compatibility_count / self.documents_with_compatibility) if self.documents_with_compatibility > 0 else 0,
            "pattern_group_counts": self.pattern_counts,
            "relation_type_distribution": dict(self.relation_types),
            "pattern_performance_summary": {
                "top_patterns": [
                    {
                        "pattern_index": idx,
                        "pattern": PATTERN_INDEX_MAP[idx],
                        "group": PATTERN_GROUP_MAP[idx],
                        "matches": count
                    }
                    for idx, count in sorted(self.top_performing_patterns.items(), key=lambda x: x[1], reverse=True)
                ],
                "low_performing_patterns": [
                    {
                        "pattern_index": idx,
                        "pattern": PATTERN_INDEX_MAP[idx],
                        "group": PATTERN_GROUP_MAP[idx],
                        "matches": count
                    }
                    for idx, count in sorted(self.low_performing_patterns.items(), key=lambda x: x[1])
                ]
            },
            "suggested_patterns_count": len(suggested_patterns),
            "discovered_patterns_count": len(self.discovered_patterns)
        }
        
        summary_file = RESULTS_STRUCTURE["reports"] / f"compatibility_pro_summary_{self.timestamp}.json"
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)
        
        # 2. Skapa en detaljerad mönsterprestationsrapport (JSON)
        pattern_report = {
            "timestamp": self.timestamp,
            "total_patterns": len(ALL_PATTERNS),
            "patterns_with_matches": len(self.individual_pattern_counts),
            "individual_pattern_performance": pattern_performance,
            "pattern_group_performance": {
                group: {
                    "total_matches": count,
                    "percentage_of_all_matches": (count / self.compatibility_count * 100) if self.compatibility_count > 0 else 0
                }
                for group, count in self.pattern_counts.items() if count > 0
            }
        }
        
        pattern_report_file = RESULTS_STRUCTURE["patterns"] / f"pattern_performance_{self.timestamp}.json"
        with open(pattern_report_file, 'w', encoding='utf-8') as f:
            json.dump(pattern_report, f, ensure_ascii=False, indent=2)
        
        # 3. Skapa validerings- och verifikationsrapport
        validation_report = {
            "timestamp": self.timestamp,
            "validation_summary": {
                "total_relations": self.compatibility_count,
                "potential_issues": 0  # Lägger till detta för framtida användning
            },
            "relation_type_summary": dict(self.relation_types)
        }
        
        validation_report_file = RESULTS_STRUCTURE["validation"] / f"validation_report_{self.timestamp}.json"
        with open(validation_report_file, 'w', encoding='utf-8') as f:
            json.dump(validation_report, f, ensure_ascii=False, indent=2)
        
        # 4. Skapa en omfattande markdown-rapport
        self.generate_markdown_report(
            total_files=total_files,
            summary=summary,
            pattern_report=pattern_report,
            validation_report=validation_report,
            compat_file=compat_file,
            no_compat_file=no_compat_file,
            samples_file=samples_file,
            discovered_file=discovered_file,
            suggested_patterns=suggested_patterns,
            summary_file=summary_file,
            pattern_report_file=pattern_report_file,
            validation_report_file=validation_report_file
        )

    def generate_markdown_report(self, total_files: int, summary: Dict, pattern_report: Dict,
                            validation_report: Dict, compat_file: Path, no_compat_file: Path, 
                            samples_file: Path, discovered_file: Path, suggested_patterns: List,
                            summary_file: Path, pattern_report_file: Path, validation_report_file: Path) -> None:
        """Generera en detaljerad markdown-rapport med alla resultat och analyser"""
        
        report_file = RESULTS_STRUCTURE["reports"] / f"compatibility_pro_report_{self.timestamp}.md"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            # Huvudrubrik och inledning
            f.write(f"# Detaljerad Kompatibilitetsextraktionsrapport\n\n")
            f.write(f"**Datum och tid:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"Denna rapport innehåller en detaljerad analys av kompatibilitetsinformation extraherad från _pro-dokument.\n\n")
            
            # Innehållsförteckning
            f.write("## Innehåll\n\n")
            f.write("1. [Sammanfattning](#sammanfattning)\n")
            f.write("2. [Relationstyper](#relationstyper)\n")
            f.write("3. [Mönsterprestanda](#mönsterprestanda)\n")
            f.write("   - [Toppresterande mönster](#toppresterande-mönster)\n")
            f.write("   - [Bottenprestanda mönster](#bottenprestanda-mönster)\n")
            f.write("   - [Mönstergruppernas prestanda](#mönstergruppernas-prestanda)\n")
            f.write("4. [Upptäckta fraser och mönsterförslag](#upptäckta-fraser-och-mönsterförslag)\n")
            f.write("5. [Dokument och filer](#dokument-och-filer)\n")
            f.write("6. [Nästa steg](#nästa-steg)\n\n")
            
            # Övergripande sammanfattning
            f.write("## Sammanfattning\n\n")
            f.write(f"- **Totalt antal _pro-filer:** {total_files}\n")
            f.write(f"- **Filer med kompatibilitetsinformation:** {self.documents_with_compatibility} ({summary['compatibility_coverage_percentage']:.1f}%)\n")
            f.write(f"- **Filer utan kompatibilitetsinformation:** {self.documents_without_compatibility}\n")
            f.write(f"- **Totalt antal kompatibilitetsrelationer:** {self.compatibility_count}\n")
            f.write(f"- **Genomsnittligt antal relationer per dokument:** {summary['average_relations_per_document']:.1f}\n")
            f.write(f"- **Antal upptäckta potentiella nya fraser:** {summary['discovered_patterns_count']}\n")
            f.write(f"- **Antal föreslagna nya mönster:** {summary['suggested_patterns_count']}\n\n")
            
            # Relationstyper
            f.write("## Relationstyper\n\n")
            f.write("Nedan visas fördelningen av olika typer av kompatibilitetsrelationer som hittades:\n\n")
            f.write("| Relationstyp | Antal träffar | Procentandel |\n")
            f.write("|--------------|--------------|---------------|\n")
            
            # Sortera efter antal träffar
            for relation_type, count in sorted(self.relation_types.items(), key=lambda x: x[1], reverse=True):
                percentage = (count / self.compatibility_count * 100) if self.compatibility_count > 0 else 0
                f.write(f"| {relation_type} | {count} | {percentage:.1f}% |\n")
            
            # Mönsterprestanda
            f.write("\n## Mönsterprestanda\n\n")
            f.write(f"Totalt används {len(ALL_PATTERNS)} mönster för extraktion, varav {len(self.individual_pattern_counts)} gav träffar.\n\n")
            
            # Toppresterande mönster
            f.write("### Toppresterande mönster\n\n")
            f.write("De mönster som gav flest träffar:\n\n")
            f.write("| Mönsterindex | Grupp | Antal träffar | Procentandel | Mönster |\n")
            f.write("|--------------|-------|--------------|--------------|--------|\n")
            
            for idx, count in sorted(self.top_performing_patterns.items(), key=lambda x: x[1], reverse=True):
                percentage = (count / self.compatibility_count * 100) if self.compatibility_count > 0 else 0
                pattern = PATTERN_INDEX_MAP[idx]
                group = PATTERN_GROUP_MAP[idx]
                # Begränsa längden på mönstret i tabellen
                short_pattern = pattern[:70] + "..." if len(pattern) > 70 else pattern
                f.write(f"| {idx} | {group} | {count} | {percentage:.1f}% | `{short_pattern}` |\n")
            
            # Bottenprestanda mönster
            f.write("\n### Bottenprestanda mönster\n\n")
            f.write("De mönster som gav minst antal träffar (men fortfarande gav några träffar):\n\n")
            f.write("| Mönsterindex | Grupp | Antal träffar | Procentandel | Mönster |\n")
            f.write("|--------------|-------|--------------|--------------|--------|\n")
            
            for idx, count in sorted(self.low_performing_patterns.items(), key=lambda x: x[1]):
                percentage = (count / self.compatibility_count * 100) if self.compatibility_count > 0 else 0
                pattern = PATTERN_INDEX_MAP[idx]
                group = PATTERN_GROUP_MAP[idx]
                # Begränsa längden på mönstret i tabellen
                short_pattern = pattern[:70] + "..." if len(pattern) > 70 else pattern
                f.write(f"| {idx} | {group} | {count} | {percentage:.1f}% | `{short_pattern}` |\n")
            
            # Mönstergruppernas prestanda
            f.write("\n### Mönstergruppernas prestanda\n\n")
            f.write("Prestanda per mönstergrupp:\n\n")
            f.write("| Mönstergrupp | Antal träffar | Procentandel |\n")
            f.write("|--------------|--------------|---------------|\n")
            
            for group, count in sorted(self.pattern_counts.items(), key=lambda x: x[1], reverse=True):
                if count > 0:
                    percentage = (count / self.compatibility_count * 100) if self.compatibility_count > 0 else 0
                    f.write(f"| {group} | {count} | {percentage:.1f}% |\n")
            
            # Upptäckta fraser och mönsterförslag
            f.write("\n## Upptäckta fraser och mönsterförslag\n\n")
            
            if suggested_patterns:
                f.write(f"Baserat på analys av dokument och frekventa fraser, föreslås följande {len(suggested_patterns)} nya mönster:\n\n")
                f.write("| Originalfras | Föreslagen relationstyp | Föreslagen regex | Förekomster |\n")
                f.write("|--------------|-------------------------|-----------------|-------------|\n")
                
                for suggestion in suggested_patterns[:20]:  # Visa bara de 20 första förslagen
                    f.write(f"| {suggestion['phrase'][:50]}... | {suggestion['relation_type']} | `{suggestion['suggested_pattern']}` | {suggestion['occurrences']} |\n")
                
                if len(suggested_patterns) > 20:
                    f.write(f"\n*...och {len(suggested_patterns) - 20} ytterligare förslag. Se JSON-filen för fullständig lista.*\n")
                    
                f.write("\nSe den fullständiga listan i JSON-filen för föreslagna mönster.\n\n")
            else:
                f.write("Inga nya mönsterförslag genererades i denna körning.\n\n")
            
            # Dokument och filer
            f.write("## Dokument och filer\n\n")
            f.write("### Resultatfiler\n\n")
            f.write(f"- **Extraherade kompatibilitetsrelationer:** [{compat_file.name}]({compat_file})\n")
            f.write(f"- **Dokument utan kompatibilitetsinformation:** [{no_compat_file.name}]({no_compat_file})\n")
            f.write(f"- **Exempel på dokument utan kompatibilitet:** [{samples_file.name}]({samples_file})\n")
            f.write(f"- **Upptäckta potentiella fraser:** [{discovered_file.name}]({discovered_file})\n")
            f.write(f"- **Mönsterprestanda (JSON):** [{pattern_report_file.name}]({pattern_report_file})\n")
            f.write(f"- **Valideringsrapport (JSON):** [{validation_report_file.name}]({validation_report_file})\n")
            f.write(f"- **Sammanfattning (JSON):** [{summary_file.name}]({summary_file})\n\n")
            
            # Relationsspecifika filer
            relation_files = []
            for relation_dir in (RESULTS_STRUCTURE["relations"]).glob("*"):
                if relation_dir.is_dir():
                    for rel_file in relation_dir.glob(f"*_{self.timestamp}.jsonl"):
                        relation_files.append((relation_dir.name, rel_file))
            
            if relation_files:
                f.write("### Relationsspecifika filer\n\n")
                for rel_type, rel_file in sorted(relation_files):
                    f.write(f"- **{rel_type}:** [{rel_file.name}]({rel_file})\n")
            
            # Nästa steg
            f.write("\n## Nästa steg\n\n")
            f.write("Baserat på denna analys rekommenderas följande åtgärder:\n\n")
            f.write("1. **Granska upptäckta fraser** för att identifiera nya mönster och förbättra befintliga\n")
            f.write("2. **Implementera föreslagna mönster** och jämför resultaten i nästa körning\n")
            f.write("3. **Förfina lågpresterande mönster** eller överväg att ta bort dem om de är redundanta\n")
            f.write("4. **Utveckla specifika extraktorer för andra dokumenttyper** (_TEK, _produktblad, etc.)\n")
            f.write("5. **Expandera NLP-metoder** för att upptäcka mer sofistikerade relationer\n")
            f.write("6. **Validera extraherade relationer** med produkt-till-produktkontroller\n\n")
            
            f.write("---\n\n")
            f.write(f"Rapport genererad: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        logger.info(f"Genererade detaljerad kompatibilitetsrapport: {report_file}")

def main():
    """Huvudfunktion för kompatibilitetsextraktorn"""
    start_time = datetime.now()
    logger.info(f"Startar förbättrad kompatibilitetsextraktion från _pro-dokument: {start_time}")
    
    # Skapa och kör extraktorn
    extractor = EnhancedCompatibilityExtractorPro(BASE_DIR, OUTPUT_DIR)
    extractor.process_documents()
    
    end_time = datetime.now()
    duration = end_time - start_time
    logger.info(f"Extraktion slutförd på {duration.total_seconds():.1f} sekunder")

if __name__ == "__main__":
    main()


