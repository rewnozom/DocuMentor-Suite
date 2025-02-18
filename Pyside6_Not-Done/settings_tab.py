# settings_tab.py
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QSpinBox, QComboBox, QCheckBox,
    QGroupBox, QFormLayout, QLineEdit, QFileDialog,
    QScrollArea
)
from PySide6.QtCore import Qt, Signal, Slot
from pathlib import Path
import json

class SettingsTab(QWidget):
    """Tab for application settings"""
    
    # Signal when settings are changed
    settings_changed = Signal(dict)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.load_settings()
    
    def setup_ui(self):
        """Setup the UI components"""
        # Create scroll area for settings
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        # Main widget for scroll area
        main_widget = QWidget()
        layout = QVBoxLayout(main_widget)
        
        # Processing Settings
        proc_group = QGroupBox("Processing Settings")
        proc_layout = QFormLayout()
        
        self.worker_spin = QSpinBox()
        self.worker_spin.setRange(1, 32)
        self.worker_spin.setValue(4)
        proc_layout.addRow("Number of Workers:", self.worker_spin)
        
        self.chunk_spin = QSpinBox()
        self.chunk_spin.setRange(1, 100)
        self.chunk_spin.setValue(10)
        proc_layout.addRow("Chunk Size:", self.chunk_spin)
        
        self.max_files_spin = QSpinBox()
        self.max_files_spin.setRange(0, 10000)
        self.max_files_spin.setValue(0)
        self.max_files_spin.setSpecialValueText("No limit")
        proc_layout.addRow("Max Files (0 = no limit):", self.max_files_spin)
        
        proc_group.setLayout(proc_layout)
        layout.addWidget(proc_group)
        
        # Dataset Settings
        dataset_group = QGroupBox("Dataset Settings")
        dataset_layout = QFormLayout()
        
        self.output_format = QComboBox()
        self.output_format.addItems(["JSON", "CSV", "Both"])
        dataset_layout.addRow("Output Format:", self.output_format)
        
        self.validation_enabled = QCheckBox()
        self.validation_enabled.setChecked(True)
        dataset_layout.addRow("Enable Validation:", self.validation_enabled)
        
        self.strict_validation = QCheckBox()
        dataset_layout.addRow("Strict Validation:", self.strict_validation)
        
        dataset_group.setLayout(dataset_layout)
        layout.addWidget(dataset_group)
        
        # Training Settings
        training_group = QGroupBox("Training Settings")
        training_layout = QFormLayout()
        
        self.model_type = QComboBox()
        self.model_type.addItems(["GPT", "BERT", "RoBERTa", "Custom"])
        training_layout.addRow("Default Model:", self.model_type)
        
        self.batch_size = QSpinBox()
        self.batch_size.setRange(1, 128)
        self.batch_size.setValue(32)
        training_layout.addRow("Default Batch Size:", self.batch_size)
        
        self.epochs = QSpinBox()
        self.epochs.setRange(1, 100)
        self.epochs.setValue(10)
        training_layout.addRow("Default Epochs:", self.epochs)
        
        self.learning_rate = QComboBox()
        self.learning_rate.addItems(["0.001", "0.0001", "0.00001"])
        training_layout.addRow("Default Learning Rate:", self.learning_rate)
        
        training_group.setLayout(training_layout)
        layout.addWidget(training_group)
        
        # Path Settings
        paths_group = QGroupBox("Path Settings")
        paths_layout = QFormLayout()
        
        # Default input directory
        input_layout = QHBoxLayout()
        self.input_dir = QLineEdit()
        input_layout.addWidget(self.input_dir)
        self.browse_input = QPushButton("Browse")
        self.browse_input.clicked.connect(self.browse_input_dir)
        input_layout.addWidget(self.browse_input)
        paths_layout.addRow("Default Input Directory:", input_layout)
        
        # Default output directory
        output_layout = QHBoxLayout()
        self.output_dir = QLineEdit()
        output_layout.addWidget(self.output_dir)
        self.browse_output = QPushButton("Browse")
        self.browse_output.clicked.connect(self.browse_output_dir)
        output_layout.addWidget(self.browse_output)
        paths_layout.addRow("Default Output Directory:", output_layout)
        
        paths_group.setLayout(paths_layout)
        layout.addWidget(paths_group)
        
        # Add stretcher
        layout.addStretch()
        
        # Button row
        button_layout = QHBoxLayout()
        
        self.apply_btn = QPushButton("Apply")
        self.apply_btn.clicked.connect(self.apply_settings)
        button_layout.addWidget(self.apply_btn)
        
        self.reset_btn = QPushButton("Reset to Defaults")
        self.reset_btn.clicked.connect(self.reset_settings)
        button_layout.addWidget(self.reset_btn)
        
        layout.addLayout(button_layout)
        
        # Set main widget to scroll area
        scroll.setWidget(main_widget)
        
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll)
    
    def load_settings(self):
        """Load settings from file"""
        try:
            settings_path = Path.home() / '.markdown_analyzer' / 'settings.json'
            if settings_path.exists():
                with open(settings_path, 'r') as f:
                    settings = json.load(f)
                self.apply_loaded_settings(settings)
        except Exception as e:
            self.parent().parent().show_error(
                "Error",
                f"Failed to load settings: {str(e)}"
            )
    
    def apply_loaded_settings(self, settings: dict):
        """Apply loaded settings to UI"""
        # Processing settings
        self.worker_spin.setValue(settings.get('workers', 4))
        self.chunk_spin.setValue(settings.get('chunk_size', 10))
        self.max_files_spin.setValue(settings.get('max_files', 0))
        
        # Dataset settings
        self.output_format.setCurrentText(settings.get('output_format', 'Both'))
        self.validation_enabled.setChecked(settings.get('validation_enabled', True))
        self.strict_validation.setChecked(settings.get('strict_validation', False))
        
        # Training settings
        self.model_type.setCurrentText(settings.get('model_type', 'GPT'))
        self.batch_size.setValue(settings.get('batch_size', 32))
        self.epochs.setValue(settings.get('epochs', 10))
        self.learning_rate.setCurrentText(settings.get('learning_rate', '0.001'))
        
        # Path settings
        self.input_dir.setText(settings.get('input_dir', ''))
        self.output_dir.setText(settings.get('output_dir', ''))
    
    def get_current_settings(self) -> dict:
        """Get current settings from UI"""
        return {
            'workers': self.worker_spin.value(),
            'chunk_size': self.chunk_spin.value(),
            'max_files': self.max_files_spin.value(),
            'output_format': self.output_format.currentText(),
            'validation_enabled': self.validation_enabled.isChecked(),
            'strict_validation': self.strict_validation.isChecked(),
            'model_type': self.model_type.currentText(),
            'batch_size': self.batch_size.value(),
            'epochs': self.epochs.value(),
            'learning_rate': self.learning_rate.currentText(),
            'input_dir': self.input_dir.text(),
            'output_dir': self.output_dir.text()
        }
    
    def apply_settings(self):
        """Apply and save current settings"""
        settings = self.get_current_settings()
        
        try:
            # Create settings directory if it doesn't exist
            settings_dir = Path.home() / '.markdown_analyzer'
            settings_dir.mkdir(exist_ok=True)
            
            # Save settings
            with open(settings_dir / 'settings.json', 'w') as f:
                json.dump(settings, f, indent=2)
            
            # Emit settings changed signal
            self.settings_changed.emit(settings)
            
            self.parent().parent().show_success(
                "Success",
                "Settings saved successfully"
            )
            
        except Exception as e:
            self.parent().parent().show_error(
                "Error",
                f"Failed to save settings: {str(e)}"
            )
    
    def reset_settings(self):
        """Reset settings to defaults"""
        self.worker_spin.setValue(4)
        self.chunk_spin.setValue(10)
        self.max_files_spin.setValue(0)
        self.output_format.setCurrentText("Both")
        self.validation_enabled.setChecked(True)
        self.strict_validation.setChecked(False)
        self.model_type.setCurrentText("GPT")
        self.batch_size.setValue(32)
        self.epochs.setValue(10)
        self.learning_rate.setCurrentText("0.001")
        self.input_dir.clear()
        self.output_dir.clear()
    
    def browse_input_dir(self):
        """Browse for input directory"""
        directory = QFileDialog.getExistingDirectory(
            self,
            "Select Input Directory",
            self.input_dir.text(),
            QFileDialog.ShowDirsOnly
        )
        if directory:
            self.input_dir.setText(directory)
    
    def browse_output_dir(self):
        """Browse for output directory"""
        directory = QFileDialog.getExistingDirectory(
            self,
            "Select Output Directory",
            self.output_dir.text(),
            QFileDialog.ShowDirsOnly
        )
        if directory:
            self.output_dir.setText(directory)