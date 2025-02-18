# markdown_analyzer/core/patterns.py
"""
Regex-mönster för extraktion av olika typer av information.

Denna modul innehåller de konsoliderade mönsterdefinitionerna:
  - ARTICLE_NUMBER_PATTERNS: Identifiering av artikelnummer
  - TECHNICAL_PATTERNS: Tekniska specifikationer (dimensioner, elektrisk, vikt etc.)
  - COMPATIBILITY_PATTERNS: Grundläggande kompatibilitetsmönster
  - COMPATIBILITY_RELATIONSHIPS: Detaljerade kompatibilitetsrelationer per typ
"""

# Artikelnummermönster (konsoliderad version)
ARTICLE_NUMBER_PATTERNS = [
    # Direct number matches (most specific)
    r'(?i)(50\d{6})',                                        # Specific format starting with 50
    r'(?i)E-nummer:\s*(\d{7})',                             # E-number format
    r'(?i)EAN:\s*(\d{13})',                                 # EAN format
    
    # Article number variations with prefix
    r'(?i)art\.?\s*n[ro]\.?\s*:?\s*(\d{5,8})',            # Common abbreviation
    r'(?i)Art\.no:\s*(\d{6})',                             # Specific Art.no format
    r'(?i)artikel\s*n[ro]\.?\s*:?\s*(\d{5,8})',           # Full Swedish
    r'(?i)product\s*n[ro]\.?\s*:?\s*(\d{5,8})',           # Full English
    r'(?i)item\s*n[ro]\.?\s*:?\s*(\d{5,8})',              # Alternative English
    
    # Generic number pattern (least specific)
    r'(?<!\d)(\d{5,8})(?!\d)'                              # Any 5-8 digit number
]

# Technical patterns - comprehensive version
TECHNICAL_PATTERNS = {
    'dimensions': [
        # Direct dimension specifications
        r'(?i)dimensioner\s*:\s*([^\.]+)',
        r'(?i)dimensions?\s*:\s*([^\.]+)',
        r'(?i)mått\s*:\s*([^\.]+)',
        r'(?i)measurements?\s*:\s*([^\.]+)',
        
        # Specific measurements with units
        r'(?i)(\d+(?:\.\d+)?)\s*(?:mm|cm|m)\s*x\s*(\d+(?:\.\d+)?)\s*(?:mm|cm|m)\s*(?:x\s*(\d+(?:\.\d+)?)\s*(?:mm|cm|m))?',
        
        # Individual dimension measurements
        r'(?i)(?:height|höjd)\s*:\s*(\d+(?:\.\d+)?)\s*(?:mm|cm|m)',
        r'(?i)(?:width|bredd)\s*:\s*(\d+(?:\.\d+)?)\s*(?:mm|cm|m)',
        r'(?i)(?:depth|djup)\s*:\s*(\d+(?:\.\d+)?)\s*(?:mm|cm|m)',
        r'(?i)(?:length|längd)\s*:\s*(\d+(?:\.\d+)?)\s*(?:mm|cm|m)'
    ],
    
    'electrical': [
        # Voltage patterns
        r'(?i)(?:spänning|voltage)\s*:\s*(\d+(?:\.\d+)?)\s*(?:V|kV|mV)',
        r'(?i)(?:matningsspänning|supply voltage)\s*:\s*(\d+(?:\.\d+)?)\s*(?:V|kV|mV)',
        
        # Current patterns
        r'(?i)(?:ström|current)\s*:\s*(\d+(?:\.\d+)?)\s*(?:A|mA)',
        r'(?i)(?:strömförbrukning|current consumption)\s*:\s*(\d+(?:\.\d+)?)\s*(?:A|mA)',
        
        # Power patterns
        r'(?i)(?:effekt|power)\s*:\s*(\d+(?:\.\d+)?)\s*(?:W|kW)',
        r'(?i)(?:effektförbrukning|power consumption)\s*:\s*(\d+(?:\.\d+)?)\s*(?:W|kW)'
    ],
    
    'weight': [
        # Weight patterns
        r'(?i)(?:vikt|weight)\s*:\s*(\d+(?:\.\d+)?)\s*(?:kg|g)',
        r'(?i)(?:massa|mass)\s*:\s*(\d+(?:\.\d+)?)\s*(?:kg|g)',
        
        # Specific weight types
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
            r'(?i)(?:kapslingsklass|protection\s+class|IP\s+class):\s*(IP\d{2}[K|X]?)',
            r'(?i)(?:skyddsklass|protection\s+rating):\s*((?:IP)?\d{2}[K|X]?)'
        ]
    }
}

# Compatibility patterns - basic patterns for backward compatibility
COMPATIBILITY_PATTERNS = [
    r'(?i)kompatibel\s+med\s+([^\.]+)',
    r'(?i)compatible\s+with\s+([^\.]+)',
    r'(?i)passar\s+(?:till|med|för)\s+([^\.]+)',
    r'(?i)passar\s+(?:på|i)?\s*([^\.]+)',
    r'(?i)kan\s+användas\s+(?:till|med)\s+([^\.]+)',
    r'(?i)(?:monteras|installeras)\s+tillsammans\s+med\s+([^\.]+)',
    r'(?i)fungerar\s+(?:med|tillsammans\s+med)\s+([^\.]+)',
    r'(?i)(?:godkänd|certifierad)\s+för\s+(?:användning\s+med)?\s+([^\.]+)',
    r'(?i)anpassad\s+för\s+([^\.]+)',
    r'(?i)avsedd\s+för\s+([^\.]+)',
    r'(?i)lämplig\s+(?:till|för)\s+([^\.]+)',
    r'(?i)ersätter\s+([^\.]+)',
    r'(?i)tillbehör\s+till\s+([^\.]+)',
    r'(?i)kräver\s+([^\.]+)',
    r'(?i)rekommenderas?\s+(?:till|med|för)\s+([^\.]+)'
]

# Detailed compatibility relationships
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

# Export all pattern constants
__all__ = [
    'ARTICLE_NUMBER_PATTERNS',
    'TECHNICAL_PATTERNS',
    'COMPATIBILITY_PATTERNS',
    'COMPATIBILITY_RELATIONSHIPS'
]