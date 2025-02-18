# markdown_analyzer/trainers/__init__.py
from .base import BaseTrainer
from .formatters import MarkdownFormatter
from .commands import BasicInfoTrainer, SummaryTrainer, TechnicalTrainer, CompatibilityTrainer
from typing import List, Dict, Optional

class TrainerRegistry:
    """Register för att hantera alla trainers."""
    
    def __init__(self):
        self.trainers = {
            'f': BasicInfoTrainer(),
            's': SummaryTrainer(),
            't': TechnicalTrainer(),
            'c': CompatibilityTrainer()
        }
        self.formatter = MarkdownFormatter()
    
    def get_trainer(self, command: str):
        """Returnera trainer för ett specifikt kommando."""
        return self.trainers.get(command)
    
    def create_training_data(self, doc, command: str) -> List[Dict]:
        """Skapa träningsdata med lämplig trainer."""
        trainer = self.get_trainer(command)
        if not trainer:
            raise ValueError(f"No trainer found for command: {command}")
        examples = trainer.create_training_data(doc)
        return examples if examples else []

        
__all__ = [
    'BaseTrainer',
    'MarkdownFormatter',
    'BasicInfoTrainer',
    'SummaryTrainer',
    'TechnicalTrainer',
    'CompatibilityTrainer'
]
