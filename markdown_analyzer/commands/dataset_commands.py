import click
import logging
from pathlib import Path
from typing import List, Optional, Dict

from .base import BaseCommand
from ..dataset.generator import DatasetGenerator
from ..dataset.validators import DatasetValidator
from ..dataset.exporters import MultiFormatExporter, DatasetExporter

class DatasetGenerateCommand(BaseCommand):
    """Command for generating training datasets"""
    
    def __init__(self, input_dirs: List[str], output_dir: str, max_length: int):
        super().__init__()
        self.input_dirs = input_dirs
        self.output_dir = output_dir
        self.max_length = max_length
        self.generator = DatasetGenerator(list(input_dirs), output_dir)
        self.validator = DatasetValidator(max_length=max_length)
        self.exporter = MultiFormatExporter(output_dir, self.validator)

    def process(self, commands: List[str], workers: int = 4) -> Dict:
        """Process the dataset generation"""
        # Generate dataset
        self.generator.generate_dataset(num_workers=workers)
        
        results = {}
        # Export for each command
        for cmd in commands:
            samples = self.generator.get_samples_for_command(cmd)
            if samples:
                result = self.exporter.export_dataset(
                    samples,
                    f'training_data_{cmd}'
                )
                results[cmd] = result
        
        return results

class DatasetValidateCommand(BaseCommand):
    """Command for validating training datasets"""
    
    def __init__(self, max_length: int):
        super().__init__()
        self.validator = DatasetValidator(max_length=max_length)

    def process(self, input_file: str) -> Dict:
        """Process the dataset validation"""
        path = Path(input_file)
        samples = self._read_samples(path)
        
        return self.validator.validate_training_samples(samples)

    def _read_samples(self, path: Path) -> List[Dict]:
        """Read samples from file"""
        if path.suffix == '.json':
            import json
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        elif path.suffix == '.csv':
            import csv
            samples = []
            with open(path, 'r', encoding='utf-8', newline='') as f:
                reader = csv.DictReader(f)
                samples.extend(reader)
            return samples
        else:
            raise ValueError("File format must be .json or .csv")

class DatasetConvertCommand(BaseCommand):
    """Command for converting between dataset formats"""
    
    def __init__(self, output_dir: str):
        super().__init__()
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.exporter = DatasetExporter(self.output_dir)

    def process(self, input_file: str, format: str = 'both') -> Dict:
        """Process the dataset conversion"""
        path = Path(input_file)
        samples = self._read_samples(path)
        
        results = {'files': []}
        
        if format in ['json', 'both'] and path.suffix != '.json':
            json_path = self.exporter.export_to_json(samples, path.stem)
            results['files'].append(('json', json_path))
            
        if format in ['csv', 'both'] and path.suffix != '.csv':
            csv_paths = self.exporter.export_to_csv(samples, path.stem)
            for csv_path in csv_paths:
                results['files'].append(('csv', csv_path))
        
        return results

    def _read_samples(self, path: Path) -> List[Dict]:
        """Read samples from file"""
        if path.suffix == '.json':
            import json
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        elif path.suffix == '.csv':
            import csv
            samples = []
            with open(path, 'r', encoding='utf-8', newline='') as f:
                reader = csv.DictReader(f)
                samples.extend(reader)
            return samples
        else:
            raise ValueError("File format must be .json or .csv")

# CLI interface
class DatasetCommands:
    """CLI command handler for dataset operations"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    @click.group()
    def dataset():
        """Commands for handling training data"""
        pass

    @dataset.command()
    @click.option('--input-dirs', '-i', multiple=True,
                 help='Input directories to scan for markdown files')
    @click.option('--output-dir', '-o', default='./output',
                 help='Directory for output files')
    @click.option('--commands', '-c', multiple=True,
                 default=['f', 's', 't', 'c'],
                 help='Commands to generate training data for')
    @click.option('--workers', '-w', default=4,
                 help='Number of parallel workers')
    @click.option('--max-length', '-m', default=131072,
                 help='Maximum length for output text')
    def generate(input_dirs: List[str], output_dir: str, 
                commands: List[str], workers: int, max_length: int):
        """Generate training data from markdown files"""
        try:
            command = DatasetGenerateCommand(input_dirs, output_dir, max_length)
            results = command.process(commands, workers)
            
            for cmd, result in results.items():
                print(f"\nExport of data for command '{cmd}':")
                print(f"  Number of examples: {result['stats']['total_samples']}")
                print(f"  JSON: {result['files']['json']}")
                print(f"  CSV: {len(result['files']['csv'])} files")
                
                if result['validation'].warnings:
                    print("\nWarnings:")
                    for warning in result['validation'].warnings:
                        print(f"  - {warning}")
                        
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            raise click.Abort()

    @dataset.command()
    @click.argument('input_file')
    @click.option('--max-length', '-m', default=131072,
                 help='Maximum length for output text')
    def validate(input_file: str, max_length: int):
        """Validate an existing training data file"""
        try:
            command = DatasetValidateCommand(max_length)
            result = command.process(input_file)
            
            print("\nValidation Result:")
            print(f"  Number of examples: {result.stats['total_samples']}")
            print(f"  Large outputs: {result.stats['large_outputs']}")
            print(f"  Empty inputs: {result.stats['empty_inputs']}")
            print(f"  Empty outputs: {result.stats['empty_outputs']}")
            
            if result.errors:
                print("\nErrors:")
                for error in result.errors:
                    print(f"  - {error}")
            
            if result.warnings:
                print("\nWarnings:")
                for warning in result.warnings:
                    print(f"  - {warning}")
                    
            if not (result.errors or result.warnings):
                print("\nNo issues found!")
                
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            raise click.Abort()

    @dataset.command()
    @click.argument('input_file')
    @click.option('--output-dir', '-o', default='./output',
                 help='Directory for output files')
    @click.option('--format', '-f',
                 type=click.Choice(['json', 'csv', 'both']),
                 default='both',
                 help='Output format')
    def convert(input_file: str, output_dir: str, format: str):
        """Convert between JSON and CSV formats"""
        try:
            command = DatasetConvertCommand(output_dir)
            results = command.process(input_file, format)
            
            for fmt, path in results['files']:
                if fmt == 'json':
                    print(f"\nExported JSON: {path}")
                else:
                    print(f"\nExported CSV: {path}")
                    
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            raise click.Abort()