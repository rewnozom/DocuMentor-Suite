from unsloth import FastLanguageModel

class ModelManager:
    def __init__(self, model_name, max_seq_length, dtype, load_in_4bit):
        self.model_name = model_name
        self.max_seq_length = max_seq_length
        self.dtype = dtype
        self.load_in_4bit = load_in_4bit
        self.model = None
        self.tokenizer = None

    def load_model(self):
        print(f"Loading model {self.model_name}")
        self.model, self.tokenizer = FastLanguageModel.from_pretrained(
            model_name=self.model_name,
            max_seq_length=self.max_seq_length,
            dtype=self.dtype,
            load_in_4bit=self.load_in_4bit,
        )
        return self.model, self.tokenizer

    def get_model(self):
        return self.model, self.tokenizer
