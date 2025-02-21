from unsloth import FastLanguageModel

class LoraManager:
    def __init__(self, model, config):
        self.model = model
        self.config = config

    def apply_lora(self):
        print("Applying LoRA settings")
        self.model = FastLanguageModel.get_peft_model(
            self.model,
            r=self.config.get("LORA_R", 16),
            target_modules=self.config.get("TARGET_MODULES", []),
            lora_alpha=self.config.get("LORA_ALPHA", 16),
            lora_dropout=self.config.get("LORA_DROPOUT", 0),
            bias=self.config.get("BIAS", "none"),
            use_gradient_checkpointing=self.config.get("USE_GRADIENT_CHECKPOINTING", "unsloth"),
            random_state=self.config.get("RANDOM_STATE", 3407),
            use_rslora=self.config.get("USE_RSLORA", False),
            loftq_config=self.config.get("LOFTQ_CONFIG", None),
        )
        return self.model
