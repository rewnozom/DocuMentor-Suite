# processing_tab.py
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
    QLabel, QProgressBar, QTextEdit, QTreeWidget,
    QTreeWidgetItem, QFileDialog, QSpinBox
)

from PySide6.QtCore import Qt, Signal, Slot, QThread
from pathlib import Path

class ProcessingWorker(QThread):
    """Worker thread for file processing"""
    progress = Signal(int)
    finished = Signal(dict)
    error = Signal(str)
    
    def __init__(self, input_dir: str, num_workers: int):
        super().__init__()
        self.input_dir = input_dir
        self.num_workers = num_workers
        self.generator = DatasetGenerator([input_dir], "./output")
    
    def run(self):
        try:
            # Process files
            total_files = len(list(Path(self.input_dir).rglob("*.md")))
            processed = 0
            
            for doc in self.generator.process_directory(self.num_workers):
                processed += 1
                self.progress.emit(int((processed / total_files) * 100))
            
            # Get statistics
            stats = self.generator.get_statistics()
            self.finished.emit(stats)
            
        except Exception as e:
            self.error.emit(str(e))

class ProcessingTab(QWidget):
    """Tab for processing markdown files"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.worker = None
    
    def setup_ui(self):
        """Setup the UI components"""
        layout = QVBoxLayout(self)
        
        # Input directory selection
        input_layout = QHBoxLayout()
        self.input_label = QLabel("Input Directory:")
        self.input_path = QLabel("No directory selected")
        self.browse_btn = QPushButton("Browse")
        self.browse_btn.clicked.connect(self.browse_directory)
        input_layout.addWidget(self.input_label)
        input_layout.addWidget(self.input_path, 1)
        input_layout.addWidget(self.browse_btn)
        layout.addLayout(input_layout)
        
        # Worker configuration
        worker_layout = QHBoxLayout()
        self.worker_label = QLabel("Number of Workers:")
        self.worker_spin = QSpinBox()
        self.worker_spin.setRange(1, 32)
        self.worker_spin.setValue(4)
        worker_layout.addWidget(self.worker_label)
        worker_layout.addWidget(self.worker_spin)
        worker_layout.addStretch()
        layout.addLayout(worker_layout)
        
        # Progress bar
        self.progress = QProgressBar()
        self.progress.setTextVisible(True)
        layout.addWidget(self.progress)
        
        # Process button
        self.process_btn = QPushButton("Start Processing")
        self.process_btn.clicked.connect(self.start_processing)
        layout.addWidget(self.process_btn)
        
        # Results tree
        self.results_tree = QTreeWidget()
        self.results_tree.setHeaderLabels(["Category", "Value"])
        self.results_tree.setColumnCount(2)
        layout.addWidget(self.results_tree)
        
        # Log output
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        layout.addWidget(self.log_output)
    
    def browse_directory(self):
        """Open directory browser dialog"""
        directory = QFileDialog.getExistingDirectory(
            self,
            "Select Input Directory",
            "",
            QFileDialog.ShowDirsOnly
        )
        if directory:
            self.input_path.setText(directory)
            self.process_btn.setEnabled(True)
    
    def start_processing(self):
        """Start the processing worker"""
        if not self.input_path.text() or self.input_path.text() == "No directory selected":
            self.parent().parent().show_error(
                "Error",
                "Please select an input directory first"
            )
            return
        
        # Disable UI elements
        self.process_btn.setEnabled(False)
        self.browse_btn.setEnabled(False)
        self.worker_spin.setEnabled(False)
        
        # Clear previous results
        self.results_tree.clear()
        self.log_output.clear()
        self.progress.setValue(0)
        
        # Create and start worker
        self.worker = ProcessingWorker(
            self.input_path.text(),
            self.worker_spin.value()
        )
        self.worker.progress.connect(self.update_progress)
        self.worker.finished.connect(self.processing_finished)
        self.worker.error.connect(self.processing_error)
        self.worker.start()
    
    @Slot(int)
    def update_progress(self, value: int):
        """Update progress bar"""
        self.progress.setValue(value)
        self.log_output.append(f"Processed {value}% of files...")
    
    @Slot(dict)
    def processing_finished(self, stats: dict):
        """Handle processing completion"""
        # Enable UI elements
        self.process_btn.setEnabled(True)
        self.browse_btn.setEnabled(True)
        self.worker_spin.setEnabled(True)
        
        # Update results tree
        self.update_results_tree(stats)
        
        # Show success message
        self.parent().parent().show_success(
            "Success",
            "Processing completed successfully"
        )
        
        self.log_output.append("Processing completed successfully!")
    
    @Slot(str)
    def processing_error(self, error: str):
        """Handle processing error"""
        # Enable UI elements
        self.process_btn.setEnabled(True)
        self.browse_btn.setEnabled(True)
        self.worker_spin.setEnabled(True)
        
        # Show error message
        self.parent().parent().show_error(
            "Error",
            f"Processing failed: {error}"
        )
        
        self.log_output.append(f"Error: {error}")
    
    def update_results_tree(self, stats: dict):
        """Update results tree with statistics"""
        self.results_tree.clear()
        
        # Add statistics to tree
        for category, value in stats.items():
            if isinstance(value, dict):
                parent = QTreeWidgetItem([category, ""])
                for sub_cat, sub_val in value.items():
                    QTreeWidgetItem(parent, [sub_cat, str(sub_val)])
                self.results_tree.addTopLevelItem(parent)
            else:
                self.results_tree.addTopLevelItem(
                    QTreeWidgetItem([category, str(value)])
                )
        
        # Expand all items
        self.results_tree.expandAll()