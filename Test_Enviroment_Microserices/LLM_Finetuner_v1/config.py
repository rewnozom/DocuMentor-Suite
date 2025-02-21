# config.py
# Globala konfigurationsparametrar för applikationen.
CONFIG = {
    # Experimentinställningar
    "experiment_name": "Copiax-Tobias-Raanaes_V0.01.1.1",
    "dataset": "auto-analyzer-data_v1",
    "llm_backbone": "h2oai/h2o-danube3-500m-base",
    
    # Modellinställningar
    "model_name": "unsloth/Llama-3.2-3B-Instruct",
    "output_dir": "./outputs",
    "max_seq_length": 2048,
    "dtype": None,            # Exempel: None, torch.float16, etc.
    "load_in_4bit": True,

    # LoRA-inställningar
    "lora": True,
    "LORA_R": 4,             # Rekommenderat värde enligt tabell
    "LORA_ALPHA": 16,
    "LORA_DROPOUT": 0.05,
    "BIAS": "none",
    "USE_GRADIENT_CHECKPOINTING": "unsloth",
    "RANDOM_STATE": 3407,
    "USE_RSLORA": False,
    "LOFTQ_CONFIG": None,

    # Datasetinställningar
    "train_dataframe": "combined_dataset.parquet",
    "validation_strategy": "Automatic holdout validation",
    "validation_size": 0.01,  # Överväg att öka till 0.05
    "prompt_column": "user_input",
    "answer_column": "ai_output",
    "prompt_column_separator": "\n\n",
    "text_prompt_start": "<prompt>",
    "text_answer_separator": "<answer>",
    "add_eos_token_to_prompt": True,
    "add_eos_token_to_answer": True,
    "mask_prompt_labels": True,
    "max_length": 80000,  # Rekommenderas sänkas till 4096-8192 vid behov

    # Träningsinställningar
    "loss_function": "TokenAveragedCrossEntropy",
    "metric": "Perplexity",
    "optimizer": "AdamW",   # Alternativ: "adamw_8bit", "AdamW"
    "learning_rate": 0.0003,  # Alternativ: 2e-4 kan ge bättre stabilitet
    "batch_size": 2,          # Testa 4-8 om VRAM tillåter
    "epochs": 9,
    "schedule": "Cosine",
    "warmup_epochs": 0.1,
    "weight_decay": 0,
    "gradient_clip": 0,
    "grad_accumulation": 1,

    # Inferensinställningar
    "inference_max_length": 512,
    "inference_batch_size": 6,
    "temperature": 1,
    "repetition_penalty": 1,
    "top_k": 0,
    "top_p": 1,

    # Miljöinställningar
    "gpu": "GPU #1",
    "mixed_precision": True,
    "mixed_precision_dtype": "float16",
    "compile_model": True,
    "use_deepspeed": False,
    "find_unused_parameters": True,
    "trust_remote_code": True,
    "number_of_workers": 4,
    "seed": 42,

    # Övriga inställningar
    "train_model": False,
    "train_only_responses": True,
}
