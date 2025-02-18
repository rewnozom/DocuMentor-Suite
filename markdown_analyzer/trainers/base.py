# markdown_analyzer/trainers/base.py
from typing import Dict, List, Optional
from dataclasses import dataclass
from ..core.document import DocumentStructure
from .formatters import MarkdownFormatter

@dataclass
class TrainingExample:
    """Ett träningsexempel för LLM"""
    command: str
    article_number: str
    input_text: str
    output_text: str
    confidence: float = 1.0

class BaseTrainer:
    """Basklass för alla träningsdatageneratorer"""
    
    def __init__(self):
        self.formatter = MarkdownFormatter()
    
    def create_training_data(self, doc: DocumentStructure) -> List[TrainingExample]:
        """
        Skapar träningsexempel från ett dokument.
        Måste implementeras av subklasser.
        """
        raise NotImplementedError
    
    def validate_example(self, example: TrainingExample) -> bool:
        """Validerar ett träningsexempel"""
        if not example.input_text or not example.output_text:
            return False
        if not example.article_number:
            return False
        return True


