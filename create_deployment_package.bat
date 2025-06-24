@echo off
echo ================================================================
echo              CREATING DEPLOYMENT PACKAGE
echo ================================================================
echo.

set PACKAGE_NAME=instagram_scraper_deployment_package
set CURRENT_DIR=%CD%

echo 📦 Creating deployment package: %PACKAGE_NAME%.zip
echo.

REM List files to be included in the package
echo 📋 Files to include in package:
echo    ✅ instagram_scraper.py
echo    ✅ main.py  
echo    ✅ requirements.txt
echo    ✅ README.md
echo    ✅ DEPLOYMENT_GUIDE.md
echo    ✅ DEPLOYMENT_PACKAGE.md
echo    ✅ deploy_install.bat
echo    ✅ deploy_run.bat
echo    ✅ deploy_install.sh
echo    ✅ deploy_run.sh
echo    ✅ sample_websites.csv
echo.

REM Check if PowerShell is available for compression
powershell -Command "Get-Command Compress-Archive" >nul 2>&1
if %errorlevel% equ 0 (
    echo 🗜️ Using PowerShell to create ZIP archive...
    powershell -Command "Compress-Archive -Path 'instagram_scraper.py','main.py','requirements.txt','README.md','DEPLOYMENT_GUIDE.md','DEPLOYMENT_PACKAGE.md','deploy_install.bat','deploy_run.bat','deploy_install.sh','deploy_run.sh','sample_websites.csv' -DestinationPath '%PACKAGE_NAME%.zip' -Force"
    if %errorlevel% equ 0 (
        echo ✅ Package created successfully: %PACKAGE_NAME%.zip
    ) else (
        echo ❌ Failed to create package with PowerShell
    )
) else (
    echo ⚠️ PowerShell Compress-Archive not available
    echo 📁 Please manually create a ZIP file with the following files:
    echo    - instagram_scraper.py
    echo    - main.py
    echo    - requirements.txt
    echo    - README.md
    echo    - DEPLOYMENT_GUIDE.md
    echo    - DEPLOYMENT_PACKAGE.md
    echo    - deploy_install.bat
    echo    - deploy_run.bat
    echo    - deploy_install.sh
    echo    - deploy_run.sh
    echo    - sample_websites.csv
)

echo.
echo ================================================================
echo                   📦 PACKAGE READY FOR DEPLOYMENT
echo ================================================================
echo.
echo 🎯 To deploy on another PC:
echo    1. Copy %PACKAGE_NAME%.zip to target PC
echo    2. Extract the ZIP file
echo    3. Run deploy_install.bat (Windows) or deploy_install.sh (Linux/Mac)
echo    4. Run deploy_run.bat (Windows) or deploy_run.sh (Linux/Mac)
echo.
echo 📖 For detailed instructions, see DEPLOYMENT_GUIDE.md
echo.
pause
