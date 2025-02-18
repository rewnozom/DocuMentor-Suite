# ..\..\markdown_analyzer\tests\test_dataset.py
import pytest
import json
import csv
from pathlib import Path
from typing import List, Dict
import tempfile
import shutil

from ..dataset.generator import DatasetGenerator
from ..dataset.processors import DocumentProcessor, TrainingDataProcessor
from ..dataset.validators import DatasetValidator
from ..dataset.exporters import DatasetExporter, MultiFormatExporter
from ..core.document import DocumentStructure

# Uppdaterad SAMPLE_TRAINING_DATA med längre ai_output
SAMPLE_TRAINING_DATA = [
    {
        "user_input": "-f 12345",
        "ai_output": "# Test Product\n\nProduct description here. This description is now extended to meet the minimum length requirement."
    },
    {
        "user_input": "-s 67890",
        "ai_output": "## Technical Specifications\n- Spec 1\n- Spec 2\nAdditional details to ensure output is sufficiently long."
    }
]

@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files"""
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)

@pytest.fixture
def sample_markdown_file(temp_dir):
    """Create a sample markdown file for testing"""
    content = """# Test Product (Art.nr: 12345)

A test product description.

## Technical Specifications
- Voltage: 230V
- Weight: 5kg

## Compatibility
- Compatible with XYZ (Art.nr: 67890)
"""
    file_path = Path(temp_dir) / "test_12345.md"
    file_path.write_text(content)
    return file_path

class TestDatasetGenerator:
    """Test dataset generation functionality"""
    
    def test_generate_dataset(self, temp_dir, sample_markdown_file):
        """Test basic dataset generation"""
        generator = DatasetGenerator([str(sample_markdown_file.parent)], temp_dir)
        generator.generate_dataset()
        
        # Verify output files were created
        output_dir = Path(temp_dir)
        assert list(output_dir.glob("*.json"))  # Should have JSON output
        assert list(output_dir.glob("*.csv"))   # Should have CSV output
    
    def test_generate_specific_commands(self, temp_dir, sample_markdown_file):
        """Test generation with specific commands"""
        generator = DatasetGenerator([str(sample_markdown_file.parent)], temp_dir)
        generator.generate_dataset(commands=['f', 't'])
        
        # Verify only specified command outputs exist
        output_dir = Path(temp_dir)
        assert (output_dir / "training_data_f.json").exists()
        assert (output_dir / "training_data_t.json").exists()
        assert not (output_dir / "training_data_s.json").exists()
    
    def test_parallel_processing(self, temp_dir, sample_markdown_file):
        """Test parallel processing of files"""
        generator = DatasetGenerator([str(sample_markdown_file.parent)], temp_dir)
        generator.generate_dataset(num_workers=2)
        
        # Verify successful generation
        assert generator.documents is not None
        assert len(generator.documents) > 0

class TestDocumentProcessor:
    """Test document processing functionality"""
    
    def setup_method(self):
        self.processor = DocumentProcessor([])  # Empty extractor list for testing
    
    def test_process_document(self, sample_markdown_file):
        """Test basic document processing"""
        doc = self.processor.process_document(sample_markdown_file)
        
        assert doc is not None
        assert doc.article_number == "12345"
        assert "Test Product" in doc.product_name
    
    def test_file_encoding_handling(self, temp_dir):
        """Test handling of different file encodings"""
        # Create files with different encodings
        encodings = ['utf-8', 'latin-1']
        files = []
        
        for encoding in encodings:
            content = f"# Test Product ({encoding})"
            file_path = Path(temp_dir) / f"test_{encoding}.md"
            file_path.write_text(content, encoding=encoding)
            files.append(file_path)
        
        # Test processing
        for file_path in files:
            doc = self.processor.process_document(file_path)
            assert doc is not None

class TestTrainingDataProcessor:
    """Test training data processing functionality"""
    
    def setup_method(self):
        self.processor = TrainingDataProcessor()
    
    def test_create_training_examples(self, sample_markdown_file):
        """Test creation of training examples"""
        doc = DocumentStructure(
            filename=sample_markdown_file.name,
            article_number="12345",
            document_type="manual",
            product_name="Test Product",
            description="Test description"
        )
        
        examples = self.processor.create_training_examples(doc, ['f', 's'])
        
        assert len(examples) > 0
        for example in examples:
            assert example['user_input'].startswith('-')
            assert len(example['ai_output']) > 0
    
    def test_output_segmentation(self):
        """Test segmentation of long outputs"""
        long_output = "Test\n" * 1000  # Create long output
        doc = DocumentStructure(
            filename="test.md",
            article_number="12345",
            document_type="manual",
            product_name="Test Product",
            description=long_output
        )
        
        examples = self.processor.create_training_examples(doc, ['f'])
        
        # Verify segmentation
        assert len(examples) > 1
        for example in examples:
            assert len(example['ai_output']) <= self.processor.chars_per_segment

class TestDatasetValidator:
    """Test dataset validation functionality"""
    
    def setup_method(self):
        self.validator = DatasetValidator()
    
    def test_validate_training_samples(self):
        """Test validation of training samples"""
        result = self.validator.validate_training_samples(SAMPLE_TRAINING_DATA)
        
        assert result.is_valid
        assert len(result.errors) == 0
        assert result.stats['total_samples'] == len(SAMPLE_TRAINING_DATA)
    
    def test_invalid_samples(self):
        """Test validation of invalid samples"""
        invalid_data = [
            {
                "user_input": "invalid",  # Missing command prefix
                "ai_output": "Test output"
            },
            {
                "user_input": "-f 12345",
                "ai_output": ""  # Empty output
            }
        ]
        
        result = self.validator.validate_training_samples(invalid_data)
        
        assert not result.is_valid
        assert len(result.errors) > 0
        assert result.stats['empty_outputs'] > 0

class TestDatasetExporter:
    """Test dataset export functionality"""
    
    def setup_method(self):
        self.exporter = DatasetExporter("output", 1000)
    
    def test_export_to_json(self, temp_dir):
        """Test JSON export"""
        output_file = self.exporter.export_to_json(
            SAMPLE_TRAINING_DATA, 
            "test_data"
        )
        
        assert Path(output_file).exists()
        with open(output_file) as f:
            data = json.load(f)
            assert len(data) == len(SAMPLE_TRAINING_DATA)
    
    def test_export_to_csv(self, temp_dir):
        """Test CSV export"""
        output_files = self.exporter.export_to_csv(
            SAMPLE_TRAINING_DATA, 
            "test_data"
        )
        
        assert len(output_files) > 0
        for file_path in output_files:
            assert Path(file_path).exists()
            with open(file_path, newline='') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                assert len(rows) > 0

class TestMultiFormatExporter:
    """Test multi-format export functionality"""
    
    def setup_method(self):
        self.exporter = MultiFormatExporter("output", DatasetValidator())
    
    def test_export_dataset(self, temp_dir):
        """Test export to multiple formats"""
        result = self.exporter.export_dataset(
            SAMPLE_TRAINING_DATA,
            "test_data"
        )
        
        assert result['validation'].is_valid
        assert 'json' in result['files']
        assert 'csv' in result['files']
        assert result['stats']['total_samples'] == len(SAMPLE_TRAINING_DATA)
    
    def test_export_with_validation(self, temp_dir):
        """Test export with validation handling"""
        invalid_data = SAMPLE_TRAINING_DATA + [{"invalid": "data"}]
        
        result = self.exporter.export_dataset(
            invalid_data,
            "test_data"
        )
        
        assert not result['validation'].is_valid
        assert len(result['validation'].errors) > 0

if __name__ == "__main__":
    pytest.main([__file__])
