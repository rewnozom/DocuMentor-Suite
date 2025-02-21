import os

class FileManager:
    @staticmethod
    def save_model(model, tokenizer, save_path):
        print(f"Saving model to {save_path}")
        model.save_pretrained(save_path)
        tokenizer.save_pretrained(save_path)

    @staticmethod
    def load_file(file_path):
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                data = f.read()
            return data
        else:
            raise FileNotFoundError(f"{file_path} does not exist")
