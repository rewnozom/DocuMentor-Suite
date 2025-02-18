# html_logger.py
"""
HTMLLogHandler: A logging handler that collects log records during a run and writes an HTML report.

This handler gathers all log records and, upon closure, writes an HTML file that features:
- A dark-themed design with dark-gray background and orange accents.
- A header with a search box, dynamic level filter buttons (using allowed levels such as ERROR, WARNING, SUCCESS plus custom levels based on your SUFFIX_MAP),
  and "Collapse All"/"Expand All" buttons.
- A table listing each log record with the columns:
    Timestamp | Level | Filens titel | Filens artikelnummer | User Input | AI Output
- The AI Output column is contained in a collapsible code block that starts collapsed.
- A status bar that displays the number of visible logs versus total logs.
  
Log messages for training samples should be formatted as follows:

    Training Sample:
    User Input: <user_input>
    AI Output:
    <ai_output>

The handler then attempts to parse the user_input to extract "filens titel" (assumed second token) and "filens artikelnummer" (assumed third token).
"""

import logging
import datetime
from pathlib import Path
import re

# Definiera dina custom kategorier (t.ex. från din SUFFIX_MAP)
CUSTOM_CATEGORIES = [
    "installationer",
    "produktinfo",
    "manual",
    "produktblad",
    "ospecificerad",
    "certifieringar",
    "broschyr"
]

# De standardnivåer som alltid ska visas
STANDARD_LEVELS = ["ERROR", "WARNING", "SUCCESS"]

def allowed_levels():
    """
    Returnerar en uppsättning av tillåtna nivåer: STANDARD_LEVELS plus de custom kategorierna (uppercased).
    """
    return set(STANDARD_LEVELS).union({cat.upper() for cat in CUSTOM_CATEGORIES})

