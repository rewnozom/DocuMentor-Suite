from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QFormLayout

class InferenceSettings(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        form_layout = QFormLayout()
        
        # Max antal tokens för inferens
        self.max_tokens_edit = QLineEdit("64")
        form_layout.addRow("Max New Tokens:", self.max_tokens_edit)
        
        # Temperatur
        self.temperature_edit = QLineEdit("1")
        form_layout.addRow("Temperature:", self.temperature_edit)
        
        # Repetition Penalty
        self.repetition_penalty_edit = QLineEdit("1")
        form_layout.addRow("Repetition Penalty:", self.repetition_penalty_edit)
        
        # Top K
        self.top_k_edit = QLineEdit("0")
        form_layout.addRow("Top K:", self.top_k_edit)
        
        # Top P
        self.top_p_edit = QLineEdit("1")
        form_layout.addRow("Top P:", self.top_p_edit)
        
        layout.addLayout(form_layout)
