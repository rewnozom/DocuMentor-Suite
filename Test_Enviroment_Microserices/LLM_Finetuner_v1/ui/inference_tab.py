from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from config import CONFIG
from backend.inference.inference_manager import InferenceManager
from backend.model.model_manager import ModelManager
from unsloth import FastLanguageModel

class InferenceTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.setup_inference_manager()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        self.info_label = QLabel("Inference Module")
        layout.addWidget(self.info_label)
        
        self.run_inference_button = QPushButton("Run Inference")
        self.run_inference_button.clicked.connect(self.run_inference)
        layout.addWidget(self.run_inference_button)
    
    def setup_inference_manager(self):
        # Här laddas modell och tokenizer – i praktiken borde de vara laddade en gång globalt.
        self.model_manager = ModelManager(CONFIG["model_name"], CONFIG["max_seq_length"], CONFIG["dtype"], CONFIG["load_in_4bit"])
        self.model, self.tokenizer = self.model_manager.load_model()
        # Aktivera snabb inference (om metoden finns)
        try:
            from unsloth import FastLanguageModel
            FastLanguageModel.for_inference(self.model)
        except Exception as e:
            print("Inference acceleration not enabled:", e)
        self.inference_manager = InferenceManager(self.model, self.tokenizer, CONFIG)

    def run_inference(self):
        prompt = "Continue the Fibonacci sequence: 1, 1, 2, 3, 5, 8,"
        result = self.inference_manager.run_inference(prompt)
        QMessageBox.information(self, "Inference", "\n".join(result))
