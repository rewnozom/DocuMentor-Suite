
1. DatasetGenerator:
- Basic dataset generation
- Command-specific generation
- Parallel processing capabilities

2. DocumentProcessor:
- Document parsing and processing
- File encoding handling
- Error handling

3. TrainingDataProcessor:
- Training example creation
- Output segmentation
- Example formatting

4. DatasetValidator:
- Training sample validation
- Error detection
- Statistics generation

5. DatasetExporter:
- JSON export functionality
- CSV export functionality
- File management

6. MultiFormatExporter:
- Multiple format handling
- Validation integration
- Error handling

To run these tests, you would:

1. Create a tests/dataset directory
2. Save this as test_dataset.py
3. Run with pytest:

```bash
pytest tests/dataset/test_dataset.py -v
```

