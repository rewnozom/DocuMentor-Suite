from PySide6.QtWidgets import QWidget, QComboBox, QVBoxLayout, QLineEdit, QFormLayout

class ModelSettings(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        form_layout = QFormLayout()
        
        # Dropdown för modellval
        self.model_combo = QComboBox()
        self.model_combo.addItems([
            "unsloth/Llama-3.2-1B-Instruct",
            "unsloth/Llama-3.2-3B-Instruct",
            "unsloth/Llama-3.3-70B-Instruct-bnb-4bit"
        ])
        form_layout.addRow("Model:", self.model_combo)
        
        # Max sekvenslängd
        self.seq_length_edit = QLineEdit("2048")
        form_layout.addRow("Max Seq Length:", self.seq_length_edit)
        
        layout.addLayout(form_layout)
