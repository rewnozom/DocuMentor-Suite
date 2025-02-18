# theme_manager.py
from PySide6.QtGui import QPalette, QColor, QFont
from PySide6.QtCore import Qt

class ThemeManager:
    """Manages application theming and styles"""
    
    # Define color constants
    BACKGROUND_PRIMARY = "#1e1e1e"
    BACKGROUND_SECONDARY = "#252526"
    BACKGROUND_TERTIARY = "#2d2d2d"
    FOREGROUND_PRIMARY = "#ffffff"
    FOREGROUND_SECONDARY = "#cccccc"
    ACCENT_PRIMARY = "#0078d7"
    ACCENT_SECONDARY = "#1084d8"
    ACCENT_TERTIARY = "#006cc1"
    ERROR_COLOR = "#ff3333"
    SUCCESS_COLOR = "#33cc33"
    WARNING_COLOR = "#ffcc00"
    
    @classmethod
    def get_dark_palette(cls) -> QPalette:
        """Get dark theme palette"""
        palette = QPalette()
        
        # Set color roles
        palette.setColor(QPalette.Window, QColor(cls.BACKGROUND_PRIMARY))
        palette.setColor(QPalette.WindowText, QColor(cls.FOREGROUND_PRIMARY))
        palette.setColor(QPalette.Base, QColor(cls.BACKGROUND_SECONDARY))
        palette.setColor(QPalette.AlternateBase, QColor(cls.BACKGROUND_TERTIARY))
        palette.setColor(QPalette.ToolTipBase, QColor(cls.BACKGROUND_SECONDARY))
        palette.setColor(QPalette.ToolTipText, QColor(cls.FOREGROUND_PRIMARY))
        palette.setColor(QPalette.Text, QColor(cls.FOREGROUND_PRIMARY))
        palette.setColor(QPalette.Button, QColor(cls.BACKGROUND_TERTIARY))
        palette.setColor(QPalette.ButtonText, QColor(cls.FOREGROUND_PRIMARY))
        palette.setColor(QPalette.BrightText, QColor(cls.FOREGROUND_PRIMARY))
        palette.setColor(QPalette.Highlight, QColor(cls.ACCENT_PRIMARY))
        palette.setColor(QPalette.HighlightedText, QColor(cls.FOREGROUND_PRIMARY))
        
        return palette
    
    @classmethod
    def get_dark_stylesheet(cls) -> str:
        """Get dark theme stylesheet"""
        return f"""
            /* Main Window */
            QMainWindow {{
                background-color: {cls.BACKGROUND_PRIMARY};
                color: {cls.FOREGROUND_PRIMARY};
            }}
            
            /* Buttons */
            QPushButton {{
                background-color: {cls.ACCENT_PRIMARY};
                color: {cls.FOREGROUND_PRIMARY};
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }}
            
            QPushButton:hover {{
                background-color: {cls.ACCENT_SECONDARY};
            }}
            
            QPushButton:pressed {{
                background-color: {cls.ACCENT_TERTIARY};
            }}
            
            QPushButton:disabled {{
                background-color: {cls.BACKGROUND_TERTIARY};
                color: {cls.FOREGROUND_SECONDARY};
            }}
            
            /* Tab Widget */
            QTabWidget::pane {{
                border: 1px solid {cls.BACKGROUND_TERTIARY};
                background-color: {cls.BACKGROUND_SECONDARY};
            }}
            
            QTabBar::tab {{
                background-color: {cls.BACKGROUND_TERTIARY};
                color: {cls.FOREGROUND_PRIMARY};
                padding: 8px 16px;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }}
            
            QTabBar::tab:selected {{
                background-color: {cls.ACCENT_PRIMARY};
            }}
            
            QTabBar::tab:hover {{
                background-color: {cls.ACCENT_SECONDARY};
            }}
            
            /* ComboBox */
            QComboBox {{
                background-color: {cls.BACKGROUND_TERTIARY};
                color: {cls.FOREGROUND_PRIMARY};
                border: 1px solid {cls.BACKGROUND_TERTIARY};
                padding: 5px;
                border-radius: 4px;
            }}
            
            QComboBox:hover {{
                border: 1px solid {cls.ACCENT_PRIMARY};
            }}
            
            QComboBox::drop-down {{
                border: none;
                padding-right: 10px;
            }}
            
            QComboBox::down-arrow {{
                image: url(:/icons/down-arrow.png);
            }}
            
            /* SpinBox */
            QSpinBox {{
                background-color: {cls.BACKGROUND_TERTIARY};
                color: {cls.FOREGROUND_PRIMARY};
                border: 1px solid {cls.BACKGROUND_TERTIARY};
                padding: 5px;
                border-radius: 4px;
            }}
            
            QSpinBox:hover {{
                border: 1px solid {cls.ACCENT_PRIMARY};
            }}
            
            /* ProgressBar */
            QProgressBar {{
                border: 1px solid {cls.BACKGROUND_TERTIARY};
                border-radius: 4px;
                text-align: center;
            }}
            
            QProgressBar::chunk {{
                background-color: {cls.ACCENT_PRIMARY};
            }}
            
            /* ScrollBar */
            QScrollBar:vertical {{
                background-color: {cls.BACKGROUND_SECONDARY};
                width: 12px;
                margin: 0;
            }}
            
            QScrollBar::handle:vertical {{
                background-color: {cls.BACKGROUND_TERTIARY};
                min-height: 20px;
                border-radius: 6px;
            }}
            
            QScrollBar::handle:vertical:hover {{
                background-color: {cls.ACCENT_PRIMARY};
            }}
            
            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {{
                height: 0;
            }}
            
            /* TreeWidget */
            QTreeWidget {{
                background-color: {cls.BACKGROUND_SECONDARY};
                color: {cls.FOREGROUND_PRIMARY};
                border: 1px solid {cls.BACKGROUND_TERTIARY};
            }}
            
            QTreeWidget::item:hover {{
                background-color: {cls.BACKGROUND_TERTIARY};
            }}
            
            QTreeWidget::item:selected {{
                background-color: {cls.ACCENT_PRIMARY};
            }}
            
            /* TextEdit */
            QTextEdit {{
                background-color: {cls.BACKGROUND_SECONDARY};
                color: {cls.FOREGROUND_PRIMARY};
                border: 1px solid {cls.BACKGROUND_TERTIARY};
                padding: 5px;
            }}
            
            /* GroupBox */
            QGroupBox {{
                background-color: {cls.BACKGROUND_SECONDARY};
                color: {cls.FOREGROUND_PRIMARY};
                border: 1px solid {cls.BACKGROUND_TERTIARY};
                border-radius: 4px;
                margin-top: 1em;
                padding-top: 10px;
            }}
            
            QGroupBox::title {{
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 0 5px;
                color: {cls.FOREGROUND_PRIMARY};
            }}
        """
    
    @staticmethod
    def get_default_font() -> QFont:
        """Get default application font"""
        font = QFont("Segoe UI", 10)
        font.setStyleStrategy(QFont.PreferAntialias)
        return font
    
    @classmethod
    def apply_theme(cls, app):
        """Apply theme to application"""
        # Set palette
        app.setPalette(cls.get_dark_palette())
        
        # Set stylesheet
        app.setStyleSheet(cls.get_dark_stylesheet())
        
        # Set default font
        app.setFont(cls.get_default_font())