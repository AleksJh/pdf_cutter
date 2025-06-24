# PDF Tools - Executable Version

## Overview

This is the standalone executable version of the PDF Tools application. It does not require Python or any dependencies to be installed on your system.

## How to Use

1. Double-click on `Launch PDF Tools (Executable).bat` to start the application
   - Alternatively, you can directly run `dist\pdf_tools.exe`

2. From the main menu, you can:
   - Launch the PDF Cutter GUI to extract pages from PDF files
   - View documentation
   - Check for updates

## Features

- **PDF Cutter**: Extract specific pages from PDF files using a user-friendly interface
- **No Installation Required**: The executable contains all necessary components
- **No Console Windows**: All console windows are hidden for a clean user experience

## Troubleshooting

If you encounter any issues:

1. Make sure the `file_types_pdf_21313.ico` file is in the same directory as the executable
2. Ensure that the README.md file is present for the documentation feature to work
3. If the application doesn't start, try running it as administrator

## Building from Source

If you want to rebuild the executable:

1. Make sure you have Poetry installed
2. Run `build_exe.bat` to create a new executable
3. The new executable will be placed in the `dist` directory