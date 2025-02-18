# markdown_analyzer/extractors/technical/units.py
from typing import Dict

# Local imports
from .models import TechnicalUnit, UnitCategory


UNIT_DEFINITIONS: Dict[str, TechnicalUnit] = {
    # Längd
    "mm": TechnicalUnit("millimeter", UnitCategory.LENGTH, base_unit=True),
    "cm": TechnicalUnit("centimeter", UnitCategory.LENGTH, conversion_factor=10),
    "m": TechnicalUnit("meter", UnitCategory.LENGTH, conversion_factor=1000),
    
    # Spänning
    "V": TechnicalUnit("volt", UnitCategory.VOLTAGE, base_unit=True),
    "kV": TechnicalUnit("kilovolt", UnitCategory.VOLTAGE, conversion_factor=1000),
    "mV": TechnicalUnit("millivolt", UnitCategory.VOLTAGE, conversion_factor=0.001),
    
    # Ström
    "A": TechnicalUnit("ampere", UnitCategory.CURRENT, base_unit=True),
    "mA": TechnicalUnit("milliampere", UnitCategory.CURRENT, conversion_factor=0.001),
    
    # Effekt
    "W": TechnicalUnit("watt", UnitCategory.POWER, base_unit=True),
    "kW": TechnicalUnit("kilowatt", UnitCategory.POWER, conversion_factor=1000),
    
    # Temperatur
    "C": TechnicalUnit("Celsius", UnitCategory.TEMPERATURE, base_unit=True),
    "F": TechnicalUnit("Fahrenheit", UnitCategory.TEMPERATURE, 
                      conversion_factor=1.8, conversion_offset=32),
    
    # Frekvens
    "Hz": TechnicalUnit("hertz", UnitCategory.FREQUENCY, base_unit=True),
    "kHz": TechnicalUnit("kilohertz", UnitCategory.FREQUENCY, conversion_factor=1000),
    "MHz": TechnicalUnit("megahertz", UnitCategory.FREQUENCY, conversion_factor=1000000),
}