# Instagram Scraper - Complete Deployment Package

## 📦 Package Contents

This package contains everything needed to deploy the Instagram Scraper on another PC.

### Files Included:
- `instagram_scraper.py` - Main scraper module
- `main.py` - Entry point with interactive menu
- `requirements.txt` - Python dependencies
- `README.md` - User documentation
- `DEPLOYMENT_GUIDE.md` - Detailed deployment instructions
- `sample_websites.csv` - Sample input data

### Installation Scripts:
- `deploy_install.bat` - Windows installation script
- `deploy_run.bat` - Windows run script
- `deploy_install.sh` - Linux/Mac installation script
- `deploy_run.sh` - Linux/Mac run script

## 🚀 Quick Start

### For Windows:
1. Copy entire folder to target PC
2. Double-click `deploy_install.bat`
3. Double-click `deploy_run.bat` to start

### For Linux/Mac:
1. Copy entire folder to target PC
2. Run: `chmod +x *.sh && ./deploy_install.sh`
3. Run: `./deploy_run.sh` to start

## 📋 What the Scraper Does

1. **Input**: Takes a CSV file with company website URLs
2. **Process**: Scrapes each website for Instagram profile links
3. **Output**: Creates a CSV with clickable Instagram hyperlinks

### Sample Input (CSV):
```csv
Company_Name,Website_URL,Industry
Apple Inc.,https://www.apple.com,Technology
Starbucks Corporation,https://www.starbucks.com,Food & Beverage
```

### Sample Output (CSV):
```csv
Firm_Name,Website_URL,Number_of_Instagram_Accounts,Status,Instagram_Account_1
Apple Inc.,https://www.apple.com,0,No Instagram Found,
Starbucks Corporation,https://www.starbucks.com,1,Success,"=HYPERLINK(""https://www.instagram.com/starbucks"",""@starbucks"")"
```

## 🔧 System Requirements

- **Python 3.7+** (3.8+ recommended)
- **Internet connection** for scraping
- **2GB RAM minimum**
- **Windows 10/11** or **Linux/macOS**

## 📞 Support

If you encounter issues:
1. Check `DEPLOYMENT_GUIDE.md` for troubleshooting
2. Ensure Python is properly installed
3. Verify internet connection
4. Check that all files are present

## 🎯 Features

✅ **No Selenium required** - Uses lightweight requests + BeautifulSoup  
✅ **Handles multiple Instagram accounts** per company  
✅ **Clickable hyperlinks** in output CSV  
✅ **Robust encoding support** (UTF-8, Latin-1, CP1252)  
✅ **Error handling** for timeouts and failed connections  
✅ **Interactive menu** for easy use  
✅ **Cross-platform** (Windows, Linux, macOS)  

## 📄 License

This tool is for educational and legitimate business use only. Please respect website terms of service and rate limiting.
