# Utvecklardokumentation

## Arkitekturöversikt

Markdown Analyzer är uppbyggd kring flera nyckelkoncept:

### 1. Dokumentstruktur

`DocumentStructure` är den centrala dataklassen som håller all extraherad information:

```python
@dataclass
class DocumentStructure:
    filename: str
    article_number: str
    document_type: str
    product_name: str
    description: str
    # ... mer information
```

### 2. Extraktorer

Varje extraktor är specialiserad på en typ av information:

- `MetadataExtractor`: dokumentinformation
- `CompatibilityExtractor`: Produktrelationer
- `TechnicalExtractor`: Tekniska specifikationer
- `ImageExtractor`: Produktbilder

### 3. Trainers

Trainers genererar träningsdata för specifika kommandon:

- `BasicInfoTrainer`: produktinfo (-f)
- `SummaryTrainer`: Produktsammanfattningar (-s)
- `TechnicalTrainer`: Teknisk information (-t)
- `CompatibilityTrainer`: Kompatibilitetsinfo (-c)

## Dataflöde

1. **Dokumentinläsning**
   ```
   Markdown-fil -> TextProcessor -> Rensat innehåll
   ```

2. **Informationsextraktion**
   ```
   Innehåll -> Extraktorer -> DocumentStructure
   ```

3. **Träningsdatagenerering**
   ```
   DocumentStructure -> Trainers -> TrainingExample
   ```

## Implementationsguide

### Lägga till ny Extraktor

1. Skapa ny klass i `extractors/`:

```python
from .base import BaseExtractor
from typing import Dict, Any

class NewExtractor(BaseExtractor):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def extract(self, content: str) -> Dict[str, Any]:
        try:
            # Implementera extraktion
            result = self._extract_specific_data(content)
            
            # Validera resultat
            if self.validate_output(result):
                return result
            
            self.logger.warning("Invalid extraction result")
            return {}
            
        except Exception as e:
            self.logger.error(f"Extraction failed: {str(e)}")
            return {}
    
    def validate_output(self, data: Dict[str, Any]) -> bool:
        # Implementera validering
        return True
```

2. Uppdatera `MarkdownAnalyzer`:

```python
from .extractors import NewExtractor

class MarkdownAnalyzer:
    def __init__(self):
        # ...
        self.new_extractor = NewExtractor()
    
    def process_file(self, filepath: Path) -> Optional[DocumentStructure]:
        # ...
        # Lägg till ny extraktion
        new_data = self.new_extractor.extract(content)
        doc.new_field = new_data
        # ...
```

### Lägga till nytt Kommando

1. Skapa ny Trainer:

```python
from .base import BaseTrainer
from ..core.document import DocumentStructure
from typing import List

class NewCommandTrainer(BaseTrainer):
    def create_training_data(self, doc: DocumentStructure) -> List[TrainingExample]:
        if not self._has_required_data(doc):
            return []
        
        output_parts = []
        
        # Formattera output
        output_parts.append(self.formatter.format_heading("New Data"))
        # ... Lägg till mer formattering
        
        example = TrainingExample(
            command="new",
            article_number=doc.article_number,
            input_text=f"-new {doc.article_number}",
            output_text="".join(output_parts)
        )
        
        return [example] if self.validate_example(example) else []
    
    def _has_required_data(self, doc: DocumentStructure) -> bool:
        # Kontrollera att nödvändig data finns
        return True
```

2. Registrera i system:

```python
class MarkdownAnalyzer:
    def __init__(self):
        # ...
        self.trainers['new'] = NewCommandTrainer()
```

### Testning

1. Skapa testfixtures:

```python
# tests/fixtures/test_document.md
# Test Product
Article number: 12345

Technical specifications:
- Voltage: 230V
- Current: 10A
```

2. Implementera tester:

```python
# tests/test_extractors.py
import pytest
from markdown_analyzer.extractors import NewExtractor

def test_new_extractor():
    extractor = NewExtractor()
    content = "Test content"
    
    result = extractor.extract(content)
    assert result
    assert "expected_field" in result
    assert result["expected_field"] == "expected_value"
```

### Felhantering

Använd dedikerade felklasser:

```python
# markdown_analyzer/core/errors.py
class ExtractionError(MarkdownAnalyzerError):
    """Fel vid extraktion av data"""
    pass

class ValidationError(MarkdownAnalyzerError):
    """Fel vid validering av data"""
    pass

# I kod
try:
    result = self._extract_data(content)
except Exception as e:
    raise ExtractionError(f"Failed to extract data: {str(e)}")
```

### Loggning

Använd strukturerad loggning:

