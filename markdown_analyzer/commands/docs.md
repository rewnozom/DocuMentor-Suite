# Commands Directory Documentation

## Overview
The `commands` directory contains the command system for the markdown analyzer framework. It implements a command pattern design that handles various operations on markdown documents and dataset generation.

## Directory Structure
```
commands/
├── __init__.py           # Public API exports
├── base.py              # Base command class
├── registry.py          # Command registry system
├── implementations.py   # Command implementations
└── dataset_commands.py  # Dataset-specific commands
```

## Key Components

### 1. Base Command System (`base.py`)
The `BaseCommand` class serves as the foundation for all commands in the system.

```python
class BaseCommand:
    def process(self, doc: DocumentStructure) -> Dict:
        """Process a document and return training data"""

    def validate(self, result: Dict) -> bool:
        """Validate the result"""
```

Key features:
- Abstract base class for all commands
- Provides validation and formatting interfaces
- Handles common command functionality

### 2. Command Registry (`registry.py`)
The `CommandRegistry` manages command registration and access.

```python
registry = CommandRegistry()
registry.register_command('f', FullInfoCommand)
command = registry.get_command('f')
```

Features:
- Central command management
- Dynamic command registration
- Command lookup and instantiation

### 3. Standard Commands (`implementations.py`)
Standard commands for document processing:

#### FullInfoCommand (-f)
- Generates complete product information
- Includes images, descriptions, and specifications
- Example: `-f 12345`

#### SummaryCommand (-s)
- Creates concise product summaries
- Extracts key information
- Example: `-s 12345`

#### TechnicalCommand (-t)
- Extracts technical specifications
- Formats technical data
- Example: `-t 12345`

#### CompatibilityCommand (-c)
- Handles compatibility information
- Shows product relationships
- Example: `-c 12345`

### 4. Dataset Commands (`dataset_commands.py`)
Commands for handling training datasets:

#### DatasetGenerateCommand
```python
generator = DatasetGenerateCommand(input_dirs=['./docs'], output_dir='./output')
results = generator.process(['f', 's', 't', 'c'])
```

Features:
- Generates training datasets from markdown files
- Supports multiple input directories
- Parallel processing capabilities
- Validation and export functionality

#### DatasetValidateCommand
```python
validator = DatasetValidateCommand(max_length=131072)
result = validator.process('training_data.json')
```

Features:
- Validates existing training data files
- Supports JSON and CSV formats
- Comprehensive validation checks
- Detailed validation reporting

#### DatasetConvertCommand
```python
converter = DatasetConvertCommand(output_dir='./output')
result = converter.process('data.json', format='csv')
```

Features:
- Converts between JSON and CSV formats
- Handles large datasets
- Maintains data integrity
- Flexible output options

## Usage Examples

### 1. Basic Command Usage
```python
from markdown_analyzer.commands import CommandRegistry
from markdown_analyzer.core.document import DocumentStructure

# Initialize registry
registry = CommandRegistry()

# Get and use a command
command = registry.get_command('f')
result = command.process(document)
```

### 2. Dataset Generation
```python
from markdown_analyzer.commands.dataset_commands import DatasetGenerateCommand

# Initialize generator
generator = DatasetGenerateCommand(
    input_dirs=['./docs'],
    output_dir='./output',
    max_length=131072
)

# Generate datasets
results = generator.process(
    commands=['f', 's', 't', 'c'],
    workers=4
)
```

### 3. Dataset Validation
```python
from markdown_analyzer.commands.dataset_commands import DatasetValidateCommand

# Initialize validator
validator = DatasetValidateCommand(max_length=131072)

# Validate dataset
result = validator.process('training_data.json')
```

## Command Line Interface

The system provides a CLI interface through Click:

```bash
# Generate training data
python -m markdown_analyzer dataset generate -i ./docs -o ./output -c f s t c

# Validate training data
python -m markdown_analyzer dataset validate training_data.json

# Convert formats
python -m markdown_analyzer dataset convert data.json -f csv
```

## Best Practices

1. Command Implementation
   - Always inherit from `BaseCommand`
   - Implement `process()` method
   - Add proper validation
   - Include comprehensive error handling

2. Error Handling
   - Use specific exception types
   - Provide clear error messages
   - Handle edge cases appropriately
   - Log errors for debugging

3. Data Validation
   - Validate input data
   - Check output formats
   - Verify file paths
   - Validate configurations

4. Performance
   - Use parallel processing when appropriate
   - Handle large datasets efficiently
   - Implement proper memory management
   - Consider resource limitations

## Extending the System

To add a new command:

1. Create a new command class:
```python
class NewCommand(BaseCommand):
    def process(self, doc: DocumentStructure) -> Dict:
        # Implement processing logic
        return {
            "user_input": f"-x {doc.article_number}",
            "ai_output": self._format_output(doc)
        }
```

2. Register the command:
```python
registry = CommandRegistry()
registry.register_command('x', NewCommand)
```

3. Add CLI support if needed:
```python
@click.command()
def new_command():
    """New command description"""
    command = NewCommand()
    # Implement CLI logic
```

## Testing

The command system includes comprehensive testing support:

```python
def test_command():
    command = YourCommand()
    result = command.process(test_document)
    assert result['user_input'].startswith('-')
    assert 'ai_output' in result
```

## Common Issues and Solutions

1. **Missing Document Data**
   - Problem: Required document fields are missing
   - Solution: Add proper null checks in command implementation

2. **Invalid File Formats**
   - Problem: Unsupported file formats
   - Solution: Add format validation and clear error messages

3. **Performance Issues**
   - Problem: Slow processing of large datasets
   - Solution: Implement batch processing and parallelization

4. **Memory Management**
   - Problem: High memory usage with large files
   - Solution: Implement streaming and chunked processing