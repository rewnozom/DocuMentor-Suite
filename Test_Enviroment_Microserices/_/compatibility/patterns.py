# compatibility/patterns.py
"""
Optimerade regex-mönster för kompatibilitetsextraktion.
Fokuserar på att extrahera kompatibilitetsinformation för -c kommandot.
"""

# Artikelnummermönster - behåller endast relevanta format
ARTICLE_NUMBER_PATTERNS = [
    r'(?i)(50\d{6})',                                # Copiax format (50xxxxxx)
    r'(?i)art\.?\s*n[ro]\.?\s*:?\s*(\d{5,8})',     # Vanlig förkortning
    r'(?i)artikel\s*n[ro]\.?\s*:?\s*(\d{5,8})',    # Svenska
    r'(?i)(?<!\d)(\d{5,8})(?!\d)'                   # 5-8 siffror (generiskt)
]

# Grundläggande kompatibilitetsmönster - optimerade för vår use case
BASIC_COMPATIBILITY_PATTERNS = [
    r'(?i)passar\s+(?:till|med|för)\s+([^\.]+)',
    r'(?i)passar\s+(?:på|i)?\s*([^\.]+)',
    r'(?i)kompatibel\s+med\s+([^\.]+)',
    r'(?i)kan\s+användas\s+(?:till|med)\s+([^\.]+)',
    r'(?i)(?:monteras|installeras)\s+tillsammans\s+med\s+([^\.]+)',
    r'(?i)fungerar\s+(?:med|tillsammans\s+med)\s+([^\.]+)',
    r'(?i)avsedd\s+för\s+([^\.]+)',
    r'(?i)tillbehör\s+till\s+([^\.]+)'
]

# Kompatibilitetsrelationer med fokus på direkta kopplingar
COMPATIBILITY_RELATIONSHIPS = {
    'direct': [
        r'(?i)kompatibel\s+med\s+([^\.]+)',
        r'(?i)fungerar\s+med\s+([^\.]+)',
        r'(?i)(?:kan|can)\s+användas\s+med\s+([^\.]+)',
        r'(?i)kan\s+kopplas\s+till\s+([^\.]+)',
        r'(?i)ansluts\s+till\s+([^\.]+)'
    ],
    'requires': [
        r'(?i)kräver\s+([^\.]+)',
        r'(?i)måste\s+ha\s+([^\.]+)',
        r'(?i)förutsätter\s+([^\.]+)'
    ]
}

# Ersättningsmönster för produktuppdateringar
REPLACEMENT_PATTERNS = [
    r'(?i)ersätter\s+([^\.]+)',
    r'(?i)ersätts\s+av\s+([^\.]+)',
    r'(?i)tidigare\s+version:\s+([^\.]+)',
    r'(?i)ny\s+version\s+av\s+([^\.]+)'
]

# Villkorsmönster för kompatibilitet
CONDITION_PATTERNS = [
    r'(?i)(?:endast|bara)\s+(?:vid|för|med)\s+([^\.]+)',
    r'(?i)kräver\s+([^\.]+)',
    r'(?i)förutsätter\s+([^\.]+)',
    r'(?i)under\s+förutsättning\s+att\s+([^\.]+)'
]

# Produktfamiljemönster
FAMILY_PATTERNS = [
    r'(?i)(?:ingår\s+i|del\s+av)\s+(?:serie|familj)?\s+([^\.]+)',
    r'(?i)tillhör\s+(?:serie|familj)\s+([^\.]+)',
    r'(?i)(?:serie|familj):\s*([^\.]+)'
]

# Export av mönsterkonstanter
__all__ = [
    'ARTICLE_NUMBER_PATTERNS',
    'BASIC_COMPATIBILITY_PATTERNS',
    'COMPATIBILITY_RELATIONSHIPS',
    'REPLACEMENT_PATTERNS',
    'CONDITION_PATTERNS',
    'FAMILY_PATTERNS'
]