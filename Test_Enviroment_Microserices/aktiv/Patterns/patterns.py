"""
patterns.py – Regex-mönster för kompatibilitetsextraktion

Detta modul innehåller grupperade mönster för:
  • Artikelnummer (ARTICLE_NUMBER_PATTERNS)
  • Grundläggande kompatibilitet (BASIC_COMPATIBILITY_PATTERNS)
  • Detaljerade kompatibilitetsrelationer (COMPATIBILITY_RELATIONSHIPS)
  • Ersättningsmönster (REPLACEMENT_PATTERNS)
  • Villkorsmönster (CONDITION_PATTERNS)
  • Familjemönster (FAMILY_PATTERNS)
  • Tekniska specifikationer (TECHNICAL_PATTERNS)
  • Certifieringsmönster (CERTIFICATION_PATTERNS)

Alla mönster exporteras via __all__.
"""

# Artikelnummermönster
ARTICLE_NUMBER_PATTERNS = [
    r'(?i)(50\d{6})',                                        # Ex. Copiax-format: 50xxxxxx
    r'(?i)E-nummer:\s*(\d{7})',
    r'(?i)EAN:\s*(\d{13})',
    r'(?i)art\.?\s*n[ro]\.?\s*:?\s*(\d{5,8})',
    r'(?i)Art\.no:\s*(\d{6})',
    r'(?i)artikel\s*n[ro]\.?\s*:?\s*(\d{5,8})',
    r'(?i)product\s*n[ro]\.?\s*:?\s*(\d{5,8})',
    r'(?i)item\s*n[ro]\.?\s*:?\s*(\d{5,8})',
    r'(?<!\d)(\d{5,8})(?!\d)'  # Generiskt 5-8 siffror
]

# Grundläggande kompatibilitetsmönster
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

# Detaljerade kompatibilitetsrelationer, grupperade per typ
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
    r'(?i)under\s+förutsättning\s+att\s+([^\.]+)',
    r'(?i)om\s+([^\.]+)',
    r'(?i)när\s+([^\.]+)'
]

# Familjemönster
FAMILY_PATTERNS = [
    r'(?i)(?:ingår\s+i|del\s+av)\s+(?:serie|familj)?\s+([^\.]+)',
    r'(?i)tillhör\s+(?:serie|familj)\s+([^\.]+)',
    r'(?i)(?:serie|familj):\s*([^\.]+)',
    r'(?i)(?:produktserie|product\s+series):\s*([^\.]+)'
]

# Tekniska specifikationer – uppdelade i grupper
TECHNICAL_PATTERNS = {
    'dimensions': [
        r'(?i)dimensioner\s*:\s*([^\.]+)',
        r'(?i)dimensions?\s*:\s*([^\.]+)',
        r'(?i)mått\s*:\s*([^\.]+)',
        r'(?i)measurements?\s*:\s*([^\.]+)',
        r'(?i)(\d+(?:\.\d+)?)\s*(?:mm|cm|m)\s*x\s*(\d+(?:\.\d+)?)\s*(?:mm|cm|m)(?:\s*x\s*(\d+(?:\.\d+)?))?',
        r'(?i)(?:height|höjd)\s*:\s*(\d+(?:\.\d+)?)\s*(?:mm|cm|m)',
        r'(?i)(?:width|bredd)\s*:\s*(\d+(?:\.\d+)?)\s*(?:mm|cm|m)',
        r'(?i)(?:depth|djup)\s*:\s*(\d+(?:\.\d+)?)\s*(?:mm|cm|m)',
        r'(?i)(?:length|längd)\s*:\s*(\d+(?:\.\d+)?)\s*(?:mm|cm|m)'
    ],
    'electrical': [
        r'(?i)(?:spänning|voltage)\s*:\s*(\d+(?:\.\d+)?)\s*(?:V|kV|mV)',
        r'(?i)(?:matningsspänning|supply voltage)\s*:\s*(\d+(?:\.\d+)?)\s*(?:V|kV|mV)',
        r'(?i)(?:ström|current)\s*:\s*(\d+(?:\.\d+)?)\s*(?:A|mA)',
        r'(?i)(?:strömförbrukning|current consumption)\s*:\s*(\d+(?:\.\d+)?)\s*(?:A|mA)',
        r'(?i)(?:effekt|power)\s*:\s*(\d+(?:\.\d+)?)\s*(?:W|kW)',
        r'(?i)(?:effektförbrukning|power consumption)\s*:\s*(\d+(?:\.\d+)?)\s*(?:W|kW)'
    ],
    'weight': [
        r'(?i)(?:vikt|weight)\s*:\s*(\d+(?:\.\d+)?)\s*(?:kg|g)',
        r'(?i)(?:massa|mass)\s*:\s*(\d+(?:\.\d+)?)\s*(?:kg|g)',
        r'(?i)(?:nettovikt|net weight)\s*:\s*(\d+(?:\.\d+)?)\s*(?:kg|g)',
        r'(?i)(?:bruttovikt|gross weight)\s*:\s*(\d+(?:\.\d+)?)\s*(?:kg|g)'
    ],
    'temperature': [
        r'(?i)(?:temperatur|temperature)\s*:\s*(-?\d+(?:\.\d+)?)\s*°?C',
        r'(?i)(?:drifttemperatur|operating temperature)\s*:\s*(-?\d+(?:\.\d+)?)\s*°?C',
        r'(?i)(?:omgivningstemperatur|ambient temperature)\s*:\s*(-?\d+(?:\.\d+)?)\s*°?C'
    ],
    'environmental': {
        'humidity': [
            r'(?i)(?:luftfuktighet|humidity):\s*(\d+(?:\.\d+)?)\s*%',
            r'(?i)(?:relativ\s+luftfuktighet|relative\s+humidity):\s*(\d+(?:\.\d+)?)\s*%'
        ],
        'protection': [
            r'(?i)(?:kapslingsklass|protection\s+class|IP\s+class):\s*(IP\d{2}[KX]?)',
            r'(?i)(?:skyddsklass|protection\s+rating):\s*((?:IP)?\d{2}[KX]?)'
        ]
    },
    'protocol': [
        r'(?i)(?:protokoll|protocol):\s*([A-Za-z0-9\-]+)',
        r'(?i)(?:gränssnitt|interface):\s*([A-Za-z0-9\-]+)',
        r'(?i)(?:kommunikation|communication):\s*([A-Za-z0-9\-]+)'
    ]
}

# Certifieringsmönster
CERTIFICATION_PATTERNS = [
    r'(?i)certifierad\s+(?:enligt|för)\s+([^\.]+)',
    r'(?i)uppfyller\s+(?:krav|standard)\s+([^\.]+)',
    r'(?i)godkänd\s+(?:enligt|för)\s+([^\.]+)',
    r'(?i)certifiering:\s*([^\.]+)',
    r'(?i)certification:\s*([^\.]+)'
]

__all__ = [
    "ARTICLE_NUMBER_PATTERNS",
    "BASIC_COMPATIBILITY_PATTERNS",
    "COMPATIBILITY_RELATIONSHIPS",
    "REPLACEMENT_PATTERNS",
    "CONDITION_PATTERNS",
    "FAMILY_PATTERNS",
    "TECHNICAL_PATTERNS",
    "CERTIFICATION_PATTERNS"
]
