#!/usr/bin/env python3
"""
combine_model.py – Kombinerar den färdigtränade modellen med sin LoRA-adapter

Detta script:
  • Laddar in basmodellen från den relativa sökvägen "./unsloth_Llama-3.2-1B-Instruct-bnb-4bit".
  • Laddar in adaptervikterna från "./unsloth_Llama-3.2-1B-Instruct-bnb-4bit/checkpoint-25624/".
  • Mergar adaptervikterna in i basmodellen, antingen med metoden merge_and_unload()
    eller genom att använda merge_lora_weights från peft.
  • Sparar den kombinerade modellen (och dess tokenizer) i mappen "./copiax/".

Kör scriptet med:
    python combine_model.py
"""

import os
import logging
from pathlib import Path
import torch
import traceback

from unsloth import FastLanguageModel

# Konfigurera loggning
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

def main():
    # Ange relativa sökvägar
    base_model_path = Path("./unsloth_Llama-3.2-1B-Instruct-bnb-4bit")
    adapter_dir = Path("./unsloth_Llama-3.2-1B-Instruct-bnb-4bit/checkpoint-25624")
    output_dir = Path("./copiax")
    
    logger.info(f"Laddar basmodell från: {base_model_path}")
    try:
        model, tokenizer = FastLanguageModel.from_pretrained(str(base_model_path))
    except Exception as e:
        logger.error(f"Fel vid inläsning av basmodellen: {e}")
        return

    logger.info(f"Laddar adapter från: {adapter_dir}")
    try:
        # Ladda in adaptervikterna från den angivna adapter-mappen
        model.load_adapter(str(adapter_dir))
        logger.info("Adapter laddad framgångsrikt.")
    except Exception as e:
        logger.error(f"Fel vid laddning av adapter: {e}")
        return

    logger.info("Mergar adaptervikter in i basmodellen...")
    try:
        # Försök använda merge_and_unload() om den finns
        if hasattr(model, "merge_and_unload"):
            model = model.merge_and_unload()
            logger.info("Adaptervikter har mergats in med merge_and_unload().")
        else:
            # Annars, försök använda merge_lora_weights från peft (om tillgängligt)
            from peft import merge_lora_weights
            model = merge_lora_weights(model)
            logger.info("Adaptervikter har mergats in med merge_lora_weights().")
    except Exception as e:
        logger.error(f"Fel vid sammanslagning av adaptervikter: {e}")
        logger.error(traceback.format_exc())
        return

    # Skapa utmatningskatalogen om den inte redan finns
    output_dir.mkdir(parents=True, exist_ok=True)
    logger.info(f"Sparar den kombinerade modellen till: {output_dir}")
    try:
        model.save_pretrained(str(output_dir))
        tokenizer.save_pretrained(str(output_dir))
        logger.info("Kombinerad modell sparad korrekt.")
    except Exception as e:
        logger.error(f"Fel vid sparande av kombinerad modell: {e}")

if __name__ == "__main__":
    main()
