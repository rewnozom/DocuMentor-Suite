# Run all tests
pytest markdown_analyzer/tests/ -v

# Run specific test file
pytest markdown_analyzer/tests/test_workflow.py -v

# Run specific test class
pytest markdown_analyzer/tests/test_workflow.py::TestWorkflow -v

# Run specific test method
pytest markdown_analyzer/tests/test_workflow.py::TestWorkflow::test_full_workflow -v