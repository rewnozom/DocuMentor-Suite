# markdown_analyzer/extractors/technical/technical_extractor.py

import re
from typing import List, Dict, Optional

from ...core.enums import TechnicalCategory, UnitCategory
from ...extractors.technical.models import TechnicalSpecification, TechnicalUnit, TechnicalValue




from .patterns import TECHNICAL_PATTERNS, IMPORTANCE_INDICATORS
from .units import UNIT_DEFINITIONS
from ..base import BaseExtractor
from ...core.constants import TECHNICAL_TABLE_HEADERS

class TechnicalExtractor(BaseExtractor):
    """Extraherar teknisk information"""

    def extract(self, content: str, tables: List[Dict]) -> List[TechnicalSpecification]:
        specs = []
        # Först: explicit extraction (t.ex. Voltage, Dimensions, Weight)
        specs.extend(self._extract_explicit_from_text(content))
        # Sedan: generisk extraction via definierade mönster
        specs.extend(self._extract_generic_from_text(content))
        # Extrahera från tabeller
        specs.extend(self._extract_from_tables(tables))
        return specs

    def _extract_explicit_from_text(self, content: str) -> List[TechnicalSpecification]:
        """Extraherar specifika tekniska värden med explicita regexar."""
        specs = []
        # Extrahera Voltage
        m = re.search(r'Voltage:\s*(\d+(?:\.\d+)?)(V)', content, re.IGNORECASE)
        if m:
            try:
                value = float(m.group(1))
            except ValueError:
                value = 0.0
            tech_value = TechnicalValue(
                value=value,
                unit=UNIT_DEFINITIONS.get(m.group(2))
            )
            specs.append(TechnicalSpecification(
                category="electrical",
                name="Voltage",
                value=tech_value,
                source_text=m.group(0),
                importance=0.9
            ))
        # Extrahera Dimensions
        m = re.search(r'Dimensions:\s*([\dx]+)\s*(mm)', content, re.IGNORECASE)
        if m:
            # Istället för att konvertera till ett numeriskt värde, bevara den ursprungliga strängen
            dim_str = m.group(1).strip()  # ex "100x200x300"
            tech_value = TechnicalValue(
                value=dim_str,  # lagrar dimensionssträngen
                unit=UNIT_DEFINITIONS.get(m.group(2))
            )
            specs.append(TechnicalSpecification(
                category="dimensions",
                name="Dimensions",
                value=tech_value,
                source_text=m.group(0),
                importance=0.95
            ))
        # Extrahera Weight
        m = re.search(r'Weight:\s*(\d+)(kg)', content, re.IGNORECASE)
        if m:
            try:
                numeric_value = float(m.group(1))
            except ValueError:
                numeric_value = 0.0
            tech_value = TechnicalValue(
                value=numeric_value,
                unit="kg"  # Här används enhet direkt
            )
            specs.append(TechnicalSpecification(
                category="weight",
                name="Weight",
                value=tech_value,
                source_text=m.group(0),
                importance=0.9
            ))
        return specs

    def _extract_generic_from_text(self, content: str) -> List[TechnicalSpecification]:
        """Extraherar tekniska specifikationer från text med hjälp av TECHNICAL_PATTERNS."""
        specs = []
        for category, patterns in TECHNICAL_PATTERNS.items():
            for pattern in patterns:
                for match in re.finditer(pattern, content):
                    value_str = match.group(1)
                    unit_match = re.search(r'(?i)(mm|cm|m|V|A|W|kg|g)', match.group(0))
                    if unit_match and unit_match.group(1) in UNIT_DEFINITIONS:
                        unit = UNIT_DEFINITIONS[unit_match.group(1)]
                        # Om värdet innehåller "x" (dimensioner), bevara som sträng
                        if "x" in value_str.lower():
                            numeric_value = value_str
                        else:
                            try:
                                numeric_value = float(value_str)
                            except ValueError:
                                numeric_value = 0.0
                        tech_value = TechnicalValue(
                            value=numeric_value,
                            unit=unit
                        )
                        specs.append(TechnicalSpecification(
                            category=category,
                            name=self._determine_spec_name(category, unit),
                            value=tech_value,
                            source_text=match.group(0),
                            importance=self._calculate_importance(match.group(0))
                        ))
        return specs

    def _extract_from_tables(self, tables: List[Dict]) -> List[TechnicalSpecification]:
        """Extraherar tekniska specifikationer från tabeller."""
        specs = []
        for table in tables:
            if any(tech_word in " ".join(table.get('headers', [])).lower() 
                   for tech_word in TECHNICAL_TABLE_HEADERS):
                for row in table.get('rows', []):
                    if len(row) >= 2:
                        key = row[0].strip().lower()
                        value_str = row[1].strip()
                        category = self._determine_category(key)
                        if category:
                            unit_match = re.search(r'(?i)(mm|cm|m|V|A|W|kg|g)$', value_str)
                            if unit_match and unit_match.group(1) in UNIT_DEFINITIONS:
                                unit = UNIT_DEFINITIONS[unit_match.group(1)]
                                # För dimensioner, bevara som sträng om det innehåller 'x'
                                if "x" in value_str.lower():
                                    numeric_value = value_str
                                else:
                                    numeric_value = float(re.sub(r'[^\d.]', '', value_str))
                                tech_value = TechnicalValue(
                                    value=numeric_value,
                                    unit=unit
                                )
                                specs.append(TechnicalSpecification(
                                    category=category,
                                    name=key,
                                    value=tech_value,
                                    source_text=f"{key}: {value_str}",
                                    importance=1.1  # Högre vikt för tabelldata
                                ))
        return specs

    def _determine_category(self, key: str) -> Optional[str]:
        """Bestämmer den tekniska kategorin baserat på nyckeln.
        Returnerar en sträng, t.ex. "electrical", "dimensions", "mechanical", "environmental".
        """
        key = key.lower()
        if any(dim in key for dim in ["mått", "dimension", "höjd", "bredd", "djup"]):
            return "dimensions"
        elif any(elec in key for elec in ["spänning", "voltage", "ström", "effekt"]):
            return "electrical"
        elif any(mech in key for mech in ["moment", "kraft"]):
            return "mechanical"
        elif any(env in key for env in ["temperatur", "fukt"]):
            return "environmental"
        return None

    def _determine_spec_name(self, category: str, unit: TechnicalUnit) -> str:
        """Bestämmer ett läsbart namn för specifikationen baserat på kategori och enhet."""
        if category == "dimensions":
            return f"Dimension ({unit.name})"
        elif category == "electrical":
            return f"Elektrisk ({unit.name})"
        return f"{category} ({unit.name})"

    def _calculate_importance(self, text: str) -> float:
        """Beräknar importance baserat på textinnehållet."""
        importance = 1.0
        for pattern in IMPORTANCE_INDICATORS.get('high', []):
            if re.search(pattern, text, re.IGNORECASE):
                importance *= 1.3
                break
        for pattern in IMPORTANCE_INDICATORS.get('medium', []):
            if re.search(pattern, text, re.IGNORECASE):
                importance *= 1.1
                break
        return importance
