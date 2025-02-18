# markdown_analyzer/extractors/compatibility/patterns.py
"""Regex-mönster för kompatibilitetsextraktion"""

# Grundläggande kompatibilitetsmönster
BASIC_COMPATIBILITY_PATTERNS = [
    r'(?i)passar\s+(?:till|med|för)\s+([^\.]+)',
    r'(?i)kompatibel\s+med\s+([^\.]+)',
    r'(?i)kan\s+användas\s+(?:till|med)\s+([^\.]+)',
    r'(?i)(?:monteras|installeras)\s+tillsammans\s+med\s+([^\.]+)',
    r'(?i)fungerar\s+(?:med|tillsammans\s+med)\s+([^\.]+)',
    r'(?i)(?:godkänd|certifierad)\s+för\s+(?:användning\s+med)?\s+([^\.]+)',
    r'(?i)anpassad\s+för\s+([^\.]+)'
]

# Ersättningsmönster
REPLACEMENT_PATTERNS = [
    r'(?i)ersätter\s+([^\.]+)',
    r'(?i)ersättning\s+för\s+([^\.]+)',
    r'(?i)ersätts\s+av\s+([^\.]+)',
    r'(?i)tidigare\s+version:\s+([^\.]+)',
    r'(?i)ny\s+version\s+av\s+([^\.]+)'
]

# Villkorsmönster
CONDITION_PATTERNS = [
    r'(?i)(?:endast|bara)\s+(?:vid|för|med)\s+([^\.]+)',
    r'(?i)kräver\s+([^\.]+)',
    r'(?i)förutsätter\s+([^\.]+)',
    r'(?i)under\s+förutsättning\s+att\s+([^\.]+)'
]

# Familjemönster
FAMILY_PATTERNS = [
    r'(?i)(?:ingår\s+i|del\s+av)\s+(?:serie|familj)?\s+([^\.]+)',
    r'(?i)tillhör\s+(?:serie|familj)\s+([^\.]+)',
    r'(?i)(?:serie|familj):\s*([^\.]+)'
]

# Tekniska kravmönster
TECHNICAL_REQUIREMENT_PATTERNS = {
    'voltage': [
        r'(?i)(?:spänning|voltage):\s*(\d+(?:\.\d+)?)\s*V',
        r'(?i)(\d+(?:\.\d+)?)\s*V(?:olt)?'
    ],
    'dimensions': [
        r'(?i)(?:mått|dimensions):\s*(\d+(?:\.\d+)?)\s*(?:x|\*)\s*(\d+(?:\.\d+)?)\s*(?:x|\*)\s*(\d+(?:\.\d+)?)\s*(?:mm|cm|m)',
        r'(?i)(?:höjd|bredd|djup):\s*(\d+(?:\.\d+)?)\s*(?:mm|cm|m)'
    ],
    'protocol': [
        r'(?i)(?:protokoll|protocol):\s*([A-Za-z0-9\-]+)',
        r'(?i)(?:gränssnitt|interface):\s*([A-Za-z0-9\-]+)'
    ]
}

# Certifieringsmönster
CERTIFICATION_PATTERNS = [
    r'(?i)certifierad\s+(?:enligt|för)\s+([^\.]+)',
    r'(?i)uppfyller\s+(?:krav|standard)\s+([^\.]+)',
    r'(?i)godkänd\s+(?:enligt|för)\s+([^\.]+)'
]