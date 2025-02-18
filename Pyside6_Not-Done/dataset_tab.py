# dataset_tab.py
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
    QLabel, QProgressBar, QTextEdit, QTableWidget,
    QTableWidgetItem, QCheckBox, QGroupBox, QComboBox,
    QSpinBox
)
from PySide6.QtCore import Qt, Signal, Slot, QThread
from pathlib import Path

class DatasetWorker(QThread):
    """Worker thread for dataset generation"""
    progress = Signal(int)
    status = Signal(str)
    finished = Signal(dict)
    error = Signal(str)
    
    def __init__(self, settings: dict):
        super().__init__()
        self.settings = settings
        
    def run(self):
        try:
            self.status.emit("Initializing dataset generation...")
            generator = DatasetGenerator(
                input_dirs=[self.settings['input_dir']],
                output_dir=self.settings['output_dir']
            )
            
            # Generate dataset
            self.status.emit("Generating dataset...")
            generator.generate_dataset(
                commands=self.settings['commands'],
                chunk_size=self.settings['chunk_size']
            )
            
            # Get statistics
            stats = generator.get_statistics()
            self.finished.emit(stats)
            
        except Exception as e:
            self.error.emit(str(e))

class DatasetTab(QWidget):
    """Tab for dataset generation and management"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.worker = None
        
    def setup_ui(self):
        """Setup the UI components"""
        layout = QVBoxLayout(self)
        
        # Dataset Configuration Group
        config_group = QGroupBox("Dataset Configuration")
        config_layout = QVBoxLayout()
        
        # Commands selection
        cmd_layout = QHBoxLayout()
        cmd_layout.addWidget(QLabel("Commands:"))
        self.cmd_checks = {}
        for cmd in ['f', 's', 't', 'c']:
            check = QCheckBox(cmd)
            check.setChecked(True)
            self.cmd_checks[cmd] = check
            cmd_layout.addWidget(check)
        cmd_layout.addStretch()
        config_layout.addLayout(cmd_layout)
        
        # Processing options
        proc_layout = QHBoxLayout()
        proc_layout.addWidget(QLabel("Chunk Size:"))
        self.chunk_spin = QSpinBox()
        self.chunk_spin.setRange(1, 100)
        self.chunk_spin.setValue(10)
        proc_layout.addWidget(self.chunk_spin)
        
        proc_layout.addWidget(QLabel("Output Format:"))
        self.format_combo = QComboBox()
        self.format_combo.addItems(["JSON", "CSV", "Both"])
        self.format_combo.setCurrentText("Both")
        proc_layout.addWidget(self.format_combo)
        proc_layout.addStretch()
        config_layout.addLayout(proc_layout)
        
        config_group.setLayout(config_layout)
        layout.addWidget(config_group)
        
        # Progress Group
        progress_group = QGroupBox("Generation Progress")
        progress_layout = QVBoxLayout()
        
        self.status_label = QLabel("Ready")
        progress_layout.addWidget(self.status_label)
        
        self.progress = QProgressBar()
        self.progress.setTextVisible(True)
        progress_layout.addWidget(self.progress)
        
        progress_group.setLayout(progress_layout)
        layout.addWidget(progress_group)
        
        # Results Table
        self.results_table = QTableWidget()
        self.results_table.setColumnCount(5)
        self.results_table.setHorizontalHeaderLabels([
            "Command", "Examples", "Average Length", "Validation Score", "Status"
        ])
        layout.addWidget(self.results_table)
        
        # Button row
        button_layout = QHBoxLayout()
        
        self.generate_btn = QPushButton("Generate Dataset")
        self.generate_btn.clicked.connect(self.start_generation)
        button_layout.addWidget(self.generate_btn)
        
        self.validate_btn = QPushButton("Validate Dataset")
        self.validate_btn.clicked.connect(self.validate_dataset)
        button_layout.addWidget(self.validate_btn)
        
        self.export_btn = QPushButton("Export Dataset")
        self.export_btn.clicked.connect(self.export_dataset)
        button_layout.addWidget(self.export_btn)
        
        layout.addLayout(button_layout)
        
        # Log output
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        layout.addWidget(self.log_output)
    
    def get_settings(self) -> dict:
        """Get current settings from UI"""
        return {
            'commands': [cmd for cmd, check in self.cmd_checks.items() if check.isChecked()],
            'chunk_size': self.chunk_spin.value(),
            'output_format': self.format_combo.currentText().lower(),
            'input_dir': self.parent().parent().current_directory,
            'output_dir': str(Path(self.parent().parent().current_directory) / "output")
        }
    
    def start_generation(self):
        """Start dataset generation"""
        if not self.parent().parent().current_directory:
            self.parent().parent().show_error(
                "Error",
                "Please select an input directory first"
            )
            return
        
        # Disable UI elements
        self.generate_btn.setEnabled(False)
        self.validate_btn.setEnabled(False)
        self.export_btn.setEnabled(False)
        
        # Clear previous results
        self.results_table.setRowCount(0)
        self.progress.setValue(0)
        self.log_output.clear()
        
        # Get settings
        settings = self.get_settings()
        
        # Create and start worker
        self.worker = DatasetWorker(settings)
        self.worker.progress.connect(self.update_progress)
        self.worker.status.connect(self.update_status)
        self.worker.finished.connect(self.generation_finished)
        self.worker.error.connect(self.generation_error)
        self.worker.start()
    
    @Slot(int)
    def update_progress(self, value: int):
        """Update progress bar"""
        self.progress.setValue(value)
    
    @Slot(str)
    def update_status(self, status: str):
        """Update status label"""
        self.status_label.setText(status)
        self.log_output.append(status)
    
    @Slot(dict)
    def generation_finished(self, stats: dict):
        """Handle generation completion"""
        # Enable UI elements
        self.generate_btn.setEnabled(True)
        self.validate_btn.setEnabled(True)
        self.export_btn.setEnabled(True)
        
        # Update results table
        self.update_results_table(stats)
        
        # Show success message
        self.parent().parent().show_success(
            "Success",
            "Dataset generation completed successfully"
        )
        
        self.log_output.append("Dataset generation completed successfully!")
    
    def update_results_table(self, stats: dict):
        """Update results table with statistics"""
        self.results_table.setRowCount(len(stats['commands']))
        
        for row, (cmd, data) in enumerate(stats['commands'].items()):
            self.results_table.setItem(row, 0, QTableWidgetItem(cmd))
            self.results_table.setItem(row, 1, QTableWidgetItem(str(data['examples'])))
            self.results_table.setItem(row, 2, QTableWidgetItem(f"{data['avg_length']:.2f}"))
            self.results_table.setItem(row, 3, QTableWidgetItem(f"{data['validation_score']:.2%}"))
            self.results_table.setItem(row, 4, QTableWidgetItem(data['status']))
        
        self.results_table.resizeColumnsToContents()
    
    def validate_dataset(self):
        """Validate the generated dataset"""
        # Implementation for dataset validation
        pass
    
    def export_dataset(self):
        """Export the dataset"""
        # Implementation for dataset export
        pass