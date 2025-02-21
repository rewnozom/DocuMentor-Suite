#!/usr/bin/env python3
"""
Main.py – Träningspipeline för LoRA-modellen med fullständig export

Denna pipeline:
  • Kontrollerar att en NVIDIA GPU finns.
  • Laddar en förtränad modell och applicerar LoRA-konfiguration.
  • Laddar träningsdata från en kombinerad Parquet-fil (ex. "combined_dedup_final.parquet")
    via Hugging Face Datasets.
  • Förbereder data med ett chat-template, tränar modellen med SFTTrainer från TRL,
    och sparar checkpoints.
  • Kompilerar modellen och sparar den i en separat mapp ("output2/compiled/").
  • Uppdaterar modellens namn genom att lägga till suffixet "(Copiax)".
  • Laddar upp hela modellen (adapter, kompilerad version, m.m.) till Hugging Face Hub.
  
Alla inställningar (sökvägar, modellparametrar, träningsparametrar, etc.) styrs via YAML‑filen "train_config.yaml".
"""

import os
import shutil
import logging
from pathlib import Path
from typing import Dict

import torch
import pandas as pd
import yaml

# -------------------------
# [Configuration] - Ladda YAML-inställningar
# -------------------------
def load_config(path: str = "train_config.yaml") -> dict:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    else:
        # Standardinställningar (justera efter behov)
        return {
            "parquet_dataset_path": "./combined_dedup_final.parquet",
            "processed_dataset_path": "processed_dataset",
            "output_dir": "./output2",
            "compiled_dir": "./output2/compiled",
            "max_seq_length": 6666,
            "load_in_4bit": True,
            "lora": {
                "r": 16,
                "lora_alpha": 16,
                "lora_dropout": 0.05,
                "target_modules": ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]
            },
            "num_epochs": 33,
            "per_device_train_batch_size": 2,
            "gradient_accumulation_steps": 4,
            "learning_rate": 3e-4,
            "warmup_ratio": 0.1,
            "output_model_repo": "rewnozom/Copiax_V1a.1",  # Repo-ID med "(Copiax)" i namnet
            "hf_token": "xxx",
            "log_level": "INFO",
            "chat_template": "llama-3.1"
        }

CONFIG = load_config()

# -------------------------
# [Logging & GPU Check]
# -------------------------
logging.basicConfig(
    level=getattr(logging, CONFIG.get("log_level", "INFO")),
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

if not torch.cuda.is_available():
    raise EnvironmentError(
        "Inga NVIDIA GPU hittades! Unsloth kräver en NVIDIA GPU. "
        "Se till att du har installerat rätt NVIDIA-drivrutiner och använder en CUDA-kompatibel version av PyTorch."
    )

# -------------------------
# [Model Setup] - Modell- & LoRA-Setup
# -------------------------
from unsloth import FastLanguageModel, is_bfloat16_supported
from unsloth.chat_templates import get_chat_template, train_on_responses_only

max_seq_length = CONFIG.get("max_seq_length")
dtype = None
load_in_4bit = CONFIG.get("load_in_4bit", True)
hf_token = CONFIG.get("hf_token")

logger.info("Laddar modell och tokenizer...")
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Llama-3.2-1B-Instruct-bnb-4bit",
    max_seq_length=max_seq_length,
    dtype=dtype,
    load_in_4bit=load_in_4bit,
    token=hf_token
)

logger.info("Tillämpa LoRA-konfiguration...")
lora_config = CONFIG.get("lora", {})
model = FastLanguageModel.get_peft_model(
    model,
    r=lora_config.get("r", 16),
    target_modules=lora_config.get("target_modules", []),
    lora_alpha=lora_config.get("lora_alpha", 16),
    lora_dropout=lora_config.get("lora_dropout", 0.05),
    bias="none",
    use_gradient_checkpointing="unsloth",
    random_state=42,
    use_rslora=False,
    loftq_config=None,
)

# -------------------------
# [DataPrep] - Ladda träningsdata från Parquet
# -------------------------
from datasets import Dataset

PARQUET_PATH = CONFIG.get("parquet_dataset_path")
if os.path.exists(PARQUET_PATH):
    logger.info(f"Laddar träningsdata från Parquet: {PARQUET_PATH}")
    df = pd.read_parquet(PARQUET_PATH)
    logger.info(f"📊 Dataform: {df.shape}")
    dataset = Dataset.from_pandas(df)
else:
    logger.error(f"🚨 Kombinerad Parquet-fil hittades inte: {PARQUET_PATH}")
    raise FileNotFoundError(f"Kunde inte hitta {PARQUET_PATH}")

