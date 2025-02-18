# main.py
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer
from pathlib import Path
import qdarkstyle
import logging

from .main_window import MainWindow
from ..utils.logging import setup_logging

class MarkdownAnalyzerApp:
    """Main application class"""
    
    def __init__(self):
        # Initialize QApplication
        self.app = QApplication(sys.argv)
        
        # Setup application properties
        self.app.setApplicationName("Markdown Analyzer")
        self.app.setApplicationVersion("1.0.0")
        self.app.setOrganizationName("MarkdownAnalyzer")
        self.app.setOrganizationDomain("markdownanalyzer.org")
        
        # Setup dark theme
        self.app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6'))
        
        # Setup logging
        setup_logging(debug=False)
        self.logger = logging.getLogger(__name__)
        
        # Create main window
        self.main_window = MainWindow()
        
        # Setup auto-save timer
        self.auto_save_timer = QTimer()
        self.auto_save_timer.timeout.connect(self.auto_save)
        self.auto_save_timer.start(300000)  # Auto-save every 5 minutes
    
    def run(self):
        """Run the application"""
        try:
            # Show main window
            self.main_window.show()
            
            # Start event loop
            return self.app.exec()
            
        except Exception as e:
            self.logger.error(f"Application error: {str(e)}")
            return 1
        finally:
            self.cleanup()
    
    def auto_save(self):
        """Auto-save current work"""
        try:
            # Get current state from main window
            state = self.main_window.get_current_state()
            
            # Create auto-save directory
            auto_save_dir = Path.home() / '.markdown_analyzer' / 'autosave'
            auto_save_dir.mkdir(parents=True, exist_ok=True)
            
            # Save state
            with open(auto_save_dir / 'last_session.json', 'w') as f:
                json.dump(state, f, indent=2)
                
            self.logger.debug("Auto-save completed")
            
        except Exception as e:
            self.logger.error(f"Auto-save failed: {str(e)}")
    
    def cleanup(self):
        """Cleanup resources before exit"""
        try:
            # Stop auto-save timer
            self.auto_save_timer.stop()
            
            # Perform auto-save one last time
            self.auto_save()
            
            # Clean up any temporary files
            temp_dir = Path.home() / '.markdown_analyzer' / 'temp'
            if temp_dir.exists():
                shutil.rmtree(temp_dir)
                
            self.logger.info("Cleanup completed")
            
        except Exception as e:
            self.logger.error(f"Cleanup failed: {str(e)}")

# Resource file (resources.qrc)
'''
<RCC>
    <qresource prefix="/">
        <file>icons/play.png</file>
        <file>icons/pause.png</file>
        <file>icons/stop.png</file>
        <file>icons/settings.png</file>
        <file>icons/folder.png</file>
        <file>icons/save.png</file>
        <file>icons/export.png</file>
        <file>icons/validate.png</file>
        <file>icons/info.png</file>
        <file>icons/warning.png</file>
        <file>icons/error.png</file>
        <file>icons/success.png</file>
    </qresource>
</RCC>
'''

# Icons module (icons.py)
from enum import Enum
from PySide6.QtGui import QIcon

class Icons(Enum):
    """Application icons"""
    PLAY = ":/icons/play.png"
    PAUSE = ":/icons/pause.png"
    STOP = ":/icons/stop.png"
    SETTINGS = ":/icons/settings.png"
    FOLDER = ":/icons/folder.png"
    SAVE = ":/icons/save.png"
    EXPORT = ":/icons/export.png"
    VALIDATE = ":/icons/validate.png"
    INFO = ":/icons/info.png"
    WARNING = ":/icons/warning.png"
    ERROR = ":/icons/error.png"
    SUCCESS = ":/icons/success.png"
    
    def icon(self) -> QIcon:
        return QIcon(self.value)

# Application entry point
if __name__ == "__main__":
    app = MarkdownAnalyzerApp()
    sys.exit(app.run())