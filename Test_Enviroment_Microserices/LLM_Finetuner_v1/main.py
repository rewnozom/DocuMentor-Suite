#!/usr/bin/env python3
import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.theme.theme_manager import ThemeManager

def main():
    app = QApplication(sys.argv)
    # Applicera dark theme med responsiv design
    ThemeManager.apply_dark_theme(app)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
