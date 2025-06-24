# Instagram Scraper - Deployment Guide

## 📦 Quick Deployment Instructions

### Option 1: Complete Package Transfer
1. Copy the entire `scrapper` folder to the target PC
2. Run `install.bat` on the target PC
3. Run `run.bat` to start the scraper

### Option 2: Fresh Installation
1. Copy only the source files (see file list below)
2. Follow the manual installation steps

## 📋 Required Files for Deployment

### Core Files (REQUIRED)
- `instagram_scraper.py` - Main scraper module
- `main.py` - Entry point
- `requirements.txt` - Python dependencies
- `README.md` - Documentation

### Installation Scripts (RECOMMENDED)
- `install.bat` - Automated installation
- `run.bat` - Easy run script

### Sample Data (OPTIONAL)
- `sample_websites.csv` - Sample input data

## 🖥️ System Requirements

### Software Requirements
- **Python 3.7+** (3.8+ recommended)
- **Windows 10/11** (scripts are Windows-optimized)
- **Internet connection** (for scraping websites)

### Python Packages (auto-installed via requirements.txt)
- requests
- beautifulsoup4
- pandas
- lxml

## 🚀 Installation Steps

### Automated Installation (Recommended)
1. Copy the scrapper folder to target PC
2. Double-click `install.bat`
3. Wait for installation to complete
4. Double-click `run.bat` to start

### Manual Installation
1. **Install Python** (if not already installed)
   - Download from: https://www.python.org/downloads/
   - Make sure to check "Add Python to PATH" during installation

2. **Open Command Prompt or PowerShell**
   ```cmd
   cd path\to\scrapper\folder
   ```

3. **Create Virtual Environment** (recommended)
   ```cmd
   python -m venv .venv
   .venv\Scripts\activate
   ```

4. **Install Dependencies**
   ```cmd
   pip install -r requirements.txt
   ```

5. **Run the Scraper**
   ```cmd
   python main.py
   ```

## 📁 File Structure After Deployment
```
scrapper/
├── instagram_scraper.py    # Main scraper module
├── main.py                 # Entry point
├── requirements.txt        # Dependencies
├── README.md              # Documentation
├── install.bat            # Installation script
├── run.bat               # Run script
├── sample_websites.csv   # Sample input (optional)
├── .venv/               # Virtual environment (created during install)
└── instagram_results.csv # Output (created after first run)
```

## 🔧 Troubleshooting

### Common Issues

#### 1. Python not found
- **Error**: `'python' is not recognized as an internal or external command`
- **Solution**: Install Python and add it to PATH, or use full path to python.exe

#### 2. Permission issues
- **Error**: Permission denied errors
- **Solution**: Run Command Prompt as Administrator

#### 3. Network issues
- **Error**: SSL/Connection errors
- **Solution**: Check internet connection and firewall settings

#### 4. Encoding issues
- **Error**: Unicode/encoding errors with CSV files
- **Solution**: The scraper handles multiple encodings automatically

### Getting Help
1. Check the error messages in the console
2. Ensure all required files are present
3. Verify Python and pip are working: `python --version` and `pip --version`
4. Make sure internet connection is stable

## 📊 Usage Instructions

1. **Prepare your data**: Create a CSV file with website URLs
2. **Run the scraper**: `python main.py` or use `run.bat`
3. **Follow the menu**: Choose option 1 for CSV processing
4. **Check results**: Output will be saved as `instagram_results.csv`

## 🎯 Features
- ✅ Scrapes Instagram profile URLs from company websites
- ✅ Outputs clickable hyperlinks in CSV format
- ✅ Handles multiple Instagram accounts per company
- ✅ Robust error handling and encoding support
- ✅ User-friendly interactive interface
- ✅ No Selenium dependencies (uses requests + BeautifulSoup)

## 🔒 Notes
- The scraper is respectful to websites (1-second delay between requests)
- No browser automation required (no driver installation needed)
- Works offline for processing already downloaded data
- Supports various CSV encodings (UTF-8, Latin-1, CP1252)
