#!/usr/bin/env python3
import os
import json
import re
import argparse
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from typing import Any, Dict, List, Union
from transformers import AutoTokenizer

# --- Logging-setup ---
LOG_FILENAME = "processing.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILENAME, mode="w", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

# --- Rensa oönskade symboler och format ---
def clean_text(text: str) -> str:
    """
    Rensar bort oönskade symboler och formatering från texten.
    Rader som börjar med '|' (data tables) lämnas oförändrade.
    """
    lines = text.splitlines()
    cleaned_lines = []
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith('|'):
            cleaned_lines.append(line)
        else:
            line = re.sub(r'�+', '', line)
            line = re.sub(r'\s+', ' ', line)
            cleaned_lines.append(line.strip())
    cleaned_text = "\n".join(cleaned_lines)
    cleaned_text = re.sub(r'\n\s*\n+', '\n\n', cleaned_text)
    return cleaned_text

# --- TokenCounter-modul ---
@dataclass
class TokenCount:
    """Token count information."""
    total_tokens: int
    prompt_tokens: int
    completion_tokens: int = 0
    metadata: Dict[str, Any] = field(default_factory=dict)

class TokenCounter:
    """Räknar tokens för olika modelltyper."""
    
    def __init__(self, model_name: str = "gpt-3.5-turbo"):
        self.model_name = model_name
        self.tokenizer = None
        self._initialize_tokenizer()
        
    def _initialize_tokenizer(self) -> None:
        """Initialisera lämplig tokenizer baserat på modellnamn."""
        try:
            if "gpt" in self.model_name.lower():
                self.tokenizer = AutoTokenizer.from_pretrained("gpt2")
            elif "claude" in self.model_name.lower():
                self.tokenizer = AutoTokenizer.from_pretrained("gpt2")
            else:
                self.tokenizer = AutoTokenizer.from_pretrained("gpt2")
        except Exception as e:
            logging.error(f"Fel vid initialisering av tokenizer: {str(e)}")
            self.tokenizer = None

    def count_tokens(self, text: Union[str, Dict, List]) -> TokenCount:
        if isinstance(text, (dict, list)):
            text = str(text)
        try:
            if self.tokenizer:
                tokens = self.tokenizer.encode(text)
                return TokenCount(
                    total_tokens=len(tokens),
                    prompt_tokens=len(tokens),
                    metadata={"tokenizer": self.tokenizer.__class__.__name__}
                )
            else:
                words = text.split()
                tokens_estimate = len(words) + len(re.findall(r'[.!?]', text))
                return TokenCount(
                    total_tokens=tokens_estimate,
                    prompt_tokens=tokens_estimate,
                    metadata={"method": "approximation"}
                )
        except Exception as e:
            logging.error(f"Fel vid token-räkning: {str(e)}")
            return TokenCount(total_tokens=0, prompt_tokens=0)

    def check_token_limit(self, text: Union[str, Dict, List], limit: int) -> bool:
        count = self.count_tokens(text)
        return count.total_tokens <= limit

    def truncate_to_token_limit(self, text: str, limit: int) -> str:
        if not self.check_token_limit(text, limit):
            if self.tokenizer:
                tokens = self.tokenizer.encode(text)
                truncated_tokens = tokens[:limit]
                return self.tokenizer.decode(truncated_tokens)
            else:
                words = text.split()
                estimated_limit = int(limit / 1.3)
                return ' '.join(words[:estimated_limit])
        return text

