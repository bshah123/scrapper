#!/bin/bash

# Instagram Scraper Runner Script for Linux/Mac
echo "================================================================"
echo "                   INSTAGRAM SCRAPER RUNNER"
echo "================================================================"
echo

# Check if virtual environment exists
if [ ! -f ".venv/bin/activate" ]; then
    echo "❌ ERROR: Virtual environment not found"
    echo
    echo "Please run './deploy_install.sh' first to install the scraper"
    echo
    exit 1
fi

echo "🔄 Activating virtual environment..."
source .venv/bin/activate
if [ $? -ne 0 ]; then
    echo "❌ ERROR: Failed to activate virtual environment"
    exit 1
fi

echo "✅ Virtual environment activated"
echo

echo "🚀 Starting Instagram Scraper..."
echo
python main.py

echo
echo "📝 Scraper finished. Check your output files!"
echo
