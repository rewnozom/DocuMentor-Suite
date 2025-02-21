try:
    from unsloth.chat_templates import get_chat_template
except NotImplementedError as e:
    print("Warning: UnsLoth requires an NVIDIA GPU. Running in CPU mode for testing purposes.")
    # Här kan du eventuellt definiera en dummy-version av get_chat_template
    def get_chat_template(tokenizer, chat_template="default"):
        return tokenizer

from transformers import TextStreamer
import torch

class InferenceManager:
    def __init__(self, model, tokenizer, config):
        self.model = model
        self.tokenizer = tokenizer
        self.config = config

    def run_inference(self, prompt):
        messages = [{"role": "user", "content": prompt}]
        inputs = self.tokenizer.apply_chat_template(
            messages,
            tokenize=True,
            add_generation_prompt=True,
            return_tensors="pt",
        ).to("cuda" if torch.cuda.is_available() else "cpu")
        outputs = self.model.generate(
            input_ids=inputs["input_ids"],
            max_new_tokens=int(self.config.get("inference_max_length", 64)),
            use_cache=True,
            temperature=float(self.config.get("temperature", 1)),
            min_p=0.0,
        )
        decoded_output = self.tokenizer.batch_decode(outputs)
        print("Inference output:", decoded_output)
        return decoded_output

    def run_inference_with_streamer(self, prompt):
        messages = [{"role": "user", "content": prompt}]
        inputs = self.tokenizer.apply_chat_template(
            messages,
            tokenize=True,
            add_generation_prompt=True,
            return_tensors="pt",
        ).to("cuda" if torch.cuda.is_available() else "cpu")
        streamer = TextStreamer(self.tokenizer, skip_prompt=True)
        self.model.generate(
            input_ids=inputs["input_ids"],
            streamer=streamer,
            max_new_tokens=int(self.config.get("inference_max_length", 64)),
            use_cache=True,
            temperature=float(self.config.get("temperature", 1)),
            min_p=0.0,
        )
