# markdown_analyzer/extractors/technical/patterns.py
"""Utökade mönster för teknisk information"""



from ...core.enums import TechnicalCategory, UnitCategory
from ...core.enums import TechnicalCategory, UnitCategory
from ...extractors.technical.models import TechnicalSpecification, TechnicalUnit, TechnicalValue



TECHNICAL_PATTERNS = {
    TechnicalCategory.DIMENSIONS: [
        r'(?i)(?:dimensioner|mått|storlek):\s*'
        r'(\d+(?:\.\d+)?)\s*(?:x|\*)\s*'
        r'(\d+(?:\.\d+)?)\s*(?:x|\*)\s*'
        r'(\d+(?:\.\d+)?)\s*(?:mm|cm|m)',
        
        r'(?i)(?:höjd|bredd|djup|längd):\s*'
        r'(\d+(?:\.\d+)?)\s*(?:mm|cm|m)'
    ],
    
    TechnicalCategory.ELECTRICAL: [
        r'(?i)(?:spänning|voltage|matningsspänning):\s*(\d+(?:\.\d+)?)\s*(?:V|kV|mV)',
        r'(?i)(?:ström|strömförbrukning):\s*(\d+(?:\.\d+)?)\s*(?:A|mA)',
        r'(?i)(?:effekt|effektförbrukning):\s*(\d+(?:\.\d+)?)\s*(?:W|kW)'
    ],
    
    TechnicalCategory.MECHANICAL: [
        r'(?i)(?:vridmoment|moment):\s*(\d+(?:\.\d+)?)\s*(?:Nm)',
        r'(?i)(?:kraft|tryckkraft):\s*(\d+(?:\.\d+)?)\s*(?:N|kN)'
    ],
    
    TechnicalCategory.ENVIRONMENTAL: [
        r'(?i)(?:temperaturområde|arbetstemperatur):\s*'
        r'(-?\d+(?:\.\d+)?)\s*(?:till|-)\s*'
        r'(-?\d+(?:\.\d+)?)\s*°?(?:C|F)',
        r'(?i)(?:luftfuktighet|fuktighet):\s*'
        r'(\d+(?:\.\d+)?)\s*%'
    ],
    
    TechnicalCategory.WEIGHT: [
        r'(?i)(?:vikt|weight):\s*(\d+(?:\.\d+)?)\s*(?:kg|g)',
        r'(?i)(?:massa|mass):\s*(\d+(?:\.\d+)?)\s*(?:kg|g)',
        r'(?i)(?:nettovikt|net weight):\s*(\d+(?:\.\d+)?)\s*(?:kg|g)',
        r'(?i)(?:bruttovikt|gross weight):\s*(\d+(?:\.\d+)?)\s*(?:kg|g)'
    ],
    
    TechnicalCategory.TEMPERATURE: [
        r'(?i)(?:temperatur|temperature):\s*(-?\d+(?:\.\d+)?)\s*°?C',
        r'(?i)(?:drifttemperatur|operating temperature):\s*(-?\d+(?:\.\d+)?)\s*°?C'
    ]
}

IMPORTANCE_INDICATORS = {
    'high': [
        r'(?i)viktigt?',
        r'(?i)observera',
        r'(?i)notera',
        r'(?i)krav',
        r'(?i)måste'
    ],
    'medium': [
        r'(?i)rekommenderad',
        r'(?i)typisk',
        r'(?i)normal'
    ]
}
