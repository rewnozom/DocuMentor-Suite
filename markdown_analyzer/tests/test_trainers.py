import pytest
from pathlib import Path
from typing import List, Dict

from ..trainers.base import BaseTrainer, TrainingExample
from ..trainers.commands import (
    BasicInfoTrainer,
    SummaryTrainer,
    TechnicalTrainer,
    CompatibilityTrainer
)
from ..trainers.formatters import MarkdownFormatter
from ..core.document import (
    DocumentStructure,
    ProductImage,
    Compatibility,
    TechnicalSpec
)

# Test fixtures and helper functions
@pytest.fixture
def sample_document() -> DocumentStructure:
    """Create a sample document for testing"""
    doc = DocumentStructure(
        filename="test.md",
        article_number="12345",
        document_type="manual",
        product_name="Test Product",
        description="A test product description"
    )
    
    # Add product images
    doc.product_images = [
        ProductImage(
            image_ref="_page_1_Picture_1.jpeg",
            page_num=1,
            image_num=1,
            mapped_path="./12345/_page_1_Picture_1.jpeg"
        )
    ]
    
    # Add compatibility info
    doc.compatibility = [
        Compatibility(
            type="fits",
            target_article="67890",
            description="Compatible with Product XYZ",
            source_section="Compatibility",
            confidence=0.9
        ),
        Compatibility(
            type="requires",
            target_article="11111",
            description="Requires Power Adapter",
            source_section="Requirements",
            confidence=0.95
        )
    ]
    
    # Add technical specs
    doc.technical_specs = [
        TechnicalSpec(
            category="electrical",
            value="230",
            unit="V",
            source="text",
            confidence=0.9
        ),
        TechnicalSpec(
            category="dimensions",
            value="100x200x300",
            unit="mm",
            source="text",
            confidence=0.95
        )
    ]
    
    return doc

class TestBaseTrainer:
    """Test base trainer functionality"""
    
    class MockTrainer(BaseTrainer):
        """Mock implementation for testing"""
        def create_training_data(self, doc: DocumentStructure) -> List[TrainingExample]:
            return [TrainingExample(
                command="test",
                article_number=doc.article_number,
                input_text=f"-test {doc.article_number}",
                output_text="Test output"
            )]
    
    def test_validate_example(self):
        """Test training example validation"""
        trainer = self.MockTrainer()
        
        # Valid example
        valid_example = TrainingExample(
            command="test",
            article_number="12345",
            input_text="-test 12345",
            output_text="Valid output"
        )
        assert trainer.validate_example(valid_example) == True
        
        # Invalid examples
        invalid_examples = [
            TrainingExample(
                command="test",
                article_number="12345",
                input_text="",  # Empty input
                output_text="Output"
            ),
            TrainingExample(
                command="test",
                article_number="",  # Empty article number
                input_text="-test",
                output_text="Output"
            )
        ]
        
        for example in invalid_examples:
            assert trainer.validate_example(example) == False

class TestBasicInfoTrainer:
    """Test BasicInfoTrainer functionality"""
    
    def setup_method(self):
        self.trainer = BasicInfoTrainer()
    
    def test_create_training_data(self, sample_document):
        """Test creation of basic info training examples"""
        examples = self.trainer.create_training_data(sample_document)
        
        assert len(examples) == 1
        example = examples[0]
        
        assert example.command == "f"
        assert example.article_number == "12345"
        assert example.input_text == "-f 12345"
        assert "# Test Product" in example.output_text
        assert "_page_1_Picture_1.jpeg" in example.output_text
        assert "test product description" in example.output_text.lower()
    
    def test_temporary_article_number(self, sample_document):
        """Test handling of temporary article numbers"""
        sample_document.article_number = "TEMP_12345"
        examples = self.trainer.create_training_data(sample_document)
        assert len(examples) == 0

class TestSummaryTrainer:
    """Test SummaryTrainer functionality"""
    
    def setup_method(self):
        self.trainer = SummaryTrainer()
    
    def test_create_training_data(self, sample_document):
        """Test creation of summary training examples"""
        examples = self.trainer.create_training_data(sample_document)
        
        assert len(examples) == 1
        example = examples[0]
        
        assert example.command == "s"
        assert example.article_number == "12345"
        assert example.input_text == "-s 12345"
        
        # Check for required sections
        assert "## Kompatibilitet" in example.output_text
        assert "## Tekniska Specifikationer" in example.output_text
        assert "Compatible with Product XYZ" in example.output_text
        assert "230V" in example.output_text
    
    def test_minimal_document(self, sample_document):
        """Test handling of documents with minimal information"""
        sample_document.compatibility = []
        sample_document.technical_specs = []
        examples = self.trainer.create_training_data(sample_document)
        assert len(examples) == 0

