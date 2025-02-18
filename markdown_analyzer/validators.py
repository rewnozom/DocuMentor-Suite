# markdown_analyzer/validators.py
from typing import List, Dict, Optional
from pydantic import BaseModel, validator
import re
from .config import Settings

class CommandValidator(BaseModel):
    """Basvalidator för kommandon"""
    user_input: str
    ai_output: str
    
    @validator('user_input')
    def validate_user_input(cls, v):
        if not v.startswith('-'):
            raise ValueError("user_input måste börja med ett kommando")
        return v

class FullInfoValidator(CommandValidator):
    """Validator för -f kommandot"""
    
    @validator('ai_output')
    def validate_full_info_output(cls, v):
        # Måste ha en huvudrubrik
        if not re.search(r'^#\s+.+', v, re.MULTILINE):
            raise ValueError("Saknar huvudrubrik (#)")
            
        # Bör innehålla en produktbild
        if not re.search(r'!\[.*?\]\(.*?\)', v):
            raise ValueError("Saknar produktbild")
            
        # Kontrollera minimalt innehåll
        if len(v.split('\n')) < 5:
            raise ValueError("För lite innehåll")
            
        return v

class SummaryValidator(CommandValidator):
    """Validator för -s kommandot"""
    
    @validator('ai_output')
    def validate_summary_output(cls, v):
        # Kontrollera sektioner
        required_sections = [
            r'##\s+(?:Viktiga egenskaper|Tekniska specifikationer|Kompatibilitet)'
        ]
        
        found_sections = 0
        for pattern in required_sections:
            if re.search(pattern, v, re.MULTILINE):
                found_sections += 1
                
        if found_sections == 0:
            raise ValueError("Saknar viktiga sektioner")
            
        # Kontrollera punktlistor
        if not re.search(r'^\s*-\s+.+', v, re.MULTILINE):
            raise ValueError("Saknar punktlistor")
            
        return v

class TechnicalValidator(CommandValidator):
    """Validator för -t kommandot"""
    
    @validator('ai_output')
    def validate_technical_output(cls, v):
        # Måste ha teknisk sektion
        if not re.search(r'##\s+Tekniska\s+[Ss]pecifikationer', v):
            raise ValueError("Saknar teknisk sektion")
            
        # Kontrollera tekniska värden
        if not re.search(r'^\s*-\s+[\w\s]+:\s+\d+(?:\.\d+)?\s*\w+', v, re.MULTILINE):
            raise ValueError("Saknar formaterade tekniska värden")
            
        # Kontrollera enheter
        valid_units = ['mm', 'cm', 'm', 'V', 'A', 'W', 'kg', 'g', 'Hz']
        found_units = re.findall(r'\b(' + '|'.join(valid_units) + r')\b', v)
        if not found_units:
            raise ValueError("Saknar giltiga enheter")
            
        return v

class CompatibilityValidator(CommandValidator):
    """Validator för -c kommandot"""
    
    @validator('ai_output')
    def validate_compatibility_output(cls, v):
        # Måste ha minst en kompatibilitetssektion
        if not re.search(r'##\s+(?:Passar till|Kräver|Ersätter|Tillbehör)', v):
            raise ValueError("Saknar kompatibilitetssektioner")
            
        # Kontrollera artikelnummerreferenser
        if not re.search(r'Art\.nr:\s*\d{5,8}', v):
            raise ValueError("Saknar artikelnummerreferenser")
            
        # Kontrollera listformat
        if not re.search(r'^\s*-\s+.+', v, re.MULTILINE):
            raise ValueError("Saknar formaterade listor")
            
        return v

