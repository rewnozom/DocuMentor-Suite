# markdown_analyzer/extractors/base.py
import re
import logging
from typing import Optional, List, Dict
from ..core.document import DocumentStructure
from ..core.errors import DocumentParsingError

class BaseExtractor:
    """Basklassen för alla extraktorer"""
    
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def extract(self, content: str) -> Dict:
        """
        Huvudmetod för extraktion som måste implementeras av subklasser
        """
        raise NotImplementedError
    
    def validate_output(self, data: Dict) -> bool:
        """
        Validerar extraherad data
        """
        return True
    
    def _clean_text(self, text: str) -> str:
        """
        Rensar text från oönskade tecken och formattering
        """
        # Remove special characters except basic punctuation
        text = re.sub(r'[^\w\s\-.,;:?!()\[\]{}"\']+', '', text)
        # Normalize whitespace
        text = re.sub(r'\s+', ' ', text)
        return text.strip()