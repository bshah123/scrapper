# Instagram Handle Scraper

A powerful Python tool to automatically extract Instagram social media handles from company websites. This scraper can process individual URLs or batch process multiple websites from a CSV file, making it perfect for social media research, lead generation, and competitor analysis.

## ✨ Features

- **Batch Processing**: Process multiple websites from CSV files
- **Interactive Mode**: Single URL processing with real-time results
- **Smart Detection**: Uses multiple patterns to find Instagram handles and URLs
- **CSV Export**: Automatically saves results to CSV files with clickable links
- **Error Handling**: Robust error handling with detailed status reporting
- **Sample Data**: Includes sample CSV with popular company websites
- **User-Friendly**: Menu-driven interface with clear progress indicators
- **Cross-Platform**: Works on Windows, Linux, and macOS
- **No Browser Dependencies**: Lightweight solution using requests + BeautifulSoup
- **Virtual Environment**: Automatic isolated Python environment setup
- **Deployment Ready**: Complete deployment scripts and package creation tools
- **Multiple Encoding Support**: Handles various CSV file encodings automatically

## 🚀 Quick Start

### Prerequisites

- **Python 3.7+** (3.8+ recommended)
- **Internet connection** for web scraping
- **2GB RAM minimum**
- **Windows 10/11**, **Linux**, or **macOS**

### Installation Options

#### Option 1: Automated Installation (Recommended)

**For Windows:**
1. Download/copy the entire `scrapper` folder
2. Double-click `deploy_install.bat`
3. Double-click `deploy_run.bat` to start

**For Linux/Mac:**
1. Download/copy the entire `scrapper` folder
2. Run: `chmod +x *.sh && ./deploy_install.sh`
3. Run: `./deploy_run.sh` to start

#### Option 2: Manual Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/scrapper.git
   cd scrapper
   ```

2. **Create virtual environment** (recommended):
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # Linux/Mac
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```

### 📦 Deployment Package

For easy deployment to other systems, use the deployment package creator:

**Windows:**
```bash
create_deployment_package.bat
```

This creates `instagram_scraper_deployment_package.zip` containing:
- All source files
- Installation scripts for Windows and Linux/Mac
- Documentation and sample data
- Ready-to-run deployment scripts

## 📖 Usage

### Menu Options

The application provides four main options:

#### 1. Process CSV File (Batch Mode)
- Process multiple websites from a CSV file
- Input CSV should have columns: `Company_Name`, `Website_URL`
- Outputs results to a new CSV file with Instagram handles and clickable links

#### 2. Interactive Mode
- Enter individual website URLs for real-time processing
- Optional company name input
- Option to save results to CSV

#### 3. Create Sample CSV
- Generates a sample CSV file with popular company websites
- Perfect for testing and getting started

#### 4. Exit
- Safely close the application

### Input CSV Format

Your input CSV file should have the following structure:

```csv
Company_Name,Website_URL
Apple Inc.,https://www.apple.com
Microsoft Corporation,https://www.microsoft.com
Nike Inc.,https://www.nike.com
```

### Output Format

The scraper generates CSV files with the following columns:

- `Firm_Name`: Company name
- `Website_URL`: Original website URL
- `Number_of_Instagram_Accounts`: Count of found Instagram accounts
- `Instagram_Handles`: Extracted Instagram usernames
- `Instagram_URLs`: Full Instagram URLs (clickable in Excel/Sheets)
- `Status`: Success/Error status
- `Error_Message`: Details if any errors occurred
- `Processing_Time`: Time taken to process each URL

## 🛠️ Technical Details

### Dependencies

- **requests**: HTTP requests handling
- **beautifulsoup4**: HTML parsing and content extraction
- **pandas**: Data manipulation and CSV processing
- **lxml**: XML/HTML parser for BeautifulSoup

### How It Works

1. **URL Cleaning**: Validates and normalizes input URLs
2. **Web Scraping**: Fetches website content using HTTP requests
3. **Pattern Matching**: Uses regex patterns to find Instagram handles and URLs
4. **Data Processing**: Extracts and cleans Instagram information
5. **Export**: Saves results to CSV with proper formatting

### Instagram Detection Patterns

The scraper looks for:
- Full Instagram URLs: `https://instagram.com/username`
- Instagram mentions: `@username`
- Short URLs: `instagr.am/username`, `ig.me/username`
- Text references: `instagram.com/username`

## 📁 File Structure

