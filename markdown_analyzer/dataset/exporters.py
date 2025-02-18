# ..\..\markdown_analyzer\dataset\exporters.py
# markdown_analyzer/dataset/exporters.py
import csv
import json
from pathlib import Path
from typing import List, Dict, Optional
import logging
from tqdm import tqdm

from ..dataset.validators import DatasetValidator

class DatasetExporter:
    """
    Hanterar export av träningsdata till olika format.
    """
    
    def __init__(self, output_dir: str, max_rows_per_file: int = 1000):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)  # Ensure directory exists
        self.max_rows_per_file = max_rows_per_file
        self.logger = logging.getLogger(__name__)

    def export_to_json(self, samples: List[Dict], filename: str) -> str:
        """
        Exporterar träningsdata till JSON-format.
        """
        output_path = self.output_dir / f"{filename}.json"
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(samples, f, ensure_ascii=False, indent=2)
        self.logger.info(f"Exporterade {len(samples)} exempel till {output_path}")
        return str(output_path)

    def export_to_csv(self, samples: List[Dict], base_filename: str) -> List[str]:
        """
        Exporterar träningsdata till CSV-format, uppdelat i flera filer vid behov.
        """
        output_files = []
        total_samples = len(samples)
        num_files = (total_samples + self.max_rows_per_file - 1) // self.max_rows_per_file

        for i in range(num_files):
            start_idx = i * self.max_rows_per_file
            end_idx = min((i + 1) * self.max_rows_per_file, total_samples)
            chunk = samples[start_idx:end_idx]
            
            filename = f"{base_filename}_{i:02d}.csv"
            output_path = self.output_dir / filename
            
            self._write_csv_chunk(chunk, output_path)
            output_files.append(str(output_path))
            self.logger.info(f"Exporterade {len(chunk)} exempel till {output_path}")

        return output_files

    def _write_csv_chunk(self, chunk: List[Dict], output_path: Path) -> None:
        """Skriver en del av datasetet till CSV.
        
        Endast exempel som innehåller både 'user_input' och 'ai_output' skrivs ut.
        """
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['user_input', 'ai_output']
            writer = csv.DictWriter(
                csvfile, 
                fieldnames=fieldnames,
                escapechar='\\',
                quoting=csv.QUOTE_MINIMAL
            )
            writer.writeheader()
            for sample in chunk:
                if 'user_input' in sample and 'ai_output' in sample:
                    writer.writerow({
                        'user_input': sample['user_input'],
                        'ai_output': sample['ai_output']
                    })
                else:
                    self.logger.warning(f"Hoppar över ogiltigt exempel: {sample}")

class MultiFormatExporter:
    """
    Hanterar export till flera format samtidigt och validerar resultaten.
    """
    
    def __init__(self, output_dir: str, validator: DatasetValidator):
        self.exporter = DatasetExporter(output_dir)
        self.validator = validator
        self.logger = logging.getLogger(__name__)

    def export_dataset(self, samples: List[Dict], base_filename: str) -> Dict:
        """
        Exporterar dataset till både JSON och CSV format.
        
        Returns:
            Dict med information om exporterade filer och valideringsresultat.
        """
        # Validera först
        validation = self.validator.validate_training_samples(samples)
        if not validation.is_valid:
            self.logger.warning("Validering visade problem i datasetet:")
            for error in validation.errors:
                self.logger.warning(f"  - {error}")

        result = {
            'validation': validation,
            'files': {
                'json': self.exporter.export_to_json(samples, base_filename),
                'csv': self.exporter.export_to_csv(samples, base_filename)
            },
            'stats': {
                'total_samples': len(samples),
                'formats_exported': ['json', 'csv']
            }
        }

        self._log_export_results(result)
        return result

    def _log_export_results(self, result: Dict) -> None:
        """Loggar information om exporten"""
        self.logger.info("=== Export Slutförd ===")
        self.logger.info(f"Totalt antal exempel: {result['stats']['total_samples']}")
        
        if result['validation'].warnings:
            self.logger.warning("Varningar under validering:")
            for warning in result['validation'].warnings:
                self.logger.warning(f"  - {warning}")
        
        self.logger.info("Exporterade filer:")
        for format_name, filepath in result['files'].items():
            if isinstance(filepath, list):
                self.logger.info(f"  {format_name.upper()}: {len(filepath)} filer")
                for f in filepath:
                    self.logger.info(f"    - {f}")
            else:
                self.logger.info(f"  {format_name.upper()}: {filepath}")
