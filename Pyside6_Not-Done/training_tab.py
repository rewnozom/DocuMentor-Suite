# training_tab.py
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
    QLabel, QProgressBar, QTextEdit, QTableWidget,
    QTableWidgetItem, QGroupBox, QComboBox, QSpinBox,
    QSplitter, QTreeWidget, QTreeWidgetItem
)
from PySide6.QtCore import Qt, Signal, Slot, QThread
from pathlib import Path

class TrainingMonitor(QThread):
    """Worker thread for monitoring training progress"""
    progress = Signal(dict)
    status = Signal(str)
    error = Signal(str)
    
    def __init__(self, settings: dict):
        super().__init__()
        self.settings = settings
        self.is_running = True
    
    def run(self):
        try:
            while self.is_running:
                # Monitor training progress and emit updates
                # This would integrate with your training framework
                pass
        except Exception as e:
            self.error.emit(str(e))
    
    def stop(self):
        self.is_running = False

class TrainingTab(QWidget):
    """Tab for training monitoring and control"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.monitor = None
        
    def setup_ui(self):
        """Setup the UI components"""
        layout = QVBoxLayout(self)
        
        # Create splitter for flexible layout
        splitter = QSplitter(Qt.Horizontal)
        
        # Left panel - Training Controls
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        
        # Training Configuration
        config_group = QGroupBox("Training Configuration")
        config_layout = QVBoxLayout()
        
        # Model selection
        model_layout = QHBoxLayout()
        model_layout.addWidget(QLabel("Model Type:"))
        self.model_combo = QComboBox()
        self.model_combo.addItems(["GPT", "BERT", "RoBERTa", "Custom"])
        model_layout.addWidget(self.model_combo)
        config_layout.addLayout(model_layout)
        
        # Training parameters
        param_layout = QHBoxLayout()
        param_layout.addWidget(QLabel("Batch Size:"))
        self.batch_spin = QSpinBox()
        self.batch_spin.setRange(1, 128)
        self.batch_spin.setValue(32)
        param_layout.addWidget(self.batch_spin)
        
        param_layout.addWidget(QLabel("Epochs:"))
        self.epoch_spin = QSpinBox()
        self.epoch_spin.setRange(1, 100)
        self.epoch_spin.setValue(10)
        param_layout.addWidget(self.epoch_spin)
        
        param_layout.addWidget(QLabel("Learning Rate:"))
        self.lr_combo = QComboBox()
        self.lr_combo.addItems(["0.001", "0.0001", "0.00001"])
        param_layout.addWidget(self.lr_combo)
        config_layout.addLayout(param_layout)
        
        config_group.setLayout(config_layout)
        left_layout.addWidget(config_group)
        
        # Training Controls
        control_group = QGroupBox("Training Controls")
        control_layout = QVBoxLayout()
        
        # Progress indicators
        self.epoch_progress = QProgressBar()
        self.epoch_progress.setFormat("Epoch %v of %m")
        control_layout.addWidget(self.epoch_progress)
        
        self.batch_progress = QProgressBar()
        self.batch_progress.setFormat("Batch %v of %m")
        control_layout.addWidget(self.batch_progress)
        
        # Control buttons
        button_layout = QHBoxLayout()
        self.start_btn = QPushButton("Start Training")
        self.start_btn.clicked.connect(self.start_training)
        button_layout.addWidget(self.start_btn)
        
        self.pause_btn = QPushButton("Pause")
        self.pause_btn.clicked.connect(self.pause_training)
        self.pause_btn.setEnabled(False)
        button_layout.addWidget(self.pause_btn)
        
        self.stop_btn = QPushButton("Stop")
        self.stop_btn.clicked.connect(self.stop_training)
        self.stop_btn.setEnabled(False)
        button_layout.addWidget(self.stop_btn)
        
        control_layout.addLayout(button_layout)
        control_group.setLayout(control_layout)
        left_layout.addWidget(control_group)
        
        # Add stretcher to left panel
        left_layout.addStretch()
        
        # Right panel - Training Metrics
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        
        # Metrics view
        metrics_group = QGroupBox("Training Metrics")
        metrics_layout = QVBoxLayout()
        
        # Metrics tree
        self.metrics_tree = QTreeWidget()
        self.metrics_tree.setHeaderLabels(["Metric", "Value"])
        self.metrics_tree.setColumnCount(2)
        metrics_layout.addWidget(self.metrics_tree)
        
        metrics_group.setLayout(metrics_layout)
        right_layout.addWidget(metrics_group)
        
        # Add panels to splitter
        splitter.addWidget(left_panel)
        splitter.addWidget(right_panel)
        layout.addWidget(splitter)
        
        # Log output at bottom
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.log_output.setMaximumHeight(150)
        layout.addWidget(self.log_output)
    
# training_tab.py (fortsättning)

    def start_training(self):
        """Start the training process"""
        # Get training settings
        settings = {
            'model_type': self.model_combo.currentText(),
            'batch_size': self.batch_spin.value(),
            'epochs': self.epoch_spin.value(),
            'learning_rate': float(self.lr_combo.currentText())
        }
        
        # Update UI state
        self.start_btn.setEnabled(False)
        self.pause_btn.setEnabled(True)
        self.stop_btn.setEnabled(True)
        
        # Configure progress bars
        self.epoch_progress.setMaximum(settings['epochs'])
        self.epoch_progress.setValue(0)
        self.batch_progress.setValue(0)
        
        # Start monitoring
        self.monitor = TrainingMonitor(settings)
        self.monitor.progress.connect(self.update_training_progress)
        self.monitor.status.connect(self.update_status)
        self.monitor.error.connect(self.training_error)
        self.monitor.start()
        
        self.log_output.append("Training started...")
    
    def pause_training(self):
        """Pause the training process"""
        if self.monitor and self.monitor.isRunning():
            # Implement pause logic
            self.pause_btn.setText("Resume")
            self.log_output.append("Training paused")
        else:
            # Implement resume logic
            self.pause_btn.setText("Pause")
            self.log_output.append("Training resumed")
    
    def stop_training(self):
        """Stop the training process"""
        if self.monitor:
            self.monitor.stop()
            self.monitor.wait()
            
        # Reset UI state
        self.start_btn.setEnabled(True)
        self.pause_btn.setEnabled(False)
        self.stop_btn.setEnabled(False)
        self.pause_btn.setText("Pause")
        
        self.log_output.append("Training stopped")
    
    @Slot(dict)
    def update_training_progress(self, progress: dict):
        """Update training progress and metrics"""
        # Update progress bars
        if 'epoch' in progress:
            self.epoch_progress.setValue(progress['epoch'])
        if 'batch' in progress:
            self.batch_progress.setValue(progress['batch'])
        
        # Update metrics tree
        self.update_metrics_tree(progress.get('metrics', {}))
    
    def update_metrics_tree(self, metrics: dict):
        """Update the metrics tree with current values"""
        self.metrics_tree.clear()
        
        # Add main metrics
        loss_item = QTreeWidgetItem(["Loss", f"{metrics.get('loss', 0.0):.4f}"])
        accuracy_item = QTreeWidgetItem(["Accuracy", f"{metrics.get('accuracy', 0.0):.2%}"])
        
        self.metrics_tree.addTopLevelItem(loss_item)
        self.metrics_tree.addTopLevelItem(accuracy_item)
        
        # Add detailed metrics if available
        if 'details' in metrics:
            details_item = QTreeWidgetItem(["Detailed Metrics", ""])
            for name, value in metrics['details'].items():
                QTreeWidgetItem(details_item, [name, f"{value:.4f}"])
            self.metrics_tree.addTopLevelItem(details_item)
        
        # Expand all items
        self.metrics_tree.expandAll()
    
    @Slot(str)
    def update_status(self, status: str):
        """Update status in log output"""
        self.log_output.append(status)
    
    @Slot(str)
    def training_error(self, error: str):
        """Handle training error"""
        # Reset UI state
        self.start_btn.setEnabled(True)
        self.pause_btn.setEnabled(False)
        self.stop_btn.setEnabled(False)
        
        # Show error message
        self.parent().parent().show_error(
            "Training Error",
            f"Training failed: {error}"
        )
        
        self.log_output.append(f"Error: {error}")