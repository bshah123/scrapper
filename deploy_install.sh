#!/bin/bash

# Instagram Scraper Installation Script for Linux/Mac
echo "================================================================"
echo "                   INSTAGRAM SCRAPER INSTALLER"
echo "================================================================"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ ERROR: Python3 is not installed"
    echo
    echo "Please install Python3:"
    echo "  Ubuntu/Debian: sudo apt update && sudo apt install python3 python3-pip python3-venv"
    echo "  CentOS/RHEL: sudo yum install python3 python3-pip"
    echo "  macOS: brew install python3"
    echo
    exit 1
fi

echo "✅ Python3 is installed"
python3 --version

echo
echo "📦 Setting up virtual environment..."
python3 -m venv .venv
if [ $? -ne 0 ]; then
    echo "❌ ERROR: Failed to create virtual environment"
    exit 1
fi

echo "✅ Virtual environment created"

echo
echo "🔄 Activating virtual environment..."
source .venv/bin/activate
if [ $? -ne 0 ]; then
    echo "❌ ERROR: Failed to activate virtual environment"
    exit 1
fi

echo "✅ Virtual environment activated"

echo
echo "📥 Installing required packages..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "❌ ERROR: Failed to install required packages"
    exit 1
fi

echo "✅ All packages installed successfully"

echo
echo "🧪 Testing installation..."
python -c "from instagram_scraper import InstagramScraper; print('✅ Instagram scraper imports successfully')"
if [ $? -ne 0 ]; then
    echo "❌ ERROR: Installation test failed"
    exit 1
fi

python -c "import main; print('✅ Main module imports successfully')"
if [ $? -ne 0 ]; then
    echo "❌ ERROR: Main module test failed"
    exit 1
fi

echo
echo "================================================================"
echo "                    🎉 INSTALLATION COMPLETE! 🎉"
echo "================================================================"
echo
echo "The Instagram Scraper has been successfully installed!"
echo
echo "🚀 To run the scraper:"
echo "    source .venv/bin/activate && python main.py"
echo "    OR use the run script: ./deploy_run.sh"
echo
echo "📁 Files you can customize:"
echo "    - Put your website URLs in a CSV file"
echo "    - Results will be saved as 'instagram_results.csv'"
echo
echo "📖 For detailed instructions, see DEPLOYMENT_GUIDE.md"
echo
