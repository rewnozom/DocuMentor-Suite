from PySide6.QtWidgets import QApplication

class ThemeManager:
    @staticmethod
    def apply_dark_theme(app: QApplication):
        # Professionellt dark theme med gradienter, skuggor och rundade hörn
        dark_style = """
            /* Grundläggande widget-stilar */
            QWidget {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,
                    stop:0 #1a1a1a, stop:1 #2d2d2d);
                color: #e0e0e0;
                font-family: "Segoe UI";
            }
            /* Inmatningsfält och dropdowns */
            QLineEdit, QComboBox {
                background-color: #2d2d2d;
                border: 1px solid #555;
                border-radius: 5px;
                padding: 5px;
                font-family: Consolas;
            }
            /* Professionella knappar */
            QPushButton {
                background-color: #e67e00;
                border: none;
                border-radius: 5px;
                padding: 8px;
                font-family: "Segoe UI";
            }
            QPushButton:hover {
                background-color: #ff9800;
            }
            /* TabWidget och containrar */
            QTabWidget::pane { 
                border: 1px solid #444;
                border-radius: 5px;
                padding: 5px;
            }
            /* Responsiva marginaler och padding */
            QVBoxLayout, QHBoxLayout {
                margin: 5px;
                spacing: 10px;
            }
        """
        app.setStyleSheet(dark_style)