```
scrapper/
├── main.py                           # Main application with menu interface
├── instagram_scraper.py              # Core scraping functionality
├── requirements.txt                  # Python dependencies
├── sample_websites.csv               # Sample data for testing
├── README.md                         # This documentation
├── DEPLOYMENT_GUIDE.md               # Detailed deployment instructions
├── DEPLOYMENT_PACKAGE.md             # Package contents documentation
├── 
├── # Installation Scripts
├── install.bat                       # Basic Windows installation
├── run.bat                          # Basic Windows run script
├── deploy_install.bat               # Advanced Windows deployment installer
├── deploy_run.bat                   # Advanced Windows deployment runner
├── deploy_install.sh                # Linux/Mac deployment installer
├── deploy_run.sh                    # Linux/Mac deployment runner
├── create_deployment_package.bat    # Creates deployment ZIP package
├── 
├── # Generated Files (after installation/use)
├── .venv/                           # Virtual environment (created during install)
├── instagram_results.csv            # Output files (created after processing)
├── instagram_scraper_deployment_package.zip  # Deployment package
└── __pycache__/                     # Python cache files
```

## 🔧 Deployment & Distribution

### Creating Deployment Package

To create a complete deployment package for distribution:

1. **Run the package creator**:
   ```bash
   create_deployment_package.bat
   ```

2. **Share the generated ZIP file**: `instagram_scraper_deployment_package.zip`

### Deployment on Target Systems

#### Quick Deployment (Windows)
1. Extract the deployment package
2. Double-click `deploy_install.bat`
3. Double-click `deploy_run.bat`

#### Quick Deployment (Linux/Mac)
1. Extract the deployment package
2. Run: `chmod +x *.sh && ./deploy_install.sh`
3. Run: `./deploy_run.sh`

### System Requirements for Deployment

- **Minimum RAM**: 2GB
- **Disk Space**: 500MB (including Python virtual environment)
- **Network**: Internet connection required for scraping
- **Python**: 3.7+ (automatically validated by install scripts)

### Troubleshooting Deployment

Common deployment issues and solutions:

#### Python Not Found
- **Error**: `'python' is not recognized`
- **Solution**: Install Python from python.org, ensure "Add to PATH" is checked

#### Permission Issues
- **Error**: Permission denied during installation
- **Solution**: Run as Administrator (Windows) or use `sudo` (Linux/Mac)

#### Network/SSL Issues
- **Error**: SSL certificate verification failed
- **Solution**: Check firewall settings and internet connection

#### Virtual Environment Issues
- **Error**: Failed to create virtual environment
- **Solution**: Ensure Python venv module is installed: `pip install virtualenv`

## 📊 Example Output

```
Processing completed!
📁 Results saved to: instagram_results.csv
📊 Total websites processed: 50
✅ Successful scrapes: 45
❌ No Instagram found: 5

Sample results:
    Firm_Name               Number_of_Instagram_Accounts    Status
0   Apple Inc.              2                              Success
1   Microsoft Corporation   1                              Success
2   Nike Inc.              3                              Success
```

## 🚨 Important Notes

- **Rate Limiting**: Built-in delays (1 second) to respect website servers
- **Error Handling**: Continues processing even if individual sites fail
- **Legal Compliance**: Only scrapes publicly available information
- **Performance**: Optimized for batch processing of large datasets
- **Cross-Platform**: Works on Windows, Linux, and macOS
- **No Browser Required**: Uses lightweight requests + BeautifulSoup (no Selenium)
- **Virtual Environment**: Automatically creates isolated Python environment
- **Encoding Support**: Handles multiple CSV encodings (UTF-8, Latin-1, CP1252)

## 📋 Additional Documentation

For detailed information, see these additional files:

- **[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)** - Complete deployment instructions and troubleshooting
- **[DEPLOYMENT_PACKAGE.md](DEPLOYMENT_PACKAGE.md)** - Information about the deployment package contents
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Guidelines for contributing to the project
- **[GITHUB_SETUP.md](GITHUB_SETUP.md)** - GitHub repository setup instructions

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is for educational and research purposes only. Please ensure you comply with:
- Website terms of service
- Applicable laws and regulations
- Ethical web scraping practices
- Rate limiting and respectful usage

## 🆘 Support

If you encounter any issues or have questions:

1. Check the existing issues in the repository
2. Create a new issue with detailed information
3. Include error messages and steps to reproduce

## 🏆 Acknowledgments

- Built with Python and open-source libraries
- Inspired by the need for efficient social media research tools
- Thanks to the Python community for excellent web scraping tools

---

**Happy Scraping! 🕷️✨**