import re
import pytest
from datetime import datetime
from pathlib import Path
from ..core.document import (
    DocumentStructure, ProductImage, Compatibility,
    TechnicalSpec, InstallationInfo, TableInfo, CrossReference
)
from ..core.patterns import (
    ARTICLE_NUMBER_PATTERNS, COMPATIBILITY_PATTERNS, TECHNICAL_PATTERNS
)
from ..core.errors import (
    MarkdownAnalyzerError, DocumentParsingError,
    ArticleNumberError, ValidationError
)

# Test DocumentStructure and related classes
def test_document_structure_creation():
    """Test creating a DocumentStructure with all fields"""
    doc = DocumentStructure(
        filename="test.md",
        article_number="12345",
        document_type="manual",
        product_name="Test Product",
        description="Test Description",
        manufacturer="Test Manufacturer"
    )
    
    assert doc.filename == "test.md"
    assert doc.article_number == "12345"
    assert doc.document_type == "manual"
    assert doc.product_name == "Test Product"
    assert doc.description == "Test Description"
    assert doc.manufacturer == "Test Manufacturer"
    assert isinstance(doc.product_images, list)
    assert isinstance(doc.compatibility, list)
    assert isinstance(doc.technical_specs, list)
    assert isinstance(doc.processing_errors, list)

def test_product_image():
    """Test ProductImage class"""
    image = ProductImage(
        image_ref="test.jpg",
        page_num=1,
        image_num=2,
        mapped_path="/path/to/image"
    )
    
    assert image.image_ref == "test.jpg"
    assert image.page_num == 1
    assert image.image_num == 2
    assert image.mapped_path == "/path/to/image"

def test_compatibility():
    """Test Compatibility class"""
    compat = Compatibility(
        type="fits",
        target_article="67890",
        description="Compatible with Product B",
        source_section="Compatibility",
        confidence=0.9,
        context="Some context",
        source_file="source.md"
    )
    
    assert compat.type == "fits"
    assert compat.target_article == "67890"
    assert compat.description == "Compatible with Product B"
    assert compat.confidence == 0.9
    assert compat.context == "Some context"
    assert compat.source_file == "source.md"

def test_technical_spec():
    """Test TechnicalSpec class"""
    spec = TechnicalSpec(
        category="dimensions",
        value="100",
        unit="mm",
        source="text",
        confidence=0.95
    )
    
    assert spec.category == "dimensions"
    assert spec.value == "100"
    assert spec.unit == "mm"
    assert spec.source == "text"
    assert spec.confidence == 0.95

# Test Patterns
def test_article_number_patterns():
    """Test article number pattern matching"""
    test_cases = [
        ("Article no: 12345", "12345"),
        ("Art.nr: 67890", "67890"),
        ("Product number: 11111", "11111"),
        ("Invalid", None)
    ]
    
    for text, expected in test_cases:
        match = None
        for pattern in ARTICLE_NUMBER_PATTERNS:
            if m := re.search(pattern, text):
                match = m.group(1)
                break
        assert match == expected

def test_compatibility_patterns():
    """Test compatibility pattern matching"""
    test_cases = [
        ("Compatible with Product X", True),
        ("Fits with model ABC", True),
        ("Can be used with system Y", True),
        ("Random text", False)
    ]
    
    for text, should_match in test_cases:
        matched = any(re.search(pattern, text, re.IGNORECASE) 
                     for pattern in COMPATIBILITY_PATTERNS)
        assert matched == should_match

def test_technical_patterns():
    """Test technical specification pattern matching"""
    test_cases = [
        ("Dimensions: 100x200x300 mm", "dimensions", True),
        ("Voltage: 230V", "electrical", True),
        ("Weight: 5kg", "weight", True),
        ("Random text", None, False)
    ]
    
    for text, category, should_match in test_cases:
        matched = False
        if category:
            patterns = TECHNICAL_PATTERNS.get(category, [])
            matched = any(re.search(pattern, text) for pattern in patterns)
        else:
            matched = any(any(re.search(pattern, text) 
                            for pattern in cat_patterns)
                        for cat_patterns in TECHNICAL_PATTERNS.values())
        assert matched == should_match

# Test Error Classes
def test_markdown_analyzer_error():
    """Test MarkdownAnalyzerError"""
    with pytest.raises(MarkdownAnalyzerError):
        raise MarkdownAnalyzerError("Test error")

def test_document_parsing_error():
    """Test DocumentParsingError"""
    with pytest.raises(DocumentParsingError):
        raise DocumentParsingError("Test parsing error")

def test_article_number_error():
    """Test ArticleNumberError"""
    with pytest.raises(ArticleNumberError):
        raise ArticleNumberError("Test article number error")

def test_validation_error():
    """Test ValidationError"""
    with pytest.raises(ValidationError):
        raise ValidationError("Test validation error")

# Test Complex Document Structure
def test_complex_document_structure():
    """Test a complex document structure with all possible fields"""
    doc = DocumentStructure(
        filename="complex.md",
        article_number="12345",
        document_type="manual",
        product_name="Complex Product",
        description="Complex Description",
        manufacturer="Test Manufacturer"
    )
    
    # Add product images
    doc.product_images.append(ProductImage(
        image_ref="image1.jpg",
        page_num=1,
        image_num=1,
        mapped_path="/path/to/image1"
    ))
    
    # Add compatibility info
    doc.compatibility.append(Compatibility(
        type="fits",
        target_article="67890",
        description="Compatible with Product B",
        source_section="Compatibility",
        confidence=0.9
    ))
    
    # Add technical specs
    doc.technical_specs.append(TechnicalSpec(
        category="dimensions",
        value="100",
        unit="mm",
        source="text",
        confidence=0.95
    ))
    
    # Add installation info
    doc.installation = InstallationInfo(
        requirements=["Req1", "Req2"],
        steps=["Step1", "Step2"],
        warnings=["Warning1"],
        tools_needed=["Tool1"]
    )
    
    # Add tables
    doc.tables.append(TableInfo(
        headers=["Col1", "Col2"],
        rows=[["Data1", "Data2"]],
        context="Table context",
        type="specs"
    ))
    
    # Verify complex structure
    assert len(doc.product_images) == 1
    assert len(doc.compatibility) == 1
    assert len(doc.technical_specs) == 1
    assert len(doc.installation.requirements) == 2
    assert len(doc.tables) == 1
    assert doc.confidence_score == 1.0
    assert isinstance(doc.last_updated, str)

# Test Edge Cases
def test_empty_document_structure():
    """Test document structure with minimal required fields"""
    doc = DocumentStructure(
        filename="empty.md",
        article_number="12345",
        document_type="manual",
        product_name="Empty Product",
        description="Empty Description"
    )
    
    assert len(doc.product_images) == 0
    assert len(doc.compatibility) == 0
    assert len(doc.technical_specs) == 0
    assert doc.installation is None
    assert len(doc.tables) == 0

def test_document_structure_validation():
    """Test document structure field validation"""
    with pytest.raises(TypeError):
        DocumentStructure(
            filename=123,  # Should be string
            article_number="12345",
            document_type="manual",
            product_name="Test Product",
            description="Test Description"
        )

    with pytest.raises(TypeError):
        DocumentStructure(
            filename="test.md",
            article_number="12345",
            document_type="manual",
            product_name="Test Product",
            description="Test Description",
            product_images="invalid"  # Should be list
        )

if __name__ == "__main__":
    pytest.main([__file__])