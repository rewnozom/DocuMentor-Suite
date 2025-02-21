from transformers import TrainingArguments, DataCollatorForSeq2Seq
from trl import SFTTrainer
from unsloth import is_bfloat16_supported
from unsloth.chat_templates import standardize_sharegpt, train_on_responses_only
from datasets import load_dataset
import os

class TrainingManager:
    def __init__(self, model, tokenizer, config):
        self.model = model
        self.tokenizer = tokenizer
        self.config = config

    def load_dataset(self, dataset_path, dataset_format="json"):
        ext = os.path.splitext(dataset_path)[-1].lower()
        print(f"Loading dataset: {dataset_path} with format {ext}")
        if ext == ".json":
            dataset = load_dataset("json", data_files=dataset_path)["train"]
        elif ext == ".csv":
            dataset = load_dataset("csv", data_files=dataset_path)["train"]
        elif ext in [".parquet", ".pq"]:
            dataset = load_dataset("parquet", data_files=dataset_path)["train"]
        else:
            raise ValueError("Unsupported dataset format")
        return dataset

    def prepare_dataset(self, dataset):
        def formatting_prompts_func(examples):
            convos = examples.get("conversations", [])
            texts = [
                self.tokenizer.apply_chat_template(convo, tokenize=False, add_generation_prompt=False)
                for convo in convos
            ]
            examples["text"] = texts
            return examples

        dataset = standardize_sharegpt(dataset)
        dataset = dataset.map(formatting_prompts_func, batched=True)
        return dataset

    def train(self, dataset_path):
        dataset = self.load_dataset(dataset_path)
        dataset = self.prepare_dataset(dataset)
        
        training_args = TrainingArguments(
            per_device_train_batch_size=int(self.config.get("batch_size", 2)),
            gradient_accumulation_steps=int(self.config.get("grad_accumulation", 1)),
            warmup_steps=int(self.config.get("warmup_epochs", 0.1)*100),  # Omvandla om nödvändigt
            max_steps=int(self.config.get("max_steps", 60)),
            learning_rate=float(self.config.get("learning_rate", 0.0003)),
            fp16=not is_bfloat16_supported(),
            bf16=is_bfloat16_supported(),
            logging_steps=int(self.config.get("logging_steps", 1)),
            optim=self.config.get("optimizer", "adamw_8bit"),
            weight_decay=float(self.config.get("weight_decay", 0)),
            lr_scheduler_type=self.config.get("schedule", "Cosine"),
            seed=int(self.config.get("seed", 42)),
            output_dir=self.config.get("output_dir", "./outputs"),
            report_to=self.config.get("report_to", "none"),
        )
        
        data_collator = DataCollatorForSeq2Seq(tokenizer=self.tokenizer)
        trainer = SFTTrainer(
            model=self.model,
            tokenizer=self.tokenizer,
            train_dataset=dataset,
            dataset_text_field="text",
            max_seq_length=int(self.config.get("max_seq_length", 2048)),
            data_collator=data_collator,
            dataset_num_proc=2,
            packing=False,
            args=training_args,
        )
        
        if self.config.get("train_only_responses", True):
            trainer = train_on_responses_only(
                trainer,
                instruction_part="<|start_header_id|>user<|end_header_id>\n\n",
                response_part="<|start_header_id|>assistant<|end_header_id>\n\n",
            )
            print("Training on responses only.")
        else:
            print("Training on full conversations.")
        
        trainer_stats = trainer.train()
        print("Training complete.")
        return trainer_stats