class HTMLLogHandler(logging.Handler):
    """
    HTMLLogHandler collects log records and writes an HTML report on closure.
    
    The HTML report includes:
      - A header with search and filter controls.
      - A table with columns: Timestamp, Level, Filens titel, Filens artikelnummer, User Input, AI Output.
      - The AI Output is displayed in a collapsible code block (collapsed by default).
    """
    def __init__(self, log_dir: str = "logs", filename_prefix: str = "training_dataset_log"):
        """
        Initialize the HTMLLogHandler.
        
        Args:
            log_dir (str): Directory where the HTML log file will be saved.
            filename_prefix (str): Prefix for the generated HTML file name.
        """
        super().__init__()
        self.records = []
        self.level_counts = {}  # Räknar förekomsten av varje level
        self.log_dir = Path(log_dir)
        if not self.log_dir.exists():
            self.log_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.filename = self.log_dir / f"{filename_prefix}_{timestamp}.html"
        self.records = []
        self.level_counts = {}

    def formatTime(self, record, datefmt=None):
        """
        Formats the record timestamp.
        """
        ct = datetime.datetime.fromtimestamp(record.created)
        if datefmt:
            s = ct.strftime(datefmt)
        else:
            s = ct.strftime("%Y-%m-%d %H:%M:%S")
        return s

    def emit(self, record: logging.LogRecord):
        """
        Processes a log record and appends an HTML table row to self.records.
        
        If the log message is in the format:
        
            Training Sample:
            User Input: <user_input>
            AI Output:
            <ai_output>
        
        it extracts user_input and ai_output and then attempts to extract:
          - Filens titel: assumed as the second token of user_input.
          - Filens artikelnummer: assumed som den tredje tokenen.
          
        Otherwise, the whole message is used as AI Output.
        """
        try:
            msg_text = record.getMessage()
            # Standardvärden
            user_input = ""
            ai_output = ""
            file_title = ""
            article_number = ""
            # Försök att extrahera med en regex
            pattern = r"Training Sample:\s*User Input:\s*(.*?)\s*AI Output:\s*(.*)"
            m = re.search(pattern, msg_text, re.DOTALL)
            if m:
                user_input = m.group(1).strip()
                ai_output = m.group(2).strip()
            else:
                # Om inte, använd hela meddelandet som ai_output
                ai_output = msg_text

            # Försök att extrahera filens titel och artikelnummer från user_input
            if user_input.startswith("-f"):
                tokens = user_input.split()
                if len(tokens) >= 3:
                    file_title = tokens[1]
                    article_number = tokens[2]
                elif len(tokens) >= 2:
                    file_title = tokens[1]
            # Uppdatera nivåräkning
            self.level_counts[record.levelname] = self.level_counts.get(record.levelname, 0) + 1

            timestamp = self.formatTime(record, "%Y-%m-%d %H:%M:%S")
            row_id = f"log_row_{len(self.records)}"
            # Bygg HTML-raden med de önskade kolumnerna
            row = (
                f"<tr id='{row_id}'>"
                f"<td class='timestamp'>{timestamp}</td>"
                f"<td class='level-{record.levelname.lower()}'>{record.levelname}</td>"
                f"<td class='file-title'>{file_title}</td>"
                f"<td class='article-number'>{article_number}</td>"
                f"<td class='user-input'>{user_input}</td>"
                f"<td class='ai-output'>"
                f"<button class='toggle-button' onclick='toggleMessage(this)'>Expand</button> "
                f"<button class='copy-button' onclick='copyToClipboard(this)'>Copy</button>"
                f"<div class='collapsible-content'><div class='code-block'><pre>{ai_output}</pre></div></div>"
                f"</td>"
                f"</tr>\n"
            )
            self.records.append(row)
        except Exception:
            self.handleError(record)

    def _generate_filter_buttons(self):
        """
        Generates HTML for filter buttons based on allowed levels and the level_counts.
        """
        buttons = ""
        levels = allowed_levels()
        for level in sorted(self.level_counts.keys()):
            if level in levels:
                count = self.level_counts.get(level, 0)
                buttons += f"<button class='level-filter' data-level='{level}' onclick='toggleLevelFilter(\"{level}\")'>{level} <span class='badge badge-{level.lower()}'>{count}</span></button>\n"
        return buttons

    def close(self):
        """
        Writes out the complete HTML log report and then closes the handler.
        The HTML report includes:
          - A header with a search box and dynamic filter buttons.
          - A table with columns: Timestamp, Level, Filens titel, Filens artikelnummer, User Input, AI Output.
          - AI Output is contained in a collapsible code block that starts collapsed.
          - JavaScript controls for toggling individual rows and for "Collapse All"/"Expand All".
        """
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                f.write("<!DOCTYPE html>\n<html>\n<head>\n")
                f.write("<meta charset='utf-8'>\n")
                f.write("<title>LoRA LLM Data Training Log Report</title>\n")
                # CSS-stilar
                f.write("<style>\n")
                f.write("body { font-family: 'Segoe UI', Arial, sans-serif; margin: 0; background: #1a1a1a; color: #e0e0e0; }\n")
                f.write(".container { max-width: 1400px; margin: 0 auto; padding: 2rem; }\n")
                f.write("header { padding: 1rem 0; border-bottom: 2px solid #3d3d3d; display: flex; flex-wrap: wrap; gap: 1rem; align-items: center; }\n")
                f.write("header h1 { margin: 0; font-size: 1.8rem; color: #fff; }\n")
                f.write(".header-controls { display: flex; gap: 0.5rem; flex-wrap: wrap; }\n")
                f.write(".search-box { padding: 0.5rem; border-radius: 4px; border: 1px solid #444; background: #2d2d2d; color: #fff; }\n")
                f.write("button { padding: 8px 16px; margin: 0.2rem; border: none; border-radius: 4px; cursor: pointer; background: #e67e00; color: #fff; transition: background 0.2s ease; }\n")
                f.write("button:hover { background: #ff9008; }\n")
                f.write(".level-filter { background: #2d2d2d; }\n")
                f.write(".level-filter.active { background: #e67e00; }\n")
                f.write(".badge { padding: 2px 8px; border-radius: 12px; background: #555; margin-left: 0.5rem; }\n")
                f.write("table { width: 100%; border-collapse: collapse; margin-top: 1rem; }\n")
                f.write("th, td { padding: 12px; border: 1px solid #333; text-align: left; vertical-align: top; }\n")
                f.write("th { background: #383838; position: sticky; top: 0; }\n")
                f.write("tr:nth-child(even) { background: #2d2d2d; }\n")
                f.write(".toggle-button, .copy-button { font-size: 0.8rem; margin-right: 4px; }\n")
                # Gör code-block som collapsable och startar som collapsed
                f.write(".code-block { background: #2d2d2d; border: 1px solid #444; border-radius: 4px; padding: 8px; margin: 8px 0; max-height: 200px; overflow-y: auto; display: none; }\n")
                f.write(".collapsible-content { display: none; }\n")
                f.write(".timestamp { font-size: 0.9rem; color: #aaa; }\n")
                f.write(".file-title, .article-number, .user-input { font-family: 'Consolas', monospace; font-size: 0.9rem; }\n")
                f.write(".status-bar { margin-top: 1rem; padding: 0.5rem; background: #383838; border-radius: 4px; font-size: 0.9rem; }\n")
                f.write("::-webkit-scrollbar { width: 8px; }\n")
                f.write("::-webkit-scrollbar-thumb { background: #666; border-radius: 4px; }\n")
                f.write("</style>\n")
                f.write("</head>\n<body>\n")
                f.write("<div class='container'>\n")
                f.write("<header>\n")
                f.write(f"<h1>LoRA LLM Data Training Log Report - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</h1>\n")
                f.write("<div class='header-controls'>\n")
                f.write("<input type='text' id='searchBox' class='search-box' placeholder='Search logs...' oninput='filterLogs()'>\n")
                f.write(self._generate_filter_buttons())
                f.write("<button onclick='collapseAll()'>Collapse All</button>\n")
                f.write("<button onclick='expandAll()'>Expand All</button>\n")
                f.write("</div>\n</header>\n")
                f.write("<div class='table-container'>\n")
                f.write("<table>\n<thead>\n<tr>\n")
                f.write("<th>Timestamp</th>\n")
                f.write("<th>Level</th>\n")
                f.write("<th>Filens titel</th>\n")
                f.write("<th>Filens artikelnummer</th>\n")
                f.write("<th>User Input</th>\n")
                f.write("<th>AI Output</th>\n")
                f.write("</tr>\n</thead>\n<tbody>\n")
                for row in self.records:
                    f.write(row)
                f.write("</tbody>\n</table>\n</div>\n")
                f.write("<div class='status-bar' id='statusBar'>\n")
                f.write("<span id='logCount'>Showing 0 logs</span>\n")
                f.write("<span>HTMLLogHandler v1.0.0</span>\n")
                f.write("</div>\n")
                f.write("</div>\n")
                f.write("<script>\n")
                # Alla collapsible code blocks startar som dolda
                f.write("document.addEventListener('DOMContentLoaded', function() {\n")
                f.write("  var blocks = document.querySelectorAll('.code-block');\n")
                f.write("  blocks.forEach(function(block) { block.style.display = 'none'; });\n")
                f.write("  var contents = document.querySelectorAll('.collapsible-content');\n")
                f.write("  contents.forEach(function(content) { content.style.display = 'none'; });\n")
                f.write("  updateStatusBar(0);\n")
                f.write("});\n")
                f.write("function toggleMessage(btn) {\n")
                f.write("  var contentDiv = btn.parentElement.querySelector('.collapsible-content');\n")
                f.write("  var codeBlock = contentDiv.querySelector('.code-block');\n")
                f.write("  if (contentDiv.style.display === 'none') {\n")
                f.write("    contentDiv.style.display = 'block';\n")
                f.write("    codeBlock.style.display = 'block';\n")
                f.write("    btn.textContent = 'Collapse';\n")
                f.write("  } else {\n")
                f.write("    contentDiv.style.display = 'none';\n")
                f.write("    codeBlock.style.display = 'none';\n")
                f.write("    btn.textContent = 'Expand';\n")
                f.write("  }\n")
                f.write("}\n")
                f.write("function collapseAll() {\n")
                f.write("  var toggleButtons = document.getElementsByClassName('toggle-button');\n")
                f.write("  Array.from(toggleButtons).forEach(function(btn) {\n")
                f.write("    btn.textContent = 'Expand';\n")
                f.write("    var contentDiv = btn.parentElement.querySelector('.collapsible-content');\n")
                f.write("    var codeBlock = contentDiv.querySelector('.code-block');\n")
                f.write("    contentDiv.style.display = 'none';\n")
                f.write("    codeBlock.style.display = 'none';\n")
                f.write("  });\n")
                f.write("  filterLogs();\n")
                f.write("}\n")
                f.write("function expandAll() {\n")
                f.write("  var toggleButtons = document.getElementsByClassName('toggle-button');\n")
                f.write("  Array.from(toggleButtons).forEach(function(btn) {\n")
                f.write("    btn.textContent = 'Collapse';\n")
                f.write("    var contentDiv = btn.parentElement.querySelector('.collapsible-content');\n")
                f.write("    var codeBlock = contentDiv.querySelector('.code-block');\n")
                f.write("    contentDiv.style.display = 'block';\n")
                f.write("    codeBlock.style.display = 'block';\n")
                f.write("  });\n")
                f.write("  filterLogs();\n")
                f.write("}\n")
                f.write("function filterLogs() {\n")
                f.write("  var searchText = document.getElementById('searchBox').value.toLowerCase();\n")
                f.write("  var rows = document.querySelectorAll('tbody tr');\n")
                f.write("  var visible = 0;\n")
                f.write("  rows.forEach(function(row) {\n")
                f.write("    var text = row.textContent.toLowerCase();\n")
                f.write("    var display = text.includes(searchText);\n")
                f.write("    row.style.display = display ? '' : 'none';\n")
                f.write("    if (display) visible++;\n")
                f.write("  });\n")
                f.write("  updateStatusBar(visible);\n")
                f.write("}\n")
                f.write("function updateStatusBar(visibleCount) {\n")
                f.write("  var total = document.querySelectorAll('tbody tr').length;\n")
                f.write("  document.getElementById('logCount').textContent = 'Showing ' + visibleCount + ' of ' + total + ' logs';\n")
                f.write("}\n")
                f.write("function toggleLevelFilter(level) {\n")
                f.write("  var btn = document.querySelector('button[data-level=\"' + level + '\"]');\n")
                f.write("  btn.classList.toggle('active');\n")
                f.write("  filterByLevels();\n")
                f.write("}\n")
                f.write("function filterByLevels() {\n")
                f.write("  var active = Array.from(document.querySelectorAll('button.level-filter.active')).map(function(btn){ return btn.dataset.level; });\n")
                f.write("  var rows = document.querySelectorAll('tbody tr');\n")
                f.write("  var visible = 0;\n")
                f.write("  rows.forEach(function(row) {\n")
                f.write("    var level = row.querySelector('td:nth-child(2)').textContent;\n")
                f.write("    var display = (active.length === 0 || active.indexOf(level) !== -1) && row.style.display !== 'none';\n")
                f.write("    row.style.display = display ? '' : 'none';\n")
                f.write("    if (display) visible++;\n")
                f.write("  });\n")
                f.write("  updateStatusBar(visible);\n")
                f.write("}\n")
                f.write("function copyToClipboard(btn) {\n")
                f.write("  var content = btn.parentElement.querySelector('.code-block pre').textContent;\n")
                f.write("  navigator.clipboard.writeText(content);\n")
                f.write("  var original = btn.textContent;\n")
                f.write("  btn.textContent = 'Copied!';\n")
                f.write("  setTimeout(function(){ btn.textContent = original; }, 1000);\n")
                f.write("}\n")
                f.write("</script>\n")
                f.write("</body>\n</html>\n")
        except Exception as e:
            print(f"Error writing HTML log file: {str(e)}")
        finally:
            super().close()
