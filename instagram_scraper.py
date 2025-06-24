import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
import logging
from urllib.parse import urljoin, urlparse
import os

class InstagramScraper:
    def __init__(self, use_selenium=False, headless=True):
        """
        Initialize the Instagram scraper
        
        Args:
            use_selenium (bool): Whether to use Selenium for JavaScript-heavy sites
            headless (bool): Whether to run browser in headless mode
        """
        self.use_selenium = use_selenium
        self.headless = headless
        self.driver = None
        
        # Set up logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
        
        # Instagram URL patterns - now extracting full URLs
        self.instagram_url_patterns = [
            r'https?://(?:www\.)?instagram\.com/([a-zA-Z0-9_.]+)/?',
            r'https?://(?:www\.)?instagr\.am/([a-zA-Z0-9_.]+)/?',
            r'https?://ig\.me/([a-zA-Z0-9_.]+)/?'
        ]
        
        # Instagram handle patterns (for text mentions)
        self.instagram_handle_patterns = [
            r'@([a-zA-Z0-9_.]+)',
            r'instagram\.com/([a-zA-Z0-9_.]+)',
            r'instagr\.am/([a-zA-Z0-9_.]+)',
            r'ig\.me/([a-zA-Z0-9_.]+)'
        ]
    
    def _clean_url(self, url):
        """Clean and validate URL"""
        if not url:
            return None
            
        url = url.strip()
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            
        return url
    
    def _extract_instagram_from_text(self, text):
        """Extract Instagram URLs from text using regex patterns"""
        instagram_urls = set()
        
        # First, look for complete Instagram URLs
        for pattern in self.instagram_url_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches:
                if match and len(match) > 0 and not match.startswith('p/'):
                    instagram_urls.add(f"https://www.instagram.com/{match}")
        
        # Then, look for handles and convert them to full URLs
        for pattern in self.instagram_handle_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches:
                if match and len(match) > 0 and not match.startswith('p/'):
                    instagram_urls.add(f"https://www.instagram.com/{match}")
        
        return list(instagram_urls)
    
    def _scrape_with_requests(self, url):
        """Scrape website using requests and BeautifulSoup"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Get all text content
            text_content = soup.get_text()
            
            # Look for Instagram links in href attributes
            instagram_links = []
            for link in soup.find_all('a', href=True):
                href = link['href']
                if 'instagram.com' in href.lower():
                    instagram_links.append(href)
            
            # Extract URLs from text and links
            urls_from_text = self._extract_instagram_from_text(text_content)
            urls_from_links = []
            
            for link in instagram_links:
                urls = self._extract_instagram_from_text(link)
                urls_from_links.extend(urls)
            
            all_urls = list(set(urls_from_text + urls_from_links))
            return all_urls
            
        except Exception as e:
            self.logger.error(f"Error scraping {url} with requests: {e}")
            return []
    
    def scrape_instagram_handle(self, url):
        """
        Scrape Instagram URLs from a given website URL
        
        Args:
            url (str): Website URL to scrape
            
        Returns:
            list: List of Instagram profile URLs found
        """
        url = self._clean_url(url)
        if not url:
            return []
        
        self.logger.info(f"Scraping: {url}")
        
        # Use requests for scraping (Selenium disabled due to driver issues)
        instagram_urls = self._scrape_with_requests(url)
        
        # Clean and validate URLs
        cleaned_urls = []
        for instagram_url in instagram_urls:
            if instagram_url and len(instagram_url) > 0 and not '/p/' in instagram_url:
                cleaned_urls.append(instagram_url)
        
        self.logger.info(f"Found {len(cleaned_urls)} Instagram URLs for {url}")
        return cleaned_urls
    
    def process_websites_from_csv(self, input_file, output_file=None):
        """
        Process a list of websites from CSV and extract Instagram URLs
        
        Args:
            input_file (str): Path to input CSV file with website URLs
            output_file (str): Path to output CSV file (optional)
            
        Returns:
            pandas.DataFrame: DataFrame with results
        """
        try:
            # Read input CSV with encoding handling
            self.logger.info(f"Reading CSV file: {input_file}")
            try:
                df = pd.read_csv(input_file, encoding='utf-8')
                self.logger.info(f"Successfully read CSV with utf-8 encoding")
            except UnicodeDecodeError:
                self.logger.warning("UTF-8 failed, trying latin-1 encoding")
                try:
                    df = pd.read_csv(input_file, encoding='latin-1')
                    self.logger.info(f"Successfully read CSV with latin-1 encoding")
                except UnicodeDecodeError:
                    self.logger.warning("latin-1 failed, trying cp1252 encoding")
                    df = pd.read_csv(input_file, encoding='cp1252')
                    self.logger.info(f"Successfully read CSV with cp1252 encoding")
            
            # Determine the column name for URLs
            url_column = None
            for col in df.columns:
                if any(keyword in col.lower() for keyword in ['url', 'website', 'link', 'site']):
                    url_column = col
                    break
            
            if url_column is None:
                # Use the first column if no obvious URL column found
                url_column = df.columns[0]
                self.logger.warning(f"No obvious URL column found. Using '{url_column}'")
            
            results = []
            
            for index, row in df.iterrows():
                url = row[url_column]
                
                # Handle NaN/empty values
                if pd.isna(url) or url == '' or str(url).strip() == '':
                    self.logger.warning(f"Skipping row {index+1}: Empty or invalid URL")
                    continue
                
                firm_name = row.get('name', row.get('company', row.get('firm', f'Company_{index+1}')))
                
                self.logger.info(f"Processing {index+1}/{len(df)}: {firm_name} - {url}")
                
                instagram_urls = self.scrape_instagram_handle(url)
                
                result = {
                    'Firm_Name': firm_name,
                    'Website_URL': url,
                    'Number_of_Instagram_Accounts': len(instagram_urls),
                    'Status': 'Success' if instagram_urls else 'No Instagram Found'
                }
                
                # Add Instagram URLs in separate columns with clickable hyperlinks
                max_instagram_accounts = 5  # Maximum number of Instagram accounts to handle
                for i in range(max_instagram_accounts):
                    col_name = f'Instagram_Account_{i+1}'
                    if i < len(instagram_urls):
                        # Create hyperlink format for CSV: =HYPERLINK("URL","Display Text")
                        url_text = instagram_urls[i]
                        display_text = url_text.replace('https://www.instagram.com/', '@')
                        result[col_name] = f'=HYPERLINK("{url_text}","{display_text}")'
                    else:
                        result[col_name] = ''
                
                # Add original columns
                for col in df.columns:
                    if col not in ['name', 'company', 'firm'] and col != url_column:
                        result[col] = row[col]
                
                results.append(result)
                
                # Add delay to be respectful to websites
                time.sleep(1)
            
            results_df = pd.DataFrame(results)
            
            # Save to CSV if output file specified
            if output_file:
                # Ensure the output file has .csv extension
                if not output_file.lower().endswith('.csv'):
                    output_file = output_file + '.csv'
                results_df.to_csv(output_file, index=False, encoding='utf-8')
                self.logger.info(f"Results saved to {output_file}")
            
            return results_df
            
        except Exception as e:
            self.logger.error(f"Error processing CSV file: {e}")
            raise
    
    def process_single_url(self, url, firm_name=None):
        """
        Process a single URL and return results
        
        Args:
            url (str): Website URL
            firm_name (str): Optional firm name
            
        Returns:
            dict: Results dictionary
        """
        instagram_urls = self.scrape_instagram_handle(url)
        
        result = {
            'Firm_Name': firm_name or 'Unknown',
            'Website_URL': url,
            'Number_of_Instagram_Accounts': len(instagram_urls),
            'Status': 'Success' if instagram_urls else 'No Instagram Found'
        }
        
        # Add Instagram URLs in separate columns
        max_instagram_accounts = 5
        for i in range(max_instagram_accounts):
            col_name = f'Instagram_Account_{i+1}'
            if i < len(instagram_urls):
                url_text = instagram_urls[i]
                display_text = url_text.replace('https://www.instagram.com/', '@')
                result[col_name] = f'=HYPERLINK("{url_text}","{display_text}")'
            else:
                result[col_name] = ''
        
        return result
    
    def close(self):
        """Close the Selenium driver if it's open"""
        if self.driver:
            self.driver.quit()
            self.logger.info("Selenium driver closed")

def main():
    """Example usage"""
    scraper = InstagramScraper(use_selenium=False, headless=True)
    
    try:
        # Example: Process CSV file
        input_file = "sample_websites.csv"
        output_file = "instagram_results.csv"
        
        if os.path.exists(input_file):
            results = scraper.process_websites_from_csv(input_file, output_file)
            print(f"\nProcessed {len(results)} websites")
            print(f"Results saved to {output_file}")
            print("\nSample results:")
            print(results.head())
        else:
            print(f"Input file '{input_file}' not found.")
            print("Please create a CSV file with website URLs.")
    
    finally:
        scraper.close()

if __name__ == "__main__":
    main()