# --- Funktion för att bearbeta en enskild fil i mindre batchar ---
def process_file(input_file_path: str, output_file_path: str, token_limit: int, model_name: str, batch_size: int = 100) -> List[str]:
    """
    Bearbetar en fil:
      1. Rensar varje 'ai_output' med clean_text.
      2. Bearbetar texten i mindre batchar för batch-tokenisering.
      3. Trimmar texten om tokenantalet överstiger token_limit.
    Returnerar en lista med loggrad för trimming-händelser.
    """
    local_logs = []
    token_counter = TokenCounter(model_name=model_name)
    logging.info(f"Bearbetar fil: {input_file_path}")
    try:
        with open(input_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # Rensa och uppdatera varje ai_output
        for entry in data:
            original_text = entry.get("ai_output", "")
            cleaned = clean_text(original_text)
            entry["ai_output"] = cleaned

        # Bearbeta entries i mindre batchar
        total = len(data)
        for start in range(0, total, batch_size):
            end = min(start + batch_size, total)
            texts = [entry.get("ai_output", "") for entry in data[start:end]]
            if token_counter.tokenizer:
                tokenized = token_counter.tokenizer(texts, add_special_tokens=False)["input_ids"]
                for i, tokens in enumerate(tokenized):
                    if len(tokens) > token_limit:
                        idx = start + i
                        user_input = data[idx].get("user_input", "")
                        log_msg = f"{user_input} Original tokenantal: {len(tokens)}"
                        local_logs.append(log_msg)
                        logging.info(f"Trimmar 'ai_output' för entry: {log_msg}")
                        truncated_tokens = tokens[:token_limit]
                        data[idx]["ai_output"] = token_counter.tokenizer.decode(truncated_tokens)
            else:
                # Fallback: Bearbeta en entry i taget
                for idx in range(start, end):
                    ai_output = data[idx].get("ai_output", "")
                    token_count = token_counter.count_tokens(ai_output)
                    if token_count.total_tokens > token_limit:
                        log_msg = f"{data[idx].get('user_input')} Original tokenantal: {token_count.total_tokens}"
                        local_logs.append(log_msg)
                        logging.info(f"Trimmar 'ai_output' för entry: {log_msg}")
                        data[idx]["ai_output"] = token_counter.truncate_to_token_limit(ai_output, token_limit)
        
        with open(output_file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logging.info(f"Bearbetad fil sparad till: {output_file_path}")
    except Exception as e:
        logging.error(f"Fel vid bearbetning av fil {input_file_path}: {str(e)}")
    
    return local_logs

# --- Huvudfunktion: Bearbeta träningsdata med parallell körning ---
def process_training_data(input_dir: str, output_dir: str, token_limit: int, model_name: str, batch_size: int = 100) -> None:
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    files = [f for f in os.listdir(input_dir) if f.endswith(".json")]
    all_logs = []
    with ThreadPoolExecutor(max_workers=6) as executor:
        future_to_file = {
            executor.submit(
                process_file,
                os.path.join(input_dir, filename),
                os.path.join(output_dir, filename),
                token_limit,
                model_name,
                batch_size
            ): filename
            for filename in files
        }
        for future in as_completed(future_to_file):
            file_logs = future.result()
            all_logs.extend(file_logs)
    
    summary_log_path = os.path.join(output_dir, "summary.log")
    try:
        with open(summary_log_path, "w", encoding="utf-8") as log_file:
            for log_line in all_logs:
                log_file.write(log_line + "\n")
        logging.info(f"Sammanfattande logg sparad till: {summary_log_path}")
    except Exception as e:
        logging.error(f"Fel vid sparande av sammanfattande logg: {str(e)}")

# --- Kör scriptet ---
if __name__ == "__main__":
    # Standardvärden
    INPUT_DIR = "./data/"
    OUTPUT_DIR = "data_with_cutted_tokens/"
    TOKEN_LIMIT = 2048
    MODEL_NAME = "gpt-3.5-turbo"
    BATCH_SIZE = 100  # Justera vid behov
    
    parser = argparse.ArgumentParser(
        description="Bearbeta och trimma 'ai_output' i träningsdata med rensning, batch-tokenisering och parallell körning"
    )
    parser.add_argument("--input_dir", type=str, default=INPUT_DIR, help="Mapp med JSON-filer för träningsdata")
    parser.add_argument("--output_dir", type=str, default=OUTPUT_DIR, help="Mapp där bearbetade filer sparas")
    parser.add_argument("--token_limit", type=int, default=TOKEN_LIMIT, help="Maximalt antal tokens tillåtna i 'ai_output'")
    parser.add_argument("--model_name", type=str, default=MODEL_NAME, help="Modellnamn att använda vid token-räkning")
    parser.add_argument("--batch_size", type=int, default=BATCH_SIZE, help="Antal entries per batch vid tokenisering")
    
    args = parser.parse_args()
    
    process_training_data(
        input_dir=args.input_dir,
        output_dir=args.output_dir,
        token_limit=args.token_limit,
        model_name=args.model_name,
        batch_size=args.batch_size
    )
