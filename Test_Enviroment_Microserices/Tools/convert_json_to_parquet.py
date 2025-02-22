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
            "json_input_directory": "./omformaterad_data_klar",
            "json_output_directory": "./converted_to_parquet",
            "combine_files": True,
            "combined_parquet_filename": "combined.parquet",
            "log_level": "INFO"
        }

CONFIG = load_config()

logging.basicConfig(
    level=getattr(logging, CONFIG.get("log_level", "INFO")),
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

def convert_and_validate_json_to_parquet():
    input_directory = CONFIG.get("json_input_directory")
    output_directory = CONFIG.get("json_output_directory")
    combine_files = CONFIG.get("combine_files", False)
    
    Path(output_directory).mkdir(parents=True, exist_ok=True)

    # Hitta både .json och .jsonl filer
    json_files = glob.glob(os.path.join(input_directory, "*.json*"))
    if not json_files:
        logger.error(f"🚨 Inga JSON-filer hittades i {input_directory}")
        return

    if combine_files:
        # Slå ihop alla filer till en DataFrame
        dataframes = []
        for json_file in json_files:
            try:
                if json_file.endswith(".jsonl"):
                    df = pd.read_json(json_file, lines=True)
                else:
                    df = pd.read_json(json_file)
                logger.info(f"📄 '{json_file}' lästes in med form: {df.shape}")
                dataframes.append(df)
            except Exception as e:
                logger.error(f"⚠️ Fel vid läsning av '{json_file}': {e}")
        
        if not dataframes:
            logger.error("🚨 Ingen giltig data kunde läsas in för sammanslagning.")
            return

        combined_df = pd.concat(dataframes, ignore_index=True)
        logger.info(f"📊 Totalt sammanslagen data: {combined_df.shape}")

        combined_filename = CONFIG.get("combined_parquet_filename", "combined.parquet")
        output_file = os.path.join(output_directory, combined_filename)
        combined_df.to_parquet(output_file, index=False)
        logger.info(f"✅ All data sparad som Parquet: {output_file}")

        try:
            df_parquet = pd.read_parquet(output_file)
            if combined_df.shape == df_parquet.shape:
                logger.info(f"✔️ Validering lyckades för sammanslagen fil (form: {combined_df.shape})")
            else:
                logger.error(f"❌ Validering misslyckades: {combined_df.shape} vs {df_parquet.shape}")
        except Exception as e:
            logger.error(f"⚠️ Fel vid validering av sammanslagen fil: {e}")
    else:
        # Bearbeta varje fil separat
        for json_file in json_files:
            try:
                if json_file.endswith(".jsonl"):
                    df = pd.read_json(json_file, lines=True)
                else:
                    df = pd.read_json(json_file)
                logger.info(f"📄 '{json_file}' lästes in med form: {df.shape}")

                parquet_file = os.path.join(output_directory, os.path.basename(json_file).replace('.jsonl', '.parquet').replace('.json', '.parquet'))
                df.to_parquet(parquet_file, index=False)
                logger.info(f"✅ '{json_file}' konverterad till '{parquet_file}'")

                df_parquet = pd.read_parquet(parquet_file)
                if df.shape == df_parquet.shape:
                    logger.info(f"✔️ Validering lyckades för '{json_file}' (form: {df.shape})")
                else:
                    logger.error(f"❌ Validering misslyckades för '{json_file}': {df.shape} vs {df_parquet.shape}")
            except Exception as e:
                logger.error(f"⚠️ Ett fel inträffade vid bearbetning av '{json_file}': {e}")

if __name__ == "__main__":
    convert_and_validate_json_to_parquet()
