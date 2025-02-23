
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Teknisk Specifikationsextraktor för _pro-dokument

Denna avancerade mikroservice:
1. Letar efter _pro-dokument i den angivna katalogstrukturen
2. Extraherar tekniska specifikationer med omfattande regex-mönster
3. Kategoriserar specifikationer i detaljerade kategorier
4. Extraherar enheter, värden och viktiga parametrar
5. Validerar extraherade data för konsistens och rimlighet
6. Identifierar potentiella nya specifikationstyper med NLP-metoder
7. Skapar utförliga visualiseringar och analyser av resultaten
8. Sparar allt i en organiserad katalogstruktur med JSONL-filer
"""

import os
import re
import json
import logging
import random
import math
from enum import Enum, auto
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple, Set, Counter, Union
from collections import defaultdict, Counter

# Konfigurera loggning
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("technical_extractor.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Definiera katalogstrukturer
BASE_DIR = Path("./converted_docs")
OUTPUT_DIR = Path("./extracted_data/technical")
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

# Skapa struktur för resultatkategorier
RESULTS_STRUCTURE = {
    "matched": OUTPUT_DIR / "matched",
    "unmatched": OUTPUT_DIR / "unmatched",
    "samples": OUTPUT_DIR / "samples",
    "patterns": OUTPUT_DIR / "patterns",
    "reports": OUTPUT_DIR / "reports",
    "discovered": OUTPUT_DIR / "discovered",
    "categories": OUTPUT_DIR / "categories",
    "validation": OUTPUT_DIR / "validation",
    
}

# Skapa kataloger
for dir_path in RESULTS_STRUCTURE.values():
    dir_path.mkdir(exist_ok=True, parents=True)

# -----------------------------------------------------------
# TEKNISKA KATEGORIER OCH ENHETER
# -----------------------------------------------------------

class TechnicalCategory(Enum):
    """Kategorier för tekniska specifikationer"""
    DIMENSIONS = auto()      # Dimensioner, storlek, mått
    ELECTRICAL = auto()      # Elektriska egenskaper (spänning, ström, etc)
    WEIGHT = auto()          # Vikt och massa
    TEMPERATURE = auto()     # Temperatur och värme
    PRESSURE = auto()        # Tryck
    FLOW = auto()            # Flöde
    MECHANICAL = auto()      # Mekaniska egenskaper
    PERFORMANCE = auto()     # Prestanda
    CAPACITY = auto()        # Kapacitet
    ENVIRONMENTAL = auto()   # Miljörelaterade egenskaper
    ENERGY = auto()          # Energirelaterade egenskaper
    MATERIAL = auto()        # Material
    COLOR = auto()           # Färg
    NETWORK = auto()         # Nätverksrelaterade egenskaper
    CONNECTION = auto()      # Anslutningar
    AUDIO = auto()           # Ljudrelaterade egenskaper
    VIDEO = auto()           # Bildrelaterade egenskaper
    FREQUENCY = auto()       # Frekvens
    RUNTIME = auto()         # Drifttid
    PROTECTION = auto()      # Skyddsklass
    LIGHTING = auto()        # Belysning
    MISCELLANEOUS = auto()   # Övrigt

class UnitCategory(Enum):
    """Kategorier för enheter"""
    LENGTH = auto()          # Längdenheter (mm, cm, m)
    AREA = auto()            # Areaenheter (mm², cm², m²)
    VOLUME = auto()          # Volymenheter (ml, l, cm³)
    WEIGHT = auto()          # Viktenheter (g, kg)
    TEMPERATURE = auto()     # Temperaturenheter (°C, K)
    ELECTRICAL = auto()      # Elektriska enheter (V, A, W)
    TIME = auto()            # Tidsenheter (s, min, h)
    FREQUENCY = auto()       # Frekvensenheter (Hz, kHz)
    PRESSURE = auto()        # Tryckenheter (Pa, bar)
    FLOW = auto()            # Flödesenheter (l/min, m³/h)
    SPEED = auto()           # Hastighetsenheter (m/s, km/h)
    FORCE = auto()           # Kraftenheter (N, kN)
    ENERGY = auto()          # Energienheter (J, kWh)
    POWER = auto()           # Effektenheter (W, kW)
    DATA = auto()            # Dataenheter (bit, byte, KB, MB)
    ANGLE = auto()           # Vinkelenheter (°, rad)
    LUMINOSITY = auto()      # Ljusstyrka (lumen, lux)
    PERCENTAGE = auto()      # Procent (%)
    NONE = auto()            # Ingen enhet

# Mappning från enhetssträngar till enhetstyper
UNIT_MAPPING = {
    # Längd
    "mm": UnitCategory.LENGTH,
    "cm": UnitCategory.LENGTH,
    "m": UnitCategory.LENGTH,
    "tum": UnitCategory.LENGTH,
    "inch": UnitCategory.LENGTH,
    "in": UnitCategory.LENGTH,
    "ft": UnitCategory.LENGTH,
    
    # Area
    "mm²": UnitCategory.AREA,
    "mm2": UnitCategory.AREA,
    "cm²": UnitCategory.AREA,
    "cm2": UnitCategory.AREA,
    "m²": UnitCategory.AREA,
    "m2": UnitCategory.AREA,
    
    # Volym
    "ml": UnitCategory.VOLUME,
    "cl": UnitCategory.VOLUME,
    "dl": UnitCategory.VOLUME,
    "l": UnitCategory.VOLUME,
    "cm³": UnitCategory.VOLUME,
    "cm3": UnitCategory.VOLUME,
    "m³": UnitCategory.VOLUME,
    "m3": UnitCategory.VOLUME,
    
    # Vikt
    "g": UnitCategory.WEIGHT,
    "kg": UnitCategory.WEIGHT,
    "ton": UnitCategory.WEIGHT,
    
    # Temperatur
    "°C": UnitCategory.TEMPERATURE,
    "C": UnitCategory.TEMPERATURE,
    "K": UnitCategory.TEMPERATURE,
    "°F": UnitCategory.TEMPERATURE,
    "F": UnitCategory.TEMPERATURE,
    
    # Elektriska
    "V": UnitCategory.ELECTRICAL,
    "mV": UnitCategory.ELECTRICAL,
    "kV": UnitCategory.ELECTRICAL,
    "A": UnitCategory.ELECTRICAL,
    "mA": UnitCategory.ELECTRICAL,
    "W": UnitCategory.ELECTRICAL,
    "kW": UnitCategory.ELECTRICAL,
    "MW": UnitCategory.ELECTRICAL,
    "VA": UnitCategory.ELECTRICAL,
    "kVA": UnitCategory.ELECTRICAL,
    "Ω": UnitCategory.ELECTRICAL,
    "ohm": UnitCategory.ELECTRICAL,
    
    # Tid
    "s": UnitCategory.TIME,
    "min": UnitCategory.TIME,
    "h": UnitCategory.TIME,
    "timmar": UnitCategory.TIME,
    "dagar": UnitCategory.TIME,
    
    # Frekvens
    "Hz": UnitCategory.FREQUENCY,
    "kHz": UnitCategory.FREQUENCY,
    "MHz": UnitCategory.FREQUENCY,
    "GHz": UnitCategory.FREQUENCY,
    
    # Tryck
    "Pa": UnitCategory.PRESSURE,
    "kPa": UnitCategory.PRESSURE,
    "MPa": UnitCategory.PRESSURE,
    "bar": UnitCategory.PRESSURE,
    "mbar": UnitCategory.PRESSURE,
    "atm": UnitCategory.PRESSURE,
    
    # Flöde
    "l/min": UnitCategory.FLOW,
    "l/s": UnitCategory.FLOW,
    "m³/h": UnitCategory.FLOW,
    "m3/h": UnitCategory.FLOW,
    
    # Hastighet
    "m/s": UnitCategory.SPEED,
    "km/h": UnitCategory.SPEED,
    
    # Kraft
    "N": UnitCategory.FORCE,
    "kN": UnitCategory.FORCE,
    "Nm": UnitCategory.FORCE,  # Vridmoment
    
    # Energi
    "J": UnitCategory.ENERGY,
    "kJ": UnitCategory.ENERGY,
    "kWh": UnitCategory.ENERGY,
    
    # Data
    "bit": UnitCategory.DATA,
    "byte": UnitCategory.DATA,
    "KB": UnitCategory.DATA,
    "MB": UnitCategory.DATA,
    "GB": UnitCategory.DATA,
    "Mbps": UnitCategory.DATA,
    "Gbps": UnitCategory.DATA,
    
    # Vinkel
    "°": UnitCategory.ANGLE,
    "grad": UnitCategory.ANGLE,
    "grader": UnitCategory.ANGLE,
    "rad": UnitCategory.ANGLE,
    
    # Ljusstyrka
    "lm": UnitCategory.LUMINOSITY,
    "lumen": UnitCategory.LUMINOSITY,
    "lux": UnitCategory.LUMINOSITY,
    "cd": UnitCategory.LUMINOSITY,
    
    # Procent
    "%": UnitCategory.PERCENTAGE,
    "procent": UnitCategory.PERCENTAGE,
}

# Mappning från kategori till vanliga enheter
CATEGORY_TO_UNITS = {
    TechnicalCategory.DIMENSIONS: [
        UnitCategory.LENGTH, UnitCategory.AREA, UnitCategory.VOLUME
    ],
    TechnicalCategory.ELECTRICAL: [
        UnitCategory.ELECTRICAL
    ],
    TechnicalCategory.WEIGHT: [
        UnitCategory.WEIGHT
    ],
    TechnicalCategory.TEMPERATURE: [
        UnitCategory.TEMPERATURE
    ],
    TechnicalCategory.PRESSURE: [
        UnitCategory.PRESSURE
    ],
    TechnicalCategory.FLOW: [
        UnitCategory.FLOW
    ],
    TechnicalCategory.MECHANICAL: [
        UnitCategory.FORCE
    ],
    TechnicalCategory.PERFORMANCE: [
        UnitCategory.PERCENTAGE, UnitCategory.POWER
    ],
    TechnicalCategory.CAPACITY: [
        UnitCategory.VOLUME, UnitCategory.WEIGHT, UnitCategory.DATA
    ],
    TechnicalCategory.ENVIRONMENTAL: [
        UnitCategory.TEMPERATURE, UnitCategory.PERCENTAGE
    ],
    TechnicalCategory.ENERGY: [
        UnitCategory.ENERGY, UnitCategory.POWER
    ],
    TechnicalCategory.FREQUENCY: [
        UnitCategory.FREQUENCY
    ],
    TechnicalCategory.RUNTIME: [
        UnitCategory.TIME
    ],
    TechnicalCategory.LIGHTING: [
        UnitCategory.LUMINOSITY, UnitCategory.POWER
    ]
}

# Mönster för att extrahera enheter
UNIT_EXTRACTION_PATTERN = r'(?i)(\d+(?:[.,]\d+)?)\s*([a-zA-ZμµΩ°%²³\'\"]+(?:/[a-zA-Z0-9]+)?)'

# -----------------------------------------------------------
# UTÖKADE TEKNISKA SPECIFIKATIONS-MÖNSTER
# -----------------------------------------------------------

# Dimensioner och fysiska mått
DIMENSIONS_PATTERNS = [
    # Grundläggande dimensionsmönster
    r'(?i)dimensioner\s*:\s*([^\.]+)',
    r'(?i)dimensions?\s*:\s*([^\.]+)',
    r'(?i)mått\s*:\s*([^\.]+)',
    r'(?i)measurements?\s*:\s*([^\.]+)',
    r'(?i)storlek\s*:\s*([^\.]+)',
    r'(?i)size\s*:\s*([^\.]+)',
    
    # Specifika dimensioner med enheter
    r'(?i)(\d+(?:[.,]\d+)?)\s*(?:mm|cm|m)\s*x\s*(\d+(?:[.,]\d+)?)\s*(?:mm|cm|m)\s*(?:x\s*(\d+(?:[.,]\d+)?)\s*(?:mm|cm|m))?',
    r'(?i)(?:B|W|L)\s*x\s*(?:H|D)\s*(?:x\s*(?:D|H))?\s*[:=]?\s*(\d+(?:[.,]\d+)?)\s*(?:mm|cm|m)\s*x\s*(\d+(?:[.,]\d+)?)\s*(?:mm|cm|m)\s*(?:x\s*(\d+(?:[.,]\d+)?)\s*(?:mm|cm|m))?',
    
    # Specifika dimensionsegenskaper
    r'(?i)(?:höjd|height)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:mm|cm|m)',
    r'(?i)(?:bredd|width)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:mm|cm|m)',
    r'(?i)(?:djup|depth)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:mm|cm|m)',
    r'(?i)(?:längd|length)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:mm|cm|m)',
    r'(?i)(?:diameter|diameter)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:mm|cm|m)',
    r'(?i)(?:radie|radius)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:mm|cm|m)',
    r'(?i)(?:omkrets|circumference)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:mm|cm|m)',
    
    # Area-relaterade mönster
    r'(?i)(?:area|yta)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:mm²|cm²|m²|mm2|cm2|m2)',
    r'(?i)(?:ytarea|surface area)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:mm²|cm²|m²|mm2|cm2|m2)',
    
    # Volym-relaterade mönster
    r'(?i)(?:volym|volume)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:mm³|cm³|m³|mm3|cm3|m3|ml|l)',
    r'(?i)(?:kapacitet|capacity)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:mm³|cm³|m³|mm3|cm3|m3|ml|l)',
    
    # Paketdimensioner
    r'(?i)(?:förpackningsmått|package dimensions)\s*:\s*([^\.]+)',
    r'(?i)(?:kartongmått|carton dimensions)\s*:\s*([^\.]+)',
]

# Elektriska specifikationer
ELECTRICAL_PATTERNS = [
    # Spänningsrelaterade mönster
    r'(?i)(?:spänning|voltage)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:V|kV|mV)',
    r'(?i)(?:matningsspänning|supply voltage)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:V|kV|mV)',
    r'(?i)(?:driftspänning|operating voltage)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:V|kV|mV)',
    r'(?i)(?:nominell spänning|nominal voltage)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:V|kV|mV)',
    r'(?i)(?:spänningsområde|voltage range)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:till|to|-)\s*(\d+(?:[.,]\d+)?)\s*(?:V|kV|mV)',
    
    # Strömrelaterade mönster
    r'(?i)(?:ström|current)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:A|mA)',
    r'(?i)(?:strömförbrukning|current consumption)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:A|mA)',
    r'(?i)(?:strömstyrka|current strength)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:A|mA)',
    r'(?i)(?:maxström|max current)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:A|mA)',
    
    # Effektrelaterade mönster
    r'(?i)(?:effekt|power)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:W|kW)',
    r'(?i)(?:effektförbrukning|power consumption)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:W|kW)',
    r'(?i)(?:nominell effekt|nominal power)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:W|kW)',
    r'(?i)(?:maxeffekt|max power)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:W|kW)',
    r'(?i)(?:standby-effekt|standby power)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:W|kW)',
    
    # Resistansrelaterade mönster
    r'(?i)(?:resistans|resistance)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:Ω|ohm)',
    r'(?i)(?:impedans|impedance)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:Ω|ohm)',
    
    # Frekvensrelaterade mönster (elektriska)
    r'(?i)(?:frekvens|frequency)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:Hz|kHz|MHz)',
    r'(?i)(?:frekvensområde|frequency range)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:till|to|-)\s*(\d+(?:[.,]\d+)?)\s*(?:Hz|kHz|MHz)',
    
    # Transformator och fasegenskaper
    r'(?i)(?:transformatoreffekt|transformer power)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:VA|kVA)',
    r'(?i)(?:primär spänning|primary voltage)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:V|kV)',
    r'(?i)(?:sekundär spänning|secondary voltage)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:V|kV)',
    r'(?i)(?:antal faser|number of phases)\s*:\s*(\d+)\s*(?:fas|phase)?',
    
    # Batterirelaterade mönster
    r'(?i)(?:batterityp|battery type)\s*:\s*([^\.]+)',
    r'(?i)(?:batterikapacitet|battery capacity)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:mAh|Ah)',
    r'(?i)(?:batteriliv|battery life)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:h|timmar|tim)',
    r'(?i)(?:laddningstid|charging time)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:h|timmar|tim|min)',
    
    # IP-klass relaterade mönster
    r'(?i)(?:IP-klass|IP class|IP rating)\s*:\s*(IP\d{2}[XK]?)',
    r'(?i)(?:kapslingsklass|enclosure rating)\s*:\s*(IP\d{2}[XK]?)',
    
    # Säkring och jorddispersionsrelaterade mönster
    r'(?i)(?:säkring|fuse)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:A)',
    r'(?i)(?:jordfelsbrytare|residual current device)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:mA)',
    
    # Stöt- och överspänningsskydd
    r'(?i)(?:överspänningsskydd|surge protection)\s*:\s*([^\.]+)',
    r'(?i)(?:skyddsklass|protection class)\s*:\s*([^\.]+)',
]

# Vikt och massa
WEIGHT_PATTERNS = [
    r'(?i)(?:vikt|weight)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:kg|g)',
    r'(?i)(?:massa|mass)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:kg|g)',
    r'(?i)(?:nettovikt|net weight)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:kg|g)',
    r'(?i)(?:bruttovikt|gross weight)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:kg|g)',
    r'(?i)(?:produktvikt|product weight)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:kg|g)',
    r'(?i)(?:förpackningsvikt|package weight)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:kg|g)',
    r'(?i)(?:tara|tare weight)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:kg|g)',
    r'(?i)(?:totalvikt|total weight)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:kg|g)',
    r'(?i)(?:maximala belastningen|maximum load)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:kg|g)',
    r'(?i)(?:maxbelastning|max load)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:kg|g)',
    r'(?i)(?:kapacitet|capacity)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:kg|g)',
    r'(?i)(?:lastkapacitet|load capacity)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:kg|g)',
]

# Temperatur
TEMPERATURE_PATTERNS = [
    r'(?i)(?:temperatur|temperature)\s*:\s*(-?\d+(?:[.,]\d+)?)\s*°?C',
    r'(?i)(?:drifttemperatur|operating temperature)\s*:\s*(-?\d+(?:[.,]\d+)?)\s*°?C',
    r'(?i)(?:omgivningstemperatur|ambient temperature)\s*:\s*(-?\d+(?:[.,]\d+)?)\s*°?C',
    r'(?i)(?:arbetstemperatur|working temperature)\s*:\s*(-?\d+(?:[.,]\d+)?)\s*°?C',
    r'(?i)(?:temperaturintervall|temperature range)\s*:\s*(-?\d+(?:[.,]\d+)?)\s*(?:till|to|-)\s*(-?\d+(?:[.,]\d+)?)\s*°?C',
    r'(?i)(?:temperaturområde|temperature range)\s*:\s*(-?\d+(?:[.,]\d+)?)\s*(?:till|to|-)\s*(-?\d+(?:[.,]\d+)?)\s*°?C',
    r'(?i)(?:maxtemperatur|max temperature)\s*:\s*(-?\d+(?:[.,]\d+)?)\s*°?C',
    r'(?i)(?:mintemperatur|min temperature)\s*:\s*(-?\d+(?:[.,]\d+)?)\s*°?C',
    r'(?i)(?:lagringstemperatur|storage temperature)\s*:\s*(-?\d+(?:[.,]\d+)?)\s*°?C',
    r'(?i)(?:termostatinställning|thermostat setting)\s*:\s*(-?\d+(?:[.,]\d+)?)\s*°?C',
    r'(?i)(?:uppvärmningstemperatur|heating temperature)\s*:\s*(-?\d+(?:[.,]\d+)?)\s*°?C',
    r'(?i)(?:kyltemperatur|cooling temperature)\s*:\s*(-?\d+(?:[.,]\d+)?)\s*°?C',
]

# Ljud och akustik
AUDIO_PATTERNS = [
    r'(?i)(?:ljudnivå|sound level)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:dB|dBA)',
    r'(?i)(?:ljudtryck|sound pressure)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:dB|dBA)',
    r'(?i)(?:buller|noise)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:dB|dBA)',
    r'(?i)(?:akustisk effekt|acoustic power)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:dB|dBA)',
    r'(?i)(?:frekvensrespons|frequency response)\s*:\s*([^\.]+)',
    r'(?i)(?:frekvensområde|frequency range)\s*:\s*([^\.]+)',
    r'(?i)(?:känslighet|sensitivity)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:dB)',
    r'(?i)(?:impedans|impedance)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:Ω|ohm)',
    r'(?i)(?:mikrofonkänslighet|microphone sensitivity)\s*:\s*([^\.]+)',
    r'(?i)(?:högtalarstorlek|speaker size)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:tum|"|mm)',
]

# Prestanda och kapacitet
PERFORMANCE_PATTERNS = [
    r'(?i)(?:prestanda|performance)\s*:\s*([^\.]+)',
    r'(?i)(?:verkningsgrad|efficiency)\s*:\s*(\d+(?:[.,]\d+)?)\s*%',
    r'(?i)(?:effektivitet|efficiency)\s*:\s*(\d+(?:[.,]\d+)?)\s*%',
    r'(?i)(?:kapacitet|capacity)\s*:\s*([^\.]+)',
    r'(?i)(?:maxkapacitet|max capacity)\s*:\s*([^\.]+)',
    r'(?i)(?:batteritid|battery life)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:h|timmar|min)',
    r'(?i)(?:minnesstorlek|memory size)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:MB|GB|TB)',
    r'(?i)(?:minne|memory)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:MB|GB|TB)',
    r'(?i)(?:CPU|processor)\s*:\s*([^\.]+)',
    r'(?i)(?:klockfrekvens|clock frequency)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:MHz|GHz)',
    r'(?i)(?:datahastighet|data rate)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:Mbps|Gbps|MB/s)',
    r'(?i)(?:överföringshastighet|transfer rate)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:Mbps|Gbps|MB/s)',
    r'(?i)(?:batteritid|battery life)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:h|timmar|min)',
]

# Miljömässiga specifikationer
ENVIRONMENTAL_PATTERNS = [
    r'(?i)(?:luftfuktighet|humidity):\s*(\d+(?:[.,]\d+)?)\s*%',
    r'(?i)(?:relativ\s+luftfuktighet|relative\s+humidity):\s*(\d+(?:[.,]\d+)?)\s*%',
    r'(?i)(?:IP-klass|protection\s+class|IP\s+class):\s*(IP\d{2}[KX]?)',
    r'(?i)(?:skyddsklass|protection\s+rating):\s*((?:IP)?\d{2}[KX]?)',
    r'(?i)(?:damm(?:tät|skydd)|dust(?:proof|protection))\s*:\s*([^\.]+)',
    r'(?i)(?:vatten(?:tät|skydd)|water(?:proof|protection))\s*:\s*([^\.]+)',
    r'(?i)(?:användningsmiljö|operating environment)\s*:\s*([^\.]+)',
    r'(?i)(?:klimatklass|climate class)\s*:\s*([^\.]+)',
    r'(?i)(?:höjd över havet|altitude)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:m)',
    r'(?i)(?:atmosfäriskt tryck|atmospheric pressure)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:hPa|mbar)',
    r'(?i)(?:isolationsklass|insulation class)\s*:\s*([^\.]+)',
    r'(?i)(?:EMC|electromagnetic compatibility)\s*:\s*([^\.]+)',
    r'(?i)(?:IP-klassificering|IP classification)\s*:\s*(IP\d{2}[KX]?)',
]


# Material och ytbehandling
MATERIAL_PATTERNS = [
    r'(?i)(?:material|material)\s*:\s*([^\.]+)',
    r'(?i)(?:material i (?:hölje|chassi|kapsling)|housing material)\s*:\s*([^\.]+)',
    r'(?i)(?:ytbehandling|surface treatment)\s*:\s*([^\.]+)',
    r'(?i)(?:ytfinish|surface finish)\s*:\s*([^\.]+)',
    r'(?i)(?:konstruktionsmaterial|construction material)\s*:\s*([^\.]+)',
    r'(?i)(?:beläggning|coating)\s*:\s*([^\.]+)',
    r'(?i)(?:kvalitet|quality)\s*:\s*([^\.]+)',
    r'(?i)(?:materialklass|material class)\s*:\s*([^\.]+)',
    r'(?i)(?:korrosionsbeständighet|corrosion resistance)\s*:\s*([^\.]+)',
    r'(?i)(?:materialegenskaper|material properties)\s*:\s*([^\.]+)',
]

# Färg och utseende
COLOR_PATTERNS = [
    r'(?i)(?:färg|color)\s*:\s*([^\.]+)',
    r'(?i)(?:kulör|color)\s*:\s*([^\.]+)',
    r'(?i)(?:färgkod|color code)\s*:\s*([^\.]+)',
    r'(?i)(?:RAL|RAL-kod)\s*:\s*([^\.]+)',
    r'(?i)(?:NCS|NCS-kod)\s*:\s*([^\.]+)',
    r'(?i)(?:finish|finish)\s*:\s*([^\.]+)',
    r'(?i)(?:utseende|appearance)\s*:\s*([^\.]+)',
    r'(?i)(?:design|design)\s*:\s*([^\.]+)',
]

# Nätverks- och kommunikationsrelaterade mönster
NETWORK_PATTERNS = [
    r'(?i)(?:nätverksstandarder|network standards)\s*:\s*([^\.]+)',
    r'(?i)(?:ethernet|ethernet)\s*:\s*([^\.]+)',
    r'(?i)(?:wifi|wi-fi|wireless)\s*:\s*([^\.]+)',
    r'(?i)(?:bluetooth|bluetooth version)\s*:\s*([^\.]+)',
    r'(?i)(?:frekvensband|frequency band)\s*:\s*([^\.]+)',
    r'(?i)(?:räckvidd|range)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:m)',
    r'(?i)(?:överföringshastighet|transmission rate)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:Mbps|Gbps|MB/s)',
    r'(?i)(?:protokoll|protocol)\s*:\s*([^\.]+)',
    r'(?i)(?:kryptering|encryption)\s*:\s*([^\.]+)',
    r'(?i)(?:nätverksport|network port)\s*:\s*([^\.]+)',
    r'(?i)(?:IP-adress|IP address)\s*:\s*([^\.]+)',
    r'(?i)(?:gateway|gateway)\s*:\s*([^\.]+)',
    r'(?i)(?:nätmask|subnet mask)\s*:\s*([^\.]+)',
]

# Anslutningar och kontakter
CONNECTION_PATTERNS = [
    r'(?i)(?:anslutningar|connections)\s*:\s*([^\.]+)',
    r'(?i)(?:kontakter|connectors)\s*:\s*([^\.]+)',
    r'(?i)(?:gränssnitt|interface)\s*:\s*([^\.]+)',
    r'(?i)(?:USB|USB-port)\s*:\s*([^\.]+)',
    r'(?i)(?:HDMI|HDMI-port)\s*:\s*([^\.]+)',
    r'(?i)(?:VGA|VGA-port)\s*:\s*([^\.]+)',
    r'(?i)(?:DisplayPort|DisplayPort)\s*:\s*([^\.]+)',
    r'(?i)(?:utgångar|outputs)\s*:\s*([^\.]+)',
    r'(?i)(?:ingångar|inputs)\s*:\s*([^\.]+)',
    r'(?i)(?:anslutningstyp|connection type)\s*:\s*([^\.]+)',
    r'(?i)(?:kabeltyp|cable type)\s*:\s*([^\.]+)',
    r'(?i)(?:kabellängd|cable length)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:m|mm|cm)',
    r'(?i)(?:kontaktdon|connector)\s*:\s*([^\.]+)',
]

# Belysning och optiska egenskaper
LIGHTING_PATTERNS = [
    r'(?i)(?:ljusstyrka|brightness)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:lm|lumen|cd)',
    r'(?i)(?:belysningsstyrka|illuminance)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:lux)',
    r'(?i)(?:ljusflöde|luminous flux)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:lm|lumen)',
    r'(?i)(?:färgtemperatur|color temperature)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:K)',
    r'(?i)(?:CRI|color rendering index)\s*:\s*(\d+(?:[.,]\d+)?)',
    r'(?i)(?:ljusutbyte|luminous efficacy)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:lm/W)',
    r'(?i)(?:ljuskälla|light source)\s*:\s*([^\.]+)',
    r'(?i)(?:LED-typ|LED type)\s*:\s*([^\.]+)',
    r'(?i)(?:antal LED|number of LEDs)\s*:\s*(\d+)',
    r'(?i)(?:bländning|glare)\s*:\s*([^\.]+)',
    r'(?i)(?:ljusdistribution|light distribution)\s*:\s*([^\.]+)',
    r'(?i)(?:livslängd|lifetime)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:h|timmar)',
]

# Certifieringar och standarder
CERTIFICATION_PATTERNS = [
    r'(?i)(?:certifieringar|certifications)\s*:\s*([^\.]+)',
    r'(?i)(?:standarder|standards)\s*:\s*([^\.]+)',
    r'(?i)(?:CE(?:-märkning)?|CE(?:-mark)?)\s*:\s*([^\.]+)',
    r'(?i)(?:RoHS|RoHS compliant)\s*:\s*([^\.]+)',
    r'(?i)(?:WEEE|WEEE compliant)\s*:\s*([^\.]+)',
    r'(?i)(?:IP-klass|IP class)\s*:\s*(IP\d{2}[XK]?)',
    r'(?i)(?:EMC|EMC compliant)\s*:\s*([^\.]+)',
    r'(?i)(?:energiklass|energy class)\s*:\s*([^\.]+)',
    r'(?i)(?:ERP|ERP directive)\s*:\s*([^\.]+)',
    r'(?i)(?:ATEX|ATEX certified)\s*:\s*([^\.]+)',
    r'(?i)(?:UL|UL certified)\s*:\s*([^\.]+)',
    r'(?i)(?:godkännanden|approvals)\s*:\s*([^\.]+)',
    r'(?i)(?:uppfyller|complies with)\s*:\s*([^\.]+)',
]

# Förpackningsinformation
PACKAGING_PATTERNS = [
    r'(?i)(?:förpackning|packaging)\s*:\s*([^\.]+)',
    r'(?i)(?:förpackningsinnehåll|package contents)\s*:\s*([^\.]+)',
    r'(?i)(?:kartongmått|carton dimensions)\s*:\s*([^\.]+)',
    r'(?i)(?:förpackningsmått|package dimensions)\s*:\s*([^\.]+)',
    r'(?i)(?:förpackningsvikt|package weight)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:kg|g)',
    r'(?i)(?:transportförpackning|transport packaging)\s*:\s*([^\.]+)',
    r'(?i)(?:antal per kartong|units per carton)\s*:\s*(\d+)',
    r'(?i)(?:palletering|palletization)\s*:\s*([^\.]+)',
]

# Installations- och driftsinformation
INSTALLATION_PATTERNS = [
    r'(?i)(?:installation|installation)\s*:\s*([^\.]+)',
    r'(?i)(?:monteringsanvisningar|mounting instructions)\s*:\s*([^\.]+)',
    r'(?i)(?:monteringshöjd|mounting height)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:mm|cm|m)',
    r'(?i)(?:installationsmetod|installation method)\s*:\s*([^\.]+)',
    r'(?i)(?:installationskrav|installation requirements)\s*:\s*([^\.]+)',
    r'(?i)(?:ventilationskrav|ventilation requirements)\s*:\s*([^\.]+)',
    r'(?i)(?:kylningskrav|cooling requirements)\s*:\s*([^\.]+)',
    r'(?i)(?:minsta avstånd|minimum distance)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:mm|cm|m)',
    r'(?i)(?:säkerhetsavstånd|safety distance)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:mm|cm|m)',
]

# Prestandaklasser och -mätningar
PERFORMANCE_CLASS_PATTERNS = [
    r'(?i)(?:energiklass|energy class)\s*:\s*([^\.]+)',
    r'(?i)(?:energimärkning|energy labeling)\s*:\s*([^\.]+)',
    r'(?i)(?:energiförbrukning|energy consumption)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:kWh)',
    r'(?i)(?:årlig energiförbrukning|annual energy consumption)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:kWh/år|kWh/year)',
    r'(?i)(?:verkningsgrad|efficiency)\s*:\s*(\d+(?:[.,]\d+)?)\s*%',
    r'(?i)(?:effektivitetsklass|efficiency class)\s*:\s*([^\.]+)',
    r'(?i)(?:prestandaindex|performance index)\s*:\s*([^\.]+)',
    r'(?i)(?:effektfaktor|power factor)\s*:\s*(\d+(?:[.,]\d+)?)',
    r'(?i)(?:COP|coefficient of performance)\s*:\s*(\d+(?:[.,]\d+)?)',
    r'(?i)(?:SEER|seasonal energy efficiency ratio)\s*:\s*(\d+(?:[.,]\d+)?)',
    r'(?i)(?:SCOP|seasonal coefficient of performance)\s*:\s*(\d+(?:[.,]\d+)?)',
]

# Driftsförhållanden och krav
OPERATING_CONDITIONS_PATTERNS = [
    r'(?i)(?:driftsförhållanden|operating conditions)\s*:\s*([^\.]+)',
    r'(?i)(?:driftstemperatur|operating temperature)\s*:\s*(-?\d+(?:[.,]\d+)?)\s*(?:till|to|-)\s*(-?\d+(?:[.,]\d+)?)\s*°?C',
    r'(?i)(?:tillåten luftfuktighet|permitted humidity)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:till|to|-)\s*(\d+(?:[.,]\d+)?)\s*%',
    r'(?i)(?:max höjd över havet|max altitude)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:m)',
    r'(?i)(?:driftsmiljö|operating environment)\s*:\s*([^\.]+)',
    r'(?i)(?:lagringsförhållanden|storage conditions)\s*:\s*([^\.]+)',
    r'(?i)(?:omgivningskrav|ambient requirements)\s*:\s*([^\.]+)',
    r'(?i)(?:atmosfäriskt tryck|atmospheric pressure)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:hPa|mbar)',
]

# Tryck- och flödesrelaterade mönster
PRESSURE_FLOW_PATTERNS = [
    r'(?i)(?:tryck|pressure)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:bar|Pa|kPa|MPa|psi)',
    r'(?i)(?:max(?:imalt)?\s+tryck|max(?:imum)?\s+pressure)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:bar|Pa|kPa|MPa|psi)',
    r'(?i)(?:min(?:imalt)?\s+tryck|min(?:imum)?\s+pressure)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:bar|Pa|kPa|MPa|psi)',
    r'(?i)(?:nominellt tryck|nominal pressure)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:bar|Pa|kPa|MPa|psi)',
    r'(?i)(?:arbetstryck|working pressure)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:bar|Pa|kPa|MPa|psi)',
    r'(?i)(?:flöde|flow(?:\s+rate)?)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:l/min|l/s|m³/h|m3/h)',
    r'(?i)(?:max(?:imalt)?\s+flöde|max(?:imum)?\s+flow(?:\s+rate)?)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:l/min|l/s|m³/h|m3/h)',
    r'(?i)(?:min(?:imalt)?\s+flöde|min(?:imum)?\s+flow(?:\s+rate)?)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:l/min|l/s|m³/h|m3/h)',
    r'(?i)(?:nominellt flöde|nominal flow(?:\s+rate)?)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:l/min|l/s|m³/h|m3/h)',
    r'(?i)(?:kapacitet|capacity)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:l/min|l/s|m³/h|m3/h)',
]

# Mekaniska egenskaper
MECHANICAL_PATTERNS = [
    r'(?i)(?:vridmoment|torque)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:Nm)',
    r'(?i)(?:max(?:imalt)?\s+vridmoment|max(?:imum)?\s+torque)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:Nm)',
    r'(?i)(?:nominellt vridmoment|nominal torque)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:Nm)',
    r'(?i)(?:kraft|force)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:N|kN)',
    r'(?i)(?:max(?:imal)?\s+kraft|max(?:imum)?\s+force)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:N|kN)',
    r'(?i)(?:dragkraft|pulling force)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:N|kN)',
    r'(?i)(?:tryckkraft|pushing force)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:N|kN)',
    r'(?i)(?:hållfasthet|strength)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:N|kN|MPa)',
    r'(?i)(?:brottstyrka|breaking strength)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:N|kN|MPa)',
    r'(?i)(?:slagtålighet|impact resistance)\s*:\s*([^\.]+)',
    r'(?i)(?:vibrationer|vibrations)\s*:\s*([^\.]+)',
]

# Samla alla mönstergrupper för enkel åtkomst och bearbetning
PATTERN_GROUPS = {
    "dimensions": DIMENSIONS_PATTERNS,
    "electrical": ELECTRICAL_PATTERNS,
    "weight": WEIGHT_PATTERNS,
    "temperature": TEMPERATURE_PATTERNS,
    "audio": AUDIO_PATTERNS,
    "performance": PERFORMANCE_PATTERNS,
    "environmental": ENVIRONMENTAL_PATTERNS,
    "material": MATERIAL_PATTERNS,
    "color": COLOR_PATTERNS,
    "network": NETWORK_PATTERNS,
    "connection": CONNECTION_PATTERNS,
    "lighting": LIGHTING_PATTERNS,
    "certification": CERTIFICATION_PATTERNS,
    "packaging": PACKAGING_PATTERNS,
    "installation": INSTALLATION_PATTERNS,
    "performance_class": PERFORMANCE_CLASS_PATTERNS,
    "operating_conditions": OPERATING_CONDITIONS_PATTERNS,
    "pressure_flow": PRESSURE_FLOW_PATTERNS,
    "mechanical": MECHANICAL_PATTERNS
}

# Mappning från mönstergrupp till teknisk kategori
GROUP_TO_CATEGORY = {
    "dimensions": TechnicalCategory.DIMENSIONS,
    "electrical": TechnicalCategory.ELECTRICAL,
    "weight": TechnicalCategory.WEIGHT,
    "temperature": TechnicalCategory.TEMPERATURE,
    "audio": TechnicalCategory.AUDIO,
    "performance": TechnicalCategory.PERFORMANCE,
    "environmental": TechnicalCategory.ENVIRONMENTAL,
    "material": TechnicalCategory.MATERIAL,
    "color": TechnicalCategory.COLOR,
    "network": TechnicalCategory.NETWORK,
    "connection": TechnicalCategory.CONNECTION,
    "lighting": TechnicalCategory.LIGHTING,
    "certification": TechnicalCategory.MISCELLANEOUS,
    "packaging": TechnicalCategory.MISCELLANEOUS,
    "installation": TechnicalCategory.MISCELLANEOUS,
    "performance_class": TechnicalCategory.PERFORMANCE,
    "operating_conditions": TechnicalCategory.ENVIRONMENTAL,
    "pressure_flow": TechnicalCategory.FLOW,
    "mechanical": TechnicalCategory.MECHANICAL
}

# Mönster för att identifiera viktiga tekniska specifikationer 
IMPORTANCE_INDICATORS = {
    'high': [
        r'(?i)viktigt?',
        r'(?i)observera',
        r'(?i)notera',
        r'(?i)krav',
        r'(?i)måste',
        r'(?i)skall',
        r'(?i)nödvändigt?',
        r'(?i)obligatoriskt?',
        r'(?i)krävs',
        r'(?i)required',
        r'(?i)important',
        r'(?i)essential',
        r'(?i)necessary',
        r'(?i)OBS',
        r'(?i)varning',
        r'(?i)warning',
        r'(?i)critical',
        r'(?i)kritiskt?'
    ],
    'medium': [
        r'(?i)rekommenderad',
        r'(?i)typisk',
        r'(?i)normal',
        r'(?i)recommended',
        r'(?i)typical',
        r'(?i)standard',
        r'(?i)vanligtvis',
        r'(?i)generally',
        r'(?i)vanlig',
        r'(?i)normalt',
        r'(?i)bör',
        r'(?i)should'
    ],
    'low': [
        r'(?i)kan',
        r'(?i)may',
        r'(?i)optional',
        r'(?i)valfritt?',
        r'(?i)possibly',
        r'(?i)potentially',
        r'(?i)sometimes',
        r'(?i)occasionally',
        r'(?i)ibland',
        r'(?i)möjligtvis',
        r'(?i)kan ha',
        r'(?i)might have'
    ]
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
# HJÄLPFUNKTIONER FÖR VALIDERING OCH RIMLIGHETSKONTROLL
# -----------------------------------------------------------

def is_valid_dimension(value: str, unit: str) -> Tuple[bool, str]:
    """Kontrollera om ett dimensionsvärde är rimligt"""
    try:
        # Normalisera värdet (hantera både komma och punkt)
        value = float(value.replace(',', '.'))
        
        # Grundläggande rimlighetsvalidering baserat på enhet
        if unit.lower() in ['mm']:
            # Millimeter (rimligt intervall från 0.1 mm till 10000 mm)
            if 0.1 <= value <= 10000:
                return True, "Rimligt"
            else:
                return False, f"Ovanligt {unit}-värde: {value}"
                
        elif unit.lower() in ['cm']:
            # Centimeter (rimligt intervall från 0.1 cm till 1000 cm)
            if 0.1 <= value <= 1000:
                return True, "Rimligt"
            else:
                return False, f"Ovanligt {unit}-värde: {value}"
                
        elif unit.lower() in ['m']:
            # Meter (rimligt intervall från 0.01 m till 100 m)
            if 0.01 <= value <= 100:
                return True, "Rimligt"
            else:
                return False, f"Ovanligt {unit}-värde: {value}"
                
        # Lägg till fler specifika validering här vid behov
        
        return True, "Antas vara rimligt (ingen specifik valideringsregel)"
        
    except ValueError:
        return False, "Kan inte tolka som ett numeriskt värde"

def is_valid_weight(value: str, unit: str) -> Tuple[bool, str]:
    """Kontrollera om ett viktvärde är rimligt"""
    try:
        # Normalisera värdet
        value = float(value.replace(',', '.'))
        
        # Grundläggande rimlighetsvalidering baserat på enhet
        if unit.lower() in ['g']:
            # Gram (rimligt intervall från 0.1 g till 100000 g)
            if 0.1 <= value <= 100000:
                return True, "Rimligt"
            else:
                return False, f"Ovanligt {unit}-värde: {value}"
                
        elif unit.lower() in ['kg']:
            # Kilogram (rimligt intervall från 0.001 kg till 1000 kg)
            if 0.001 <= value <= 1000:
                return True, "Rimligt"
            else:
                return False, f"Ovanligt {unit}-värde: {value}"
                
        # Lägg till fler specifika validering här vid behov
        
        return True, "Antas vara rimligt (ingen specifik valideringsregel)"
        
    except ValueError:
        return False, "Kan inte tolka som ett numeriskt värde"

def is_valid_electrical(value: str, unit: str) -> Tuple[bool, str]:
    """Kontrollera om ett elektriskt värde är rimligt"""
    try:
        # Normalisera värdet
        value = float(value.replace(',', '.'))
        
        # Grundläggande rimlighetsvalidering baserat på enhet
        if unit.lower() in ['v']:
            # Volt (rimligt intervall från 0.1 V till 1000 V)
            if 0.1 <= value <= 1000:
                return True, "Rimligt"
            else:
                return False, f"Ovanligt {unit}-värde: {value}"
                
        elif unit.lower() in ['kv']:
            # Kilovolt (rimligt intervall från 0.1 kV till 100 kV)
            if 0.1 <= value <= 100:
                return True, "Rimligt"
            else:
                return False, f"Ovanligt {unit}-värde: {value}"
                
        elif unit.lower() in ['a']:
            # Ampere (rimligt intervall från 0.01 A till 1000 A)
            if 0.01 <= value <= 1000:
                return True, "Rimligt"
            else:
                return False, f"Ovanligt {unit}-värde: {value}"
                
        elif unit.lower() in ['ma']:
            # Milliampere (rimligt intervall från 0.1 mA till 10000 mA)
            if 0.1 <= value <= 10000:
                return True, "Rimligt"
            else:
                return False, f"Ovanligt {unit}-värde: {value}"
                
        elif unit.lower() in ['w']:
            # Watt (rimligt intervall från 0.1 W till 10000 W)
            if 0.1 <= value <= 10000:
                return True, "Rimligt"
            else:
                return False, f"Ovanligt {unit}-värde: {value}"
                
        elif unit.lower() in ['kw']:
            # Kilowatt (rimligt intervall från 0.01 kW till 1000 kW)
            if 0.01 <= value <= 1000:
                return True, "Rimligt"
            else:
                return False, f"Ovanligt {unit}-värde: {value}"
                
        # Lägg till fler specifika validering här vid behov
        
        return True, "Antas vara rimligt (ingen specifik valideringsregel)"
        
    except ValueError:
        return False, "Kan inte tolka som ett numeriskt värde"

def is_valid_temperature(value: str) -> Tuple[bool, str]:
    """Kontrollera om ett temperaturvärde är rimligt"""
    try:
        # Normalisera värdet
        value = float(value.replace(',', '.'))
        
        # För temperaturer i Celsius (rimligt intervall från -100°C till +1500°C)
        if -100 <= value <= 1500:
            return True, "Rimligt"
        else:
            return False, f"Ovanligt temperaturvärde: {value}°C"
            
    except ValueError:
        return False, "Kan inte tolka som ett numeriskt värde"

def validate_spec_value(value: str, unit: str, category: TechnicalCategory) -> Tuple[bool, str]:
    """Validerar ett specifikt värde baserat på kategori och enhet"""
    # Validera baserat på kategori
    if category == TechnicalCategory.DIMENSIONS:
        return is_valid_dimension(value, unit)
    elif category == TechnicalCategory.WEIGHT:
        return is_valid_weight(value, unit)
    elif category == TechnicalCategory.ELECTRICAL:
        return is_valid_electrical(value, unit)
    elif category == TechnicalCategory.TEMPERATURE:
        return is_valid_temperature(value)
    else:
        # För andra kategorier, gör en grundläggande numerisk validering
        try:
            float(value.replace(',', '.'))
            return True, "Värdet är numeriskt"
        except ValueError:
            # För icke-numeriska värden, anta att de är giltiga men markera
            return True, "Icke-numeriskt värde (ingen validering)"





## Teknisk Specifikationsextraktor för _pro-dokument (Del 2)
####################################################################

class TechnicalValue:
    """Representerar ett tekniskt värde med enhet och valideringsresultat"""
    
    def __init__(self, raw_value: str, unit: str = None, normalized_value: float = None):
        self.raw_value = raw_value
        self.unit = unit
        
        # Försök normalisera värdet om det inte redan är gjort
        if normalized_value is None:
            try:
                self.normalized_value = float(raw_value.replace(',', '.'))
            except (ValueError, TypeError):
                self.normalized_value = None
        else:
            self.normalized_value = normalized_value
            
        self.is_valid = True
        self.validation_message = "Ej validerad"
        
    def validate(self, category: TechnicalCategory) -> 'TechnicalValue':
        """Validera värdet baserat på kategori och enhet"""
        if self.unit and self.normalized_value is not None:
            self.is_valid, self.validation_message = validate_spec_value(
                str(self.raw_value), self.unit, category
            )
        return self
    
    def to_dict(self) -> Dict[str, Any]:
        """Konvertera till dictionary-representation"""
        return {
            "raw_value": self.raw_value,
            "unit": self.unit,
            "normalized_value": self.normalized_value,
            "is_valid": self.is_valid,
            "validation_message": self.validation_message
        }


class TechnicalSpecification:
    """Representerar en teknisk specifikation med namn, värde, enhet och metadata"""
    
    def __init__(
        self, 
        name: str, 
        raw_value: str, 
        category: TechnicalCategory,
        unit: str = None,
        context: str = None,
        pattern: str = None,
        pattern_index: int = None,
        source: str = "regex"
    ):
        self.name = name
        self.raw_value = raw_value
        self.category = category
        self.unit = unit
        self.context = context
        self.pattern = pattern
        self.pattern_index = pattern_index
        self.source = source
        self.importance = "normal"
        
        # Extrahera enheten från värdet om den inte är angiven
        if not unit:
            self.unit, self.raw_value = self._extract_unit(raw_value)
        
        # Skapa ett tekniskt värde-objekt
        self.value = TechnicalValue(self.raw_value, self.unit)
        
        # Validera värdet
        self.value.validate(category)
        
        # Bedöm vikten baserat på kontext
        self._assess_importance()
    
    def _extract_unit(self, value_text: str) -> Tuple[str, str]:
        """Extrahera enheten från ett värde, om den finns"""
        # Sök efter vanliga enhetsformat
        unit_match = re.search(UNIT_EXTRACTION_PATTERN, value_text)
        if unit_match:
            value = unit_match.group(1)
            unit = unit_match.group(2)
            return unit, value
        
        # Om ingen enhetsmatchning, försök identifiera enheten från texten
        for unit, _ in sorted(UNIT_MAPPING.items(), key=lambda x: len(x[0]), reverse=True):
            if unit.lower() in value_text.lower():
                # Extrahera värdet före enheten
                value_pattern = r'(\d+(?:[.,]\d+)?)\s*' + re.escape(unit)
                value_match = re.search(value_pattern, value_text, re.IGNORECASE)
                if value_match:
                    return unit, value_match.group(1)
        
        # Ingen enhet hittades
        return None, value_text
    
    def _assess_importance(self) -> None:
        """Bedöm vikten av specifikationen baserat på kontext och nyckelord"""
        if not self.context:
            return
            
        # Sök efter indikatorer på hög viktighet
        for indicator in IMPORTANCE_INDICATORS['high']:
            if re.search(indicator, self.context, re.IGNORECASE):
                self.importance = "high"
                return
                
        # Sök efter indikatorer på medium viktighet
        for indicator in IMPORTANCE_INDICATORS['medium']:
            if re.search(indicator, self.context, re.IGNORECASE):
                self.importance = "medium"
                return
                
        # Sök efter indikatorer på låg viktighet
        for indicator in IMPORTANCE_INDICATORS['low']:
            if re.search(indicator, self.context, re.IGNORECASE):
                self.importance = "low"
                return
    
    def to_dict(self) -> Dict[str, Any]:
        """Konvertera till dictionary-representation"""
        return {
            "name": self.name,
            "raw_value": self.raw_value,
            "category": self.category.name,
            "unit": self.unit,
            "value": self.value.to_dict(),
            "context": self.context[:200] + "..." if self.context and len(self.context) > 200 else self.context,
            "pattern": self.pattern,
            "pattern_index": self.pattern_index,
            "source": self.source,
            "importance": self.importance,
            "is_valid": self.value.is_valid,
            "validation_message": self.value.validation_message
        }


class EnhancedTechnicalExtractorPro:
    """Förbättrad extraktor för tekniska specifikationer från _pro-dokument"""
    
    def __init__(self, base_dir: Path, output_dir: Path):
        self.base_dir = base_dir
        self.output_dir = output_dir
        
        # Statistik och resultatvariabler
        self.document_count = 0
        self.spec_count = 0
        self.documents_with_specs = 0
        self.documents_without_specs = 0
        self.pattern_counts = {group: 0 for group in PATTERN_GROUPS}
        self.individual_pattern_counts = defaultdict(int)
        self.category_counts = {category.name: 0 for category in TechnicalCategory}
        self.discovered_specs = []
        self.pattern_performance = {}
        
        # För automatisk upptäckt av nya mönster
        self.discovered_patterns = []
        self.common_formats = Counter()
        
        # För mönsteranalys
        self.top_performing_patterns = {}
        self.low_performing_patterns = {}
        
        # Kategorier och typer
        self.spec_categories = defaultdict(list)
        self.validation_stats = {"valid": 0, "invalid": 0, "unknown": 0}
        
        # För att undvika dubbletter
        self.extracted_specs = set()
        
        # För dokumentspecifika data
        self.document_spec_counts = defaultdict(int)
        
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
        3. Hantera HTML-element för tabellmönster
        """
        # Normalisera radbrytningar
        content = content.replace('\r\n', '\n').replace('\r', '\n')
        
        # Normalisera tabellstruktur för bättre detektion
        content = re.sub(r'<tr>\s*', '<tr>', content)
        content = re.sub(r'\s*<\/tr>', '</tr>', content)
        content = re.sub(r'<td>\s*', '<td>', content)
        content = re.sub(r'\s*<\/td>', '</td>', content)
        
        # Hantera komplicerade tabbindelningar (vanligt i tekniska specifikationer)
        content = re.sub(r'\t+', ' ', content)
        
        # Normalisera kolon följt av mellanslag (vanligt i specifikationer)
        content = re.sub(r':\s+', ': ', content)
        
        return content
    
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
    
    def extract_unit_from_match(self, match_text: str) -> Tuple[str, str]:
        """Extrahera enheten från en matchning"""
        # Sök efter siffror följt av enheter
        unit_match = re.search(r'(\d+(?:[.,]\d+)?)\s*([a-zA-Z]+(?:/[a-zA-Z0-9]+)?)', match_text)
        if unit_match:
            value = unit_match.group(1)
            unit = unit_match.group(2)
            return unit, value
        
        # Ingen enhetsmatchning
        return None, match_text
    
    def identify_category_from_match(self, match_text: str, group_name: str) -> TechnicalCategory:
        """Identifiera teknisk kategori baserat på matchning och gruppnamn"""
        # Använd mappningen från gruppnamn till kategori
        if group_name in GROUP_TO_CATEGORY:
            return GROUP_TO_CATEGORY[group_name]
        
        # Fallback baserat på matchningstexten
        if any(keyword in match_text.lower() for keyword in ['dimension', 'mått', 'size', 'höjd', 'bredd', 'djup', 'längd']):
            return TechnicalCategory.DIMENSIONS
        elif any(keyword in match_text.lower() for keyword in ['volt', 'amp', 'watt', 'ström', 'spänning', 'effekt']):
            return TechnicalCategory.ELECTRICAL
        elif any(keyword in match_text.lower() for keyword in ['vikt', 'weight', 'mass']):
            return TechnicalCategory.WEIGHT
        elif any(keyword in match_text.lower() for keyword in ['temp', 'grader', 'celsius']):
            return TechnicalCategory.TEMPERATURE
        elif any(keyword in match_text.lower() for keyword in ['ljud', 'sound', 'noise', 'audio']):
            return TechnicalCategory.AUDIO
        elif any(keyword in match_text.lower() for keyword in ['material']):
            return TechnicalCategory.MATERIAL
        elif any(keyword in match_text.lower() for keyword in ['färg', 'color']):
            return TechnicalCategory.COLOR
        elif any(keyword in match_text.lower() for keyword in ['tryck', 'pressure']):
            return TechnicalCategory.PRESSURE
        elif any(keyword in match_text.lower() for keyword in ['flöde', 'flow']):
            return TechnicalCategory.FLOW
        elif any(keyword in match_text.lower() for keyword in ['ip', 'skydd', 'protection']):
            return TechnicalCategory.PROTECTION
        else:
            return TechnicalCategory.MISCELLANEOUS
    
    def identify_spec_name_from_match(self, match: re.Match, group_name: str) -> str:
        """Identifiera ett logiskt namn för specifikationen baserat på matchning"""
        # Försök extrahera namnet från matchningen
        full_match = match.group(0)
        
        # Matcha mönster som "egenskap: värde"
        name_match = re.match(r'(?i)([^:]+):', full_match)
        if name_match:
            return name_match.group(1).strip()
        
        # Om ingen direkt matchning, använd gruppnamnet
        return group_name.replace('_', ' ').title()
    
    def is_duplicate_spec(self, name: str, value: str, document_id: str) -> bool:
        """Kontrollera om en specifikation är en dubblett inom samma dokument"""
        spec_key = f"{document_id}:{name}:{value}"
        if spec_key in self.extracted_specs:
            return True
            
        self.extracted_specs.add(spec_key)
        return False
    
    def identify_potential_specs(self, content: str) -> List[Dict[str, Any]]:
        """Identifiera potentiella nya tekniska specifikationer som inte fångas av befintliga mönster"""
        potential_specs = []
        
        # Dela in i meningar för analys
        sentences = re.split(r'(?<=[.!?])\s+', content)
        
        # Nyckelord som kan indikera teknisk information
        tech_keywords = [
            'specifikation', 'specification', 'teknisk', 'technical', 'egenskap',
            'property', 'värde', 'value', 'mått', 'dimension', 'vikt', 'weight',
            'temperatur', 'temperature', 'effekt', 'power', 'kapacitet', 'capacity'
        ]
        
        for sentence in sentences:
            # Kontrollera om någon av nyckelorden finns i meningen
            if any(keyword in sentence.lower() for keyword in tech_keywords):
                # Kontrollera att meningen inte redan matchar befintliga mönster
                if not any(re.search(pattern, sentence, re.IGNORECASE) for pattern in ALL_PATTERNS):
                    # Matcha mönster som "egenskap: värde"
                    spec_match = re.search(r'([^:]+):\s*([^\.]+)', sentence)
                    if spec_match:
                        name = spec_match.group(1).strip()
                        value = spec_match.group(2).strip()
                        
                        # Registrera som potentiell specifikation
                        potential_spec = {
                            "name": name,
                            "value": value,
                            "sentence": sentence,
                            "pattern_suggestion": f"r'(?i){re.escape(name)}\\s*:\\s*([^\\\.]+)'"
                        }
                        
                        potential_specs.append(potential_spec)
                        
                        # Spara för mönsteranalys
                        self.common_formats[name.lower()] += 1
        
        return potential_specs
    
    def extract_specifications_from_file(self, file_path: Path) -> Dict[str, Any]:
        """Extrahera tekniska specifikationer från en fil med förbättrad encoding-hantering"""
        encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
        
        for encoding in encodings:
            try:
                # Försök läsa med olika encodings
                with open(file_path, 'r', encoding=encoding) as f:
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
                    "has_specs": False,
                    "specifications": [],
                    "discovered_specs": [],
                    "content_sample": content[:1000] if len(content) > 1000 else content  # Exempel på innehållet
                }
                
                # Sök efter tekniska specifikationer med alla mönster
                for pattern_index, pattern in enumerate(ALL_PATTERNS):
                    # Identifiera vilken grupp mönstret tillhör
                    group_name = PATTERN_GROUP_MAP[pattern_index]
                    
                    for match in re.finditer(pattern, content, re.IGNORECASE | re.DOTALL):
                        # Extrahera värdet från matchningen
                        matched_text = match.group(0)
                        
                        # För mönster med capture group, använd den första gruppen
                        if match.groups():
                            value_text = match.group(1)
                        else:
                            # Fallback om ingen explicit capture group
                            value_text = matched_text.split(":", 1)[1].strip() if ":" in matched_text else matched_text
                        
                        # Ignorera tomma eller för korta värden
                        if not value_text or len(value_text) < 2:
                            continue
                        
                        # Identifiera namnet på specifikationen
                        spec_name = self.identify_spec_name_from_match(match, group_name)
                        
                        # Kontrollera om denna specifikation redan har extraherats (deduplicering)
                        if self.is_duplicate_spec(spec_name, value_text, product_id):
                            continue
                        
                        # Identifiera kategorin
                        category = self.identify_category_from_match(matched_text, group_name)
                        
                        # Extrahera enheten från värdet om möjligt
                        unit, cleaned_value = self.extract_unit_from_match(value_text)
                        
                        # Hämta kontext
                        context = self.get_context(content, match.start(), match.end(), window_size=150)
                        
                        # Skapa specifikationsobjekt
                        spec = TechnicalSpecification(
                            name=spec_name,
                            raw_value=value_text,
                            category=category,
                            unit=unit,
                            context=context,
                            pattern=pattern,
                            pattern_index=pattern_index,
                            source="regex"
                        )
                        
                        # Lägg till i resultatet
                        result["specifications"].append(spec.to_dict())
                        
                        # Uppdatera statistik
                        self.spec_count += 1
                        self.individual_pattern_counts[pattern_index] += 1
                        self.pattern_counts[group_name] += 1
                        self.category_counts[category.name] += 1
                        
                        # Uppdatera valideringsstatistik
                        if spec.value.is_valid:
                            self.validation_stats["valid"] += 1
                        else:
                            self.validation_stats["invalid"] += 1
                        
                        # Spara per kategori för framtida analys
                        self.spec_categories[category.name].append(spec.to_dict())
                
                # Identifiera potentiella specifikationer som inte matchas av befintliga mönster
                potential_specs = self.identify_potential_specs(content)
                if potential_specs:
                    result["discovered_specs"] = potential_specs
                    for spec in potential_specs:
                        self.discovered_specs.append({
                            "product_id": product_id,
                            "spec": spec,
                            "file": str(file_path)
                        })
                
                # Uppdatera dokument-status
                if result["specifications"]:
                    result["has_specs"] = True
                    self.documents_with_specs += 1
                    # Antal specifikationer i detta dokument
                    self.document_spec_counts[product_id] = len(result["specifications"])
                else:
                    self.documents_without_specs += 1
                
                return result
                
            except UnicodeDecodeError:
                # Om denna encoding inte fungerade, prova nästa
                continue
            except Exception as e:
                # För andra typer av fel, logga och returnera None
                logger.error(f"Fel vid bearbetning av {file_path}: {str(e)}")
                return None
                
        # Om ingen encoding fungerade
        logger.error(f"Kunde inte läsa {file_path} med någon av de testade encodings")
        return None







