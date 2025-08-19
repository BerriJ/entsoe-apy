# Development

This page provides information for developers who want to contribute to or extend the ENTSO-E API Python library.

## Development Setup

### Prerequisites

- Python 3.8 or higher
- Git
- A virtual environment tool (venv, conda, etc.)

### Getting Started

1. Clone the repository:
```bash
git clone https://github.com/BerriJ/entsoe-apy.git
cd entsoe-apy
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install development dependencies:
```bash
pip install -e ".[dev]"
```

## Project Structure

```
entsoe-apy/
├── src/entsoe_api_py/
│   ├── Base/
│   │   └── Balancing.py          # Base classes
│   ├── Balancing/
│   │   └── specific_params.py    # Parameter classes
│   ├── Items/
│   │   └── __init__.py          # Code-based access
│   └── xml_models/              # Generated XML models
├── docs/                        # Documentation
├── tests/                       # Test files
├── pyproject.toml              # Project configuration
└── mkdocs.yml                  # Documentation configuration
```

## Adding New Parameter Classes

### Step 1: Define the Class

Create a new parameter class in `src/entsoe_api_py/Balancing/specific_params.py`:

```python
class NewParameterClass(Balancing):
    """Parameters for X.Y.Z New Parameter Description.

    Data view:
    https://transparency.entsoe.eu/path/to/data/view

    Fixed parameters:
    - documentType: AXX (Description)

    Optional parameters:
    - businessType: Description of business types
    """

    code = "X.Y.Z"

    def __init__(
        self,
        security_token: str,
        period_start: int,
        period_end: int,
        bidding_zone_domain: str,
        # Add specific parameters here
        timeout: int = 60,
        offset: Optional[int] = None,
    ):
        """Initialize parameters."""
        super().__init__(
            document_type="AXX",  # Set appropriate document type
            security_token=security_token,
            period_start=period_start,
            period_end=period_end,
            bidding_zone_domain=bidding_zone_domain,
            timeout=timeout,
            offset=offset,
        )
```

### Step 2: Add to Imports

Add the new class to the imports in `src/entsoe_api_py/Items/__init__.py`:

```python
from ..Balancing.specific_params import (
    # ... existing imports
    NewParameterClass,
)
```

### Step 3: Update Code Mapping

Add the class to the `_CODE_MAPPING` dictionary:

```python
_CODE_MAPPING = {
    # ... existing mappings
    NewParameterClass: "X.Y.Z",
}
```

### Step 4: Add to __all__

Include the class name in the `__all__` list for proper exports.

## Testing

### Running Tests

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=entsoe_api_py

# Run specific test file
python -m pytest tests/test_specific_file.py
```

### Writing Tests

Create test files in the `tests/` directory:

```python
import pytest
from entsoe_api_py.Items import NewParameterClass

def test_new_parameter_class():
    """Test the new parameter class."""
    params = NewParameterClass(
        security_token="test-token",
        period_start=202301010000,
        period_end=202301020000,
        bidding_zone_domain="10Y1001A1001A83F"
    )
    
    assert params.code == "X.Y.Z"
    # Add more assertions
```

## Documentation

### Building Documentation

```bash
# Install documentation dependencies
pip install mkdocs mkdocs-material mkdocstrings[python]

# Serve documentation locally
mkdocs serve

# Build documentation
mkdocs build
```

### Documentation Guidelines

- Use clear, concise language
- Include practical examples
- Link to ENTSO-E data views where applicable
- Follow existing documentation patterns

## Code Style

### Formatting

The project uses:
- **Black** for code formatting
- **isort** for import sorting
- **Ruff** for linting

```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Lint code
ruff check src/ tests/
```

### Type Hints

- Use type hints for all public methods
- Import types from `typing` module
- Use `Optional[T]` for optional parameters

### Docstrings

Follow Google-style docstrings:

```python
def example_function(param1: str, param2: int) -> bool:
    """Short description of the function.

    Longer description if needed.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ValueError: When something goes wrong
    """
```

## Contributing

### Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Update documentation
6. Submit a pull request

### Commit Messages

Use conventional commit format:
- `feat: add new parameter class for X.Y.Z`
- `fix: correct code mapping for existing class`
- `docs: update API reference`
- `test: add tests for new functionality`

## Release Process

1. Update version in `pyproject.toml`
2. Update CHANGELOG.md
3. Create a new release on GitHub
4. The CI/CD pipeline will handle PyPI publication

## Getting Help

- Open an issue on GitHub for bugs or feature requests
- Check existing issues and discussions
- Review the ENTSO-E Transparency Platform documentation
