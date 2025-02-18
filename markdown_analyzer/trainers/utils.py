# markdown_analyzer/trainers/utils.py
from typing import Dict, List
import csv
import json
from datetime import datetime
from .base import TrainingExample

def save_training_data(examples: List[TrainingExample], output_dir: str):
    """Sparar träningsexempel i både JSON och CSV format"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Spara som JSON
    json_path = f"{output_dir}/training_data_{timestamp}.json"
    json_data = [
        {
            'command': ex.command,
            'article_number': ex.article_number,
            'input': ex.input_text,
            'output': ex.output_text,
            'confidence': ex.confidence
        }
        for ex in examples
    ]
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    
    # Spara som CSV
    csv_path = f"{output_dir}/training_data_{timestamp}.csv"
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['command', 'article_number', 'input', 'output', 'confidence'])
        for ex in examples:
            writer.writerow([
                ex.command,
                ex.article_number,
                ex.input_text,
                ex.output_text,
                ex.confidence
            ])

def validate_training_data(examples: List[TrainingExample]) -> List[str]:
    """Validerar en samling träningsexempel"""
    validation_errors = []
    
    for i, example in enumerate(examples):
        # Kontrollera obligatoriska fält
        if not example.article_number:
            validation_errors.append(f"Example {i}: Saknar artikelnummer")
        if not example.input_text:
            validation_errors.append(f"Example {i}: Saknar input")
        if not example.output_text:
            validation_errors.append(f"Example {i}: Saknar output")
            
        # Kontrollera kommandoformat
        if not example.command in {'f', 's', 't', 'c'}:
            validation_errors.append(f"Example {i}: Ogiltigt kommando {example.command}")
            
        # Kontrollera input-format
        expected_input = f"-{example.command} {example.article_number}"
        if example.input_text != expected_input:
            validation_errors.append(
                f"Example {i}: Felaktigt input-format. "
                f"Förväntade {expected_input}, fick {example.input_text}"
            )
            
        # Kontrollera markdown-formattering i output
        if '##' in example.output_text and not example.output_text.startswith('#'):
            validation_errors.append(
                f"Example {i}: Felaktig rubrikstruktur i output"
            )
    
    return validation_errors