@echo off
echo Building PDF Tools executable...

:: Clean previous build artifacts
if exist "dist\pdf_tools.exe" del /F /Q "dist\pdf_tools.exe"
if exist "build" rmdir /S /Q "build"

:: Build the executable using PyInstaller with our spec file
poetry run pyinstaller pdf_tools.spec

echo.
if exist "dist\pdf_tools.exe" (
    echo Build successful! Executable created at dist\pdf_tools.exe
) else (
    echo Build failed. Please check the error messages above.
)

pause