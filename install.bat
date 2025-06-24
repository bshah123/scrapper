@echo off
echo Installing Instagram Handle Scraper dependencies...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://python.org
    pause
    exit /b 1
)

echo Python found. Installing dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo Error installing dependencies. Please check your internet connection and try again.
    pause
    exit /b 1
)

echo.
echo ✅ Installation completed successfully!
echo.
echo To run the scraper:
echo   python main.py
echo.
pause
