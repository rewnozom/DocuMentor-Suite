from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QFormLayout, QComboBox

class TrainingSettings(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        form_layout = QFormLayout()
        
        # Batchstorlek
        self.batch_size_edit = QLineEdit("2")
        form_layout.addRow("Batch Size:", self.batch_size_edit)
        
        # Inlärningshastighet
        self.lr_edit = QLineEdit("0.0003")
        form_layout.addRow("Learning Rate:", self.lr_edit)
        
        # Dropdown för optimizer
        self.optimizer_combo = QComboBox()
        self.optimizer_combo.addItems(["adamw_8bit", "AdamW"])
        form_layout.addRow("Optimizer:", self.optimizer_combo)
        
        # Epochs
        self.epochs_edit = QLineEdit("9")
        form_layout.addRow("Epochs:", self.epochs_edit)
        
        # Schedule
        self.schedule_combo = QComboBox()
        self.schedule_combo.addItems(["Cosine", "Linear", "Step"])
        form_layout.addRow("Schedule:", self.schedule_combo)
        
        # Warmup Epochs
        self.warmup_edit = QLineEdit("0.1")
        form_layout.addRow("Warmup Epochs:", self.warmup_edit)
        
        # Weight Decay
        self.weight_decay_edit = QLineEdit("0")
        form_layout.addRow("Weight Decay:", self.weight_decay_edit)
        
        # Gradient Clip
        self.grad_clip_edit = QLineEdit("0")
        form_layout.addRow("Gradient Clip:", self.grad_clip_edit)
        
        # Grad Accumulation
        self.grad_accum_edit = QLineEdit("1")
        form_layout.addRow("Grad Accumulation:", self.grad_accum_edit)
        
        layout.addLayout(form_layout)
