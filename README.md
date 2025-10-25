# Python Function Accelerator

This folder contains boilerplate for a minimal Python function app.

Structure:

- src/: package with main entry and handlers
- tests/: pytest tests
- requirements.txt: test/runtime dependencies
- Dockerfile: simple image that installs requirements and prints a sample run

Quickstart (from repo root):

Install test deps and run tests:

```bash
python -m pip install -r python-function-accelerator/requirements.txt
python -m pytest -q python-function-accelerator/tests
```

Import and call programmatically:

```python
from src.main import handle_request
print(handle_request({"data": "hello"}))
```
