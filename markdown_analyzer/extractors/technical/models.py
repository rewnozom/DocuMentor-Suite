from dataclasses import dataclass, field
from typing import Optional, Union, Dict, Any, List

from ...core.enums import TechnicalCategory, UnitCategory

@dataclass
class TechnicalUnit:
    """Teknisk enhet med konverteringsinformation."""
    name: str
    category: UnitCategory
    base_unit: bool = False
    conversion_factor: float = 1.0
    conversion_offset: float = 0.0

@dataclass
class TechnicalRange:
    """Omfång för tekniska värden med enheter."""
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    typical_value: Optional[float] = None
    unit: Optional[TechnicalUnit] = None
    tolerance: Optional[float] = None
    confidence: float = 1.0

    def __post_init__(self):
        if self.min_value is not None and self.max_value is not None:
            if self.min_value > self.max_value:
                raise ValueError("min_value cannot be greater than max_value")
        if self.typical_value is not None:
            if (self.min_value is not None and self.typical_value < self.min_value) or \
               (self.max_value is not None and self.typical_value > self.max_value):
                raise ValueError("typical_value must be within min_value and max_value range")

@dataclass
class TechnicalValue:
    """Utökat tekniskt värde med extra metadata."""
    value: Union[float, str, TechnicalRange]
    unit: TechnicalUnit
    precision: int = 2
    confidence: float = 1.0
    source: Optional[str] = None
    notes: List[str] = field(default_factory=list)
    validation_rules: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        # Om värdet är numeriskt (int eller float) konverteras det till float
        if isinstance(self.value, (int, float)):
            self.value = float(self.value)

    def format_value(self) -> str:
        """Formatera det tekniska värdet som en sträng."""
        if isinstance(self.value, TechnicalRange):
            if self.value.typical_value is not None:
                base = f"{self.value.typical_value:.{self.precision}f}"
                if self.value.tolerance is not None:
                    return f"{base} ±{self.value.tolerance:.{self.precision}f} {self.unit.name}"
                return f"{base} {self.unit.name} (typiskt)"
            elif self.value.min_value is not None and self.value.max_value is not None:
                return f"{self.value.min_value:.{self.precision}f} - {self.value.max_value:.{self.precision}f} {self.unit.name}"
        elif isinstance(self.value, float):
            return f"{self.value:.{self.precision}f} {self.unit.name}"
        return f"{self.value} {self.unit.name}"

    def validate(self) -> List[str]:
        """Validera det tekniska värdet baserat på angivna regler."""
        errors = []
        if 'allowed_range' in self.validation_rules:
            min_val, max_val = self.validation_rules['allowed_range']
            if isinstance(self.value, float):
                if not (min_val <= self.value <= max_val):
                    errors.append(f"Value {self.value} outside allowed range [{min_val}, {max_val}]")
        if 'max_precision' in self.validation_rules:
            if self.precision > self.validation_rules['max_precision']:
                errors.append(f"Precision {self.precision} exceeds maximum allowed {self.validation_rules['max_precision']}")
        if 'allowed_units' in self.validation_rules:
            if self.unit.name not in self.validation_rules['allowed_units']:
                errors.append(f"Unit {self.unit.name} not in allowed units: {self.validation_rules['allowed_units']}")
        return errors

    def convert_to(self, target_unit: TechnicalUnit) -> 'TechnicalValue':
        """Konvertera värdet till en annan enhet."""
        if target_unit.category != self.unit.category:
            raise ValueError(f"Cannot convert between different unit categories: {self.unit.category} and {target_unit.category}")
        if isinstance(self.value, float):
            base_value = self.value * self.unit.conversion_factor
            new_value = base_value / target_unit.conversion_factor
            return TechnicalValue(
                value=new_value,
                unit=target_unit,
                precision=self.precision,
                confidence=self.confidence,
                source=self.source,
                notes=self.notes.copy(),
                validation_rules=self.validation_rules.copy()
            )
        elif isinstance(self.value, TechnicalRange):
            new_range = TechnicalRange(
                min_value=self.value.min_value * self.unit.conversion_factor / target_unit.conversion_factor if self.value.min_value is not None else None,
                max_value=self.value.max_value * self.unit.conversion_factor / target_unit.conversion_factor if self.value.max_value is not None else None,
                typical_value=self.value.typical_value * self.unit.conversion_factor / target_unit.conversion_factor if self.value.typical_value is not None else None,
                unit=target_unit,
                tolerance=self.value.tolerance * self.unit.conversion_factor / target_unit.conversion_factor if self.value.tolerance is not None else None,
                confidence=self.value.confidence
            )
            return TechnicalValue(
                value=new_range,
                unit=target_unit,
                precision=self.precision,
                confidence=self.confidence,
                source=self.source,
                notes=self.notes.copy(),
                validation_rules=self.validation_rules.copy()
            )
        else:
            raise ValueError(f"Cannot convert non-numeric value: {self.value}")

@dataclass
class TechnicalSpecification:
    """En teknisk specifikation."""
    category: TechnicalCategory
    name: str
    value: TechnicalValue
    description: Optional[str] = None
    importance: float = 1.0  # För sammanfattningar
    source_text: Optional[str] = None
    notes: List[str] = field(default_factory=list)
