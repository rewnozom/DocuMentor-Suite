
# markdown_analyzer/core/constants.py

from typing import Dict


# Konfigurationskonstanter
CHARS_PER_SEGMENT = 60000  # Max tecken per segment
FIELD_LIMIT = 131072      # Max tecken per CSV-fält
CSV_SPLIT_ROWS = 1000     # Max rader per CSV-fil

# Dokumenttypsmappning
SUFFIX_MAP: Dict[str, str] = {
    "ins": "installationer",
    "pro": "produktinfo",
    "man": "manual",
    "produktblad": "produktblad",
    "mdek": "ospecificerad",
    "cert": "certifieringar",
    "bro": "broschyr",
    "sak": "säkerhetsinformation",
    "TEK": "teknisk_specifikation"
}


"""Konstanter och konfigurationsvärden"""

VALID_DOCUMENT_TYPES: Dict[str, str] = {
    "pro": "produktinfo",
    "pre": "produktinfo",         # _PRE
    "produktblad": "produktblad",
    "prodblad": "produktblad",    # _prodblad
    "tek": "teknisk_specifikation",
    "sak": "säkerhetsinformation",
    "man": "manual",
    "ins": "installationer",
    "cert": "certifieringar",
    "bro": "broschyr",
    "mdek": "ospecificerad"
}

TECHNICAL_TABLE_HEADERS = [
    'Technical specifikation',
    'Tekniska data',
    'Teknisk information',
    'Specifikationer'
]