```python
def process_file(self, filepath: Path) -> Optional[DocumentStructure]:
    logger = logging.getLogger(__name__)
    
    logger.info("Processing file", extra={
        'filepath': str(filepath),
        'file_size': filepath.stat().st_size
    })
    
    try:
        # Process file
        logger.debug("Extraction complete", extra={
            'extracted_fields': ['field1', 'field2']
        })
    except Exception as e:
        logger.error("Processing failed", extra={
            'error': str(e),
            'filepath': str(filepath)
        })
```

## Prestandaoptimering

### Caching

```python
from functools import lru_cache

class Extractor:
    @lru_cache(maxsize=1000)
    def _extract_pattern(self, content: str) -> List[str]:
        # Implementera tidskrävande extraktion
        pass
```

### Parallell Processering

```python
def process_files(self, files: List[Path], num_workers: int = 4) -> None:
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = [
            executor.submit(self.process_file, file)
            for file in files
        ]
        
        for future in as_completed(futures):
            try:
                result = future.result()
                if result:
                    self.documents.append(result)
            except Exception as e:
                self.logger.error(f"Processing failed: {str(e)}")

```

### Minnesoptimering

För stora dataset, implementera strömhantering:

```python
def process_large_file(self, filepath: Path) -> Generator[Dict, None, None]:
    with filepath.open('r', encoding='utf-8') as f:
        buffer = []
        for line in f:
            if line.strip():
                buffer.append(line)
            if len(buffer) >= 1000:  # Process i batches
                yield self._process_buffer(buffer)
                buffer = []
        if buffer:
            yield self._process_buffer(buffer)
```

## API-dokumentation

### Core Module

#### DocumentStructure

```python
@dataclass
class DocumentStructure:
    """
    Huvudstruktur för ett analyserat dokument.
    
    Attributes:
        filename (str): Namn på källfilen
        article_number (str): Produktens artikelnummer
        document_type (str): Typ av dokument
        product_name (str): Produktnamn
        description (str): Produktbeskrivning
        manufacturer (Optional[str]): Tillverkare
        product_images (List[ProductImage]): Lista av produktbilder
        compatibility (List[Compatibility]): Kompatibilitetsinformation
        technical_specs (List[TechnicalSpec]): Tekniska specifikationer
        installation (Optional[InstallationInfo]): Installationsinformation
        processing_errors (List[str]): Eventuella fel vid processering
    """
```

#### Patterns

```python
# core/patterns.py
ARTICLE_NUMBER_PATTERNS: List[str]
    """Regex-mönster för att matcha artikelnummer."""

COMPATIBILITY_PATTERNS: List[str]
    """Mönster för att identifiera kompatibilitetsinformation."""

TECHNICAL_PATTERNS: Dict[str, List[str]]
    """Mönster för olika typer av tekniska specifikationer."""
```

### Extractors Module

#### BaseExtractor

```python
class BaseExtractor:
    """
    Basklass för alla extraktorer.
    
    Methods:
        extract(content: str) -> Dict:
            Extraherar information från innehåll.
            
        validate_output(data: Dict) -> bool:
            Validerar extraherad data.
            
        _clean_text(text: str) -> str:
            Rensar text från oönskade tecken.
    """
```

#### MetadataExtractor

```python
class MetadataExtractor(BaseExtractor):
    """
    Extraherar metadata från dokument.
    
    Methods:
        extract_article_number(filename: str, content: str) -> str:
            Extraherar artikelnummer från filnamn och innehåll.
            
        extract_document_type(filename: str) -> str:
            Bestämmer dokumenttyp baserat på filnamn.
            
        extract_product_name(content: str) -> str:
            Extraherar produktnamn från innehåll.
    """
```

### Trainers Module

#### BaseTrainer

```python
class BaseTrainer:
    """
    Basklass för alla träningsdatageneratorer.
    
    Methods:
        create_training_data(doc: DocumentStructure) -> List[TrainingExample]:
            Skapar träningsexempel från ett dokument.
            
        validate_example(example: TrainingExample) -> bool:
            Validerar ett träningsexempel.
    """
```

#### MarkdownFormatter

```python
class MarkdownFormatter:
    """
    Hanterar formattering av markdown-output.
    
    Methods:
        format_heading(text: str, level: int = 1) -> str:
            Formaterar en rubrik.
            
        format_image(image_ref: str, alt_text: str = "") -> str:
            Formaterar en bildreferens.
            
        format_list(items: List[str], ordered: bool = False) -> str:
            Formaterar en lista.
    """
```

## Bästa Praxis

### Kodstandard

1. **Typning**
   - Använd alltid typannotationer
   - Använd Optional för optionella värden
   - Definiera custom types för komplex logik

