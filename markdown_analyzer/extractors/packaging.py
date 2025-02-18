# markdown_analyzer/extractors/packaging.py

from typing import List
from .base import BaseExtractor
from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class PackagingInfo:
    """Information om förpackning och logistik"""
    package_type: str
    ean: Optional[str]
    dimensions: Dict[str, float]
    weight_gross: Optional[float]
    weight_net: Optional[float]
    units_per_package: int
    volume: Optional[float]

class PackagingExtractor(BaseExtractor):
    """Extraherar förpackningsinformation"""
    
    def extract(self, content: str, tables: List[Dict]) -> List[PackagingInfo]:
        packaging_info = []
        
        for table in tables:
            if 'Packaging information' in table.context:
                headers = [h.lower() for h in table.headers]
                for row in table.rows:
                    if len(row) >= len(headers):
                        try:
                            info = self._create_packaging_info(row, headers)
                            if info:
                                packaging_info.append(info)
                        except (ValueError, IndexError) as e:
                            self.logger.warning(f"Kunde inte extrahera förpackningsinfo: {str(e)}")
        
        return packaging_info
    
    def _create_packaging_info(self, row: List[str], headers: List[str]) -> Optional[PackagingInfo]:
        """Skapar ett PackagingInfo-objekt från en tabellrad"""
        try:
            return PackagingInfo(
                package_type=row[headers.index('package_type')],
                ean=row[headers.index('ean')] if 'ean' in headers else None,
                dimensions={
                    'length': float(row[headers.index('längd')]),
                    'height': float(row[headers.index('höjd')]),
                    'width': float(row[headers.index('bredd')])
                },
                weight_gross=float(row[headers.index('bruttovikt')]),
                weight_net=float(row[headers.index('net weight')]) if 'net weight' in headers else None,
                units_per_package=int(row[headers.index('antal st')]),
                volume=float(row[headers.index('volym')]) if 'volym' in headers else None
            )
        except (ValueError, IndexError) as e:
            self.logger.debug(f"Kunde inte skapa förpackningsinfo: {str(e)}")
            return None