# Tillämpa chat template
logger.info("Tillämpa chat template...")
tokenizer = get_chat_template(tokenizer, chat_template=CONFIG.get("chat_template"))
def create_conversation(example):
    return {
        "conversations": [
            {"role": "user", "content": example["user_input"]},
            {"role": "assistant", "content": example["ai_output"]}
        ]
    }
dataset = dataset.map(create_conversation)
def formatting_prompts_func(examples):
    texts = []
    for convo in examples["conversations"]:
        try:
            text = tokenizer.apply_chat_template(convo, tokenize=False, add_generation_prompt=False)
            texts.append(text)
        except Exception as e:
            logger.error(f"Fel vid tillämpning av chat template: {e}")
            raise
    return {"text": texts}
dataset = dataset.map(formatting_prompts_func, batched=True)
logger.info("Dataförberedelse klar.")

# Spara dataset till disk (om önskat)
PROCESSED_DATASET_PATH = CONFIG.get("processed_dataset_path")
if PROCESSED_DATASET_PATH:
    dataset.save_to_disk(PROCESSED_DATASET_PATH)
    logger.info(f"Dataset sparat till disk: {PROCESSED_DATASET_PATH}")

# -------------------------
# [Train] - Träna modellen
# -------------------------
from trl import SFTTrainer
from transformers import TrainingArguments, DataCollatorForSeq2Seq

num_epochs = CONFIG.get("num_epochs", 33)
warmup_ratio = CONFIG.get("warmup_ratio", 0.1)
total_steps = len(dataset) * num_epochs
warmup_steps = int(total_steps * warmup_ratio)

training_args = TrainingArguments(
    num_train_epochs=num_epochs,
    per_device_train_batch_size=CONFIG.get("per_device_train_batch_size", 2),
    gradient_accumulation_steps=CONFIG.get("gradient_accumulation_steps", 4),
    learning_rate=CONFIG.get("learning_rate", 3e-4),
    lr_scheduler_type="cosine",
    warmup_steps=warmup_steps,
    optim="adamw_torch",
    weight_decay=0.03,
    fp16=not is_bfloat16_supported(),
    bf16=is_bfloat16_supported(),
    logging_steps=1,
    save_strategy="epoch",
    seed=42,
    output_dir=CONFIG.get("output_dir", "./output2"),
    report_to="none",
)

from transformers import TrainerCallback

class LocalSaveCallback(TrainerCallback):
    def on_epoch_end(self, args, state, control, **kwargs):
        epoch = int(round(state.epoch))
        epoch_dir = os.path.join(args.output_dir, f"epoch_{epoch}")
        os.makedirs(epoch_dir, exist_ok=True)
        trainer = kwargs.get("trainer", None)
        if trainer is not None:
            logging.info(f"Sparar modellcheckpoint för epoch {epoch} i {epoch_dir}...")
            trainer.model.save_pretrained(epoch_dir)
            trainer.tokenizer.save_pretrained(epoch_dir)
        return control

trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset,
    dataset_text_field="text",
    max_seq_length=max_seq_length,
    data_collator=DataCollatorForSeq2Seq(tokenizer=tokenizer),
    dataset_num_proc=1,
    packing=False,
    args=training_args,
    callbacks=[LocalSaveCallback()]
)

# Anpassa tränaren så att endast assistentens svar tränas
from unsloth.chat_templates import train_on_responses_only
trainer = train_on_responses_only(
    trainer,
    instruction_part="<|start_header_id|>user<|end_header_id|>\n\n",
    response_part="<|start_header_id|>assistant<|end_header_id|>\n\n",
)

logger.info("Startar träning...")
trainer_stats = trainer.train()
logger.info("Träningen är klar.")

# -------------------------
# [Compile Model] - Kompilera modellen
# -------------------------
compiled_dir = Path(CONFIG.get("compiled_dir", "./output2/compiled"))
compiled_dir.mkdir(parents=True, exist_ok=True)
logger.info("Kompilerar modellen...")
try:
    model_compiled = torch.compile(trainer.model)
    model_compiled.save_pretrained(str(compiled_dir))
    trainer.tokenizer.save_pretrained(str(compiled_dir))
    logger.info(f"✅ Kompilerad modell sparad i: {compiled_dir}")
except Exception as e:
    logger.error(f"Fel vid kompilering: {e}")

# -------------------------
# [Save & Upload] - Spara & ladda upp modellen
# -------------------------
from huggingface_hub import HfApi, create_repo

