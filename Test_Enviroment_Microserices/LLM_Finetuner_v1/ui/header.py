from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide6.QtGui import QFont

class Header(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QHBoxLayout(self)
        label = QLabel("LLM Finetuner")
        label.setFont(QFont("Segoe UI", 20))
        layout.addWidget(label)
        layout.addStretch()
