

This workflow test suite integrates all components and tests:

1. Full Workflow:
- Document processing
- Information extraction
- Training data generation
- Validation
- Output verification

2. Error Handling:
- Invalid file processing
- Error collection
- Graceful degradation

3. Command-Specific Testing:
- Selective command processing
- Output verification
- Command isolation

4. Incremental Processing:
- File addition handling
- Document state management
- Duplicate prevention

5. Statistics Generation:
- Document counting
- Error tracking
- Category statistics

6. Parallel Processing:
- Multi-worker processing
- Resource management
- Concurrent file handling

To run the full workflow tests:

1. Create a tests directory
2. Add all test files (test_core.py, test_extractors.py, test_trainers.py, test_dataset.py)
3. Add this new file as test_workflow.py
4. Run with pytest:

```bash
# Run individual components
pytest tests/test_core.py -v
pytest tests/test_extractors.py -v
pytest tests/test_trainers.py -v
pytest tests/test_dataset.py -v

# Run full workflow tests
pytest tests/test_workflow.py -v

# Run all tests
pytest tests/ -v
```

The workflow tests ensure that all components work together correctly and handle various scenarios appropriately.