# markdown_analyzer/dataset/validators.py

import logging
import re
from typing import List, Dict, Any
from dataclasses import dataclass

from core.document import DocumentStructure

@dataclass
class ValidationResult:
    """Resultat från validering."""
    is_valid: bool
    errors: List[str]
    warnings: List[str]
    stats: Dict[str, int]

class DatasetValidator:
    """
    Validerar träningsdata för att säkerställa kvalitet och konsistens.
    
    Denna implementation kontrollerar att varje träningsdataexempel (en dict)
    innehåller rätt fält, att input och output inte är tomma eller för korta/långa,
    samt att exempel med tekniskt innehåll har en rimlig formatstruktur.
    Extra statistik samlas även, såsom antal exempel med låg confidence.
    """
    
    def __init__(self, max_length: int = 131072):
        self.max_length = max_length
        self.logger = logging.getLogger(__name__)
    
    def validate_training_samples(self, samples: List[Dict]) -> Dict[str, Any]:
        """
        Validerar en samling träningsexempel.
        
        Returnerar en dictionary med:
          - is_valid: bool
          - errors: lista med felmeddelanden
          - warnings: lista med varningar
          - stats: statistik över valideringen
        """
        errors = []
        warnings = []
        stats = {
            "total_samples": len(samples),
            "large_outputs": 0,
            "empty_inputs": 0,
            "empty_outputs": 0,
            "low_confidence": 0
        }
        
        for idx, sample in enumerate(samples):
            if not self._validate_sample_structure(sample):
                errors.append(f"Sample {idx}: Invalid structure")
                continue
            
            user_input = sample.get("user_input", "")
            ai_output = sample.get("ai_output", "")
            
            input_validation = self._validate_input(user_input)
            if input_validation:
                errors.extend(f"Sample {idx}: {err}" for err in input_validation)
                stats["empty_inputs"] += 1
            
            output_validation = self._validate_output(ai_output)
            if output_validation:
                errors.extend(f"Sample {idx}: {err}" for err in output_validation)
                stats["empty_outputs"] += 1
            
            # Kontrollera confidence (om den finns)
            confidence = sample.get("confidence", 1.0)
            if confidence < 0.7:
                stats["low_confidence"] += 1
                warnings.append(f"Sample {idx}: Low confidence score ({confidence})")
            
            if len(ai_output) > self.max_length:
                warnings.append(
                    f"Sample {idx}: Output exceeds max length ({len(ai_output)} > {self.max_length})"
                )
                stats["large_outputs"] += 1
            
            # Vid tekniska exempel (-t) utförs extra kontroller på markdown-formattering
            if user_input.startswith("-t"):
                tech_validation = self._validate_technical_output(ai_output)
                if tech_validation:
                    warnings.extend(f"Sample {idx}: {warn}" for warn in tech_validation)
        
        is_valid = len(errors) == 0
        return {
            "is_valid": is_valid,
            "errors": errors,
            "warnings": warnings,
            "stats": stats
        }
    
    def _validate_sample_structure(self, sample: Dict) -> bool:
        """Kontrollerar att sample innehåller fälten 'user_input' och 'ai_output'."""
        return all(k in sample for k in ['user_input', 'ai_output'])
    
    def _validate_input(self, user_input: str) -> List[str]:
        """Validerar user_input."""
        errors = []
        if not user_input.strip():
            errors.append("Input is empty")
        return errors
    
    def _validate_output(self, ai_output: str) -> List[str]:
        """Validerar ai_output."""
        errors = []
        if not ai_output.strip():
            errors.append("Output is empty")
        if len(ai_output.strip()) < 10:
            errors.append("Output is too short")
        if len(ai_output) > self.max_length:
            errors.append("Output is too long")
        return errors
    
    def _validate_technical_output(self, output: str) -> List[str]:
        """Specifik validering för teknisk output-format."""
        warnings = []
        # Kontrollera att det finns en rubrik (markdown-format: '## ...')
        if not re.search(r'##\s+[\w\s]+', output):
            warnings.append("Missing section headers in technical output")
        # Kontrollera att tekniska värden är korrekt formaterade (exempel: '- 12.5 kg')
        values = re.findall(r'-\s*(\d+(?:\.\d+)?)\s*([A-Za-z]+)', output)
        if not values:
            warnings.append("No properly formatted technical values found")
        return warnings


class ValidationPipeline:
    """
    Fullständig valideringspipeline för datasetgenerering.
    
    Pipeline: 
      - Validerar dokument genom att skapa ett exempel från ett DocumentStructure.
      - Validerar enskilda träningsexempel med fältkrav och kommando-specifik logik.
    """
    
    def __init__(self):
        self.document_validator = DatasetValidator()
        # Ytterligare validatorer kan läggas till vid behov, t.ex. training_validator eller format_validator.
        self.training_validator = None
        self.format_validator = None
    
    def validate_document(self, doc: DocumentStructure) -> List[str]:
        """
        Validerar ett dokument genom att skapa ett träningsdataexempel 
        (exempelvis med fullständig information) och kör validatorn.
        
        Returnerar en lista med felmeddelanden om några.
        """
        sample = {
            "user_input": f"-f {doc.article_number}",
            "ai_output": doc.description  # Exempelvärde, här används dokumentets beskrivning
        }
        result = self.document_validator.validate_training_samples([sample])
        return result.get("errors", [])
    
    def validate_training_example(self, example: Dict[str, str], command: str) -> List[str]:
        """
        Validerar ett enskilt träningsexempel.
        
        Exempelvis kontrolleras att fält finns, att user_input börjar med '-' samt att ai_output inte är för kort.
        Returnerar en lista med felmeddelanden om några.
        """
        errors = []
        if not all(k in example for k in ['user_input', 'ai_output']):
            errors.append("Missing required fields in training example")
            return errors
        if not example["user_input"].startswith("-"):
            errors.append("user_input must start with a '-'")
        if len(example["ai_output"].strip()) < 10:
            errors.append("ai_output is too short")
        return errors
