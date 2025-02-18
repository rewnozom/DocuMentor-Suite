import pytest
import re
from pathlib import Path
from typing import Dict, List

from ..extractors.base import BaseExtractor
from ..extractors.metadata import MetadataExtractor
from ..extractors.compatibility.extractor import CompatibilityExtractor
from ..extractors.technical.technical_extractor import TechnicalExtractor
from ..extractors.images import ImageExtractor
from ..core.document import DocumentStructure, ProductImage, Compatibility, TechnicalSpec

# Sample test data
SAMPLE_MARKDOWN = """# Test Product Manual (Art.nr: 12345)

![Product Image](_page_1_Picture_1.jpeg)

## Description
This is a test product with amazing features.

## Technical Specifications
- Voltage: 230V
- Dimensions: 100x200x300 mm
- Weight: 5kg

## Compatibility
- Compatible with Product XYZ (Art.nr: 67890)
- Can be used with System ABC
- Requires Power Adapter (Art.nr: 11111)
"""

class TestBaseExtractor:
    """Test the base extractor functionality"""
    
    class MockExtractor(BaseExtractor):
        """Mock implementation for testing"""
        def extract(self, content: str) -> Dict:
            return {"cleaned": self._clean_text(content)}
    
    def test_clean_text(self):
        """Test text cleaning functionality"""
        extractor = self.MockExtractor()
        test_cases = [
            ("  Test  Text  ", "Test Text"),
            ("Line1\n\nLine2", "Line1 Line2"),
            ("Special@#$%Characters", "SpecialCharacters")
        ]
        
        for input_text, expected in test_cases:
            assert extractor._clean_text(input_text) == expected
    
    def test_validate_output(self):
        """Test output validation"""
        extractor = self.MockExtractor()
        assert extractor.validate_output({"test": "data"}) == True

class TestMetadataExtractor:
    """Test metadata extraction functionality"""
    
    def setup_method(self):
        self.extractor = MetadataExtractor()
    
    def test_extract_article_number(self):
        """Test article number extraction"""
        test_cases = [
            ("filename_12345.md", "12345"),
            ("art.nr_67890_manual.md", "67890"),
            ("no_article_number.md", None)
        ]
        
        for filename, expected in test_cases:
            result = self.extractor.extract_article_number(filename, "")
            if expected:
                assert result == expected
            else:
                assert result.startswith("TEMP_")
    
    def test_extract_document_type(self):
        """Test document type extraction"""
        test_cases = [
            ("manual_ins.md", "installationer"),
            ("guide_pro.md", "produktinfo"),
            ("doc_man.md", "manual"),
            ("unknown.md", "ospecificerad")
        ]
        
        for filename, expected in test_cases:
            assert self.extractor.extract_document_type(filename) == expected

class TestCompatibilityExtractor:
    """Test compatibility extraction functionality"""
    
    def setup_method(self):
        self.extractor = CompatibilityExtractor()
    
    def test_extract_compatibility(self):
        """Test compatibility information extraction"""
        sections = {
            "Compatibility": """
            Compatible with Product XYZ (Art.nr: 67890)
            Can be used with System ABC
            Requires Power Adapter (Art.nr: 11111)
            """
        }
        
        results = self.extractor.extract(SAMPLE_MARKDOWN, sections)
        
        assert len(results) > 0
        assert any(r.target_article == "67890" for r in results)
        assert any(r.type == "requires" for r in results)
    
    def test_confidence_levels(self):
        """Test confidence level assignment"""
        sections = {
            "Compatibility": "Compatible with Product XYZ (Art.nr: 67890)"
        }
        
        results = self.extractor.extract(SAMPLE_MARKDOWN, sections)
        
        # Verify higher confidence for entries with article numbers
        for result in results:
            if result.target_article:
                assert result.confidence >= 0.8
            else:
                assert result.confidence < 0.8

