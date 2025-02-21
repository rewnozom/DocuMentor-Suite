from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from PySide6.QtCore import QThread, Signal
from config import CONFIG

class TrainingWorker(QThread):
    finished = Signal(dict)

    def __init__(self, config, dataset_path, parent=None):
        super().__init__(parent)
        self.config = config
        self.dataset_path = dataset_path

    def run(self):
        # Här skulle du normalt kalla backend/training/training_manager.py:s logik.
        # I detta exempel simuleras träningsprocessen med en sömn.
        import time
        time.sleep(2)  # Simulera träningstid
        self.finished.emit({"status": "Training complete", "loss": 0.123})

class TrainingTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        self.info_label = QLabel("Training Module")
        layout.addWidget(self.info_label)
        
        self.train_button = QPushButton("Start Training")
        self.train_button.clicked.connect(self.start_training)
        layout.addWidget(self.train_button)
        
    def start_training(self):
        # Här skulle man normalt hämta dataset-vägen från Dataset-tabben
        dataset_path = "path/to/dataset"  # Dummy-värde
        self.info_label.setText("Training started...")
        self.train_button.setEnabled(False)
        
        self.worker = TrainingWorker(CONFIG, dataset_path)
        self.worker.finished.connect(self.on_training_finished)
        self.worker.start()
    
    def on_training_finished(self, result):
        self.info_label.setText(result.get("status", "Training complete"))
        self.train_button.setEnabled(True)
        QMessageBox.information(self, "Training", f"Training complete with loss: {result.get('loss')}")
