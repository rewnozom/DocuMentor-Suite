#!/usr/bin/env python3
import os
import glob
import logging
import yaml
import pandas as pd
from pathlib import Path

def load_config(path: str = "conversion_config.yaml") -> dict:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    else:
        return {
            "parquet_input_directory": "./parquet_input",
            "parquet_output_directory": "./converted_to_json",
            "log_level": "INFO"
        }

CONFIG = load_config()

logging.basicConfig(
    level=getattr(logging, CONFIG.get("log_level", "INFO")),
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

def convert_and_validate_parquet_to_json():
    input_directory = CONFIG.get("parquet_input_directory")
    output_directory = CONFIG.get("parquet_output_directory")
    Path(output_directory).mkdir(parents=True, exist_ok=True)

    parquet_files = glob.glob(os.path.join(input_directory, '*.parquet'))
    if not parquet_files:
        logger.error(f"🚨 Inga Parquet-filer hittades i {input_directory}")
        return

    for parquet_file in parquet_files:
        try:
            df = pd.read_parquet(parquet_file)
            logger.info(f"📄 '{parquet_file}' lästes in med form: {df.shape}")

            json_file = os.path.join(output_directory, os.path.basename(parquet_file).replace('.parquet', '.json'))
            df.to_json(json_file, orient='records', force_ascii=False, indent=2)
            logger.info(f"✅ '{parquet_file}' konverterad till '{json_file}'")

            df_json = pd.read_json(json_file)
            if df.shape == df_json.shape:
                logger.info(f"✔️ Validering lyckades för '{parquet_file}' (form: {df.shape})")
            else:
                logger.error(f"❌ Validering misslyckades för '{parquet_file}': {df.shape} vs {df_json.shape}")
        except Exception as e:
            logger.error(f"⚠️ Ett fel inträffade vid bearbetning av '{parquet_file}': {e}")

if __name__ == "__main__":
    convert_and_validate_parquet_to_json()
