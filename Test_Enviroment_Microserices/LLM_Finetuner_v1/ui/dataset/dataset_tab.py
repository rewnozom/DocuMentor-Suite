from PySide6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QComboBox, QFileDialog, QLabel

class DatasetTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        form_layout = QFormLayout()
        
        # Filväg för dataset
        self.file_path_edit = QLineEdit()
        browse_btn = QPushButton("Browse")
        browse_btn.clicked.connect(self.browse_file)
        form_layout.addRow("Dataset File:", self.file_path_edit)
        
        # Dropdown för dataset-format
        self.format_combo = QComboBox()
        self.format_combo.addItems(["json", "csv", "parquet"])
        form_layout.addRow("Format:", self.format_combo)
        
        layout.addLayout(form_layout)
        
        # Status för dataset
        self.status_label = QLabel("No dataset loaded.")
        layout.addWidget(self.status_label)
        
    def browse_file(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "Select Dataset File")
        if file_path:
            self.file_path_edit.setText(file_path)
            self.status_label.setText(f"Selected: {file_path}")