hf_username = "rewnozom"  # Ersätt med ditt HF-användarnamn
# Använd det repo-ID som redan innehåller suffixet (Copiax)
model_repo = CONFIG.get("output_model_repo", "rewnozom/Copiax_V1a.1")
REPO_ID = model_repo  # Exempel: "rewnozom/Copiax_V1a.1"

base_export = "model_export"
formats = {
    "lora": os.path.join(base_export, "lora"),
    "compiled": os.path.join(base_export, "compiled"),
    "gguf": os.path.join(base_export, "gguf")
}
for path in formats.values():
    os.makedirs(path, exist_ok=True)

logger.info("Sparar LoRA-modellen lokalt...")
trainer.model.save_pretrained(formats["lora"])
trainer.tokenizer.save_pretrained(formats["lora"])

logger.info("Sparar kompilerad version lokalt...")
try:
    # Vi använder den kompilerade modellen vi sparade tidigare
    shutil.copytree(compiled_dir, formats["compiled"], dirs_exist_ok=True)
    logger.info("✅ Kompilerad version kopierad till export-mappen.")
except Exception as e:
    logger.error(f"Fel vid kopiering av kompilerad version: {e}")

logger.info("Skapar GGUF-versioner lokalt...")
quant_methods = ["q2_k", "q3_k_m", "q4_0", "q4_k_m", "q5_0", "q5_k_m", "q6_k", "q8_0", "f16", "f32"]
try:
    trainer.model.save_pretrained_gguf(formats["gguf"], trainer.tokenizer, quantization_method=quant_methods)
except Exception as e:
    logger.error(f"Fel vid skapande av GGUF-versioner: {e}")

readme_content = f"""# {model_repo}

Detta är en finetunad LoRA-modell för DocuMentor-Suite, med fullständig produktinformation (Copiax).

## Modellformat

- **LoRA**: Sparad i `/lora`
- **Compiled**: Sparad i `/compiled`
- **GGUF**: Sparad i `/gguf` med följande kvantiseringar:
{chr(10).join(['  - ' + method for method in quant_methods])}

## Träningsdetaljer
- Epochs: {num_epochs}
- Learning Rate: {CONFIG.get("learning_rate", 3e-4)}
- LoRA Rank: {lora_config.get("r", 16)}
- LoRA Dropout: {lora_config.get("lora_dropout", 0.05)}
- Scheduler: Cosine
- Max Sequence Length: {max_seq_length} tokens
"""

readme_path = os.path.join(base_export, "README.md")
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

logger.info("Laddar upp modellen till Hugging Face Hub...")
try:
    create_repo(repo_id=REPO_ID, token=CONFIG.get("hf_token"), private=False, repo_type="model", exist_ok=True)
except Exception as e:
    logger.warning(f"Repo-skapande/uppdatering: {e}")

from huggingface_hub import HfApi
api = HfApi()
outputs_dir = CONFIG.get("output_dir", "./output2")
if os.path.exists(outputs_dir):
    for checkpoint_dir in sorted(os.listdir(outputs_dir)):
        checkpoint_path = os.path.join(outputs_dir, checkpoint_dir)
        if os.path.isdir(checkpoint_path) and checkpoint_dir.startswith("epoch_"):
            logger.info(f"Laddar upp checkpoint: {checkpoint_path}")
            try:
                api.upload_folder(
                    folder_path=checkpoint_path,
                    repo_id=REPO_ID,
                    repo_type="model",
                    token=CONFIG.get("hf_token")
                )
            except Exception as e:
                logger.error(f"Fel vid uppladdning av {checkpoint_path}: {e}")
else:
    logger.warning("Mappen './output2/' hittades inte.")

try:
    api.upload_folder(
        folder_path=base_export,
        repo_id=REPO_ID,
        repo_type="model",
        token=CONFIG.get("hf_token")
    )
except Exception as e:
    logger.error(f"Fel vid uppladdning av huvudmodellen: {e}")

logger.info(f"Uppladdning klar! Modellen finns nu på: https://huggingface.co/{REPO_ID}")

# -------------------------
# [Overview] - Checkpoints & Översikt
# -------------------------
if os.path.exists(outputs_dir):
    checkpoints = [f for f in os.listdir(outputs_dir) if f.startswith("epoch_")]
    if checkpoints:
        print("Sparade checkpoints:", checkpoints)
    else:
        print("⚠️ Inga checkpoints hittades i './output2/'.")
else:
    print("⚠️ './output2/' katalogen finns inte.")

print("\nTränings- och modell-exportpipen är klar!")
