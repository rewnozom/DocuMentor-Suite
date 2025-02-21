# markdown_analyzer/utils/file_utils.py
from datetime import datetime
from pathlib import Path
from typing import List
import os
import logging

logger = logging.getLogger(__name__)

def find_markdown_files(directories: List[str]) -> List[Path]:
    """Hittar alla markdown-filer i angivna kataloger"""
    markdown_files = []
    
    for directory in directories:
        dir_path = Path(directory)
        if not dir_path.exists():
            logger.warning(f"Katalog existerar inte: {directory}")
            continue
        
        logger.info(f"Skannar katalog: {directory}")
        # Hitta alla .md-filer rekursivt
        markdown_files.extend(dir_path.rglob("*.md"))
        
        # Logga antal hittade filer
        count = len([f for f in markdown_files if str(f).startswith(str(dir_path))])
        logger.info(f"Hittade {count} markdown-filer i {directory}")
    
    return markdown_files

def ensure_dir(directory: str) -> None:
    """Säkerställer att en katalog existerar"""
    os.makedirs(directory, exist_ok=True)

def get_file_hash(filepath: Path) -> str:
    """Beräknar en hash för en fil"""
    import hashlib
    
    with open(filepath, 'rb') as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    
    return file_hash.hexdigest()

def backup_file(filepath: Path, backup_dir: str = "backups") -> None:
    """Skapar en backup av en fil"""
    backup_path = Path(backup_dir)
    backup_path.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = backup_path / f"{filepath.stem}_{timestamp}{filepath.suffix}"
    
    import shutil
    shutil.copy2(filepath, backup_file)
    logger.info(f"Skapade backup: {backup_file}")