from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton

class SideMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        # Navigeringsknappar
        self.btn_settings = QPushButton("Settings")
        self.btn_dataset = QPushButton("Dataset")
        self.btn_training = QPushButton("Training")
        self.btn_inference = QPushButton("Inference")
        
        layout.addWidget(self.btn_settings)
        layout.addWidget(self.btn_dataset)
        layout.addWidget(self.btn_training)
        layout.addWidget(self.btn_inference)
        layout.addStretch()
