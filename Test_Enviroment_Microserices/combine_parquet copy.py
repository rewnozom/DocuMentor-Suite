#!/usr/bin/env python3
"""
combine_parquet.py – Kombinerar flera Parquet-filer till en enda

Detta script läser in Parquet-filer (t.ex. "combined_dedup_ALL.parquet" och "combined_dedup.parquet")
som anges i YAML-konfigurationsfilen, slår ihop dem till en enda DataFrame och sparar resultatet
som en ny Parquet-fil. Validering sker genom att jämföra dimensionerna för den sammanslagna DataFrame
och den sparade filen.
"""

import os
import logging
import yaml
import pandas as pd
from pathlib import Path

def load_config(config_path: str = "combine_config.yaml") -> dict:
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    else:
        # Standardinställningar om konfigfilen saknas
        return {
            "parquet_files": [
                "./combined_dedup_ALL.parquet",
                "./combined_dedup.parquet"
            ],
            "output_parquet": "./combined_dedup_final.parquet",
            "log_level": "INFO"
        }

CONFIG = load_config()

logging.basicConfig(
    level=getattr(logging, CONFIG.get("log_level", "INFO")),
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

def combine_parquet_files():
    parquet_files = CONFIG.get("parquet_files", [])
    output_parquet = CONFIG.get("output_parquet")
    
    combined_dfs = []
    for file in parquet_files:
        if os.path.exists(file):
            try:
                df = pd.read_parquet(file)
                logger.info(f"📄 {file} lästes in med form: {df.shape}")
                combined_dfs.append(df)
            except Exception as e:
                logger.error(f"⚠️ Fel vid läsning av {file}: {e}")
        else:
            logger.error(f"🚨 Filen {file} existerar inte.")
    
    if not combined_dfs:
        logger.error("🚨 Ingen giltig data kunde läsas in från angivna filer.")
        return
    
    combined_df = pd.concat(combined_dfs, ignore_index=True)
    logger.info(f"📊 Totalt sammanslagen data: {combined_df.shape}")
    
    # Se till att utdata-katalogen existerar
    output_path = Path(output_parquet)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        combined_df.to_parquet(output_parquet, index=False)
        logger.info(f"✅ Sammanslagen Parquet-fil sparad: {output_parquet}")
        
        # Validering: Läs in sparad fil och jämför dimensioner
        df_val = pd.read_parquet(output_parquet)
        if df_val.shape == combined_df.shape:
            logger.info(f"✔️ Validering lyckades: {df_val.shape}")
        else:
            logger.error(f"❌ Validering misslyckades: Ursprunglig form {combined_df.shape} vs sparad {df_val.shape}")
    except Exception as e:
        logger.error(f"⚠️ Fel vid sparande av sammanslagen fil: {e}")

if __name__ == "__main__":
    combine_parquet_files()
