#!/usr/bin/env python3
"""
convert_to_jsonl.py – Omvandlar JSON-filer till en enhetlig JSONL-struktur

Alla JSON-filer i den angivna indata-katalogen läses in och varje träningsexempel 
omvandlas så att endast fälten "user_input" och "ai_output" bevaras. Om ett 
objekt innehåller "qa_pairs" itereras över dessa och varje QA-pair omvandlas 
till ett objekt med fälten "user_input" (från QA-pairens "user_input") och 
"ai_output" (från QA-pairens "output"). Övriga extra fält tas bort.

Resultatet sparas i output-katalogen i JSONL-format (ett JSON-objekt per rad).
"""

import os
import glob
import json
import logging
import yaml
from pathlib import Path

def load_config(config_path: str = "convert_config.yaml") -> dict:
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    else:
        # Standardinställningar
        return {
            "input_directory": "./data",
            "output_directory": "./omformaterad_data_klar",
            "log_level": "INFO"
        }

CONFIG = load_config()

logging.basicConfig(
    level=getattr(logging, CONFIG.get("log_level", "INFO")),
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

def reformat_to_jsonl():
    input_directory = CONFIG.get("input_directory")
    output_directory = CONFIG.get("output_directory")

    # Skapa utdata-katalogen om den inte finns
    Path(output_directory).mkdir(parents=True, exist_ok=True)

    json_files = glob.glob(os.path.join(input_directory, "*.json"))
    if not json_files:
        logger.error(f"🚨 Inga JSON-filer hittades i {input_directory}")
        return

    for json_file in json_files:
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            if not isinstance(data, list):
                logger.warning(f"⚠️ Filen {json_file} innehåller inte en lista, hoppar över.")
                continue

            # Lista med omformaterade exemplar
            reformatted = []
            for entry in data:
                # Om entry innehåller "qa_pairs" - iterera över dessa
                if "qa_pairs" in entry:
                    for qa in entry["qa_pairs"]:
                        user_input = qa.get("user_input", "").strip()
                        output_text = qa.get("output", "").strip()
                        if user_input and output_text:
                            reformatted.append({
                                "user_input": user_input,
                                "ai_output": output_text
                            })
                else:
                    # Annars, plocka ut "user_input" och "ai_output"/"output"
                    user_input = entry.get("user_input", "").strip()
                    # Bevara även om det finns extra fält, men endast de två ska ut
                    if not user_input:
                        continue
                    # Om user_input börjar med "-f", behåll det inte (filtrera bort) 
                    # (Enligt tidigare krav: de med "-f" ska uteslutas)
                    if user_input.startswith("-f"):
                        continue

                    # Prioritera ai_output, annars output
                    if "ai_output" in entry:
                        output_text = entry["ai_output"].strip()
                    elif "output" in entry:
                        output_text = entry["output"].strip()
                    else:
                        continue

                    if user_input and output_text:
                        reformatted.append({
                            "user_input": user_input,
                            "ai_output": output_text
                        })

            # Spara omformaterade data som JSONL (en rad per objekt)
            output_file = Path(output_directory) / os.path.basename(json_file).replace(".json", ".jsonl")
            with open(output_file, "w", encoding="utf-8") as f:
                for obj in reformatted:
                    f.write(json.dumps(obj, ensure_ascii=False) + "\n")
            logger.info(f"✅ {os.path.basename(json_file)} omformaterad och sparad till {output_file} (antal exemplar: {len(reformatted)})")
        except Exception as e:
            logger.error(f"⚠️ Fel vid omformatering av {json_file}: {e}")

if __name__ == "__main__":
    reformat_to_jsonl()
