# DocuMentor-Suite


Ett kraftfullt verktyg för att analysera markdown-dokument och generera högkvalitativ träningsdata för LLM-modeller, speciellt anpassat för teknisk produktdokumentation.

## Funktioner

- **Robust Dokumentanalys**
  - Extraherar artikelnummer och metadata
  - Identifierar produktrelationer och kompatibilitet
  - Hanterar tekniska specifikationer
  - Processerar produktbilder

- **Träningsdatagenerering**
  - Stöd för flera kommandotyper:
    - `-f` (fullständig produktinfo)
    - `-s` (produktsammanfattningar)
    - `-t` (tekniska detaljer)
    - `-c` (kompatibilitetsinformation)
  - Konsekvent markdown-formattering
  - Validering av träningsdata

- **Bildhantering**
  - Automatisk extrahering av produktbilder
  - Länkning mellan artikelnummer och bilder
  - Stöd för olika bildformat

- **Avancerad Textanalys**
  - Sektionsbaserad innehållsanalys
  - Mönsterigenkänning för tekniska data
  - Robust felhantering

## Installation

### Med Poetry (rekommenderat)

```bash
# Klona repository
git clone https://github.com/yourusername/markdown-analyzer.git
cd markdown-analyzer

# Installera med Poetry
poetry install
```

### Med pip

```bash
pip install markdown-analyzer
```

## Användning

### Kommandorad

Analysera en katalog med markdown-filer:

```bash
markdown-analyzer --input-dir ./docs --output-dir ./output
```

Generera specifika träningskommandon:

```bash
markdown-analyzer --input-dir ./docs --commands f s t
```


```bash
markdown-analyzer --input-dir ./docs --commands f s t --output-dir ./output
```

### Python API

```python
from markdown_analyzer import MarkdownAnalyzer

# Initiera analyzer
analyzer = MarkdownAnalyzer(debug=True)

# Processa dokument
analyzer.process_directory("./docs", num_workers=4)

# Generera träningsdata
analyzer.generate_training_data("./output", commands=['f', 's', 't', 'c'])

# Skriv ut statistik
analyzer.print_summary()
```

## Projektstruktur

```
markdown_analyzer/
├── core/
│   ├── document.py        # Datastrukturer
│   ├── patterns.py        # Regex-mönster
│   └── errors.py         # Felhantering
├── extractors/
│   ├── base.py           # Basextraktor
│   ├── metadata.py       # Metadataextraktor
│   ├── compatibility.py  # Kompatibilitetsextraktor
│   └── technical.py      # Teknisk extraktor
├── trainers/
│   ├── base.py           # Bastrainer
│   ├── formatters.py     # Outputformattering
│   └── commands.py       # Kommandoimplementationer
└── utils/
    ├── text.py           # Textbehandling
    ├── validation.py     # Datavalidering
    └── logging.py        # Loggning
```

## Konfiguration

### Loggning

Loggning kan konfigureras genom att sätta debug-flaggan:

```python
analyzer = MarkdownAnalyzer(debug=True)
```

### Parallell Processering

Antal parallella arbetare kan justeras:

```bash
markdown-analyzer --input-dir ./docs --workers 8
```

## Utveckling

### Förutsättningar

- Python 3.8+
- Poetry
- Git

### Utvecklingsmiljö

```bash
# Klona repository
git clone https://github.com/yourusername/markdown-analyzer.git
cd markdown-analyzer

# Installera utvecklingsberoenden
poetry install --with dev

# Aktivera virtual environment
poetry shell

# Kör tester
pytest
```

### Kodkvalitet

Vi använder flera verktyg för att säkerställa kodkvalitet:

- **black** för kodformattering
- **isort** för importsortering
- **mypy** för typkontroll
- **pylint** för kodanalys

Kör alla kvalitetskontroller:

```bash
poetry run black .
poetry run isort .
poetry run mypy .
poetry run pylint markdown_analyzer
```

## Utöka Funktionalitet

### Lägga till ny Extraktor

1. Skapa ny klass i extractors/:
```python
from .base import BaseExtractor

class NewExtractor(BaseExtractor):
    def extract(self, content: str) -> Dict:
        # Implementera extraktion
        pass
```

2. Registrera i MarkdownAnalyzer:
```python
self.new_extractor = NewExtractor()
```

### Lägga till nytt Kommando

1. Skapa ny Trainer i trainers/commands.py:
```python
class NewCommandTrainer(BaseTrainer):
    def create_training_data(self, doc: DocumentStructure) -> List[TrainingExample]:
        # Implementera träningsdatagenerering
        pass
```

2. Registrera i MarkdownAnalyzer:
```python
self.trainers['new'] = NewCommandTrainer()
```
