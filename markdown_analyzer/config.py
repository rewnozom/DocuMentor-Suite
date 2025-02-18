# markdown_analyzer/config.py

from pydantic import BaseSettings
from typing import Dict, List

class Settings(BaseSettings):
    """Globala konfigurationsinställningar för Markdown Analyzer."""
    
    # Bearbetningsinställningar
    MAX_WORKERS: int = 4  # Antal parallella trådar/processer
    CHUNK_SIZE: int = 10  # Antal dokument att bearbeta per batch
    
    # Segmentering och fältlängd
    CHARS_PER_SEGMENT: int = 60000  # Max tecken per segment
    MAX_FIELD_LENGTH: int = 131072  # Max längd för CSV-fält
    MAX_ROWS_PER_FILE: int = 1000   # Max antal rader per CSV-fil
    
    # Kommandon och formattering
    COMMAND_PREFIXES: Dict[str, str] = {
        'f': 'full_info',
        's': 'summary',
        't': 'technical',
        'c': 'compatibility'
    }
    MIN_EXAMPLES_PER_COMMAND: int = 10  # Minsta antal exempel per kommando
    
    # Validering och valideringskrav
    REQUIRED_FIELDS: List[str] = ['user_input', 'ai_output']
    MIN_OUTPUT_LENGTH: int = 10
    MAX_OUTPUT_LENGTH: int = 131072
    VALIDATION_ENABLED: bool = True  # Slå på/av validering
    STRICT_VALIDATION: bool = False  # Aktivera strikta valideringsregler
    
    # Exportinställningar
    SUPPORTED_FORMATS: List[str] = ['json', 'csv']
    OUTPUT_FORMAT: str = "both"  # Kan vara "json", "csv" eller "both"
    CSV_ENCODING: str = 'utf-8'
    
    # Loggningsinställningar
    LOG_LEVEL: str = "INFO"  # Kan vara "DEBUG", "INFO", "WARNING", "ERROR"
    SHOW_PROGRESS: bool = True  # Visa bearbetningsprogress i terminalen
    
    class Config:
        env_prefix = "MARKDOWN_ANALYZER_"  # Prefix för miljövariabler

# Skapa en global instans av inställningarna
settings = Settings()
