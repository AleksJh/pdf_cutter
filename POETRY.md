# Poetry Setup for PDF Cutting Tool

## Overview

This project uses Poetry for dependency management and has been configured with the following development tools:

- **Black**: Code formatter with a line length of 88 characters
- **Flake8**: Linter for style guide enforcement
- **isort**: Import sorter configured to be compatible with Black

## Configuration

The tools are configured in the following files:

- `pyproject.toml`: Contains configuration for Poetry, Black, and isort
- `.flake8`: Contains configuration for Flake8

## Using the Tools

### Installing Dependencies

```bash
# Install Poetry (if not already installed)
pip install poetry

# Install project dependencies
poetry install
```

### Running the Tools Individually

```bash
# Format code with Black
poetry run black <file_or_directory>

# Sort imports with isort
poetry run isort <file_or_directory>

# Check code style with Flake8
poetry run flake8 <file_or_directory>
```

### Using the Format Script

A convenience script `format_code.py` is provided to run all three tools in sequence:

```bash
# Format a single file
poetry run python format_code.py path/to/file.py

# Format multiple files
poetry run python format_code.py file1.py file2.py file3.py
```

## Tool Configuration Details

### Black

Black is configured with a line length of 88 characters (the default) and targets Python 3.8+.

```toml
[tool.black]
line-length = 88
target-version = ['py38']
include = '\.pyi?$'
```

### isort

isort is configured to be compatible with Black using the "black" profile and the same line length.

```toml
[tool.isort]
profile = "black"
line_length = 88
```

### Flake8

Flake8 is configured with a line length of 88 characters to match Black and ignores E203 which is recommended when using Black.

```ini
[flake8]
max-line-length = 88
extend-ignore = E203
exclude = .git,__pycache__,build,dist,.venv
```

## Virtual Environment

Poetry automatically creates and manages a virtual environment for the project. You can activate it with:

```bash
poetry shell
```

Or run commands within it without activation:

```bash
poetry run <command>
```