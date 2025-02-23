#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Förbättrad EAN-Extraktor för _pro-dokument

Denna avancerade mikroservice:
1. Letar efter _pro-dokument i den angivna katalogstrukturen
2. Extraherar EAN-koder och andra produktidentifierare med omfattande regex-mönster
3. Validerar extraherade koder med avancerade algoritmer
4. Klassificerar identifierare i tydliga kategorier (EAN-13, EAN-8, E-nummer, artikelnummer)
5. Identifierar potentiella nya identifieringsformer med NLP-metoder
6. Skapar utförliga visualiseringar och analyser av resultaten
7. Sparar allt i en organiserad katalogstruktur med JSONL-filer
"""

import os
import re
import json
import logging
import random
import shutil
import math
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple, Set, Counter
from collections import defaultdict, Counter

# Konfigurera loggning
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("enhanced_ean_extractor.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Definiera katalogstrukturer
BASE_DIR = Path("./converted_docs")
OUTPUT_DIR = Path("./extracted_data/artikel")
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

# Skapa struktur för resultatkategorier
RESULTS_STRUCTURE = {
    "matched": OUTPUT_DIR / "matched",
    "unmatched": OUTPUT_DIR / "unmatched",
    "samples": OUTPUT_DIR / "samples",
    "patterns": OUTPUT_DIR / "patterns",
    "reports": OUTPUT_DIR / "reports",
    "discovered": OUTPUT_DIR / "discovered",
    "types": OUTPUT_DIR / "types",
    "validation": OUTPUT_DIR / "validation"
}

# Skapa kataloger
for dir_path in RESULTS_STRUCTURE.values():
    dir_path.mkdir(exist_ok=True, parents=True)

# -----------------------------------------------------------
# UTÖKADE EAN/PRODUKTIDENTIFIERING-MÖNSTER
# -----------------------------------------------------------

# EAN-13 och GTIN-13
EAN13_PATTERNS = [
    r'(?i)EAN(?:-13)?[:.\-]?\s*(\d{13})(?!\d)',
    r'(?i)GTIN(?:-13)?[:.\-]?\s*(\d{13})(?!\d)',
    r'(?i)(?:Global Trade Item Number|EAN-kod)[:.\-]?\s*(\d{13})(?!\d)',
    r'(?i)streckkod[:.\-]?\s*(\d{13})(?!\d)',
    r'(?i)bar ?code[:.\-]?\s*(\d{13})(?!\d)',
    r'(?<!\d)(\d{13})(?!\d)',  # Ensam 13-siffrig kod
]

# EAN-8 och GTIN-8
EAN8_PATTERNS = [
    r'(?i)EAN(?:-8)?[:.\-]?\s*(\d{8})(?!\d)',
    r'(?i)GTIN(?:-8)?[:.\-]?\s*(\d{8})(?!\d)',
    r'(?i)streckkod \(kort\)[:.\-]?\s*(\d{8})(?!\d)',
]

# E-nummer (svensk standard)
ENUMMER_PATTERNS = [
    r'(?i)E-n[ru](?:mmer)?[:.\-]?\s*(\d{7})(?!\d)',
    r'(?i)E-n[ru][:\.]?\s*(\d{7})(?!\d)',
    r'(?i)E-nr\.?\s*(\d{7})(?!\d)',
    r'(?i)Enr\.?\s*(\d{7})(?!\d)',
    r'(?<![a-zA-Z0-9])E(\d{7})(?!\d)',  # E följt av 7 siffror
]

# Artikelnummer
ARTICLE_PATTERNS = [
    r'(?i)Art(?:ikel)?\.?n[ro]\.?[:.\-]?\s*([A-Z0-9]{5,10})(?![A-Z0-9])',
    r'(?i)Art(?:ikel)?\.?n[ro][:.\-]?\s*([A-Z0-9]{5,10})(?![A-Z0-9])',
    r'(?i)Art(?:ikel)?\.?(?:nummer|nr)[:.\-]?\s*([A-Z0-9]{5,10})(?![A-Z0-9])',
    r'(?i)Prod(?:ukt)?\.?n[ro]\.?[:.\-]?\s*([A-Z0-9]{5,10})(?![A-Z0-9])',
    r'(?i)Prod(?:ukt)?\.?n[ro][:.\-]?\s*([A-Z0-9]{5,10})(?![A-Z0-9])',
    r'(?i)Prod(?:ukt)?\.?(?:nummer|nr)[:.\-]?\s*([A-Z0-9]{5,10})(?![A-Z0-9])',
    r'(?i)Product n[ro][:.\-]?\s*([A-Z0-9]{5,10})(?![A-Z0-9])',
    r'(?i)Item n[ro][:.\-]?\s*([A-Z0-9]{5,10})(?![A-Z0-9])',
    r'(?i)Model(l)?\.?\s*n[ro]\.?[:.\-]?\s*([A-Z0-9]{5,10})(?![A-Z0-9])',
    r'(?i)REF\.?\s*[:.\-]?\s*([A-Z0-9]{5,10})(?![A-Z0-9])',
    r'(?i)Artikel:?\s*([A-Z0-9]{5,10})(?![A-Z0-9])',
    r'(?i)Art\.?:?\s*([A-Z0-9]{5,10})(?![A-Z0-9])',
    r'(?i)Ref(?:erence)?\.?:?\s*([A-Z0-9]{5,10})(?![A-Z0-9])',
]

# RSK-nummer (VVS-branschens artikelnummer, 7 siffror med bindestreck)
RSK_PATTERNS = [
    r'(?i)RSK(?:-| )?nummer:?\s*(\d{3}[ -]?\d{4})(?!\d)',
    r'(?i)RSK:?\s*(\d{3}[ -]?\d{4})(?!\d)',
    r'(?i)RSK\.?:?\s*(\d{3}[ -]?\d{4})(?!\d)',
]

# Artikelnummer med Copiax-format: 50XXXXXX
COPIAX_PATTERNS = [
    r'(?i)(?<!\d)(50\d{6})(?!\d)',
]

# Leverantörens artikelnummer (LVI-nummer etc.)
SUPPLIER_ARTICLE_PATTERNS = [
    r'(?i)Leverantörens? art(?:ikel)?\.?n[ro]\.?:?\s*([A-Z0-9\-]{5,15})(?![A-Z0-9])',
    r'(?i)Leverantör(?:ens)? n[ro]\.?:?\s*([A-Z0-9\-]{5,15})(?![A-Z0-9])',
    r'(?i)LVI[-:]n[ro]\.?:?\s*([A-Z0-9\-]{5,15})(?![A-Z0-9])',
    r'(?i)VVS[-:]n[ro]\.?:?\s*([A-Z0-9\-]{5,15})(?![A-Z0-9])',
    r'(?i)EL[-:]n[ro]\.?:?\s*([A-Z0-9\-]{5,15})(?![A-Z0-9])',
    r'(?i)Suppl(?:ier)? art(?:icle)? n[ro]\.?:?\s*([A-Z0-9\-]{5,15})(?![A-Z0-9])',
    r'(?i)Suppliera(?:rtikel)?n[ro]:?\s*([A-Z0-9\-]{5,15})(?![A-Z0-9])',
]

# UPC-A (12 siffror, används i USA)
UPC_PATTERNS = [
    r'(?i)UPC(?:-A)?[:.\-]?\s*(\d{12})(?!\d)',
    r'(?i)UPC[:.\-]?\s*(\d{12})(?!\d)',
    r'(?<!\d)(\d{12})(?!\d)',  # Ensam 12-siffrig kod
]

# ISBN (10 eller 13 siffror, kan innehålla bindestreck)
ISBN_PATTERNS = [
    r'(?i)ISBN(?:-13)?[:.\-]?\s*((?:\d[\d -]*){13})(?!\d)',
    r'(?i)ISBN(?:-10)?[:.\-]?\s*((?:\d[\d -]*){10})(?!\d)',
]

# Mönster för tabeller med EAN/artikelnummer
TABLE_PATTERNS = [
    # Rad med märkning som kan innehålla EAN/artikelnummer
    r'(?i)(?:<tr>.*?)?(?:<td>.*?)?(?:EAN|E-n[ro]|Art\.n[ro]|Artikelnummer)(?:.*?</td>)?(?:.*?<td>.*?)(\d{5,13})(?:.*?</td>(?:.*?</tr>)?)?',
    # Tabellrad med EAN-kod
    r'(?i)<tr>.*?<td[^>]*>.*?EAN.*?</td>.*?<td[^>]*>(.*?)(?:</td>|</tr>)',
    # Generell tabell med formaterade siffror (potentiella EAN)
    r'(?i)<table>.*?<tr>.*?<td[^>]*>(\d{7,14})</td>.*?</tr>.*?</table>',
]

# Speciella mönster för att upptäcka flera koder
MULTI_CODE_PATTERNS = [
    # Kommaseparerade koder
    r'(?i)EAN:?\s*((?:\d{13}(?:\s*,\s*\d{13})+))',
    # Identifierare i lista
    r'(?i)(?:EAN|Art\.nr|E-nr):?\s*\n(?:\s*[•\-*]\s*(\d{7,13}))+',
]

# Tabulärformat (flera kolumner)
TABULAR_PATTERNS = [
    r'(?i)^\s*(\d{5,8}|\d{13})\s+[^\n]{5,40}\s+(\d{5,8}|\d{13})\s*$',
]

# Sammanställ alla mönster i en struktur
PATTERN_GROUPS = {
    "ean13": EAN13_PATTERNS,
    "ean8": EAN8_PATTERNS,
    "enummer": ENUMMER_PATTERNS,
    "article": ARTICLE_PATTERNS,
    "rsk": RSK_PATTERNS,
    "copiax": COPIAX_PATTERNS,
    "supplier": SUPPLIER_ARTICLE_PATTERNS,
    "upc": UPC_PATTERNS,
    "isbn": ISBN_PATTERNS,
    "table": TABLE_PATTERNS,
    "multi_code": MULTI_CODE_PATTERNS,
    "tabular": TABULAR_PATTERNS
}

# Utökad datastruktur för att hålla reda på mönster och resultat
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

# -----------------------------------------------------------
# VALIDERING OCH VERIFIKATION
# -----------------------------------------------------------

def validate_ean13(ean: str) -> Tuple[bool, str]:
    """Validera en EAN-13 kod med kontrollsiffra"""
    if not ean or not ean.isdigit() or len(ean) != 13:
        return False, "Inte en giltig EAN-13 (måste vara 13 siffror)"
    
    # Kontrollera checksum
    sum_odd = sum(int(ean[i]) for i in range(0, 12, 2))
    sum_even = sum(int(ean[i]) * 3 for i in range(1, 12, 2))
    total = sum_odd + sum_even
    check_digit = (10 - (total % 10)) % 10
    
    if check_digit == int(ean[12]):
        return True, "Giltig EAN-13"
    else:
        return False, f"Felaktig kontrollsiffra (förväntad: {check_digit}, faktisk: {ean[12]})"

def validate_ean8(ean: str) -> Tuple[bool, str]:
    """Validera en EAN-8 kod med kontrollsiffra"""
    if not ean or not ean.isdigit() or len(ean) != 8:
        return False, "Inte en giltig EAN-8 (måste vara 8 siffror)"
    
    # Kontrollera checksum
    sum_odd = sum(int(ean[i]) for i in range(0, 7, 2))
    sum_even = sum(int(ean[i]) * 3 for i in range(1, 7, 2))
    total = sum_odd + sum_even
    check_digit = (10 - (total % 10)) % 10
    
    if check_digit == int(ean[7]):
        return True, "Giltig EAN-8"
    else:
        return False, f"Felaktig kontrollsiffra (förväntad: {check_digit}, faktisk: {ean[7]})"

def validate_upc(upc: str) -> Tuple[bool, str]:
    """Validera en UPC-A kod med kontrollsiffra"""
    if not upc or not upc.isdigit() or len(upc) != 12:
        return False, "Inte en giltig UPC-A (måste vara 12 siffror)"
    
    # Kontrollera checksum
    sum_odd = sum(int(upc[i]) * 3 for i in range(0, 11, 2))
    sum_even = sum(int(upc[i]) for i in range(1, 11, 2))
    total = sum_odd + sum_even
    check_digit = (10 - (total % 10)) % 10
    
    if check_digit == int(upc[11]):
        return True, "Giltig UPC-A"
    else:
        return False, f"Felaktig kontrollsiffra (förväntad: {check_digit}, faktisk: {upc[11]})"

def validate_enr(enr: str) -> Tuple[bool, str]:
    """Validera ett E-nummer (svensk standard)"""
    if not enr or not enr.isdigit() or len(enr) != 7:
        return False, "Inte ett giltigt E-nummer (måste vara 7 siffror)"
    
    # Specifika kontroller för E-nummer (förenklade)
    if enr.startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9')):
        return True, "Giltigt E-nummer format"
    else:
        return False, "E-nummer måste börja med 1-9"

def validate_article_number(art_nr: str) -> Tuple[bool, str]:
    """Validera artikelnummer (enkel validering)"""
    # Ta bort icke-alfanumeriska tecken
    cleaned = re.sub(r'[^A-Za-z0-9]', '', art_nr)
    
    if not cleaned or len(cleaned) < 4:
        return False, "För kort artikelnummer"
    
    # Kontrollera om det är ett Copiax-format
    if re.match(r'50\d{6}$', cleaned):
        return True, "Giltigt Copiax-format (50xxxxxx)"
    
    # Grundläggande formatkontroll
    if re.match(r'^[A-Za-z0-9\-]{4,15}$', art_nr):
        return True, "Giltigt artikelnummerformat"
    
    return False, "Ogiltigt artikelnummerformat"

def normalize_ean(ean: str) -> str:
    """Normalisera en EAN-kod genom att ta bort mellanslag, bindestreck, etc."""
    return re.sub(r'[^0-9]', '', ean)

def classify_product_identifier(identifier: str) -> Dict[str, Any]:
    """Klassificera en produktidentifierare baserat på format och validitet"""
    # Normalisera först
    normalized = normalize_ean(identifier)
    
    # Kontrollera olika möjliga typer
    if len(normalized) == 13:
        is_valid, message = validate_ean13(normalized)
        return {
            "original": identifier,
            "normalized": normalized,
            "type": "EAN-13",
            "is_valid": is_valid,
            "validation_message": message
        }
    elif len(normalized) == 8:
        is_valid, message = validate_ean8(normalized)
        return {
            "original": identifier,
            "normalized": normalized,
            "type": "EAN-8",
            "is_valid": is_valid,
            "validation_message": message
        }
    elif len(normalized) == 12:
        is_valid, message = validate_upc(normalized)
        return {
            "original": identifier,
            "normalized": normalized,
            "type": "UPC-A",
            "is_valid": is_valid,
            "validation_message": message
        }
    elif len(normalized) == 7:
        is_valid, message = validate_enr(normalized)
        return {
            "original": identifier,
            "normalized": normalized,
            "type": "E-nummer",
            "is_valid": is_valid,
            "validation_message": message
        }
    elif re.match(r'50\d{6}$', normalized):
        is_valid, message = validate_article_number(normalized)
        return {
            "original": identifier,
            "normalized": normalized,
            "type": "Copiax-artikel",
            "is_valid": is_valid,
            "validation_message": message
        }
    else:
        is_valid, message = validate_article_number(normalized)
        return {
            "original": identifier,
            "normalized": normalized,
            "type": "Artikelnummer",
            "is_valid": is_valid,
            "validation_message": message
        }


class EnhancedEanExtractorPro:
    """Förbättrad extraktor för EAN-koder och produktidentifierare från _pro-dokument"""
    
    def __init__(self, base_dir: Path, output_dir: Path):
        self.base_dir = base_dir
        self.output_dir = output_dir
        
        # Statistik och resultatvariabler
        self.document_count = 0
        self.identifier_count = 0
        self.documents_with_identifiers = 0
        self.documents_without_identifiers = 0
        self.pattern_counts = {group: 0 for group in PATTERN_GROUPS}
        self.individual_pattern_counts = defaultdict(int)
        self.discovered_formats = []
        self.identifier_types = Counter()
        self.validation_stats = {"valid": 0, "invalid": 0, "unknown": 0}
        self.pattern_performance = {}
        
        # För automatisk upptäckt av nya mönster
        self.discovered_patterns = []
        self.common_formats = Counter()
        
        # För mönsteranalys
        self.top_performing_patterns = {}
        self.low_performing_patterns = {}
        
        # Typer och kategorier
        self.identifier_type_counts = defaultdict(int)
        self.identifier_categories = defaultdict(list)
        
        # För att undvika dubbletter
        self.extracted_identifiers = set()
        
        # För dokumentspecifika data
        self.document_identifier_counts = defaultdict(int)
        
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
        2. Hantera HTML-element för tabellmönster
        3. Normalisera strukturer som kan innehålla EAN-koder
        """
        # Normalisera radbrytningar
        content = content.replace('\r\n', '\n').replace('\r', '\n')
        
        # Normalisera HTML-tabeller för bättre detektion
        content = re.sub(r'<tr>\s*', '<tr>', content)
        content = re.sub(r'\s*<\/tr>', '</tr>', content)
        content = re.sub(r'<td>\s*', '<td>', content)
        content = re.sub(r'\s*<\/td>', '</td>', content)
        
        # Normalisera punktlistor för bättre detektion
        content = re.sub(r'^\s*[-•*]\s*', '• ', content, flags=re.MULTILINE)
        
        # Normalisera kolon följt av mellanslag (vanligt i specifikationer)
        content = re.sub(r':\s+', ': ', content)
        
        return content
    
    def clean_match_text(self, text: str) -> str:
        """Rensa matchad text för bättre kvalitet"""
        # Rensa bort icke-numeriska tecken för EAN och liknande koder
        if re.match(r'^\s*\d[\d\s\-\.]+$', text):
            return re.sub(r'[^0-9]', '', text.strip())
        
        # För övriga identifierare, behåll vissa tecken men ta bort onödiga
        text = re.sub(r'[.,;:]+', '', text.strip())
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Ta bort parenteser om de omsluter hela strängen
        if text.startswith('(') and text.endswith(')'):
            text = text[1:-1].strip()
            
        return text
    
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
    
    def extract_multi_codes(self, text: str) -> List[str]:
        """Extrahera flera koder från kommaseparerad text eller listor"""
        codes = []
        
        # Försök med kommaseparation först
        if ',' in text:
            parts = [p.strip() for p in text.split(',')]
            for part in parts:
                cleaned = self.clean_match_text(part)
                if cleaned and len(cleaned) >= 7:  # Minimum längd för giltig kod
                    codes.append(cleaned)
        
        # Försök med radseparation om komma inte fungerade
        elif '\n' in text:
            lines = [line.strip() for line in text.split('\n')]
            for line in lines:
                # Matcha rader som innehåller punktlisteformat
                match = re.match(r'^\s*[•\-*]\s*(\d{7,13})', line)
                if match:
                    codes.append(match.group(1))
                # Eller rader som bara innehåller siffror
                elif re.match(r'^\s*\d{7,13}\s*$', line):
                    codes.append(self.clean_match_text(line))
        
        # Om vi fortfarande inte har några koder, sök efter isolerade sifferblock
        if not codes:
            for match in re.finditer(r'(?<!\d)(\d{7,13})(?!\d)', text):
                codes.append(match.group(1))
        
        return codes
    
    def identify_potential_formats(self, content: str) -> List[Dict[str, Any]]:
        """Identifiera potentiella nya produktidentifieringsformat med språkbaserad analys"""
        potential_formats = []
        
        # Dela in i meningar för analys
        sentences = re.split(r'(?<=[.!?])\s+', content)
        
        # Nyckelord som kan indikera produktidentifierare
        id_keywords = [
            'kod', 'code', 'nummer', 'number', 'ID', 'identifierare', 
            'identifier', 'referens', 'reference', 'artikelnr', 'artikel',
            'product', 'produkt', 'item', 'model', 'modell', 'ean', 'gtin',
            'upc', 'isbn', 'serienummer'
        ]
        
        for sentence in sentences:
            # Kontrollera om någon av nyckelorden finns i meningen
            if any(keyword.lower() in sentence.lower() for keyword in id_keywords):
                # Kontrollera att meningen inte redan matchar befintliga mönster
                if not any(re.search(pattern, sentence, re.IGNORECASE) for pattern in ALL_PATTERNS):
                    # Sök efter potentiella identifierare (t.ex. grupper av siffror)
                    # Först leta efter mönstret "nyckelord: värde"
                    for keyword in id_keywords:
                        pattern = fr'(?i){re.escape(keyword)}[:\s]+([A-Z0-9\-\.]+)'
                        match = re.search(pattern, sentence)
                        if match:
                            value = match.group(1).strip()
                            if value and len(value) >= 5:  # Minimum längd för en identifierare
                                # Registrera som potentiellt format
                                potential_format = {
                                    "keyword": keyword,
                                    "format": value,
                                    "sentence": sentence,
                                    "pattern_suggestion": f"r'(?i){re.escape(keyword)}[:\\s]+([A-Z0-9\\-\\.]+)'"
                                }
                                potential_formats.append(potential_format)
                                
                                # Spara för mönsteranalys
                                self.common_formats[keyword.lower()] += 1
        
        return potential_formats
    
    def is_duplicate_identifier(self, identifier: str, document_id: str) -> bool:
        """Kontrollera om en identifierare är en dubblett inom samma dokument"""
        id_key = f"{document_id}:{identifier}"
        if id_key in self.extracted_identifiers:
            return True
            
        self.extracted_identifiers.add(id_key)
        return False
    
    def extract_identifiers_from_file(self, file_path: Path) -> Dict[str, Any]:
        """Extrahera EAN-koder och produktidentifierare från en _pro-fil"""
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
                "has_identifiers": False,
                "identifiers": [],
                "discovered_formats": [],
                "content_sample": content[:1000] if len(content) > 1000 else content  # Exempel på innehållet
            }
            
            # Sök efter produktidentifierare med alla mönster
            for pattern_index, pattern in enumerate(ALL_PATTERNS):
                # Identifiera vilken grupp mönstret tillhör
                group_name = PATTERN_GROUP_MAP[pattern_index]
                
                for match in re.finditer(pattern, content, re.IGNORECASE | re.DOTALL):
                    # För mönster med capture group, använd den första gruppen
                    if match.groups():
                        identifier_text = match.group(1)
                    else:
                        # Fallback om ingen explicit capture group
                        matched_text = match.group(0)
                        if ":" in matched_text:
                            identifier_text = matched_text.split(":", 1)[1].strip()
                        else:
                            identifier_text = matched_text
                    
                    # Rensa identifieraren
                    cleaned_identifier = self.clean_match_text(identifier_text)
                    
                    # Hoppa över tomma eller för korta identifierare
                    if not cleaned_identifier or len(cleaned_identifier) < 5:
                        continue
                    
                    # Kontrollera om det är ett flerkodmönster
                    if group_name == "multi_code":
                        # Extrahera flera koder från texten
                        identifiers = self.extract_multi_codes(identifier_text)
                        
                        for id_text in identifiers:
                            # Rensa och kontrollera längd
                            id_cleaned = self.clean_match_text(id_text)
                            if not id_cleaned or len(id_cleaned) < 5:
                                continue
                                
                            # Undvik dubbletter
                            if self.is_duplicate_identifier(id_cleaned, product_id):
                                continue
                                
                            # Klassificera identifieraren
                            classification = classify_product_identifier(id_cleaned)
                            
                            # Hämta kontext
                            context = self.get_context(content, match.start(), match.end(), window_size=100)
                            
                            # Skapa identifierarstruktur
                            identifier_data = {
                                "identifier": id_cleaned,
                                "original": id_text,
                                "type": classification["type"],
                                "is_valid": classification["is_valid"],
                                "validation_message": classification["validation_message"],
                                "group": group_name,
                                "pattern_index": pattern_index,
                                "pattern": pattern,
                                "context": context,
                                "source": "multi_code"
                            }
                            
                            # Lägg till i resultatet
                            result["identifiers"].append(identifier_data)
                            
                            # Uppdatera statistik
                            self.identifier_count += 1
                            self.individual_pattern_counts[pattern_index] += 1
                            self.pattern_counts[group_name] += 1
                            self.identifier_types[classification["type"]] += 1
                            
                            # Uppdatera validieringsstatistik
                            if classification["is_valid"]:
                                self.validation_stats["valid"] += 1
                            else:
                                self.validation_stats["invalid"] += 1
                    else:
                        # Undvik dubbletter
                        if self.is_duplicate_identifier(cleaned_identifier, product_id):
                            continue
                            
                        # Klassificera identifieraren
                        classification = classify_product_identifier(cleaned_identifier)
                        
                        # Hämta kontext
                        context = self.get_context(content, match.start(), match.end(), window_size=100)
                        
                        # Skapa identifierarstruktur
                        identifier_data = {
                            "identifier": cleaned_identifier,
                            "original": identifier_text,
                            "type": classification["type"],
                            "is_valid": classification["is_valid"],
                            "validation_message": classification["validation_message"],
                            "group": group_name,
                            "pattern_index": pattern_index,
                            "pattern": pattern,
                            "context": context,
                            "source": "regex"
                        }
                        
                        # Lägg till i resultatet
                        result["identifiers"].append(identifier_data)
                        
                        # Uppdatera statistik
                        self.identifier_count += 1
                        self.individual_pattern_counts[pattern_index] += 1
                        self.pattern_counts[group_name] += 1
                        self.identifier_types[classification["type"]] += 1
                        
                        # Uppdatera valideringsstatistik
                        if classification["is_valid"]:
                            self.validation_stats["valid"] += 1
                        else:
                            self.validation_stats["invalid"] += 1
                        
                        # Spara per typ för framtida analys
                        self.identifier_categories[classification["type"]].append(identifier_data)
            
            # Identifiera potentiella nya format som inte matchas av befintliga mönster
            potential_formats = self.identify_potential_formats(content)
            if potential_formats:
                result["discovered_formats"] = potential_formats
                for format_data in potential_formats:
                    self.discovered_formats.append({
                        "product_id": product_id,
                        "format": format_data,
                        "file": str(file_path)
                    })
            
            # Uppdatera dokument-status
            if result["identifiers"]:
                result["has_identifiers"] = True
                self.documents_with_identifiers += 1
                # Antal identifierare i detta dokument
                self.document_identifier_counts[product_id] = len(result["identifiers"])
            else:
                self.documents_without_identifiers += 1
            
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
                "percentage": (count / self.identifier_count * 100) if self.identifier_count > 0 else 0
            }
        
        # Identifiera topp- och bottenprestanda
        top_count = min(20, len(sorted_patterns))
        if top_count > 0:
            self.top_performing_patterns = dict(sorted_patterns[:top_count])
            
        if len(sorted_patterns) > top_count:
            # Endast inkludera mönster med minst en matchning
            bottom_performers = [(idx, count) for idx, count in sorted_patterns if count > 0]
            bottom_count = min(20, len(bottom_performers))
            self.low_performing_patterns = dict(bottom_performers[-bottom_count:])
            
        return performance
    
    def suggest_new_patterns(self) -> List[Dict[str, Any]]:
        """Föreslå nya mönster baserat på upptäckta format"""
        suggestions = []
        
        # Analysera frekventa format
        if self.common_formats:
            # Ta de 20 vanligaste formaterna
            common_formats = self.common_formats.most_common(20)
            
            for keyword, count in common_formats:
                # Förbered förslag på mönster
                if count >= 2:  # Minst 2 förekomster
                    pattern_suggestion = {
                        "keyword": keyword,
                        "suggested_pattern": f"r'(?i){re.escape(keyword)}[:\\s]+([A-Z0-9\\-\\.]+)'",
                        "occurrences": count,
                        "potential_type": self._suggest_id_type(keyword)
                    }
                    suggestions.append(pattern_suggestion)
        
        # Analysera de upptäckta formaten
        format_patterns = defaultdict(list)
        
        for format_data in self.discovered_formats:
            keyword = format_data["format"]["keyword"].lower()
            value = format_data["format"]["format"]
            format_patterns[keyword].append(value)
        
        # Skapa mönsterförslag baserat på format
        for keyword, values in format_patterns.items():
            if len(values) >= 2:  # Minst 2 förekomster av samma nyckelord
                # Generera förslag baserat på formatexempel
                value_format = self._analyze_id_format(values)
                
                # Skapa förslag baserat på format-analys
                if value_format == "numeric":
                    pattern = f"r'(?i){re.escape(keyword)}[:\\s]+(\\d+)'",
                elif value_format == "alphanumeric":
                    pattern = f"r'(?i){re.escape(keyword)}[:\\s]+([A-Z0-9\\-\\.]+)'",
                elif value_format == "mixed":
                    pattern = f"r'(?i){re.escape(keyword)}[:\\s]+([^\\s]+)'",
                else:
                    pattern = f"r'(?i){re.escape(keyword)}[:\\s]+([^:\\s][^:]+)'",
                
                suggestion = {
                    "keyword": keyword,
                    "values": values[:5],  # Visa bara upp till 5 exempel
                    "format_type": value_format,
                    "suggested_pattern": pattern,
                    "occurrences": len(values),
                    "potential_type": self._suggest_id_type(keyword)
                }
                
                # Undvik duplikat
                if not any(s["keyword"] == keyword for s in suggestions):
                    suggestions.append(suggestion)
        
        # Spara förslagen
        if suggestions:
            suggestions_file = RESULTS_STRUCTURE["discovered"] / f"suggested_patterns_{self.timestamp}.json"
            with open(suggestions_file, 'w', encoding='utf-8') as f:
                json.dump(suggestions, f, ensure_ascii=False, indent=2)
            
            logger.info(f"Sparade {len(suggestions)} förslag på nya mönster till {suggestions_file}")
                
        return suggestions
    
    def _analyze_id_format(self, values: List[str]) -> str:
        """Analysera format på identifierare för att föreslå regex-mönster"""
        # Kontrollera om alla är numeriska
        if all(value.isdigit() for value in values):
            return "numeric"
            
        # Kontrollera om alla är alfanumeriska (bokstäver + siffror)
        if all(re.match(r'^[A-Z0-9\-\.]+$', value, re.IGNORECASE) for value in values):
            return "alphanumeric"
            
        # Kontrollera om alla är blandformat (inga mellanslag)
        if all(re.match(r'^[^\s]+$', value) for value in values):
            return "mixed"
            
        # Fallback
        return "generic"
    
    def _suggest_id_type(self, keyword: str) -> str:
        """Föreslå en identifierartyp baserat på nyckelord"""
        keyword_lower = keyword.lower()
        
        if "ean" in keyword_lower:
            return "EAN-13"
        elif "gtin" in keyword_lower:
            return "GTIN"
        elif "e-nr" in keyword_lower or "e-nummer" in keyword_lower:
            return "E-nummer"
        elif "art" in keyword_lower or "artikel" in keyword_lower:
            return "Artikelnummer"
        elif "upc" in keyword_lower:
            return "UPC"
        elif "isbn" in keyword_lower:
            return "ISBN"
        elif "rsk" in keyword_lower:
            return "RSK-nummer"
        elif "kod" in keyword_lower or "code" in keyword_lower:
            return "Produktkod"
        elif "id" in keyword_lower:
            return "Produkt-ID"
        elif "ref" in keyword_lower:
            return "Referensnummer"
        else:
            return "Okänd identifierare"
    
    def cluster_identifiers_by_type(self, identifiers: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        """Gruppera identifierare efter typ för bättre organisering"""
        clusters = defaultdict(list)
        
        for identifier in identifiers:
            id_type = identifier.get("type", "unknown")
            clusters[id_type].append(identifier)
            
        return dict(clusters)
    
    def process_documents(self) -> None:
        """Bearbeta alla _pro-dokument och extrahera produktidentifierare"""
        # Hitta alla _pro-filer
        document_files = self.find_documents()
        total_files = len(document_files)
        logger.info(f"Hittade {total_files} _pro-filer att analysera")
        
        # Skapa utdatakatalog
        self.output_dir.mkdir(exist_ok=True, parents=True)
        
        # Skapa utdatafiler
        identifiers_file = RESULTS_STRUCTURE["matched"] / f"identifiers_pro_{self.timestamp}.jsonl"
        no_identifiers_file = RESULTS_STRUCTURE["unmatched"] / f"no_identifiers_pro_{self.timestamp}.jsonl"
        samples_file = RESULTS_STRUCTURE["samples"] / f"samples_without_identifiers_{self.timestamp}.jsonl"
        discovered_file = RESULTS_STRUCTURE["discovered"] / f"discovered_formats_{self.timestamp}.jsonl"
        
        # Bearbeta varje fil
        with open(identifiers_file, 'w', encoding='utf-8') as ids_f, \
             open(no_identifiers_file, 'w', encoding='utf-8') as no_ids_f:
             
            for i, file_path in enumerate(document_files):
                # Extrahera produktidentifierare
                result = self.extract_identifiers_from_file(file_path)
                
                if result:
                    # Organisera identifierare efter typ
                    if result["has_identifiers"]:
                        # Gruppera identifierarna efter typ
                        result["grouped_identifiers"] = self.cluster_identifiers_by_type(result["identifiers"])
                        
                        # Skriv till matchningsfil
                        json_line = json.dumps(result, ensure_ascii=False)
                        ids_f.write(json_line + '\n')
                        
                        # Spara också i typspecifika filer
                        for id_type, ids in result["grouped_identifiers"].items():
                            if ids:
                                type_dir = RESULTS_STRUCTURE["types"] / id_type
                                type_dir.mkdir(exist_ok=True, parents=True)
                                
                                type_file = type_dir / f"{id_type}_{self.timestamp}.jsonl"
                                type_data = {
                                    "product_id": result["product_id"],
                                    "file_path": result["file_path"],
                                    "filename": result["filename"],
                                    "identifiers": ids
                                }
                                
                                # Append-mode för att samla alla identifierare av samma typ
                                with open(type_file, 'a', encoding='utf-8') as type_f:
                                    type_f.write(json.dumps(type_data, ensure_ascii=False) + '\n')
                    else:
                        # För filer utan identifierare, behåll bara grundläggande info
                        no_ids_record = {
                            "product_id": result["product_id"],
                            "file_path": result["file_path"],
                            "filename": result["filename"],
                            "content_sample": result["content_sample"]
                        }
                        json_line = json.dumps(no_ids_record, ensure_ascii=False)
                        no_ids_f.write(json_line + '\n')
                    
                    # Spara potentiellt upptäckta format
                    if result.get("discovered_formats"):
                        with open(discovered_file, 'a', encoding='utf-8') as disc_f:
                            for format_data in result["discovered_formats"]:
                                discovered_data = {
                                    "product_id": result["product_id"],
                                    "file_path": result["file_path"],
                                    "filename": result["filename"],
                                    "discovered_format": format_data
                                }
                                disc_f.write(json.dumps(discovered_data, ensure_ascii=False) + '\n')
                
                self.document_count += 1
                
                # Logga framsteg
                if (i+1) % 100 == 0 or i+1 == total_files:
                    logger.info(f"Bearbetade {i+1}/{total_files} filer ({(i+1)/total_files*100:.1f}%)")
        
        # Exportera slumpmässiga exempel från dokument utan identifierare för analys
        if self.documents_without_identifiers > 0:
            no_ids_records = []
            with open(no_identifiers_file, 'r', encoding='utf-8') as f:
                for line in f:
                    no_ids_records.append(json.loads(line))
            
            sample_size = min(50, len(no_ids_records))
            samples = random.sample(no_ids_records, sample_size)
            
            with open(samples_file, 'w', encoding='utf-8') as f:
                for sample in samples:
                    f.write(json.dumps(sample, ensure_ascii=False) + '\n')
            
            logger.info(f"Exporterade {sample_size} slumpmässiga exempel utan identifierare till {samples_file}")
        
        # Analysera mönsterprestanda
        pattern_performance = self.analyze_pattern_performance()
        
        # Föreslå nya mönster baserat på upptäckta format
        suggested_patterns = self.suggest_new_patterns()
        
        # Generera detaljerade rapporter
        self.generate_reports(
            total_files=total_files,
            identifiers_file=identifiers_file,
            no_identifiers_file=no_identifiers_file,
            samples_file=samples_file,
            discovered_file=discovered_file,
            pattern_performance=pattern_performance,
            suggested_patterns=suggested_patterns
        )


    def generate_reports(self, total_files: int, identifiers_file: Path, no_identifiers_file: Path, 
                         samples_file: Path, discovered_file: Path, pattern_performance: Dict,
                         suggested_patterns: List) -> None:
        """Generera detaljerade rapporter och sammanfattningar"""
        
        # 1. Skapa en detaljerad sammanfattningsfil (JSON)
        summary = {
            "timestamp": self.timestamp,
            "total_document_files": total_files,
            "total_files_processed": self.document_count,
            "documents_with_identifiers": self.documents_with_identifiers,
            "documents_without_identifiers": self.documents_without_identifiers,
            "identifier_coverage_percentage": (self.documents_with_identifiers / total_files * 100) if total_files > 0 else 0,
            "total_identifiers_found": self.identifier_count,
            "average_identifiers_per_document": (self.identifier_count / self.documents_with_identifiers) if self.documents_with_identifiers > 0 else 0,
            "pattern_group_counts": self.pattern_counts,
            "identifier_type_distribution": dict(self.identifier_types),
            "validation_stats": self.validation_stats,
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
            "discovered_formats_count": len(self.discovered_formats)
        }
        
        summary_file = RESULTS_STRUCTURE["reports"] / f"identifiers_pro_summary_{self.timestamp}.json"
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
                    "percentage_of_all_matches": (count / self.identifier_count * 100) if self.identifier_count > 0 else 0
                }
                for group, count in self.pattern_counts.items() if count > 0
            }
        }
        
        pattern_report_file = RESULTS_STRUCTURE["patterns"] / f"pattern_performance_{self.timestamp}.json"
        with open(pattern_report_file, 'w', encoding='utf-8') as f:
            json.dump(pattern_report, f, ensure_ascii=False, indent=2)
        
        # 3. Skapa validerings- och verifieringsrapport
        validation_report = {
            "timestamp": self.timestamp,
            "validation_summary": self.validation_stats,
            "validation_per_type": {
                id_type: {
                    "valid": sum(1 for id_data in ids if id_data.get("is_valid", False)),
                    "invalid": sum(1 for id_data in ids if not id_data.get("is_valid", True)),
                    "validation_issues": [
                        {
                            "product_id": id_data.get("product_id", "unknown"),
                            "identifier": id_data.get("identifier", ""),
                            "original": id_data.get("original", ""),
                            "validation_message": id_data.get("validation_message", "")
                        }
                        for id_data in ids if not id_data.get("is_valid", True)
                    ][:20]  # Visa bara de 20 första problemen
                }
                for id_type, ids in self.identifier_categories.items()
            }
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
            identifiers_file=identifiers_file,
            no_identifiers_file=no_identifiers_file,
            samples_file=samples_file,
            discovered_file=discovered_file,
            suggested_patterns=suggested_patterns,
            summary_file=summary_file,
            pattern_report_file=pattern_report_file,
            validation_report_file=validation_report_file
        )
    
    def generate_markdown_report(self, total_files: int, summary: Dict, pattern_report: Dict,
                               validation_report: Dict, identifiers_file: Path, no_identifiers_file: Path, 
                               samples_file: Path, discovered_file: Path, suggested_patterns: List,
                               summary_file: Path, pattern_report_file: Path, validation_report_file: Path) -> None:
        """Generera en detaljerad markdown-rapport med alla resultat och analyser"""
        
        report_file = RESULTS_STRUCTURE["reports"] / f"identifiers_pro_report_{self.timestamp}.md"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            # Huvudrubrik och inledning
            f.write(f"# Detaljerad Produktidentifieringsrapport\n\n")
            f.write(f"**Datum och tid:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"Denna rapport innehåller en detaljerad analys av produktidentifierare (EAN, artikelnummer, etc.) extraherade från _pro-dokument.\n\n")
            
            # Innehållsförteckning
            f.write("## Innehåll\n\n")
            f.write("1. [Sammanfattning](#sammanfattning)\n")
            f.write("2. [Identifierartyper](#identifierartyper)\n")
            f.write("3. [Mönsterprestanda](#mönsterprestanda)\n")
            f.write("   - [Toppresterande mönster](#toppresterande-mönster)\n")
            f.write("   - [Bottenprestanda mönster](#bottenprestanda-mönster)\n")
            f.write("   - [Mönstergruppernas prestanda](#mönstergruppernas-prestanda)\n")
            f.write("4. [Validering och datakvalitet](#validering-och-datakvalitet)\n")
            f.write("5. [Upptäckta format och mönsterförslag](#upptäckta-format-och-mönsterförslag)\n")
            f.write("6. [Dokument och filer](#dokument-och-filer)\n")
            f.write("7. [Nästa steg](#nästa-steg)\n\n")
            
            # Övergripande sammanfattning
            f.write("## Sammanfattning\n\n")
            f.write(f"- **Totalt antal _pro-filer:** {total_files}\n")
            f.write(f"- **Filer med produktidentifierare:** {self.documents_with_identifiers} ({summary['identifier_coverage_percentage']:.1f}%)\n")
            f.write(f"- **Filer utan produktidentifierare:** {self.documents_without_identifiers}\n")
            f.write(f"- **Totalt antal extraherade identifierare:** {self.identifier_count}\n")
            f.write(f"- **Genomsnittligt antal identifierare per dokument:** {summary['average_identifiers_per_document']:.1f}\n")
            f.write(f"- **Antal upptäckta potentiella nya format:** {summary['discovered_formats_count']}\n")
            f.write(f"- **Antal föreslagna nya mönster:** {summary['suggested_patterns_count']}\n")
            f.write(f"- **Valideringsstatus:** {self.validation_stats['valid']} giltiga, {self.validation_stats['invalid']} ogiltiga\n\n")
            
            # Identifierartyper
            f.write("## Identifierartyper\n\n")
            f.write("Nedan visas fördelningen av olika typer av produktidentifierare som hittats:\n\n")
            f.write("| Identifierartyp | Antal | Procentandel |\n")
            f.write("|----------------|-------|---------------|\n")
            
            # Sortera efter antal
            for id_type, count in sorted(self.identifier_types.items(), key=lambda x: x[1], reverse=True):
                percentage = (count / self.identifier_count * 100) if self.identifier_count > 0 else 0
                f.write(f"| {id_type} | {count} | {percentage:.1f}% |\n")
            
            # Mönsterprestanda
            f.write("\n## Mönsterprestanda\n\n")
            f.write(f"Totalt används {len(ALL_PATTERNS)} mönster för extraktion, varav {len(self.individual_pattern_counts)} gav träffar.\n\n")
            
            # Toppresterande mönster
            f.write("### Toppresterande mönster\n\n")
            f.write("De mönster som gav flest träffar:\n\n")
            f.write("| Mönsterindex | Grupp | Antal träffar | Procentandel | Mönster |\n")
            f.write("|--------------|-------|--------------|--------------|--------|\n")
            
            for idx, count in sorted(self.top_performing_patterns.items(), key=lambda x: x[1], reverse=True):
                percentage = (count / self.identifier_count * 100) if self.identifier_count > 0 else 0
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
                percentage = (count / self.identifier_count * 100) if self.identifier_count > 0 else 0
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
                    percentage = (count / self.identifier_count * 100) if self.identifier_count > 0 else 0
                    f.write(f"| {group} | {count} | {percentage:.1f}% |\n")
            
            # Validering och datakvalitet
            f.write("\n## Validering och datakvalitet\n\n")
            f.write(f"Av totalt {self.identifier_count} extraherade identifierare är {self.validation_stats['valid']} ({self.validation_stats['valid']/self.identifier_count*100:.1f}%) validerade som giltiga.\n\n")
            
            f.write("### Valideringsresultat per identifierartyp\n\n")
            f.write("| Identifierartyp | Antal valida | Antal ogiltiga | Valideringsfrekvens |\n")
            f.write("|-----------------|--------------|----------------|-----------------------|\n")
            
            for id_type, stats in validation_report.get("validation_per_type", {}).items():
                valid = stats.get("valid", 0)
                invalid = stats.get("invalid", 0)
                total = valid + invalid
                validation_rate = (valid / total * 100) if total > 0 else 0
                f.write(f"| {id_type} | {valid} | {invalid} | {validation_rate:.1f}% |\n")
            
            f.write("\n### Vanliga valideringsfel\n\n")
            
            all_issues = []
            for id_type, stats in validation_report.get("validation_per_type", {}).items():
                for issue in stats.get("validation_issues", []):
                    issue["id_type"] = id_type
                    all_issues.append(issue)
                    
            if all_issues:
                f.write("| Identifierartyp | Identifierare | Original | Felmeddelande |\n")
                f.write("|-----------------|---------------|----------|---------------|\n")
                
                for issue in all_issues[:20]:  # Visa bara de 20 första problemen
                    id_type = issue.get("id_type", "unknown")
                    identifier = issue.get("identifier", "unknown")
                    original = issue.get("original", "")
                    message = issue.get("validation_message", "")
                    f.write(f"| {id_type} | {identifier} | {original} | {message} |\n")
            else:
                f.write("Inga valieringsfel hittades.\n\n")
            
            # Upptäckta format och mönsterförslag
            f.write("\n## Upptäckta format och mönsterförslag\n\n")
            
            if suggested_patterns:
                f.write(f"Baserat på analys av dokument och frekventa identifieringsformat, föreslås följande {len(suggested_patterns)} nya mönster:\n\n")
                f.write("| Nyckelord | Potentiell typ | Föreslagen regex | Förekomster |\n")
                f.write("|-----------|---------------|-----------------|-------------|\n")
                
                for suggestion in suggested_patterns[:20]:  # Visa bara de 20 första förslagen
                    f.write(f"| {suggestion['keyword']} | {suggestion['potential_type']} | `{suggestion['suggested_pattern']}` | {suggestion['occurrences']} |\n")
                
                if len(suggested_patterns) > 20:
                    f.write(f"\n*...och {len(suggested_patterns) - 20} ytterligare förslag. Se JSON-filen för fullständig lista.*\n")
                    
                f.write("\nSe den fullständiga listan i JSON-filen för föreslagna mönster.\n\n")
            else:
                f.write("Inga nya mönsterförslag genererades i denna körning.\n\n")
            
            # Dokument och filer
            f.write("## Dokument och filer\n\n")
            f.write("### Resultatfiler\n\n")
            f.write(f"- **Extraherade produktidentifierare:** [{identifiers_file.name}]({identifiers_file})\n")
            f.write(f"- **Dokument utan identifierare:** [{no_identifiers_file.name}]({no_identifiers_file})\n")
            f.write(f"- **Exempel på dokument utan identifierare:** [{samples_file.name}]({samples_file})\n")
            f.write(f"- **Upptäckta potentiella format:** [{discovered_file.name}]({discovered_file})\n")
            f.write(f"- **Mönsterprestanda (JSON):** [{pattern_report_file.name}]({pattern_report_file})\n")
            f.write(f"- **Validering (JSON):** [{validation_report_file.name}]({validation_report_file})\n")
            f.write(f"- **Sammanfattning (JSON):** [{summary_file.name}]({summary_file})\n\n")
            
            # Typspecifika filer
            type_files = []
            for type_dir in (RESULTS_STRUCTURE["types"]).glob("*"):
                if type_dir.is_dir():
                    for type_file in type_dir.glob(f"*_{self.timestamp}.jsonl"):
                        type_files.append((type_dir.name, type_file))
            
            if type_files:
                f.write("### Identifierartypspecifika filer\n\n")
                for id_type, type_file in sorted(type_files):
                    f.write(f"- **{id_type}:** [{type_file.name}]({type_file})\n")
            
            # Nästa steg
            f.write("\n## Nästa steg\n\n")
            f.write("Baserat på denna analys rekommenderas följande åtgärder:\n\n")
            f.write("1. **Granska upptäckta format** för att identifiera nya mönster och förbättra befintliga\n")
            f.write("2. **Implementera föreslagna mönster** och jämför resultaten i nästa körning\n")
            f.write("3. **Förfina valideringslogiken** för att öka antalet korrekt validerade identifierare\n")
            f.write("4. **Utveckla specifika extraktorer för andra dokumenttyper** (_TEK, _produktblad, etc.)\n")
            f.write("5. **Expandera mönster för särskilt viktiga identifierartyper** som EAN-13 och artikelnummer\n")
            f.write("6. **Jämföra extraherade identifierare mot en känd databas** för att validera resultat\n")
            f.write("7. **Utveckla system för att följa artiklar över hela dokumentsetet** baserat på EAN-koder\n\n")
            
            f.write("---\n\n")
            f.write(f"Rapport genererad: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        logger.info(f"Genererade detaljerad produktidentifieringsrapport: {report_file}")


def main():
    """Huvudfunktion för produktidentifieringsextraktor"""
    start_time = datetime.now()
    logger.info(f"Startar förbättrad EAN/produktidentifierarextraktion från _pro-dokument: {start_time}")
    
    # Skapa och kör extraktorn
    extractor = EnhancedEanExtractorPro(BASE_DIR, OUTPUT_DIR)
    extractor.process_documents()
    
    end_time = datetime.now()
    duration = end_time - start_time
    logger.info(f"Extraktion slutförd på {duration.total_seconds():.1f} sekunder")


if __name__ == "__main__":
    main()







