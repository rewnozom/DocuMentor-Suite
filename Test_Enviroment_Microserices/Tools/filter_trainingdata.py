#!/usr/bin/env python3
import os
import glob
import json
import logging
import yaml
from pathlib import Path

def load_config(path: str = "filter_config.yaml") -> dict:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    else:
        # Standardinställningar
        return {
            "input_directory": "./data_with_cutted_tokens/",
            "output_directory": "./filtered_trainingdata/",
            "exclude_command": "-f",
            "log_level": "INFO"
        }

CONFIG = load_config()

# Konfigurera loggning
logging.basicConfig(
    level=getattr(logging, CONFIG.get("log_level", "INFO")),
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

def filter_training_data():
    input_dir = CONFIG.get("input_directory")
    output_dir = CONFIG.get("output_directory")
    exclude_command = CONFIG.get("exclude_command", "-f").strip()

    # Skapa utdata-katalogen om den inte finns
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    json_files = glob.glob(os.path.join(input_dir, '*.json'))
    if not json_files:
        logger.error(f"🚨 Inga JSON-filer hittades i {input_dir}")
        return

    for json_file in json_files:
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            original_count = len(data)
            # Filtrera bort alla entries där user_input börjar med exclude_command (ex: "-f")
            filtered_data = [entry for entry in data if not entry.get("user_input", "").strip().startswith(exclude_command)]
            filtered_count = len(filtered_data)
            logger.info(f"📄 {os.path.basename(json_file)}: {original_count} -> {filtered_count} exemplar (utslagna: {original_count - filtered_count})")

            # Spara den filtrerade filen i output-katalogen med samma namn
            output_file = Path(output_dir) / os.path.basename(json_file)
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(filtered_data, f, ensure_ascii=False, indent=2)
            logger.info(f"✅ Sparade filtrerad data till {output_file}")
        except Exception as e:
            logger.error(f"⚠️ Fel vid bearbetning av '{json_file}': {e}")

if __name__ == "__main__":
    filter_training_data()
