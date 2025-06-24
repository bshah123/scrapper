@echo off
echo ================================================================
echo                   INSTAGRAM SCRAPER RUNNER
echo ================================================================
echo.

REM Check if virtual environment exists
if not exist ".venv\Scripts\activate.bat" (
    echo ❌ ERROR: Virtual environment not found
    echo.
    echo Please run "deploy_install.bat" first to install the scraper
    echo.
    pause
    exit /b 1
)

echo 🔄 Activating virtual environment...
call .venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo ❌ ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)

echo ✅ Virtual environment activated
echo.

echo 🚀 Starting Instagram Scraper...
echo.
python main.py

echo.
echo 📝 Scraper finished. Check your output files!
echo.
pause
