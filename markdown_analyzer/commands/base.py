from typing import Dict, Optional
from ..core.document import DocumentStructure

class BaseCommand:
    """Base class for all commands"""
    def __init__(self):
        self.validator = None
        self.formatter = None

    def process(self, doc: DocumentStructure) -> Dict:
        """Processes a document and returns training data"""
        raise NotImplementedError

    def validate(self, result: Dict) -> bool:
        """Validates the result"""
        if self.validator:
            return self.validator.validate(result)
        return True

    def format_output(self, result: Dict) -> str:
        """Formats the output using the formatter if available"""
        if self.formatter:
            return self.formatter.format(result)
        return str(result)

    def set_validator(self, validator) -> None:
        """Sets the validator for this command"""
        self.validator = validator

    def set_formatter(self, formatter) -> None:
        """Sets the formatter for this command"""
        self.formatter = formatter