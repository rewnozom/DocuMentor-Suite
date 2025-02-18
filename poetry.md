

This error is due to a version mismatch between numpy and pandas in your virtual environment. The specific error:

```
ValueError: numpy.dtype size changed, may indicate binary incompatibility. Expected 96 from C header, got 88 from PyObject
```

To fix this, you need to reinstall numpy and pandas in the correct order. Here's how to do it:

1. First, activate your poetry environment if not already activated:
```bash
poetry shell
```

2. Then uninstall both pandas and numpy:
```bash
poetry remove pandas numpy
```

3. First install numpy:
```bash
poetry add numpy
```

4. Then install pandas:
```bash
poetry add pandas
```

This should resolve the binary incompatibility issue. The problem occurs because the installed versions of numpy and pandas aren't properly aligned. By installing them in the correct order (numpy first, then pandas), you ensure they're compatible.

If you're still having issues after this, you can try specifying specific versions:

```bash
poetry add numpy==1.24.0
poetry add pandas==2.1.0
```

Try these steps and run your tests again. Let me know if you need any clarification or if you're still seeing issues.





-----------------------

I see the issue. Your `pyproject.toml` specifies Python >=3.8, but the latest numpy requires Python >=3.10. Let's modify your `pyproject.toml` to use Python 3.10 since that's what you're using. Also, we'll specify compatible versions for numpy and pandas.

Modify your `pyproject.toml` Python version requirement:

```toml
[tool.poetry.dependencies]
python = "^3.10"  # Change this line
```

Then try:

1. Remove pandas first:
```bash
poetry remove pandas
```

2. Clean poetry cache:
```bash
poetry cache clear . --all
```

3. Add numpy with a specific version:
```bash
poetry add "numpy>=1.24.0,<2.0.0"
```

4. Add pandas with a specific version:
```bash
poetry add "pandas>=1.5.0,<2.0.0"
```

5. Update all dependencies:
```bash
poetry update
```

This should give you compatible versions of both packages. After this, try running your tests again:
```bash
poetry run pytest tests/ -v
```

The key is getting compatible versions of numpy and pandas working together within your Python 3.10 environment. Let me know if you still encounter any issues.