```python
from typing import Optional, List, Dict, TypeVar, Generic

T = TypeVar('T')

class DataContainer(Generic[T]):
    def __init__(self, data: T):
        self.data = data
```

2. **Felhantering**
   - Använd specifika undantag
   - Logga alltid fel med kontext
   - Implementera återhämtning där möjligt

```python
try:
    result = self.process_data(data)
except ValidationError as e:
    self.logger.warning(f"Validation failed: {e}", extra={'data': data})
    result = self.fallback_processing(data)
except ProcessingError as e:
    self.logger.error(f"Processing failed: {e}", extra={'data': data})
    raise
```

3. **Dokumentation**
   - Dokumentera alla publika metoder
   - Inkludera exempel i docstrings
   - Håll dokumentationen uppdaterad

```python
def process_data(self, data: Dict[str, Any]) -> ProcessedData:
    """
    Processar rådata till strukturerad form.
    
    Args:
        data: Dictionary med rådata att processa
        
    Returns:
        ProcessedData: Strukturerad data
        
    Raises:
        ValidationError: Om data är ogiltig
        ProcessingError: Vid processningsfel
        
    Example:
        >>> processor = DataProcessor()
        >>> result = processor.process_data({"key": "value"})
    """
```

### Testing

1. **Enhetstester**
   - Testa varje komponent isolerat
   - Använd fixtures för testdata
   - Implementera edge cases

```python
@pytest.fixture
def sample_document():
    return DocumentStructure(
        filename="test.md",
        article_number="12345",
        document_type="manual",
        # ...
    )

def test_compatibility_extraction(sample_document):
    extractor = CompatibilityExtractor()
    result = extractor.extract(sample_document.content)
    assert len(result) > 0
    assert all(isinstance(r, Compatibility) for r in result)
```

2. **Integrationstester**
   - Testa komponenter tillsammans
   - Använd verkliga exempel
   - Verifiera dataflöden

```python
def test_full_processing_pipeline(tmp_path):
    # Sätt upp testmiljö
    input_dir = tmp_path / "input"
    input_dir.mkdir()
    create_test_files(input_dir)
    
    # Kör pipeline
    analyzer = MarkdownAnalyzer()
    analyzer.process_directory(input_dir)
    
    # Verifiera resultat
    assert len(analyzer.documents) > 0
    verify_document_structure(analyzer.documents[0])
```

### Versionshantering

1. **Semantic Versioning**
   - Major.Minor.Patch
   - Dokumentera ändringar i CHANGELOG.md
   - Tagga releases

2. **Git Workflow**
   - Använd feature branches
   - Kräv code review
   - Automatisera tester vid PR

## Deployment

### Paketering

1. **Poetry**
   ```bash
   poetry build
   poetry publish
   ```

2. **Distribution**
   ```bash
   pip install dist/markdown_analyzer-0.1.0.tar.gz
   ```

### CI/CD Pipeline

```yaml
# .github/workflows/main.yml
name: CI/CD

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
      - name: Install dependencies
        run: poetry install
      - name: Run tests
        run: poetry run pytest
      - name: Run linters
        run: |
          poetry run black --check .
          poetry run mypy .
```

## Underhåll

### Loggning och Övervakning

1. **Strukturerad Loggning**
   ```python
   logger.info("Processing complete", extra={
       'document_count': len(self.documents),
       'error_count': len(self.errors),
       'processing_time': time.time() - start_time
   })
   ```

2. **Prestandamätning**
   ```python
   from contextlib import contextmanager
   import time
   
   @contextmanager
   def timing(operation: str):
       start = time.time()
       yield
       elapsed = time.time() - start
       logger.info(f"{operation} took {elapsed:.2f} seconds")
   ```

### Felsökning

1. **Debug Mode**
   ```python
   if self.debug:
       self.logger.debug("Detailed state", extra={
           'current_document': doc.filename,
           'extracted_data': extracted_data,
           'processing_stage': 'extraction'
       })
   ```

2. **Diagnostikverktyg**
   ```python
   def diagnose_document(self, doc: DocumentStructure) -> Dict[str, Any]:
       """Genererar diagnostikrapport för ett dokument."""
       return {
           'metadata_quality': self._assess_metadata(doc),
           'extraction_coverage': self._calculate_coverage(doc),
           'validation_results': self._validate_document(doc),
           'processing_history': doc.processing_history
       }
   ```

## Framtida Utveckling

1. **Planerade Funktioner**
   - Stöd för fler dokumentformat
   - Förbättrad bildanalys
   - Automatisk kvalitetsbedömning

2. **Arkitekturutveckling**
   - Modulär pluginarkitektur
   - Förbättrad parallellisering
   - Distribuerad processering

3. **Integrationer**
   - API-gateway
   - Databaskoppling
   - Webhooks