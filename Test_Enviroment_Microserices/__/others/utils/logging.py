# markdown_analyzer/utils/logging.py
import logging
from pathlib import Path
from datetime import datetime

def setup_logging(debug: bool = False, log_dir: str = "logs") -> None:
    """Konfigurerar loggning för applikationen"""
    # Skapa loggkatalog
    log_path = Path(log_dir)
    log_path.mkdir(exist_ok=True)
    
    # Skapa filnamn med tidsstämpel
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_path / f"markdown_analyzer_{timestamp}.log"
    
    # Sätt loggnivå
    level = logging.DEBUG if debug else logging.INFO
    
    # Konfigurera loggning
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    
    # Skapa logger för huvudapplikationen
    logger = logging.getLogger('markdown_analyzer')
    logger.setLevel(level)
    
    # Logga uppstart
    logger.info("=== Markdown Analyzer Started ===")
    logger.info(f"Log file: {log_file}")
    logger.info(f"Debug mode: {'enabled' if debug else 'disabled'}")