class TrainingDataValidator:
    """Huvudvalidator för träningsdata"""
    
    def __init__(self):
        self.validators = {
            'f': FullInfoValidator,
            's': SummaryValidator,
            't': TechnicalValidator,
            'c': CompatibilityValidator
        }
        
    def validate_example(self, example: Dict, command: str) -> Optional[str]:
        """
        Validerar ett träningsexempel för ett specifikt kommando.
        Returnerar felmeddelande om validering misslyckas, annars None.
        """
        try:
            # Grundläggande validering
            if not all(field in example for field in Settings.REQUIRED_FIELDS):
                return "Saknar obligatoriska fält"
                
            # Längdvalidering
            if len(example['ai_output']) > Settings.MAX_OUTPUT_LENGTH:
                return f"Output överskrider maxlängd ({len(example['ai_output'])} tecken)"
                
            if len(example['ai_output']) < Settings.MIN_OUTPUT_LENGTH:
                return f"Output är för kort ({len(example['ai_output'])} tecken)"
                
            # Kommandospecifik validering
            if command in self.validators:
                validator = self.validators[command]
                validator(**example)
                
            return None
            
        except Exception as e:
            return str(e)
            
    def validate_dataset(self, data: List[Dict], 
                        command: str) -> Dict[str, List[str]]:
        """
        Validerar ett helt dataset.
        Returnerar dictionary med fel och varningar.
        """
        errors = []
        warnings = []
        
        for idx, example in enumerate(data):
            # Validera exempel
            if error := self.validate_example(example, command):
                errors.append(f"Exempel {idx}: {error}")
                continue
                
            # Kontrollera efter varningar
            if warning := self._check_warnings(example, command):
                warnings.append(f"Exempel {idx}: {warning}")
                
        return {
            'errors': errors,
            'warnings': warnings
        }
            
    def _check_warnings(self, example: Dict, command: str) -> Optional[str]:
        """Kontrollerar efter potentiella problem som genererar varningar"""
        # Kontrollera efter långa outputs
        warnings = []
        if len(example['ai_output']) > Settings.MAX_OUTPUT_LENGTH * 0.8:
            return "Output närmar sig maxlängd"
            
        # Kontrollera efter korta outputs
        if len(example['ai_output']) < Settings.MIN_OUTPUT_LENGTH * 2:
            return "Output är relativt kort"
            

        # Kontrollera formattering
        if command == 'f':
            warnings.extend(self._check_full_info_warnings(example))
        elif command == 's':
            warnings.extend(self._check_summary_warnings(example))
        elif command == 't':
            warnings.extend(self._check_technical_warnings(example))
        elif command == 'c':
            warnings.extend(self._check_compatibility_warnings(example))
        
        return "; ".join(warnings) if warnings else None

    def _check_full_info_warnings(self, example: Dict) -> List[str]:
        """Kontrollerar varningar för full info output"""
        warnings = []
        output = example['ai_output']
        
        # Kontrollera bildkvalitet
        image_refs = re.findall(r'!\[.*?\]\((.*?)\)', output)
        if image_refs:
            if not any('_2' in ref for ref in image_refs):
                warnings.append("Använder möjligen inte bästa tillgängliga bild")
        
        # Kontrollera strukturen
        if len(re.findall(r'^#', output, re.MULTILINE)) > 3:
            warnings.append("Många rubriker kan göra innehållet svårläst")
        
        return warnings

    def _check_summary_warnings(self, example: Dict) -> List[str]:
        """Kontrollerar varningar för sammanfattningar"""
        warnings = []
        output = example['ai_output']
        
        # Kontrollera längd på punkter
        bullet_points = re.findall(r'^\s*-\s+(.+)$', output, re.MULTILINE)
        for point in bullet_points:
            if len(point) > 100:
                warnings.append("Vissa punkter är väldigt långa")
                break
        
        # Kontrollera balans mellan sektioner
        sections = re.split(r'^##\s+', output, flags=re.MULTILINE)[1:]
        if sections and len(sections) < 2:
            warnings.append("Få sektioner kan indikera ofullständig sammanfattning")
        
        return warnings

    def _check_technical_warnings(self, example: Dict) -> List[str]:
        """Kontrollerar varningar för teknisk information"""
        warnings = []
        output = example['ai_output']
        
        # Kontrollera enhetskonsistens
        measurements = re.findall(r'(\d+(?:\.\d+)?)\s*(\w+)', output)
        units = {}
        for value, unit in measurements:
            if unit not in units:
                units[unit] = []
            units[unit].append(float(value))
        
        for unit, values in units.items():
            if max(values) / min(values) > 1000:
                warnings.append(f"Stor variation i värden för enhet {unit}")
        
        # Kontrollera tekniska kategorier
        categories = re.findall(r'^##\s+(.+)$', output, re.MULTILINE)
        expected_categories = {'Dimensioner', 'Elektrisk', 'Mekanisk', 'Miljö'}
        found_categories = set(cat.lower() for cat in categories)
        if not found_categories & expected_categories:
            warnings.append("Saknar vanliga tekniska kategorier")
        
        return warnings

    def _check_compatibility_warnings(self, example: Dict) -> List[str]:
        """Kontrollerar varningar för kompatibilitetsinformation"""
        warnings = []
        output = example['ai_output']
        
        # Kontrollera artikelnummerformat
        article_numbers = re.findall(r'Art\.nr:\s*(\d+)', output)
        for num in article_numbers:
            if not (5 <= len(num) <= 8):
                warnings.append(f"Ovanlig längd på artikelnummer: {num}")
        
        # Kontrollera villkor
        conditions = re.findall(r'(\(.*?\))', output)
        if len(conditions) > 5:
            warnings.append("Många villkor kan göra informationen svårförståelig")
        
        return warnings
