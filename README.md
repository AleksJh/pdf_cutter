# PDF Cutting Tool

A simple yet powerful application for extracting specific pages from PDF files. This tool allows you to select individual pages or page ranges from a PDF and create a new PDF containing only those pages.

## Features

- **Command Line Interface**: Extract pages using simple commands
- **Graphical User Interface**: User-friendly interface for selecting and extracting pages
- **Flexible Page Selection**: Specify individual pages or page ranges (e.g., "1,3,5-7")

## Installation

1. Ensure you have Python 3.8 or higher installed
2. Clone or download this repository
3. Install Poetry (if not already installed):

```bash
pip install poetry
```

4. Install the project dependencies:

```bash
poetry install
```

For more information about using Poetry, see [POETRY.md](POETRY.md).

## Usage

### Unified Launcher

The easiest way to access all tools is through the unified launcher:

```bash
poetry run python pdf_tools.py
```

This will open a menu where you can select which tool to use.

### Command Line Interface

The command line tool is perfect for quick extractions or for use in scripts:

```bash
poetry run python pdf_cutter.py input.pdf output.pdf "1,3,5-7"
```

Where:
- `input.pdf` is the path to the source PDF file
- `output.pdf` is the path where the new PDF will be saved
- `"1,3,5-7"` specifies the pages to extract (in this example, pages 1, 3, 5, 6, and 7)

### Graphical User Interface

For a more user-friendly experience, use the GUI version:

```bash
poetry run python pdf_cutter_gui.py
```

The GUI allows you to:
1. Select input and output files using file browsers
2. Specify pages to extract using the same format as the command line (e.g., "1,3,5-7")
3. Extract pages with a single click

## Page Selection Format

The page selection format is flexible and allows for individual pages and ranges:

- Individual pages: `1,3,5`
- Page ranges: `5-10`
- Combination: `1,3,5-7,10-15`

## Examples

### Extract the first 5 pages

```bash
poetry run python pdf_cutter.py document.pdf first_five_pages.pdf "1-5"
```

### Extract specific pages

```bash
poetry run python pdf_cutter.py document.pdf selected_pages.pdf "1,3,5,7,9"
```

### Extract a combination of individual pages and ranges

```bash
poetry run python pdf_cutter.py document.pdf mixed_selection.pdf "1-3,5,7-9"
```

## Troubleshooting

- **File Not Found**: Ensure the input PDF file exists and the path is correct
- **Invalid Page Numbers**: Make sure the specified page numbers exist in the PDF
- **Permission Errors**: Ensure you have permission to read the input file and write to the output location
- **Missing Dependencies**: If you encounter import errors, make sure you've installed all required dependencies with `poetry install`

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [PyPDF2](https://github.com/py-pdf/PyPDF2) for PDF manipulation capabilities
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the graphical user interface