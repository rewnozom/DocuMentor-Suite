#!/usr/bin/env python3
"""
remove_duplicates.py – Tar bort dubbletter från en Parquet-fil

Detta script läser in en Parquet-fil med träningsdata (där varje rad har fälten "user_input" och "ai_output"),
kontrollerar om någon rad har exakt samma kombination av "user_input" och "ai_output" som en annan,
och tar bort dessa dubbletter. Resultatet sparas i en ny Parquet-fil.
"""

import os
import logging
import yaml
import pandas as pd
from pathlib import Path

def load_config(path: str = "duplicates_config.yaml") -> dict:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    else:
        return {
            "input_parquet": "./converted_to_parquet/combined.parquet",
            "output_parquet": "./converted_to_parquet/combined_dedup.parquet",
            "log_level": "INFO"
        }

CONFIG = load_config()

logging.basicConfig(
    level=getattr(logging, CONFIG.get("log_level", "INFO")),
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

def remove_duplicates():
    input_parquet = CONFIG.get("input_parquet")
    output_parquet = CONFIG.get("output_parquet")
    
    if not os.path.exists(input_parquet):
        logger.error(f"🚨 Inmatningsfilen finns inte: {input_parquet}")
        return

    try:
        df = pd.read_parquet(input_parquet)
        logger.info(f"📄 Läst in {input_parquet} med form: {df.shape}")

        # Skapa en temporär kolumn med sammanslagna user_input och ai_output
        df["combined"] = df["user_input"].astype(str) + df["ai_output"].astype(str)

        before = df.shape[0]
        df_dedup = df.drop_duplicates(subset=["combined"])
        after = df_dedup.shape[0]
        logger.info(f"✅ Dubbletter borttagna: {before - after} rader borttagna, ny form: {df_dedup.shape}")

        # Ta bort den temporära kolumnen
        df_dedup = df_dedup.drop(columns=["combined"])

        df_dedup.to_parquet(output_parquet, index=False)
        logger.info(f"💾 Sparad deduplicerad Parquet-fil: {output_parquet}")
    except Exception as e:
        logger.error(f"⚠️ Fel vid bearbetning: {e}")

if __name__ == "__main__":
    remove_duplicates()