class TestTechnicalTrainer:
    """Test TechnicalTrainer functionality"""
    
    def setup_method(self):
        self.trainer = TechnicalTrainer()
    
    def test_create_training_data(self, sample_document):
        """Test creation of technical training examples"""
        examples = self.trainer.create_training_data(sample_document)
        
        assert len(examples) == 1
        example = examples[0]
        
        assert example.command == "t"
        assert example.article_number == "12345"
        assert example.input_text == "-t 12345"
        
        # Check for technical specifications
        assert "230V" in example.output_text
        assert "100x200x300 mm" in example.output_text
    
    def test_no_technical_specs(self, sample_document):
        """Test handling of documents without technical specs"""
        sample_document.technical_specs = []
        examples = self.trainer.create_training_data(sample_document)
        assert len(examples) == 0

class TestCompatibilityTrainer:
    """Test CompatibilityTrainer functionality"""
    
    def setup_method(self):
        self.trainer = CompatibilityTrainer()
    
    def test_create_training_data(self, sample_document):
        """Test creation of compatibility training examples"""
        examples = self.trainer.create_training_data(sample_document)
        
        assert len(examples) == 1
        example = examples[0]
        
        assert example.command == "c"
        assert example.article_number == "12345"
        assert example.input_text == "-c 12345"
        
        # Check for compatibility sections
        assert "## Passar till" in example.output_text
        assert "## Kräver" in example.output_text
        assert "Product XYZ" in example.output_text
        assert "Power Adapter" in example.output_text
        assert "Art.nr: 67890" in example.output_text
    
    def test_no_compatibility(self, sample_document):
        """Test handling of documents without compatibility info"""
        sample_document.compatibility = []
        examples = self.trainer.create_training_data(sample_document)
        assert len(examples) == 0

class TestMarkdownFormatter:
    """Test MarkdownFormatter functionality"""
    
    def setup_method(self):
        self.formatter = MarkdownFormatter()
    
    def test_format_heading(self):
        """Test heading formatting"""
        assert self.formatter.format_heading("Test", 1) == "# Test\n\n"
        assert self.formatter.format_heading("Test", 2) == "## Test\n\n"
    
    def test_format_image(self):
        """Test image formatting"""
        assert self.formatter.format_image("test.jpg", "alt") == "![alt]test.jpg\n\n"
    
    def test_format_list(self):
        """Test list formatting"""
        items = ["Item 1", "Item 2"]
        # Unordered list
        unordered = self.formatter.format_list(items)
        assert "- Item 1\n" in unordered
        assert "- Item 2\n" in unordered
        
        # Ordered list
        ordered = self.formatter.format_list(items, ordered=True)
        assert "1. Item 1\n" in ordered
        assert "2. Item 2\n" in ordered

class TestIntegration:
    """Integration tests for trainers"""
    
    def test_all_trainers(self, sample_document):
        """Test all trainers with the same document"""
        trainers = [
            BasicInfoTrainer(),
            SummaryTrainer(),
            TechnicalTrainer(),
            CompatibilityTrainer()
        ]
        
        for trainer in trainers:
            examples = trainer.create_training_data(sample_document)
            assert len(examples) > 0
            for example in examples:
                # Verify common requirements
                assert example.article_number == "12345"
                assert example.input_text.startswith("-")
                assert len(example.output_text) > 0
    
    def test_markdown_consistency(self, sample_document):
        """Test consistency of markdown formatting across trainers"""
        trainers = [
            BasicInfoTrainer(),
            SummaryTrainer(),
            TechnicalTrainer(),
            CompatibilityTrainer()
        ]
        
        for trainer in trainers:
            examples = trainer.create_training_data(sample_document)
            for example in examples:
                # Check markdown formatting
                assert example.output_text.count("#") > 0  # Has headings
                assert example.output_text.endswith("\n")  # Ends with newline
                assert not example.output_text.startswith("\n")  # No leading newline

if __name__ == "__main__":
    pytest.main([__file__])