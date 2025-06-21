import argparse
import os
import sys

from PyPDF2 import PdfReader, PdfWriter


def extract_pages(input_pdf, output_pdf, pages):
    """
    Extract specific pages from a PDF file and create a new PDF with only those pages.

    Args:
        input_pdf (str): Path to the input PDF file
        output_pdf (str): Path to save the output PDF file
        pages (list): List of page numbers to extract (1-based indexing for user input)

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Validate input file exists
        if not os.path.exists(input_pdf):
            print(f"Error: Input file '{input_pdf}' does not exist.")
            return False

        # Create PDF reader and writer objects
        reader = PdfReader(input_pdf)
        writer = PdfWriter()

        # Get total number of pages in the PDF
        total_pages = len(reader.pages)
        print(f"Total pages in PDF: {total_pages}")

        # Validate page numbers
        valid_pages = []
        for page_num in pages:
            # Convert from 1-based (user input) to 0-based (PyPDF2 indexing)
            idx = page_num - 1
            if 0 <= idx < total_pages:
                valid_pages.append(idx)
            else:
                print(f"Warning: Page {page_num} is out of range and will be skipped.")

        if not valid_pages:
            print("Error: No valid pages to extract.")
            return False

        # Add selected pages to the writer
        for page_idx in valid_pages:
            writer.add_page(reader.pages[page_idx])

        # Write the output file
        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)

        print(f"Successfully created '{output_pdf}' with {len(valid_pages)} pages.")
        return True

    except Exception as e:
        print(f"Error: {str(e)}")
        return False


def parse_page_ranges(page_string):
    """
    Parse a string of page ranges into a list of page numbers.

    Examples:
        "1,3,5-7" -> [1, 3, 5, 6, 7]
        "1-3,5,7-9" -> [1, 2, 3, 5, 7, 8, 9]

    Args:
        page_string (str): Comma-separated string of page numbers and ranges

    Returns:
        list: List of page numbers
    """
    pages = []
    ranges = page_string.split(",")

    for r in ranges:
        r = r.strip()
        if "-" in r:
            start, end = map(int, r.split("-"))
            pages.extend(range(start, end + 1))
        else:
            try:
                pages.append(int(r))
            except ValueError:
                print(f"Warning: Invalid page number '{r}' will be skipped.")

    return sorted(set(pages))  # Remove duplicates and sort


def main():
    parser = argparse.ArgumentParser(
        description="Extract specific pages from a PDF file."
    )
    parser.add_argument("input_pdf", help="Path to the input PDF file")
    parser.add_argument("output_pdf", help="Path to save the output PDF file")
    parser.add_argument("pages", help='Pages to extract (e.g., "1,3,5-7")')

    args = parser.parse_args()

    # Parse page ranges
    page_list = parse_page_ranges(args.pages)

    if not page_list:
        print("Error: No valid pages specified.")
        return 1

    # Extract pages
    success = extract_pages(args.input_pdf, args.output_pdf, page_list)

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
