
# markdown_analyzer/extractors/technical/models.py
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum


class UnitCategory(Enum):
    LENGTH = "length"
    VOLTAGE = "voltage"
    CURRENT = "current"
    POWER = "power"
    TEMPERATURE = "temperature"
    PRESSURE = "pressure"
    FREQUENCY = "frequency"
    WEIGHT = "weight"

class TechnicalCategory(Enum):
    DIMENSIONS = "dimensions"
    ELECTRICAL = "electrical"
    MECHANICAL = "mechanical"
    ENVIRONMENTAL = "environmental"
    PERFORMANCE = "performance"
    CONNECTIVITY = "connectivity"
    CERTIFICATION = "certification"
    INSTALLATION = "installation"
    WEIGHT = "weight"         # NY MEDLEM
    TEMPERATURE = "temperature"  # NY MEDLEM

