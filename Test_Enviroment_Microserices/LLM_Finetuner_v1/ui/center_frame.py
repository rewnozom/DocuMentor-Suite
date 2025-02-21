from PySide6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout
from ui.settings.settings_tab import SettingsTab
from ui.dataset.dataset_tab import DatasetTab
from ui.training_tab import TrainingTab
from ui.inference_tab import InferenceTab

class CenterFrame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        self.stacked_widget = QStackedWidget()
        # Sidor: 0=Settings, 1=Dataset, 2=Training, 3=Inference
        self.settings_tab = SettingsTab()
        self.dataset_tab = DatasetTab()
        self.training_tab = TrainingTab()
        self.inference_tab = InferenceTab()
        
        self.stacked_widget.addWidget(self.settings_tab)
        self.stacked_widget.addWidget(self.dataset_tab)
        self.stacked_widget.addWidget(self.training_tab)
        self.stacked_widget.addWidget(self.inference_tab)
        
        layout.addWidget(self.stacked_widget)

    def set_current_index(self, index):
        self.stacked_widget.setCurrentIndex(index)
