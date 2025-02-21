from PySide6.QtWidgets import QWidget, QTabWidget, QVBoxLayout
from ui.settings.model_settings import ModelSettings
from ui.settings.lora_settings import LoraSettings
from ui.settings.training_settings import TrainingSettings
from ui.settings.inference_settings import InferenceSettings

class SettingsTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        
        self.model_settings_tab = ModelSettings()
        self.lora_settings_tab = LoraSettings()
        self.training_settings_tab = TrainingSettings()
        self.inference_settings_tab = InferenceSettings()
        
        self.tabs.addTab(self.model_settings_tab, "Model Settings")
        self.tabs.addTab(self.lora_settings_tab, "LoRA Settings")
        self.tabs.addTab(self.training_settings_tab, "Training Settings")
        self.tabs.addTab(self.inference_settings_tab, "Inference Settings")
        
        layout.addWidget(self.tabs)
