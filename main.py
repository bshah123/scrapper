from instagram_scraper import InstagramScraper
import pandas as pd
import os
import sys

def create_sample_csv():
    """Create a sample CSV file with website URLs"""
    sample_data = {
        'Company_Name': [
            'Apple Inc.',
            'Microsoft Corporation',
            'Google LLC',
            'Nike Inc.',
            'Coca-Cola Company'
        ],
        'Website_URL': [
            'https://www.apple.com',
            'https://www.microsoft.com',
            'https://www.google.com',
            'https://www.nike.com',
            'https://www.coca-cola.com'
        ]
    }
    
    df = pd.DataFrame(sample_data)
    df.to_csv('sample_websites.csv', index=False)
    print("Sample CSV file 'sample_websites.csv' created!")
    print(df)

def interactive_mode():
    """Interactive mode for single URL processing"""
    scraper = InstagramScraper(use_selenium=False, headless=True)
    
    try:
        while True:
            print("\n" + "="*50)
            print("Instagram Handle Scraper - Interactive Mode")
            print("="*50)
            
            url = input("Enter website URL (or 'quit' to exit): ").strip()
            
            if url.lower() in ['quit', 'exit', 'q']:
                break
            
            if not url:
                continue
            
            firm_name = input("Enter firm name (optional): ").strip()
            
            print(f"\nScraping {url}...")
            result = scraper.process_single_url(url, firm_name)
            
            print("\nResults:")
            print("-" * 30)
            for key, value in result.items():
                print(f"{key}: {value}")
            
            # Ask if user wants to save to file
            save = input("\nSave result to CSV file? (y/n): ").strip().lower()
            if save in ['y', 'yes']:
                filename = f"instagram_result_{firm_name or 'unknown'}.csv".replace(' ', '_')
                df = pd.DataFrame([result])
                df.to_csv(filename, index=False)
                print(f"Result saved to {filename}")
    
    finally:
        scraper.close()

def main():
    """Main function with menu options"""
    while True:
        print("\n" + "="*60)
        print("        INSTAGRAM HANDLE SCRAPER")
        print("="*60)
        print("1. Process CSV file with multiple websites")
        print("2. Interactive mode (single URLs)")
        print("3. Create sample CSV file")
        print("4. Exit")
        print("-" * 60)
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            # CSV processing mode
            input_file = input("Enter CSV file path (default: sample_websites.csv): ").strip()
            if not input_file:
                input_file = "sample_websites.csv"
            
            if not os.path.exists(input_file):
                print(f"Error: File '{input_file}' not found!")
                continue
            
            output_file = input("Enter output CSV file path (default: instagram_results.csv): ").strip()
            if not output_file:
                output_file = "instagram_results.csv"
            
            print(f"\nProcessing {input_file}...")
            
            scraper = InstagramScraper(use_selenium=False, headless=True)
            
            try:
                results = scraper.process_websites_from_csv(input_file, output_file)
                
                print(f"\n✅ Processing completed!")
                print(f"📁 Results saved to: {output_file}")
                print(f"📊 Total websites processed: {len(results)}")
                
                # Show summary
                successful = len(results[results['Status'] == 'Success'])
                print(f"✅ Successful scrapes: {successful}")
                print(f"❌ No Instagram found: {len(results) - successful}")
                
                # Show sample results
                print("\n📋 Sample results:")
                display_cols = ['Firm_Name', 'Number_of_Instagram_Accounts', 'Status']
                print(results[display_cols].head())
                
                print(f"\n💡 TIP: Open {output_file} in Excel or Google Sheets to see clickable Instagram links!")
                
            except Exception as e:
                print(f"❌ Error: {e}")
            finally:
                scraper.close()
        
        elif choice == '2':
            # Interactive mode
            interactive_mode()
        
        elif choice == '3':
            # Create sample CSV
            create_sample_csv()
        
        elif choice == '4':
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
