# markdown_analyzer/core/training_data.py

import re
import json
import csv
from pathlib import Path
from typing import List, Dict, Optional, Tuple, Union

import pandas as pd
from pydantic import BaseModel, validator

from ..config import Settings
from ..validators import TrainingDataValidator
from ..core.document import DocumentStructure


class TrainingDataProcessor:
    """
    Processar och validerar träningsdata innan export.
    
    Denna klass erbjuder:
      - Skapande av träningsexempel från ett DocumentStructure (create_training_examples)
      - Processering och validering av exempel (process_examples)
      - Hjälpmetoder för normalisering av input/output samt formatering av text
    """
    
    def __init__(self):
        self.validator = TrainingDataValidator()
    
    def create_training_examples(self, doc: DocumentStructure) -> List[Dict]:
        """
        Skapar träningsdataexempel från ett dokument.
        
        Exempel genereras för:
          - Fullständig information (kommando: f)
          - Tekniska specifikationer (kommando: t)
          - Kompatibilitet (kommando: c)
          
        Endast giltiga exempel (t.ex. med ett äkta artikelnummer) genereras.
        """
        examples = []
        
        # Exempel för fullständig information
        if doc.article_number and not doc.article_number.startswith("TEMP_"):
            example = {
                "user_input": f"-f {doc.article_number}",
                "ai_output": self._format_full_info(doc)
            }
            examples.append(example)
        
        # Exempel för tekniska specifikationer
        if hasattr(doc, 'technical_specs') and doc.technical_specs:
            example = {
                "user_input": f"-t {doc.article_number}",
                "ai_output": self._format_technical_specs(doc)
            }
            examples.append(example)
        
        # Exempel för kompatibilitet
        if hasattr(doc, 'compatibility') and doc.compatibility:
            example = {
                "user_input": f"-c {doc.article_number}",
                "ai_output": self._format_compatibility(doc)
            }
            examples.append(example)
        
        return examples

    def process_examples(
        self, examples: List[Dict], command: str
    ) -> Tuple[List[Dict], Dict[str, List[str]]]:
        """
        Processerar och validerar träningsexempel.
        
        För varje exempel:
          - Utför grundläggande validering
          - Normaliserar input och output (inklusive markdown‑formattering)
          - Samlar eventuella fel och varningar
          
        Returnerar en tuple med:
          - Processade exempel (som dict)
          - Ett dict med valideringsresultat (fel och varningar)
        """
        processed_examples = []
        validation_results = {'errors': [], 'warnings': []}
        
        for idx, example in enumerate(examples):
            try:
                # Grundläggande validering
                if error := self.validator.validate_example(example, command):
                    validation_results['errors'].append(f"Exempel {idx}: {error}")
                    continue
                
                # Processa exemplet
                processed = self._process_example(example, command)
                processed_examples.append(processed)
                
                # Kontrollera efter varningar
                if warning := self.validator._check_warnings(processed, command):
                    validation_results['warnings'].append(f"Exempel {idx}: {warning}")
                    
            except Exception as e:
                validation_results['errors'].append(
                    f"Fel vid processering av exempel {idx}: {str(e)}"
                )
        
        return processed_examples, validation_results

    def _process_example(self, example: Dict, command: str) -> Dict:
        """Processerar ett enskilt exempel genom att normalisera input och output."""
        processed = example.copy()
        processed['user_input'] = self._normalize_input(processed['user_input'], command)
        processed['ai_output'] = self._normalize_output(processed['ai_output'], command)
        return processed

    def _normalize_input(self, input_text: str, command: str) -> str:
        """Normaliserar input-format genom att ta bort extra mellanslag och säkerställa korrekt kommando-prefix."""
        input_text = ' '.join(input_text.split())
        if not input_text.startswith(f'-{command} '):
            input_text = f'-{command} {input_text.lstrip("-").lstrip()}'
        return input_text

    def _normalize_output(self, output_text: str, command: str) -> str:
        """Normaliserar output-format (radbrytningar, tomma rader och markdown-formattering)."""
        output_text = output_text.replace('\r\n', '\n')
        output_text = re.sub(r'\n{3,}', '\n\n', output_text)
        output_text = self._normalize_markdown(output_text, command)
        return output_text.strip()

    def _normalize_markdown(self, text: str, command: str) -> str:
        """Normaliserar markdown-formattering i texten."""
        lines = text.split('\n')
        normalized = []
        for i, line in enumerate(lines):
            if line.startswith('#'):
                line = re.sub(r'^(#+)(\S)', r'\1 \2', line)
                if i > 0 and normalized and normalized[-1] != '':
                    normalized.append('')
            elif line.strip().startswith('-'):
                line = re.sub(r'^(\s*)-(\S)', r'\1- \2', line)
            normalized.append(line)
            if line.startswith('#') and i < len(lines) - 1:
                normalized.append('')
        return '\n'.join(normalized)

    def _format_full_info(self, doc: DocumentStructure) -> str:
        """Formaterar fullständig produktinformation som markdown."""
        parts = [f"# {doc.product_name}", doc.description]
        return "\n\n".join(parts)

    def _format_technical_specs(self, doc: DocumentStructure) -> str:
        """Formaterar tekniska specifikationer som markdown."""
        output_parts = []
        specs_by_category = {}
        for spec in doc.technical_specs:
            specs_by_category.setdefault(spec.category, []).append(spec)
        for category, specs in specs_by_category.items():
            output_parts.append(f"\n## {category.title()}")
            for spec in specs:
                # Använd en metod om den finns för att formatera värdet, annars bygg en sträng
                if hasattr(spec.value, 'format_value'):
                    value = spec.value.format_value()
                else:
                    value = f"{spec.value} {spec.unit or ''}"
                output_parts.append(f"- {value}")
        return "\n".join(output_parts)

    def _format_compatibility(self, doc: DocumentStructure) -> str:
        """Formaterar kompatibilitetsinformation som markdown."""
        output_parts = []
        compat_by_type = {}
        for comp in doc.compatibility:
            compat_by_type.setdefault(comp.type, []).append(comp)
        for comp_type, comps in compat_by_type.items():
            title = {
                'fits': 'Passar till',
                'requires': 'Kräver',
                'replaces': 'Ersätter',
                'accessory': 'Tillbehör'
            }.get(comp_type, comp_type.title())
            output_parts.append(f"\n## {title}")
            for comp in comps:
                if hasattr(comp, 'target_article') and comp.target_article:
                    output_parts.append(f"- {comp.description} (Art.nr: {comp.target_article})")
                else:
                    output_parts.append(f"- {comp.description}")
        return "\n".join(output_parts)


