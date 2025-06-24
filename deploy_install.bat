@echo off
echo ================================================================
echo                   INSTAGRAM SCRAPER INSTALLER
echo ================================================================
echo.
echo This script will install the Instagram Scraper on your system.
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo ✅ Python is installed
python --version

echo.
echo 📦 Setting up virtual environment...
python -m venv .venv
if %errorlevel% neq 0 (
    echo ❌ ERROR: Failed to create virtual environment
    pause
    exit /b 1
)

echo ✅ Virtual environment created

echo.
echo 🔄 Activating virtual environment...
call .venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo ❌ ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)

echo ✅ Virtual environment activated

echo.
echo 📥 Installing required packages...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ❌ ERROR: Failed to install required packages
    pause
    exit /b 1
)

echo ✅ All packages installed successfully

echo.
echo 🧪 Testing installation...
python -c "from instagram_scraper import InstagramScraper; print('✅ Instagram scraper imports successfully')"
if %errorlevel% neq 0 (
    echo ❌ ERROR: Installation test failed
    pause
    exit /b 1
)

python -c "import main; print('✅ Main module imports successfully')"
if %errorlevel% neq 0 (
    echo ❌ ERROR: Main module test failed
    pause
    exit /b 1
)

echo.
echo ================================================================
echo                    🎉 INSTALLATION COMPLETE! 🎉
echo ================================================================
echo.
echo The Instagram Scraper has been successfully installed!
echo.
echo 🚀 To run the scraper:
echo    - Double-click "run.bat", OR
echo    - Open Command Prompt and run: python main.py
echo.
echo 📁 Files you can customize:
echo    - Put your website URLs in a CSV file
echo    - Results will be saved as "instagram_results.csv"
echo.
echo 📖 For detailed instructions, see DEPLOYMENT_GUIDE.md
echo.
pause
