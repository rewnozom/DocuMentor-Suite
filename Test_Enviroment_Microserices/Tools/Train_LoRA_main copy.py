#!/usr/bin/env python3
import os
import glob
import json
import logging
import time
import torch

# -------------------------
# [Overview] - Loggning & GPU-kontroll
# -------------------------
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler()]
)

if not torch.cuda.is_available():
    raise EnvironmentError(
        "Inga NVIDIA GPU hittades! Unsloth kräver en NVIDIA GPU. "
        "Se till att du har installerat rätt NVIDIA-drivrutiner och använder en CUDA-kompatibel version av PyTorch.\n"
        "Testa med:\n\nimport torch\nprint(torch.cuda.is_available())"
    )

# -------------------------
# [ModelSetup] - Modell- & LoRA-Setup
# -------------------------
from unsloth import FastLanguageModel, is_bfloat16_supported
from unsloth.chat_templates import get_chat_template, train_on_responses_only

# Inställningar
max_seq_length = 88888
dtype = None
load_in_4bit = True
hf_token = "xxx"  # Ersätt med din HF-token

logging.info("Laddar modell och tokenizer...")
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Llama-3.2-1B-Instruct-bnb-4bit",
    max_seq_length=max_seq_length,
    dtype=dtype,
    load_in_4bit=load_in_4bit,
    token=hf_token
)

logging.info("Tillämpa LoRA-konfiguration...")
model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                    "gate_proj", "up_proj", "down_proj"],
    lora_alpha=16,
    lora_dropout=0.05,
    bias="none",
    use_gradient_checkpointing="unsloth",
    random_state=42,
    use_rslora=False,
    loftq_config=None,
)

# -------------------------
# [DataPrep] - Dataförberedelse och Processat Dataset
# -------------------------
from datasets import Dataset, load_from_disk

# Funktion för att kombinera JSON-filer
def combine_json_files(directory="fixed_data"):
    """
    Kombinerar alla JSON-filer i den angivna mappen till en enda lista.
    Varje fil förväntas innehålla antingen ett JSON-objekt eller en lista av objekt.
    """
    json_files = glob.glob(os.path.join(directory, "*.json"))
    all_data = []
    for file in json_files:
        logging.info(f"Läser fil: {file}")
        try:
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, list):
                all_data.extend(data)
            else:
                all_data.append(data)
        except Exception as e:
            logging.error(f"Fel vid inläsning av {file}: {e}")
    logging.info(f"Totalt antal exempel: {len(all_data)}")
    return all_data

# Funktion för att skapa konversationsstruktur
def create_conversation(example):
    try:
        return {
            "conversations": [
                {"role": "user", "content": example["user_input"]},
                {"role": "assistant", "content": example["ai_output"]}
            ]
        }
    except KeyError as e:
        logging.error(f"Nyckel saknas i data: {e}")
        raise

# Funktion för att applicera chat template
def formatting_prompts_func(examples):
    texts = []
    for convo in examples["conversations"]:
        try:
            text = tokenizer.apply_chat_template(convo, tokenize=False, add_generation_prompt=False)
            texts.append(text)
        except Exception as e:
            logging.error(f"Fel vid tillämpning av chat template: {e}")
            raise
    return {"text": texts}

# Sökväg för att spara/ladda det processade datasetet
PROCESSED_DATASET_PATH = "processed_dataset"

if os.path.exists(PROCESSED_DATASET_PATH):
    logging.info(f"Laddar färdigbehandlat dataset från {PROCESSED_DATASET_PATH}...")
    dataset = load_from_disk(PROCESSED_DATASET_PATH)
else:
    logging.info("Inget färdigbehandlat dataset hittades. Bearbetar data från början...")
    combined_data = combine_json_files("fixed_data")
    dataset = Dataset.from_list(combined_data)
    dataset = dataset.map(create_conversation)
    # Uppdatera tokenizer med chat template (ex. "llama-3.1")
    tokenizer = get_chat_template(tokenizer, chat_template="llama-3.1")
    dataset = dataset.map(formatting_prompts_func, batched=True)
    logging.info("Dataförberedelse klar. Sparar dataset till disk...")
    dataset.save_to_disk(PROCESSED_DATASET_PATH)

# -------------------------
# [Train] - Träna modellen
# -------------------------
from trl import SFTTrainer
from transformers import TrainingArguments, DataCollatorForSeq2Seq

num_epochs = 12  # Justera efter behov
warmup_ratio = 0.1
total_steps = len(dataset) * num_epochs
warmup_steps = int(total_steps * warmup_ratio)

training_args = TrainingArguments(
    num_train_epochs=num_epochs,
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    learning_rate=3e-4,
    lr_scheduler_type="cosine",
    warmup_steps=warmup_steps,
    optim="adamw_torch",
    weight_decay=0.03,
    fp16=not is_bfloat16_supported(),
    bf16=is_bfloat16_supported(),
    logging_steps=1,
    save_strategy="epoch",  # Sparar checkpoint efter varje epoch
    seed=42,
    output_dir="./output",  # Huvudkatalog för checkpoint-sparning
    report_to="none",
)

from transformers import TrainerCallback

