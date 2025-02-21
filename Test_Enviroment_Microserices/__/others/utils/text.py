
# markdown_analyzer/utils/text.py
import re
from typing import List, Dict, Optional

class TextProcessor:
    """Hjälpklass för textbehandling"""
    
    @staticmethod
    def clean_text(text: str) -> str:
        """Rensar text från oönskade tecken och formattering"""
        # Ta bort överflödiga mellanslag
        text = re.sub(r'\s+', ' ', text)
        # Ta bort speciella tecken
        text = re.sub(r'[^\w\s\-.,;:?!()\[\]{}"\']+', '', text)
        return text.strip()
    
    @staticmethod
    def extract_sections(markdown: str) -> Dict[str, str]:
        """Extraherar sektioner från markdown-text"""
        sections = {}
        current_section = "root"
        current_content = []
        
        for line in markdown.split('\n'):
            if line.startswith('#'):
                # Spara föregående sektion
                if current_content:
                    sections[current_section] = '\n'.join(current_content).strip()
                    current_content = []
                
                # Starta ny sektion
                level = len(re.match(r'^#+', line).group(0))
                title = line.lstrip('#').strip()
                current_section = title
            else:
                current_content.append(line)
        
        # Spara sista sektionen
        if current_content:
            sections[current_section] = '\n'.join(current_content).strip()
        
        return sections
    
    @staticmethod
    def extract_lists(text: str) -> List[List[str]]:
        """Extraherar listor från text"""
        lists = []
        current_list = []
        
        for line in text.split('\n'):
            list_match = re.match(r'^[\s-*+]\s+(.+)$', line)
            if list_match:
                current_list.append(list_match.group(1).strip())
            elif current_list:
                lists.append(current_list)
                current_list = []
        
        if current_list:
            lists.append(current_list)
        
        return lists