class TrainingExample(BaseModel):
    """Validationsmodell för träningsexempel."""
    user_input: str
    ai_output: str

    @validator('user_input')
    def validate_user_input(cls, v):
        if not v.startswith('-'):
            raise ValueError("user_input måste börja med ett kommando (-f, -s, -t, -c)")
        command = v.split()[0][1:]
        if command not in Settings.COMMAND_PREFIXES:
            raise ValueError(f"Ogiltigt kommando: {command}")
        return v

    @validator('ai_output')
    def validate_ai_output(cls, v):
        if len(v) < Settings.MIN_OUTPUT_LENGTH:
            raise ValueError(f"ai_output är för kort ({len(v)} tecken)")
        if len(v) > Settings.MAX_OUTPUT_LENGTH:
            raise ValueError(f"ai_output är för lång ({len(v)} tecken)")
        return v


class TrainingDataExporter:
    """Hanterar export av träningsdata till olika format (JSON och CSV)."""

    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def export_data(
        self, data: List[Dict], command: str, formats: List[str] = None
    ) -> Dict[str, List[Path]]:
        """
        Exporterar träningsdata i specificerade format.
        Returnerar en dictionary med sökvägar till skapade filer.
        """
        if formats is None:
            formats = Settings.SUPPORTED_FORMATS

        # Validera data först
        validated_data = self._validate_data(data)
        exported_files = {}
        for fmt in formats:
            if fmt == 'json':
                files = self._export_json(validated_data, command)
                exported_files['json'] = files
            elif fmt == 'csv':
                files = self._export_csv(validated_data, command)
                exported_files['csv'] = files
        return exported_files

    def _validate_data(self, data: List[Dict]) -> List[Dict]:
        """Validerar alla träningsexempel med hjälp av TrainingExample-modellen."""
        validated = []
        errors = []
        for idx, example in enumerate(data):
            try:
                validated_example = TrainingExample(**example)
                validated.append(validated_example.dict())
            except Exception as e:
                errors.append(f"Fel i exempel {idx}: {str(e)}")
        if errors:
            raise ValueError("\n".join(errors))
        return validated

    def _export_json(self, data: List[Dict], command: str) -> List[Path]:
        """Exporterar data till JSON-format."""
        output_file = self.output_dir / f"training_data_{command}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return [output_file]

    def _export_csv(self, data: List[Dict], command: str) -> List[Path]:
        """Exporterar data till CSV-format med uppdelning vid behov."""
        files = []
        total_rows = len(data)
        num_files = (total_rows + Settings.MAX_ROWS_PER_FILE - 1) // Settings.MAX_ROWS_PER_FILE
        for i in range(num_files):
            start_idx = i * Settings.MAX_ROWS_PER_FILE
            end_idx = min((i + 1) * Settings.MAX_ROWS_PER_FILE, total_rows)
            chunk = data[start_idx:end_idx]
            output_file = self.output_dir / f"training_data_{command}_{i:02d}.csv"
            df = pd.DataFrame(chunk)
            df.to_csv(
                output_file,
                index=False,
                encoding=Settings.CSV_ENCODING,
                escapechar='\\',
                quoting=csv.QUOTE_MINIMAL
            )
            files.append(output_file)
        return files
