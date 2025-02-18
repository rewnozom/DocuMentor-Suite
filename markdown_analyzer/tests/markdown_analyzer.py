import json
import pytest
import tempfile
import shutil
from pathlib import Path
from typing import List, Dict

from ..analyzer import MarkdownAnalyzer
from ..core.document import DocumentStructure
from ..extractors import (
    MetadataExtractor,
    CompatibilityExtractor,
    TechnicalExtractor,
    ImageExtractor
)
from ..trainers import (
    BasicInfoTrainer,
    SummaryTrainer,
    TechnicalTrainer,
    CompatibilityTrainer
)
from ..dataset import (
    DatasetGenerator,
    DocumentProcessor,
    DatasetValidator
)

# Import helpers from existing test files
from test_core import sample_document
from test_dataset import SAMPLE_TRAINING_DATA
from test_extractors import SAMPLE_MARKDOWN
from test_trainers import sample_document as trainer_sample_doc

@pytest.fixture
def test_environment():
    """Create a temporary test environment"""
    temp_dir = tempfile.mkdtemp()
    input_dir = Path(temp_dir) / "input"
    output_dir = Path(temp_dir) / "output"
    input_dir.mkdir()
    output_dir.mkdir()
    
    # Create test files
    test_files = [
        ("product1.md", """# Product One (Art.nr: 12345)

A high-quality test product.

## Technical Specifications
- Voltage: 230V
- Weight: 5kg

## Compatibility
- Compatible with XYZ (Art.nr: 67890)
- Requires Power Adapter (Art.nr: 11111)
"""),
        ("product2.md", """# Product Two (Art.nr: 67890)

Another test product.

## Technical Specifications
- Dimensions: 100x200x300 mm
- Power: 1000W

## Installation
1. Mount the unit
2. Connect power
""")
    ]
    
    for filename, content in test_files:
        (input_dir / filename).write_text(content)
    
    yield {
        "base_dir": temp_dir,
        "input_dir": str(input_dir),
        "output_dir": str(output_dir)
    }
    
    shutil.rmtree(temp_dir)

class TestWorkflow:
    """Test complete workflow of the markdown analyzer"""
    
    def test_full_workflow(self, test_environment):
        """Test the entire workflow from document processing to training data generation"""
        
        # Step 1: Initialize analyzer
        analyzer = MarkdownAnalyzer(debug=True)
        assert analyzer is not None
        
        # Step 2: Process input directory
        analyzer.process_directory(
            test_environment["input_dir"],
            num_workers=2
        )
        
        # Verify document processing
        assert len(analyzer.documents) == 2
        assert len(analyzer.errors) == 0
        
        # Step 3: Check extracted information
        for doc in analyzer.documents:
            # Basic metadata
            assert doc.article_number in ["12345", "67890"]
            assert doc.product_name is not None
            assert doc.document_type is not None
            
            # Technical specifications
            assert len(doc.technical_specs) > 0
            
            # Compatibility (for product1)
            if doc.article_number == "12345":
                assert len(doc.compatibility) > 0
                assert any(c.target_article == "67890" for c in doc.compatibility)
        
        # Step 4: Generate training data
        analyzer.generate_training_data(
            test_environment["output_dir"],
            commands=['f', 's', 't', 'c']
        )
        
        # Verify generated files
        output_dir = Path(test_environment["output_dir"])
        assert list(output_dir.glob("*.json"))
        
        # Step 5: Validate generated data
        validator = DatasetValidator()
        for json_file in output_dir.glob("*.json"):
            with open(json_file) as f:
                data = json.load(f)
                validation_result = validator.validate_training_samples(data)
                assert validation_result.is_valid
                assert validation_result.stats['total_samples'] > 0
    
    def test_error_handling_workflow(self, test_environment):
        """Test workflow with error conditions"""
        
        # Create invalid test file
        invalid_file = Path(test_environment["input_dir"]) / "invalid.md"
        invalid_file.write_text("Invalid content without proper structure")
        
        analyzer = MarkdownAnalyzer(debug=True)
        
        # Process directory including invalid file
        analyzer.process_directory(test_environment["input_dir"])
        
        # Verify error handling
        assert len(analyzer.errors) > 0
        assert len(analyzer.documents) == 2  # Only valid documents should be processed
    
    def test_command_specific_workflow(self, test_environment):
        """Test workflow for specific commands"""
        analyzer = MarkdownAnalyzer(debug=True)
        
        # Process directory
        analyzer.process_directory(test_environment["input_dir"])
        
        # Generate data for specific commands
        commands = ['t', 'c']  # Only technical and compatibility
        analyzer.generate_training_data(
            test_environment["output_dir"],
            commands=commands
        )
        
        # Verify only specified command outputs exist
        output_dir = Path(test_environment["output_dir"])
        json_files = list(output_dir.glob("*.json"))
        assert len(json_files) == len(commands)
        for cmd in commands:
            assert output_dir.joinpath(f"training_data_{cmd}.json").exists()
    
    def test_incremental_workflow(self, test_environment):
        """Test incremental processing workflow"""
        analyzer = MarkdownAnalyzer(debug=True)
        
        # Initial processing
        analyzer.process_directory(test_environment["input_dir"])
        initial_count = len(analyzer.documents)
        
        # Add new file
        new_file = Path(test_environment["input_dir"]) / "product3.md"
        new_file.write_text("""# Product Three (Art.nr: 99999)
A new test product.
""")
        
        # Process again
        analyzer.process_directory(test_environment["input_dir"])
        
        # Verify only new content was added
        assert len(analyzer.documents) == initial_count + 1
        assert "99999" in [doc.article_number for doc in analyzer.documents]
    
    def test_statistics_workflow(self, test_environment):
        """Test workflow statistics generation"""
        analyzer = MarkdownAnalyzer(debug=True)
        
        # Process directory
        analyzer.process_directory(test_environment["input_dir"])
        
        # Get statistics
        stats = analyzer.get_statistics()
        
        # Verify statistics
        assert stats['total_documents'] == 2
        assert stats['documents_with_errors'] == 0
        assert stats['compatibility_info'] > 0
        assert stats['technical_specs'] > 0
        assert 'document_types' in stats
    
    def test_parallel_processing_workflow(self, test_environment):
        """Test workflow with parallel processing"""
        # Create multiple test files
        for i in range(5):
            file_path = Path(test_environment["input_dir"]) / f"product{i+3}.md"
            file_path.write_text(f"""# Product {i+3} (Art.nr: {50000 + i})
Test product {i+3}.
""")
        
        analyzer = MarkdownAnalyzer(debug=True)
        
        # Process with multiple workers
        analyzer.process_directory(
            test_environment["input_dir"],
            num_workers=4
        )
        
        # Verify all files were processed
        assert len(analyzer.documents) == 7  # 2 original + 5 new
        assert len(analyzer.errors) == 0

if __name__ == "__main__":
    pytest.main([__file__])