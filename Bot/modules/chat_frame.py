# modules/chat_frame.py

from datetime import datetime
import re
import markdown
from pathlib import Path

from PySide6.QtCore import Qt, Signal, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QTextBrowser, QLineEdit, QPushButton,
    QLabel, QComboBox, QScrollArea, QFrame, QSizePolicy
)

from .bot_engine import BotEngine


class ChatBubble(QFrame):
    """
    Widget som representerar en chatbubbla för att visa meddelanden.

    Denna widget visar en etikett ("Du:" eller "Bot:") ovanför meddelandet,
    samt anpassar dynamiskt höjden baserat på innehållet.
    """

    def __init__(self, message, is_user: bool = False, parent: QWidget = None):
        """
        Initierar en ChatBubble.

        Args:
            message (str or dict): Meddelandetexten eller ett objekt med nycklarna 'formatted_text' eller 'message'.
            is_user (bool): True om meddelandet kommer från användaren, annars False.
            parent (QWidget, optional): Föräldrawidget.
        """
        super().__init__(parent)

        # Extrahera texten om 'message' inte är en sträng
        if not isinstance(message, str):
            message = message.get("formatted_text", message.get("message", str(message)))

        # Ställ in stil beroende på avsändare
        if is_user:
            self.setStyleSheet("""
                QFrame {
                    background-color: #DCF8C6;
                    border-radius: 10px;
                    padding: 10px;
                    margin: 5px;
                }
            """)
        else:
            self.setStyleSheet("""
                QFrame {
                    background-color: #252526;
                    border-radius: 10px;
                    padding: 10px;
                    margin: 5px;
                }
            """)

        # Skapa layout med marginaler
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)

        # Lägg till etikett för avsändare ("Du:" eller "Bot:")
        sender_label = QLabel("Du:" if is_user else "Bot:")
        sender_label.setStyleSheet("font-weight: bold;")
        layout.addWidget(sender_label)

        # Omvandla text med markdown för bot-meddelanden om det inte redan är HTML
        if not is_user and not message.lstrip().startswith("<"):
            message = markdown.markdown(message)

        # Skapa QTextBrowser för att visa meddelandet med stöd för rich text
        msg_widget = QTextBrowser()
        msg_widget.setReadOnly(True)
        msg_widget.setAcceptRichText(True)
        msg_widget.setOpenExternalLinks(True)
        msg_widget.setHtml(message)
        msg_widget.setFrameStyle(QFrame.NoFrame)
        msg_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        # Justera höjden dynamiskt baserat på innehållets storlek med en marginal
        msg_widget.document().adjustSize()
        doc_height = msg_widget.document().size().height()
        content_height = int(doc_height) + 20
        msg_widget.setMinimumHeight(content_height)

        layout.addWidget(msg_widget)

        # För bot-meddelanden: lägg till en tidsstämpel under meddelandet
        if not is_user:
            timestamp_label = QLabel(datetime.now().strftime("%H:%M"))
            timestamp_label.setStyleSheet("color: #888888; font-size: 10px;")
            timestamp_label.setAlignment(Qt.AlignRight)
            layout.addWidget(timestamp_label)

        # Sätt widgetens storlekspolicy för att expandera horisontellt
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setLayout(layout)


