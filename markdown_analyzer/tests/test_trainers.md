
1. Base Trainer:
- Example validation
- Error handling
- Base functionality

2. BasicInfoTrainer:
- Full info example creation
- Image inclusion
- Description formatting
- Temporary article number handling

3. SummaryTrainer:
- Section organization
- Key information extraction
- Minimal document handling

4. TechnicalTrainer:
- Specification formatting
- Unit handling
- Category organization

5. CompatibilityTrainer:
- Relationship types
- Article number formatting
- Section organization

6. MarkdownFormatter:
- Heading formatting
- Image formatting
- List formatting (ordered and unordered)

7. Integration Testing:
- Trainer coordination
- Markdown consistency
- Common requirements

To run these tests, you would:

1. Create a tests/trainers directory
2. Save this as test_trainers.py
3. Run with pytest:

```bash
pytest tests/test_trainers.py -v
```
