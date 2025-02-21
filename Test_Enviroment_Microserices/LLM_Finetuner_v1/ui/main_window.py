from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QSplitter
from ui.header import Header
from ui.menu import SideMenu
from ui.center_frame import CenterFrame

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("LLM Finetuner")
        self.resize(1200, 800)
        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Lägg till header
        self.header = Header()
        main_layout.addWidget(self.header)
        
        # Splitter ger dynamisk storleksanpassning: vänster meny & central vy
        splitter = QSplitter()
        self.menu = SideMenu()
        self.center_frame = CenterFrame()
        
        splitter.addWidget(self.menu)
        splitter.addWidget(self.center_frame)
        splitter.setStretchFactor(1, 1)
        main_layout.addWidget(splitter)
        
        # Koppla side-menyns knappar till att byta sida
        self.menu.btn_settings.clicked.connect(lambda: self.center_frame.set_current_index(0))
        self.menu.btn_dataset.clicked.connect(lambda: self.center_frame.set_current_index(1))
        self.menu.btn_training.clicked.connect(lambda: self.center_frame.set_current_index(2))
        self.menu.btn_inference.clicked.connect(lambda: self.center_frame.set_current_index(3))