class ChatFrame(QWidget):
    """
    Huvudwidget för chat-gränssnittet.

    Hanterar chatt-historik, meddelandeinmatning och interaktionen med bot-motorn.
    """

    # Signal som sänds när ett kommando har utförts: (kommando, produkt_id, svar)
    command_executed = Signal(str, str, str)

    def __init__(self, config: dict, parent: QWidget = None):
        """
        Initierar ChatFrame.

        Args:
            config (dict): Konfigurationsparametrar för bot-motorn.
            parent (QWidget, optional): Föräldrawidget.
        """
        super().__init__(parent)
        self.config = config

        # Instansiera bot-motorn
        self.bot_engine = BotEngine(config)

        # Aktiv produkt för kontextbaserade kommandon
        self.active_product_id = None

        # Initiera användargränssnittet
        self.init_ui()

    def init_ui(self):
        """
        Konstruera och konfigurera gränssnittets layout och widgets.
        """
        main_layout = QVBoxLayout(self)

        # Skapa chattområdet med scrollfunktionalitet
        self.chat_area = QScrollArea()
        self.chat_area.setWidgetResizable(True)
        self.chat_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.chat_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        # Container för chatbubblorna
        self.chat_container = QWidget()
        self.chat_layout = QVBoxLayout(self.chat_container)
        self.chat_layout.setAlignment(Qt.AlignTop)
        self.chat_layout.setSpacing(10)
        self.chat_area.setWidget(self.chat_container)

        # Skapa inmatningsområdet
        input_frame = QFrame()
        input_layout = QHBoxLayout(input_frame)

        # Dropdown för att välja kommando
        self.command_combo = QComboBox()
        self.command_combo.addItem("Chat", "")
        self.command_combo.addItem("Tekniska detaljer (-t)", "-t")
        self.command_combo.addItem("Kompatibilitet (-c)", "-c")
        self.command_combo.addItem("Sammanfattning (-s)", "-s")
        self.command_combo.addItem("Fullständig info (-f)", "-f")
        input_layout.addWidget(self.command_combo)

        # Textfält för meddelandeinmatning
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Skriv kommando eller fråga här...")
        self.input_field.returnPressed.connect(self.send_message)
        input_layout.addWidget(self.input_field)

        # Skicka-knapp
        self.send_button = QPushButton("Skicka")
        self.send_button.clicked.connect(self.send_message)
        input_layout.addWidget(self.send_button)

        # Lägg till chattområdet och inmatningsområdet i huvudlayouten
        main_layout.addWidget(self.chat_area, 1)
        main_layout.addWidget(input_frame)

        self.setLayout(main_layout)

    def send_message(self):
        """
        Hantera sändning av meddelande från inmatningsfältet.
        """
        text = self.input_field.text().strip()
        if not text:
            return

        self.input_field.clear()

        # Om ett kommando är valt, lägg till det före meddelandet om det saknas
        command = self.command_combo.currentData()
        if command and not text.startswith(command):
            text = f"{command} {text}"

        # Visa användarens meddelande och processa det
        self.add_user_message(text)
        self.process_message(text)

    def process_message(self, text: str):
        """
        Skicka meddelandet till bot-motorn och visa svaret.

        Args:
            text (str): Meddelandetext från användaren.
        """
        command_match = re.match(r'^(-[tcfs])\s+(\S+)(.*)$', text)
        if command_match:
            command = command_match.group(1)
            product_id = command_match.group(2)
            rest = command_match.group(3).strip()
            response = self.bot_engine.execute_command(command, product_id, rest)
            self.add_bot_message(response)
            self.command_executed.emit(command, product_id, response)
        else:
            response = self.bot_engine.process_query(text, self.active_product_id)
            self.add_bot_message(response)

    def add_user_message(self, text: str):
        """
        Lägg till ett användarmeddelande i chattvyn.

        Args:
            text (str): Meddelandetexten.
        """
        bubble = ChatBubble(text, is_user=True)
        self.chat_layout.addWidget(bubble)
        self.scroll_to_bottom()

    def add_bot_message(self, text: str):
        """
        Lägg till ett botmeddelande i chattvyn.

        Args:
            text (str): Botens svar.
        """
        bubble = ChatBubble(text, is_user=False)
        self.chat_layout.addWidget(bubble)
        self.scroll_to_bottom()

    def display_system_message(self, html: str):
        """
        Visa ett systemmeddelande i chattvyn.

        Args:
            html (str): HTML-innehållet för systemmeddelandet.
        """
        bubble = ChatBubble(html, is_user=False)
        self.chat_layout.addWidget(bubble)
        self.scroll_to_bottom()

    def scroll_to_bottom(self):
        """
        Scrolla chattvyn till det nedre slutet.
        """
        self.chat_area.verticalScrollBar().setValue(
            self.chat_area.verticalScrollBar().maximum()
        )

    def set_active_product(self, product_id: str):
        """
        Sätt aktiv produkt för att stödja kontextbaserade kommandon.

        Args:
            product_id (str): Identifierare för produkten.
        """
        self.active_product_id = product_id
        if product_id:
            self.display_system_message(f"<p><i>Aktiv produkt ändrad till: {product_id}</i></p>")

    def clear_chat(self):
        """
        Rensa chatt-historiken och visa ett systemmeddelande.
        """
        while self.chat_layout.count():
            item = self.chat_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        self.display_system_message("<p><i>Chathistoriken har rensats.</i></p>")