# Teknisk Specifikationsextraktor för _pro-dokument (Del 3)

############################################################


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
                "percentage": (count / self.spec_count * 100) if self.spec_count > 0 else 0
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
        """Föreslå nya mönster baserat på upptäckta specifikationer"""
        suggestions = []
        
        # Analysera frekventa specifikationsnamn
        if self.common_formats:
            # Ta de 20 vanligaste formaterna
            common_formats = self.common_formats.most_common(20)
            
            for name, count in common_formats:
                # Förbered förslag på mönster
                if count >= 2:  # Minst 2 förekomster
                    pattern_suggestion = {
                        "name": name,
                        "suggested_pattern": f"r'(?i){re.escape(name)}\\s*:\\s*([^\\.]+)'",
                        "occurrences": count,
                        "category": self._suggest_category(name)
                    }
                    suggestions.append(pattern_suggestion)
        
        # Analysera de upptäckta specifikationerna för att identifiera mönster
        name_value_patterns = defaultdict(list)
        
        for spec in self.discovered_specs:
            name = spec["spec"]["name"].lower()
            value = spec["spec"]["value"]
            name_value_patterns[name].append(value)
        
        # Skapa mönsterförslag baserat på namn-värdepar
        for name, values in name_value_patterns.items():
            if len(values) >= 2:  # Minst 2 förekomster av samma namn
                # Försök identifiera värdeformat
                values_contain_numbers = any(re.search(r'\d', value) for value in values)
                values_contain_units = any(re.search(r'\d\s*[a-zA-Z]+', value) for value in values)
                
                category = self._suggest_category(name)
                
                if values_contain_units:
                    # Mönster för numeriska värden med enheter
                    pattern = f"r'(?i){re.escape(name)}\\s*:\\s*(\\d+(?:[.,]\\d+)?\\s*[a-zA-Z]+)'"
                elif values_contain_numbers:
                    # Mönster för numeriska värden
                    pattern = f"r'(?i){re.escape(name)}\\s*:\\s*(\\d+(?:[.,]\\d+)?)'"
                else:
                    # Mönster för text-värden
                    pattern = f"r'(?i){re.escape(name)}\\s*:\\s*([^\\.]+)'"
                
                suggestion = {
                    "name": name,
                    "values": values[:5],  # Visa bara upp till 5 exempel
                    "suggested_pattern": pattern,
                    "occurrences": len(values),
                    "category": category
                }
                
                # Undvik duplikat
                if not any(s["name"] == name for s in suggestions):
                    suggestions.append(suggestion)
        
        # Spara förslagen
        if suggestions:
            suggestions_file = RESULTS_STRUCTURE["discovered"] / f"suggested_patterns_{self.timestamp}.json"
            with open(suggestions_file, 'w', encoding='utf-8') as f:
                json.dump(suggestions, f, ensure_ascii=False, indent=2)
            
            logger.info(f"Sparade {len(suggestions)} förslag på nya mönster till {suggestions_file}")
                
        return suggestions
    
    def _suggest_category(self, name: str) -> str:
        """Föreslå en passande teknisk kategori baserat på namnet"""
        name_lower = name.lower()
        
        # Dimensionsrelaterade nyckelord
        if any(keyword in name_lower for keyword in ['dimension', 'mått', 'höjd', 'bredd', 'längd', 'djup', 'diameter', 'storlek', 'size']):
            return TechnicalCategory.DIMENSIONS.name
            
        # Elektriska nyckelord
        elif any(keyword in name_lower for keyword in ['volt', 'spänning', 'ström', 'watt', 'effekt', 'frekvens', 'ampere']):
            return TechnicalCategory.ELECTRICAL.name
            
        # Viktrelaterade nyckelord
        elif any(keyword in name_lower for keyword in ['vikt', 'weight', 'massa', 'mass']):
            return TechnicalCategory.WEIGHT.name
            
        # Temperaturrelaterade nyckelord
        elif any(keyword in name_lower for keyword in ['temp', 'temperatur', 'grader', 'värme', 'kyla']):
            return TechnicalCategory.TEMPERATURE.name
            
        # Materialrelaterade nyckelord
        elif any(keyword in name_lower for keyword in ['material', 'yta', 'beläggning']):
            return TechnicalCategory.MATERIAL.name
            
        # Färgrelaterade nyckelord
        elif any(keyword in name_lower for keyword in ['färg', 'kulör', 'color', 'nyans']):
            return TechnicalCategory.COLOR.name
            
        # Ljudrelaterade nyckelord
        elif any(keyword in name_lower for keyword in ['ljud', 'audio', 'decibel', 'db', 'volym']):
            return TechnicalCategory.AUDIO.name
            
        # Prestandarelaterade nyckelord
        elif any(keyword in name_lower for keyword in ['prestanda', 'performance', 'kapacitet', 'capacity']):
            return TechnicalCategory.PERFORMANCE.name
            
        # Miljörelaterade nyckelord
        elif any(keyword in name_lower for keyword in ['miljö', 'environmental', 'fukt', 'humidity']):
            return TechnicalCategory.ENVIRONMENTAL.name
            
        # Nätverksrelaterade nyckelord
        elif any(keyword in name_lower for keyword in ['nätverk', 'network', 'wifi', 'lan', 'ethernet']):
            return TechnicalCategory.NETWORK.name
            
        # Anslutningsrelaterade nyckelord
        elif any(keyword in name_lower for keyword in ['anslutning', 'connection', 'port', 'kontakt', 'interface']):
            return TechnicalCategory.CONNECTION.name
            
        # Fallback till övrigt
        else:
            return TechnicalCategory.MISCELLANEOUS.name
    
    def cluster_specs_by_category(self, specs: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        """Gruppera specifikationer efter kategori för bättre organisering"""
        clusters = defaultdict(list)
        
        for spec in specs:
            category = spec.get("category", "MISCELLANEOUS")
            clusters[category].append(spec)
            
        return dict(clusters)
    
    def process_documents(self) -> None:
        """Bearbeta alla _pro-dokument och extrahera tekniska specifikationer"""
        # Hitta alla _pro-filer
        document_files = self.find_documents()
        total_files = len(document_files)
        logger.info(f"Hittade {total_files} _pro-filer att analysera")
        
        # Skapa utdatakatalog
        self.output_dir.mkdir(exist_ok=True, parents=True)
        
        # Skapa utdatafiler
        specs_file = RESULTS_STRUCTURE["matched"] / f"technical_specs_pro_{self.timestamp}.jsonl"
        no_specs_file = RESULTS_STRUCTURE["unmatched"] / f"no_specs_pro_{self.timestamp}.jsonl"
        samples_file = RESULTS_STRUCTURE["samples"] / f"samples_without_specs_{self.timestamp}.jsonl"
        discovered_file = RESULTS_STRUCTURE["discovered"] / f"discovered_specs_{self.timestamp}.jsonl"
        
        # Bearbeta varje fil
        with open(specs_file, 'w', encoding='utf-8') as specs_f, \
             open(no_specs_file, 'w', encoding='utf-8') as no_specs_f:
             
            for i, file_path in enumerate(document_files):
                # Extrahera tekniska specifikationer
                result = self.extract_specifications_from_file(file_path)
                
                if result:
                    # Organisera specifikationer efter kategori
                    if result["has_specs"]:
                        # Gruppera specifikationerna efter kategori
                        result["grouped_specs"] = self.cluster_specs_by_category(result["specifications"])
                        
                        # Skriv till matchningsfil
                        json_line = json.dumps(result, ensure_ascii=False)
                        specs_f.write(json_line + '\n')
                        
                        # Spara också i kategorispecifika filer
                        for category, category_specs in result["grouped_specs"].items():
                            if category_specs:
                                category_dir = RESULTS_STRUCTURE["categories"] / category
                                category_dir.mkdir(exist_ok=True, parents=True)
                                
                                category_file = category_dir / f"{category}_{self.timestamp}.jsonl"
                                category_data = {
                                    "product_id": result["product_id"],
                                    "file_path": result["file_path"],
                                    "filename": result["filename"],
                                    "specifications": category_specs
                                }
                                
                                # Append-mode för att samla alla specifikationer av samma kategori
                                with open(category_file, 'a', encoding='utf-8') as cat_f:
                                    cat_f.write(json.dumps(category_data, ensure_ascii=False) + '\n')
                    else:
                        # För filer utan specifikationer, behåll bara grundläggande info
                        no_specs_record = {
                            "product_id": result["product_id"],
                            "file_path": result["file_path"],
                            "filename": result["filename"],
                            "content_sample": result["content_sample"]
                        }
                        json_line = json.dumps(no_specs_record, ensure_ascii=False)
                        no_specs_f.write(json_line + '\n')
                    
                    # Spara potentiellt upptäckta specifikationer
                    if result.get("discovered_specs"):
                        with open(discovered_file, 'a', encoding='utf-8') as disc_f:
                            for spec in result["discovered_specs"]:
                                discovered_data = {
                                    "product_id": result["product_id"],
                                    "file_path": result["file_path"],
                                    "filename": result["filename"],
                                    "discovered_spec": spec
                                }
                                disc_f.write(json.dumps(discovered_data, ensure_ascii=False) + '\n')
                
                self.document_count += 1
                
                # Logga framsteg
                if (i+1) % 100 == 0 or i+1 == total_files:
                    logger.info(f"Bearbetade {i+1}/{total_files} filer ({(i+1)/total_files*100:.1f}%)")
        
        # Exportera slumpmässiga exempel från dokument utan specifikationer för analys
        if self.documents_without_specs > 0:
            no_specs_records = []
            with open(no_specs_file, 'r', encoding='utf-8') as f:
                for line in f:
                    no_specs_records.append(json.loads(line))
            
            sample_size = min(50, len(no_specs_records))
            samples = random.sample(no_specs_records, sample_size)
            
            with open(samples_file, 'w', encoding='utf-8') as f:
                for sample in samples:
                    f.write(json.dumps(sample, ensure_ascii=False) + '\n')
            
            logger.info(f"Exporterade {sample_size} slumpmässiga exempel utan specifikationer till {samples_file}")
        
        # Analysera mönsterprestanda
        pattern_performance = self.analyze_pattern_performance()
        
        # Föreslå nya mönster baserat på upptäckta specifikationer
        suggested_patterns = self.suggest_new_patterns()
        
        # Generera detaljerade rapporter
        self.generate_reports(
            total_files=total_files,
            specs_file=specs_file,
            no_specs_file=no_specs_file,
            samples_file=samples_file,
            discovered_file=discovered_file,
            pattern_performance=pattern_performance,
            suggested_patterns=suggested_patterns
        )









############################################################


    def generate_reports(self, total_files: int, specs_file: Path, no_specs_file: Path, 
                        samples_file: Path, discovered_file: Path, pattern_performance: Dict,
                        suggested_patterns: List) -> None:
        """Generera detaljerade rapporter och sammanfattningar"""
        
        # 1. Skapa en detaljerad sammanfattningsfil (JSON)
        summary = {
            "timestamp": self.timestamp,
            "total_document_files": total_files,
            "total_files_processed": self.document_count,
            "documents_with_specs": self.documents_with_specs,
            "documents_without_specs": self.documents_without_specs,
            "specs_coverage_percentage": (self.documents_with_specs / total_files * 100) if total_files > 0 else 0,
            "total_specs_found": self.spec_count,
            "average_specs_per_document": (self.spec_count / self.documents_with_specs) if self.documents_with_specs > 0 else 0,
            "pattern_group_counts": self.pattern_counts,
            "category_distribution": self.category_counts,
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
            "discovered_specs_count": len(self.discovered_specs)
        }
        
        summary_file = RESULTS_STRUCTURE["reports"] / f"technical_specs_pro_summary_{self.timestamp}.json"
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
                    "percentage_of_all_matches": (count / self.spec_count * 100) if self.spec_count > 0 else 0
                }
                for group, count in self.pattern_counts.items() if count > 0
            }
        }
        
        pattern_report_file = RESULTS_STRUCTURE["patterns"] / f"pattern_performance_{self.timestamp}.json"
        with open(pattern_report_file, 'w', encoding='utf-8') as f:
            json.dump(pattern_report, f, ensure_ascii=False, indent=2)
        
        # 3. Skapa validerings- och rimlighetskontrollrapport
        validation_report = {
            "timestamp": self.timestamp,
            "validation_summary": self.validation_stats,
            "validation_per_category": {
                category: {
                    "valid": sum(1 for spec in specs if spec.get("is_valid", False)),
                    "invalid": sum(1 for spec in specs if not spec.get("is_valid", True)),
                    "validation_issues": [
                        {
                            "product_id": spec.get("product_id", "unknown"),
                            "name": spec.get("name", "unknown"),
                            "raw_value": spec.get("raw_value", ""),
                            "validation_message": spec.get("validation_message", "")
                        }
                        for spec in specs if not spec.get("is_valid", True)
                    ][:20]  # Visa bara de 20 första problemen
                }
                for category, specs in self.spec_categories.items()
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
            specs_file=specs_file,
            no_specs_file=no_specs_file,
            samples_file=samples_file,
            discovered_file=discovered_file,
            suggested_patterns=suggested_patterns,
            summary_file=summary_file,
            pattern_report_file=pattern_report_file,
            validation_report_file=validation_report_file
        )
  
  
    
    def generate_markdown_report(self, total_files: int, summary: Dict, pattern_report: Dict,
                            validation_report: Dict, specs_file: Path, no_specs_file: Path, 
                            samples_file: Path, discovered_file: Path, suggested_patterns: List,
                            summary_file: Path, pattern_report_file: Path, validation_report_file: Path) -> None:
        """Generera en detaljerad markdown-rapport med alla resultat och analyser"""
        
        report_file = RESULTS_STRUCTURE["reports"] / f"technical_specs_pro_report_{self.timestamp}.md"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            # Huvudrubrik och inledning
            f.write(f"# Detaljerad Teknisk Specifikationsrapport\n\n")
            f.write(f"**Datum och tid:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"Denna rapport innehåller en detaljerad analys av tekniska specifikationer extraherade från _pro-dokument.\n\n")
            
            # Innehållsförteckning
            f.write("## Innehåll\n\n")
            f.write("1. [Sammanfattning](#sammanfattning)\n")
            f.write("2. [Kategorifördelning](#kategorifördelning)\n")
            f.write("3. [Mönsterprestanda](#mönsterprestanda)\n")
            f.write("   - [Toppresterande mönster](#toppresterande-mönster)\n")
            f.write("   - [Bottenprestanda mönster](#bottenprestanda-mönster)\n")
            f.write("   - [Mönstergruppernas prestanda](#mönstergruppernas-prestanda)\n")
            f.write("4. [Validering och datakvalitet](#validering-och-datakvalitet)\n")
            f.write("5. [Upptäckta specifikationer och mönsterförslag](#upptäckta-specifikationer-och-mönsterförslag)\n")
            f.write("6. [Dokument och filer](#dokument-och-filer)\n")
            f.write("7. [Nästa steg](#nästa-steg)\n\n")
            
            # Övergripande sammanfattning
            f.write("## Sammanfattning\n\n")
            f.write(f"- **Totalt antal _pro-filer:** {total_files}\n")
            f.write(f"- **Filer med tekniska specifikationer:** {self.documents_with_specs} ({summary['specs_coverage_percentage']:.1f}%)\n")
            f.write(f"- **Filer utan tekniska specifikationer:** {self.documents_without_specs}\n")
            f.write(f"- **Totalt antal extraherade specifikationer:** {self.spec_count}\n")
            f.write(f"- **Genomsnittligt antal specifikationer per dokument:** {summary['average_specs_per_document']:.1f}\n")
            f.write(f"- **Antal upptäckta potentiella nya specifikationer:** {summary['discovered_specs_count']}\n")
            f.write(f"- **Antal föreslagna nya mönster:** {summary['suggested_patterns_count']}\n")
            f.write(f"- **Valideringsstatus:** {self.validation_stats['valid']} giltiga, {self.validation_stats['invalid']} ogiltiga\n\n")
            
            # Kategorifördelning
            f.write("## Kategorifördelning\n\n")
            f.write("Nedan visas fördelningen av tekniska specifikationer per kategori:\n\n")
            f.write("| Teknisk kategori | Antal specifikationer | Procentandel |\n")
            f.write("|-----------------|----------------------|---------------|\n")
            
            # Sortera efter antal specifikationer
            for category, count in sorted(self.category_counts.items(), key=lambda x: x[1], reverse=True):
                percentage = (count / self.spec_count * 100) if self.spec_count > 0 else 0
                f.write(f"| {category} | {count} | {percentage:.1f}% |\n")
            
            # Mönsterprestanda
            f.write("\n## Mönsterprestanda\n\n")
            f.write(f"Totalt används {len(ALL_PATTERNS)} mönster för extraktion, varav {len(self.individual_pattern_counts)} gav träffar.\n\n")
            
            # Toppresterande mönster
            f.write("### Toppresterande mönster\n\n")
            f.write("De mönster som gav flest träffar:\n\n")
            f.write("| Mönsterindex | Grupp | Antal träffar | Procentandel | Mönster |\n")
            f.write("|--------------|-------|--------------|--------------|--------|\n")
            
            for idx, count in sorted(self.top_performing_patterns.items(), key=lambda x: x[1], reverse=True):
                percentage = (count / self.spec_count * 100) if self.spec_count > 0 else 0
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
                percentage = (count / self.spec_count * 100) if self.spec_count > 0 else 0
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
                    percentage = (count / self.spec_count * 100) if self.spec_count > 0 else 0
                    f.write(f"| {group} | {count} | {percentage:.1f}% |\n")
            
            # Validering och datakvalitet
            f.write("\n## Validering och datakvalitet\n\n")
            f.write(f"Av totalt {self.spec_count} extraherade specifikationer är {self.validation_stats['valid']} ({self.validation_stats['valid']/self.spec_count*100:.1f}%) validerade som giltiga.\n\n")
            
            f.write("### Valideringsresultat per kategori\n\n")
            f.write("| Kategori | Antal valida | Antal ogiltiga | Valideringsfrekvens |\n")
            f.write("|----------|--------------|----------------|-----------------------|\n")
            
            for category, stats in validation_report.get("validation_per_category", {}).items():
                valid = stats.get("valid", 0)
                invalid = stats.get("invalid", 0)
                total = valid + invalid
                validation_rate = (valid / total * 100) if total > 0 else 0
                f.write(f"| {category} | {valid} | {invalid} | {validation_rate:.1f}% |\n")
            
            f.write("\n### Vanliga valideringsfel\n\n")
            
            all_issues = []
            for category, stats in validation_report.get("validation_per_category", {}).items():
                for issue in stats.get("validation_issues", []):
                    issue["category"] = category
                    all_issues.append(issue)
                    
            if all_issues:
                f.write("| Kategori | Specifikation | Värde | Felmeddelande |\n")
                f.write("|----------|---------------|-------|---------------|\n")
                
                for issue in all_issues[:20]:  # Visa bara de 20 första problemen
                    category = issue.get("category", "unknown")
                    name = issue.get("name", "unknown")
                    value = issue.get("raw_value", "")
                    message = issue.get("validation_message", "")
                    f.write(f"| {category} | {name} | {value} | {message} |\n")
            else:
                f.write("Inga validieringsfel hittades.\n\n")
            
            # Upptäckta specifikationer och mönsterförslag
            f.write("\n## Upptäckta specifikationer och mönsterförslag\n\n")
            
            if suggested_patterns:
                f.write(f"Baserat på analys av dokument och frekventa specifikationer, föreslås följande {len(suggested_patterns)} nya mönster:\n\n")
                f.write("| Specifikationsnamn | Föreslagen kategori | Föreslagen regex | Förekomster |\n")
                f.write("|---------------------|----------------------|-----------------|-------------|\n")
                
                for suggestion in suggested_patterns[:20]:  # Visa bara de 20 första förslagen
                    f.write(f"| {suggestion['name']} | {suggestion['category']} | `{suggestion['suggested_pattern']}` | {suggestion['occurrences']} |\n")
                
                if len(suggested_patterns) > 20:
                    f.write(f"\n*...och {len(suggested_patterns) - 20} ytterligare förslag. Se JSON-filen för fullständig lista.*\n")
                    
                f.write("\nSe den fullständiga listan i JSON-filen för föreslagna mönster.\n\n")
            else:
                f.write("Inga nya mönsterförslag genererades i denna körning.\n\n")
            
            # Dokument och filer
            f.write("## Dokument och filer\n\n")
            f.write("### Resultatfiler\n\n")
            f.write(f"- **Extraherade tekniska specifikationer:** [{specs_file.name}]({specs_file})\n")
            f.write(f"- **Dokument utan specifikationer:** [{no_specs_file.name}]({no_specs_file})\n")
            f.write(f"- **Exempel på dokument utan specifikationer:** [{samples_file.name}]({samples_file})\n")
            f.write(f"- **Upptäckta potentiella specifikationer:** [{discovered_file.name}]({discovered_file})\n")
            f.write(f"- **Mönsterprestanda (JSON):** [{pattern_report_file.name}]({pattern_report_file})\n")
            f.write(f"- **Validering (JSON):** [{validation_report_file.name}]({validation_report_file})\n")
            f.write(f"- **Sammanfattning (JSON):** [{summary_file.name}]({summary_file})\n\n")
            
            # Kategorispecifika filer
            category_files = []
            for category_dir in (RESULTS_STRUCTURE["categories"]).glob("*"):
                if category_dir.is_dir():
                    for cat_file in category_dir.glob(f"*_{self.timestamp}.jsonl"):
                        category_files.append((category_dir.name, cat_file))
            
            if category_files:
                f.write("### Kategorispecifika filer\n\n")
                for category, cat_file in sorted(category_files):
                    f.write(f"- **{category}:** [{cat_file.name}]({cat_file})\n")
            
            # Nästa steg
            f.write("\n## Nästa steg\n\n")
            f.write("Baserat på denna analys rekommenderas följande åtgärder:\n\n")
            f.write("1. **Granska upptäckta specifikationer** för att identifiera nya mönster och förbättra befintliga\n")
            f.write("2. **Implementera föreslagna mönster** och jämför resultaten i nästa körning\n")
            f.write("3. **Förfina valideringslogiken** för att öka antalet korrekt validerade specifikationer\n")
            f.write("4. **Utveckla specifika extraktorer för andra dokumenttyper** (_TEK, _produktblad, etc.)\n")
            f.write("5. **Expandera kategorierna** med mer detaljerade underkategorier vid behov\n")
            f.write("6. **Verifiera och förbättra rimlighetskontroller** för numeriska värden\n")
            f.write("7. **Utveckla statistiska normalintervall** för vanliga tekniska värden som baseras på extraherad data\n\n")
            
            f.write("---\n\n")
            f.write(f"Rapport genererad: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        logger.info(f"Genererade detaljerad teknisk specifikationsrapport: {report_file}")


def main():
    """Huvudfunktion för teknisk specifikationsextraktor"""
    start_time = datetime.now()
    logger.info(f"Startar teknisk specifikationsextraktion från _pro-dokument: {start_time}")
    
    # Skapa och kör extraktorn
    extractor = EnhancedTechnicalExtractorPro(BASE_DIR, OUTPUT_DIR)
    extractor.process_documents()
    
    end_time = datetime.now()
    duration = end_time - start_time
    logger.info(f"Extraktion slutförd på {duration.total_seconds():.1f} sekunder")


if __name__ == "__main__":
    main()


