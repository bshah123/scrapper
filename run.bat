@echo off
echo Starting Instagram Handle Scraper...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please run install.bat first
    pause
    exit /b 1
)

REM Run the main application
python main.py

pause
