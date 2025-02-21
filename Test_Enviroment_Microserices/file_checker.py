#!/usr/bin/env python3
import os
import json
import glob
import argparse
import logging
import yaml
import pandas as pd
from pathlib import Path
from transformers import AutoTokenizer

def load_config(path: str = "conversion_config.yaml") -> dict:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    else:
        return {
            "json_input_directory": "./json_input",
            "parquet_input_directory": "./parquet_input",
            "token_limit": 2048,
            "model_name": "gpt-3.5-turbo",
            "log_level": "INFO"
        }

CONFIG = load_config()

logging.basicConfig(
    level=getattr(logging, CONFIG.get("log_level", "INFO")),
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

class TokenCounter:
    """Räknar tokens för text med en transformer-tokenizer."""
    def __init__(self, model_name: str = "gpt-3.5-turbo"):
        self.model_name = model_name
        self.tokenizer = None
        self._initialize_tokenizer()
        
    def _initialize_tokenizer(self):
        try:
            if "gpt" in self.model_name.lower():
                self.tokenizer = AutoTokenizer.from_pretrained("gpt2")
            else:
                self.tokenizer = AutoTokenizer.from_pretrained("gpt2")
        except Exception as e:
            logger.error(f"Fel vid initialisering av tokenizer: {e}")
            self.tokenizer = None

    def count_tokens(self, text: str) -> int:
        try:
            if self.tokenizer:
                tokens = self.tokenizer.encode(text)
                return len(tokens)
            else:
                return len(text.split())
        except Exception as e:
            logger.error(f"Fel vid token-räkning: {e}")
            return 0

def check_files(input_dir: str, file_type: str, token_limit: int, model_name: str):
    """
    Kontrollerar att filer av angiven typ (json eller parquet) är giltiga.
    JSON-filer kontrolleras genom att räkna tokens i "ai_output", och Parquet-filer genom att läsa in dataframe.
    """
    input_dir_path = Path(input_dir)
    files = list(input_dir_path.glob(f"*.{file_type}"))
    if not files:
        logger.error(f"🚨 Inga {file_type.upper()}-filer hittades i {input_dir}")
        return

    violations = []
    logger.info(f"Startar kontroll av {len(files)} {file_type.upper()}-filer i {input_dir}")

    if file_type.lower() == "json":
        token_counter = TokenCounter(model_name=model_name)
        for file in files:
            try:
                with open(file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                for entry in data:
                    ai_output = entry.get("ai_output", "")
                    num_tokens = token_counter.count_tokens(ai_output)
                    if num_tokens > token_limit:
                        violations.append((file.name, entry.get("user_input", "Okänd input"), num_tokens))
                        logger.warning(f"⚠️ {file.name} - {entry.get('user_input', 'Okänd input')} ({num_tokens} tokens)")
            except Exception as e:
                logger.error(f"Fel vid läsning av {file}: {e}")
    elif file_type.lower() == "parquet":
        for file in files:
            try:
                df = pd.read_parquet(file)
                logger.info(f"📄 {file.name} lästes in med form: {df.shape}")
            except Exception as e:
                violations.append((file.name, str(e)))
                logger.error(f"⚠️ Fel vid läsning av {file.name}: {e}")

    # Sammanfattning
    summary_path = input_dir_path / f"{file_type}_validation_summary.log"
    with open(summary_path, "w", encoding="utf-8") as summary_file:
        summary_file.write(f"Kontrollerade {len(files)} {file_type.upper()}-filer i {input_dir}\n\n")
        if violations:
            summary_file.write("Följande filer/entries överstiger gränsen eller är ogiltiga:\n")
            for violation in violations:
                summary_file.write(" - " + " | ".join(str(v) for v in violation) + "\n")
        else:
            summary_file.write("✔️ Alla filer är giltiga!\n")
    logger.info(f"Sammanfattningsrapport sparad till: {summary_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Kontrollera giltigheten av JSON- eller Parquet-filer."
    )
    parser.add_argument("--input_dir", type=str, default=CONFIG.get("json_input_directory"), help="Katalog med filer att kontrollera")
    parser.add_argument("--file_type", type=str, choices=["json", "parquet"], default="json", help="Filtyp att kontrollera")
    parser.add_argument("--token_limit", type=int, default=CONFIG.get("token_limit"), help="Maximalt antal tokens (endast JSON)")
    parser.add_argument("--model_name", type=str, default=CONFIG.get("model_name"), help="Modellnamn för token-räkning")
    args = parser.parse_args()
    
    check_files(args.input_dir, args.file_type, args.token_limit, args.model_name)