class TestTechnicalExtractor:
    """Test technical specification extraction functionality"""
    
    def setup_method(self):
        self.extractor = TechnicalExtractor()
    
    def test_extract_technical_specs(self):
        """Test technical specification extraction"""
        tables = []  # Mock tables
        results = self.extractor.extract(SAMPLE_MARKDOWN, tables)
        
        assert len(results) > 0
        
        # Verify specific specs were extracted
        specs_found = {spec.category: spec for spec in results}
        assert "electrical" in specs_found
        assert "dimensions" in specs_found
        assert "weight" in specs_found
        
        # Verify values and units
        voltage_spec = next(s for s in results if s.category == "electrical")
        assert voltage_spec.value == "230"
        assert voltage_spec.unit == "V"
    
    def test_extract_from_tables(self):
        """Test extraction from table format"""
        tables = [{
            "headers": ["Specification", "Value"],
            "rows": [
                ["Voltage", "230V"],
                ["Weight", "5kg"]
            ],
            "context": "Technical Specifications"
        }]
        
        results = self.extractor._extract_from_tables(tables)
        assert len(results) == 2
        assert all(r.confidence == 0.9 for r in results)  # Table data has higher confidence

class TestImageExtractor:
    """Test image extraction functionality"""
    
    def setup_method(self):
        self.extractor = ImageExtractor()
    
    def test_extract_images(self):
        """Test image reference extraction"""
        results = self.extractor.extract(SAMPLE_MARKDOWN, "12345")
        
        assert len(results) > 0
        for image in results:
            assert isinstance(image, ProductImage)
            assert image.image_ref.startswith("_page_")
            assert image.mapped_path.startswith("./12345/")
    
    def test_image_ordering(self):
        """Test image extraction ordering logic"""
        markdown = """
        ![Image 1](_page_1_Picture_1.jpeg)
        ![Image 2](_page_1_Picture_2.jpeg)
        ![Image 3](_page_2_Picture_1.jpeg)
        """
        
        results = self.extractor.extract(markdown, "12345")
        
        # Verify second image is selected (per implementation logic)
        assert len(results) == 1
        assert results[0].page_num == 1
        assert results[0].image_num == 2

class TestIntegration:
    """Integration tests for extractors working together"""
    
    def test_full_document_extraction(self):
        """Test extracting all information from a complete document"""
        metadata_extractor = MetadataExtractor()
        compatibility_extractor = CompatibilityExtractor()
        technical_extractor = TechnicalExtractor()
        image_extractor = ImageExtractor()
        
        # Extract metadata
        article_number = metadata_extractor.extract_article_number(
            "test_12345.md", SAMPLE_MARKDOWN
        )
        document_type = metadata_extractor.extract_document_type("test_12345.md")
        
        # Create document structure
        doc = DocumentStructure(
            filename="test_12345.md",
            article_number=article_number,
            document_type=document_type,
            product_name="Test Product",
            description="This is a test product"
        )
        
        # Extract all components
        sections = {"Compatibility": "Compatible with Product XYZ (Art.nr: 67890)"}
        doc.compatibility = compatibility_extractor.extract(SAMPLE_MARKDOWN, sections)
        doc.technical_specs = technical_extractor.extract(SAMPLE_MARKDOWN, [])
        doc.product_images = image_extractor.extract(SAMPLE_MARKDOWN, article_number)
        
        # Verify complete extraction
        assert doc.article_number == "12345"
        assert len(doc.compatibility) > 0
        assert len(doc.technical_specs) > 0
        assert len(doc.product_images) > 0

def test_error_handling():
    """Test error handling in extractors"""
    metadata_extractor = MetadataExtractor()
    
    # Test invalid content
    assert metadata_extractor.extract_article_number("invalid.md", "").startswith("TEMP_")
    
    # Test malformed markdown
    technical_extractor = TechnicalExtractor()
    results = technical_extractor.extract("Malformed: content", [])
    assert len(results) == 0

if __name__ == "__main__":
    pytest.main([__file__])