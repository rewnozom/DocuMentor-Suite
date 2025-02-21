#!/usr/bin/env python3
"""
combine_model.py – Kombinerar basmodellen med alla LoRA-adapters i kronologisk ordning

Detta script:
  • Identifierar alla LoRA-adapters från "./output/" och "./output2/"
  • Sorterar adapters efter tidpunkt (baserat på dina bilder)
  • Laddar in basmodellen från "./unsloth_Llama-3.2-1B-Instruct-bnb-4bit"
  • Kombinerar basen med varje adapter och sparar i "Copiax_XX"-numrerade mappar
  • Använder PEFT för att merge:a och unload:a adaptervikterna
"""

import os
import logging
from pathlib import Path
import re
import shutil
from datetime import datetime

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# För adapterhantering med PEFT
try:
    from peft import PeftModel
except ImportError:
    raise ImportError("peft-biblioteket måste vara installerat (pip install peft)")

# Konfigurera loggning
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Lista med checkpoints och deras tidpunkter baserat på bilderna
CHECKPOINT_TIMES = {
    "checkpoint-6452": "2025-02-20 15:28",
    "checkpoint-12904": "2025-02-20 16:08",
    "checkpoint-19356": "2025-02-20 16:48",
    "checkpoint-25808": "2025-02-20 17:28",
    "checkpoint-32260": "2025-02-20 18:08",
    "checkpoint-38712": "2025-02-20 18:48",
    "checkpoint-45164": "2025-02-20 19:28",
    "checkpoint-51616": "2025-02-20 20:08",
    "checkpoint-58068": "2025-02-20 20:48",
    "checkpoint-64520": "2025-02-20 21:28",
    "checkpoint-70972": "2025-02-20 22:08",
    "checkpoint-77424": "2025-02-20 22:48",
    "checkpoint-83876": "2025-02-20 23:29",
    "checkpoint-90328": "2025-02-21 00:09",
    "checkpoint-12813": "2025-02-20 11:12",
    "checkpoint-25624": "2025-02-20 12:52",
}

def combine_model_with_adapter(base_model_path, adapter_path, output_path):
    """Kombinerar basmodellen med en adapter och sparar resultatet"""
    
    logger.info(f"Laddar basmodell från: {base_model_path}")
    try:
        model = AutoModelForCausalLM.from_pretrained(str(base_model_path))
        tokenizer = AutoTokenizer.from_pretrained(str(base_model_path))
    except Exception as e:
        logger.error(f"Fel vid inläsning av basmodellen: {e}")
        return False

    logger.info(f"Laddar adapter från: {adapter_path}")
    try:
        # Ladda in adaptern med PEFT
        model = PeftModel.from_pretrained(model, str(adapter_path))
        logger.info("Adapter laddad framgångsrikt.")
    except Exception as e:
        logger.error(f"Fel vid laddning av adapter: {e}")
        return False

    logger.info("Försöker merge:a adaptervikter in i basmodellen...")
    try:
        if hasattr(model, "merge_and_unload"):
            model = model.merge_and_unload()
            logger.info("Adaptervikterna har mergats in med merge_and_unload().")
        else:
            logger.error("Modellen har inte metoden 'merge_and_unload'. Adapter merging stöds inte med denna version.")
            return False
    except Exception as e:
        logger.error(f"Fel vid sammanslagning av adaptervikter: {e}")
        return False

    # Skapa output-mappen om den inte finns
    output_path.mkdir(parents=True, exist_ok=True)
    
    logger.info(f"Sparar den kombinerade modellen till: {output_path}")
    try:
        model.save_pretrained(str(output_path))
        tokenizer.save_pretrained(str(output_path))
        logger.info("Kombinerad modell sparad korrekt.")
        return True
    except Exception as e:
        logger.error(f"Fel vid sparande av kombinerad modell: {e}")
        return False

def main():
    # Relativa sökvägar
    base_model_path = Path("./unsloth_Llama-3.2-1B-Instruct-bnb-4bit")
    output_dir = Path("./output")
    output2_dir = Path("./output2")
    
    # Samla alla checkpoints från båda mapparna
    checkpoints = []
    
    # Kontrollera output-mappen
    if output_dir.exists():
        checkpoints.extend([cp for cp in output_dir.iterdir() if cp.is_dir() and cp.name.startswith("checkpoint-")])
    
    # Kontrollera output2-mappen
    if output2_dir.exists():
        checkpoints.extend([cp for cp in output2_dir.iterdir() if cp.is_dir() and cp.name.startswith("checkpoint-")])
    
    if not checkpoints:
        logger.error("Inga checkpoints hittades i output eller output2 mapparna")
        return
    
    # Sortera checkpoints baserat på tidpunkterna i CHECKPOINT_TIMES
    checkpoints_with_times = []
    for cp in checkpoints:
        if cp.name in CHECKPOINT_TIMES:
            dt = datetime.strptime(CHECKPOINT_TIMES[cp.name], "%Y-%m-%d %H:%M")
            checkpoints_with_times.append((cp, dt))
        else:
            logger.warning(f"Kunde inte hitta tidpunkt för {cp.name}, hoppar över")
    
    # Sortera efter tidpunkt
    checkpoints_with_times.sort(key=lambda x: x[1])
    
    # Processa varje checkpoint i ordning
    for i, (checkpoint_path, time) in enumerate(checkpoints_with_times, 1):
        output_path = Path(f"./Copiax_{i:02d}")
        logger.info(f"Bearbetar checkpoint {i}/{len(checkpoints_with_times)}: {checkpoint_path.name} från {time}")
        
        success = combine_model_with_adapter(base_model_path, checkpoint_path, output_path)
        if success:
            logger.info(f"Framgångsrikt skapade Copiax_{i:02d} från {checkpoint_path.name}")
        else:
            logger.error(f"Misslyckades med att skapa Copiax_{i:02d} från {checkpoint_path.name}")

if __name__ == "__main__":
    main()