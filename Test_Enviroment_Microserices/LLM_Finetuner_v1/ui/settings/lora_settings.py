from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QFormLayout

class LoraSettings(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        form_layout = QFormLayout()
        
        # LoRA R
        self.lora_r_edit = QLineEdit("4")
        form_layout.addRow("LoRA R:", self.lora_r_edit)
        
        # LoRA Alpha
        self.lora_alpha_edit = QLineEdit("16")
        form_layout.addRow("LoRA Alpha:", self.lora_alpha_edit)
        
        # LoRA Dropout
        self.lora_dropout_edit = QLineEdit("0.05")
        form_layout.addRow("LoRA Dropout:", self.lora_dropout_edit)
        
        layout.addLayout(form_layout)