class LocalSaveCallback(TrainerCallback):
    def on_epoch_end(self, args, state, control, **kwargs):
        # state.epoch kan vara en float, avrunda till närmsta heltal
        epoch = int(round(state.epoch))
        epoch_dir = os.path.join(args.output_dir, f"epoch_{epoch}")
        os.makedirs(epoch_dir, exist_ok=True)
        trainer = kwargs.get("trainer", None)
        if trainer is not None:
            logging.info(f"Sparar modellcheckpoint för epoch {epoch} i {epoch_dir}...")
            trainer.model.save_pretrained(epoch_dir)
            trainer.tokenizer.save_pretrained(epoch_dir)
        return control

# OBS! Vi sätter dataset_num_proc=1 för att undvika multiprocess-problem.
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
trainer = train_on_responses_only(
    trainer,
    instruction_part="<|start_header_id|>user<|end_header_id|>\n\n",
    response_part="<|start_header_id|>assistant<|end_header_id|>\n\n",
)

logging.info("Startar träning...")
trainer_stats = trainer.train()
logging.info("Träningen är klar.")

# -------------------------
# [SaveUpload] - Spara & Ladda upp modellen
# -------------------------
from huggingface_hub import HfApi, create_repo

hf_username = "rewnozom"       # Ersätt med ditt HF-användarnamn
model_name = "copiax_V1a.1"      # Ersätt med önskat modellnamn
REPO_ID = f"{hf_username}/{model_name}"

base_export = "model_export"
formats = {
    "lora": os.path.join(base_export, "lora"),
    "compiled": os.path.join(base_export, "compiled"),
    "gguf": os.path.join(base_export, "gguf")
}
for path in formats.values():
    os.makedirs(path, exist_ok=True)

logging.info("Sparar LoRA-modellen lokalt...")
trainer.model.save_pretrained(formats["lora"])
trainer.tokenizer.save_pretrained(formats["lora"])

logging.info("Sparar kompilerad version lokalt...")
try:
    model_compiled = torch.compile(trainer.model)
    model_compiled.save_pretrained(formats["compiled"])
    trainer.tokenizer.save_pretrained(formats["compiled"])
except Exception as e:
    logging.error(f"Fel vid kompilering: {e}")

logging.info("Skapar GGUF-versioner lokalt...")
quant_methods = ["q2_k", "q3_k_m", "q4_0", "q4_k_m", "q5_0", "q5_k_m", "q6_k", "q8_0", "f16", "f32"]
try:
    trainer.model.save_pretrained_gguf(formats["gguf"], trainer.tokenizer, quantization_method=quant_methods)
except Exception as e:
    logging.error(f"Fel vid skapande av GGUF-versioner: {e}")

readme_content = f"""# {model_name}

Detta är en finetunad LoRA-modell för DocuMentor-Suite.

## Modellformat

- **LoRA**: Sparad i `/lora`
- **Compiled**: Sparad i `/compiled`
- **GGUF**: Sparad i `/gguf` med följande kvantiseringar:
{chr(10).join(['  - ' + method for method in quant_methods])}

## Träningsdetaljer
- Epochs: {num_epochs}
- Learning Rate: 3e-4
- LoRA Rank: 16
- LoRA Dropout: 0.05
- Scheduler: Cosine
- Max Sequence Length: {max_seq_length} tokens
"""

readme_path = os.path.join(base_export, "README.md")
with open(readme_path, "w") as f:
    f.write(readme_content)

logging.info("Laddar upp modellen till Hugging Face Hub...")
try:
    create_repo(repo_id=REPO_ID, token=hf_token, private=False, repo_type="model", exist_ok=True)
except Exception as e:
    logging.warning(f"Repo-skapande/uppdatering: {e}")

api = HfApi()
outputs_dir = "./output"
if os.path.exists(outputs_dir):
    for checkpoint_dir in sorted(os.listdir(outputs_dir)):
        checkpoint_path = os.path.join(outputs_dir, checkpoint_dir)
        if os.path.isdir(checkpoint_path) and checkpoint_dir.startswith("epoch_"):
            logging.info(f"Laddar upp checkpoint: {checkpoint_path}")
            try:
                api.upload_folder(
                    folder_path=checkpoint_path,
                    repo_id=REPO_ID,
                    repo_type="model",
                    token=hf_token
                )
            except Exception as e:
                logging.error(f"Fel vid uppladdning av {checkpoint_path}: {e}")
else:
    logging.warning("Mappen './output' hittades inte.")

try:
    api.upload_folder(
        folder_path=base_export,
        repo_id=REPO_ID,
        repo_type="model",
        token=hf_token
    )
except Exception as e:
    logging.error(f"Fel vid uppladdning av huvudmodellen: {e}")

logging.info(f"Uppladdning klar! Modellen finns nu på: https://huggingface.co/{REPO_ID}")

# -------------------------
# [Overview] - Checkpoints & Översikt
# -------------------------
output_dir = "./output"
if os.path.exists(output_dir):
    checkpoints = [f for f in os.listdir(output_dir) if f.startswith("epoch_")]
    if checkpoints:
        print("Sparade checkpoints:", checkpoints)
    else:
        print("⚠️ Inga checkpoints hittades i './output/'.")
else:
    print("⚠️ './output/' katalogen finns inte.")

print("\nTränings- och modell-exportpipen är klar!")
