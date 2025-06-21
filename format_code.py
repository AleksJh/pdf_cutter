#!/usr/bin/env python
"""
A simple script to format Python code using black, isort, and flake8.

This script demonstrates how to use Poetry to run the formatting tools
with the configured settings in pyproject.toml and .flake8.
"""

import subprocess
import sys
from pathlib import Path


def run_command(command):
    """Run a command and return the exit code."""
    print(f"Running: {' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    return result.returncode


def format_file(file_path):
    """Format a Python file using black, isort, and flake8."""
    file_path = Path(file_path)
    if not file_path.exists():
        print(f"Error: File {file_path} does not exist.")
        return 1

    if not file_path.name.endswith(".py"):
        print(f"Error: File {file_path} is not a Python file.")
        return 1

    # Run isort first to sort imports
    isort_exit_code = run_command(["poetry", "run", "isort", str(file_path)])

    # Run black to format the code
    black_exit_code = run_command(["poetry", "run", "black", str(file_path)])

    # Run flake8 to check for any remaining issues
    flake8_exit_code = run_command(["poetry", "run", "flake8", str(file_path)])

    if isort_exit_code == 0 and black_exit_code == 0 and flake8_exit_code == 0:
        print(f"\n✅ Successfully formatted {file_path}")
        return 0
    else:
        print(f"\n❌ There were issues formatting {file_path}")
        return 1


def main():
    """Main function to run the script."""
    if len(sys.argv) < 2:
        print("Usage: python format_code.py <file1.py> [file2.py] ...")
        return 1

    exit_codes = []
    for file_path in sys.argv[1:]:
        exit_codes.append(format_file(file_path))

    return 1 if any(exit_codes) else 0


if __name__ == "__main__":
    sys.exit(main())
