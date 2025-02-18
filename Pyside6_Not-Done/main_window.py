# main_window.py
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QTabWidget,
    QPushButton, QLabel, QStatusBar, QMessageBox,
    QFileDialog, QSpinBox, QComboBox
)
from PySide6.QtCore import Qt, QSize, Signal, Slot
from PySide6.QtGui import QIcon, QFont, QPalette, QColor
import qdarkstyle
import resources_rc  # Will create this later for icons

class MainWindow(QMainWindow):
    """Main application window with dark theme and responsive design"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Markdown Analyzer")
        self.setMinimumSize(1200, 800)
        
        # Setup dark theme
        self.setup_theme()
        
        # Create main widget and layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout(self.main_widget)
        
        # Create tab widget for different sections
        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)
        
        # Initialize tabs
        self.init_processing_tab()
        self.init_dataset_tab()
        self.init_training_tab()
        self.init_settings_tab()
        
        # Setup status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        
        # Initialize state
        self.current_directory = None
        self.is_processing = False
    
    def setup_theme(self):
        """Setup dark theme and styling"""
        # Apply dark theme
        self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6'))
        
        # Custom palette for specific colors
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#1e1e1e"))
        palette.setColor(QPalette.WindowText, QColor("#ffffff"))
        palette.setColor(QPalette.Base, QColor("#252526"))
        palette.setColor(QPalette.AlternateBase, QColor("#2d2d2d"))
        palette.setColor(QPalette.Button, QColor("#333333"))
        palette.setColor(QPalette.ButtonText, QColor("#ffffff"))
        palette.setColor(QPalette.Highlight, QColor("#0078d7"))
        self.setPalette(palette)
        
        # Custom stylesheet for specific widgets
        self.setStyleSheet(self.setStyleSheet() + """
            QPushButton {
                background-color: #0078d7;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            
            QPushButton:hover {
                background-color: #1084d8;
            }
            
            QPushButton:pressed {
                background-color: #006cc1;
            }
            
            QPushButton:disabled {
                background-color: #333333;
                color: #666666;
            }
            
            QTabWidget::pane {
                border: 1px solid #333333;
                background-color: #252526;
            }
            
            QTabBar::tab {
                background-color: #2d2d2d;
                color: #ffffff;
                padding: 8px 16px;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }
            
            QTabBar::tab:selected {
                background-color: #0078d7;
            }
            
            QTabBar::tab:hover {
                background-color: #1084d8;
            }
            
            QComboBox {
                background-color: #333333;
                color: white;
                border: 1px solid #444444;
                padding: 5px;
                border-radius: 4px;
            }
            
            QComboBox:hover {
                border: 1px solid #0078d7;
            }
            
            QSpinBox {
                background-color: #333333;
                color: white;
                border: 1px solid #444444;
                padding: 5px;
                border-radius: 4px;
            }
            
            QSpinBox:hover {
                border: 1px solid #0078d7;
            }
            
            QProgressBar {
                border: 1px solid #444444;
                border-radius: 4px;
                text-align: center;
            }
            
            QProgressBar::chunk {
                background-color: #0078d7;
            }
        """)
    
    def init_processing_tab(self):
        """Initialize the processing tab"""
        processing_widget = ProcessingTab(self)
        self.tab_widget.addTab(processing_widget, "Processing")
    
    def init_dataset_tab(self):
        """Initialize the dataset tab"""
        dataset_widget = DatasetTab(self)
        self.tab_widget.addTab(dataset_widget, "Dataset")
    
    def init_training_tab(self):
        """Initialize the training tab"""
        training_widget = TrainingTab(self)
        self.tab_widget.addTab(training_widget, "Training")
    
    def init_settings_tab(self):
        """Initialize the settings tab"""
        settings_widget = SettingsTab(self)
        self.tab_widget.addTab(settings_widget, "Settings")
    
    def show_error(self, title: str, message: str):
        """Show error dialog with dark theme"""
        error_box = QMessageBox(self)
        error_box.setIcon(QMessageBox.Critical)
        error_box.setWindowTitle(title)
        error_box.setText(message)
        error_box.setStyleSheet("""
            QMessageBox {
                background-color: #252526;
                color: white;
            }
            QLabel {
                color: white;
            }
            QPushButton {
                background-color: #0078d7;
                color: white;
                border: none;
                padding: 6px 12px;
                border-radius: 4px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #1084d8;
            }
        """)
        error_box.exec_()
    
    def show_success(self, title: str, message: str):
        """Show success dialog with dark theme"""
        success_box = QMessageBox(self)
        success_box.setIcon(QMessageBox.Information)
        success_box.setWindowTitle(title)
        success_box.setText(message)
        success_box.setStyleSheet("""
            QMessageBox {
                background-color: #252526;
                color: white;
            }
            QLabel {
                color: white;
            }
            QPushButton {
                background-color: #0078d7;
                color: white;
                border: none;
                padding: 6px 12px;
                border-radius: 4px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #1084d8;
            }
        """)
        success_box.exec_()
    
    def update_status(self, message: str):
        """Update status bar with message"""
        self.status_bar.showMessage(message, 5000)  # Show for 5 seconds