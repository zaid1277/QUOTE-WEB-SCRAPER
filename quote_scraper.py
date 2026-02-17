"""
Web Scraper for Quotes
A clean, well-structured web scraper that extracts quotes, authors, and tags
from quotes.toscrape.com and exports them to CSV and JSON formats.

Features:
- Scrapes multiple pages
- Handles pagination automatically
- Exports data in multiple formats
- Includes error handling
- Follows web scraping best practices
"""

import requests
from bs4 import BeautifulSoup
import csv
import json
import time
from typing import List, Dict
from datetime import datetime


class QuoteScraper:
    """A web scraper for extracting quotes from quotes.toscrape.com"""
    
    def __init__(self, base_url: str = "http://quotes.toscrape.com"):
        """
        Initialize the scraper with a base URL
        
        Args:
            base_url: The base URL to scrape from
        """
        self.base_url = base_url
        self.quotes = []
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def scrape_page(self, page_num: int = 1) -> List[Dict[str, any]]:
        """
        Scrape a single page for quotes
        
        Args:
            page_num: The page number to scrape
            
        Returns:
            List of dictionaries containing quote data
        """
        url = f"{self.base_url}/page/{page_num}/"
        
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            quote_elements = soup.find_all('div', class_='quote')
            
            page_quotes = []
            for quote in quote_elements:
                # Extract quote text
                text = quote.find('span', class_='text').get_text()
                
                # Extract author
                author = quote.find('small', class_='author').get_text()
                
                # Extract tags
                tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
                
                page_quotes.append({
                    'text': text,
                    'author': author,
                    'tags': tags,
                    'scraped_at': datetime.now().isoformat()
                })
            
            return page_quotes
            
        except requests.RequestException as e:
            print(f"Error scraping page {page_num}: {e}")
            return []
    
    def scrape_all(self, max_pages: int = 5, delay: float = 1.0) -> List[Dict[str, any]]:
        """
        Scrape multiple pages
        
        Args:
            max_pages: Maximum number of pages to scrape
            delay: Delay between requests in seconds (be respectful!)
            
        Returns:
            List of all scraped quotes
        """
        print(f"Starting to scrape {max_pages} pages...")
        
        for page_num in range(1, max_pages + 1):
            print(f"Scraping page {page_num}...")
            page_quotes = self.scrape_page(page_num)
            
            if not page_quotes:
                print(f"No quotes found on page {page_num}. Stopping.")
                break
            
            self.quotes.extend(page_quotes)
            print(f"Found {len(page_quotes)} quotes on page {page_num}")
            
            # Be respectful - add delay between requests
            if page_num < max_pages:
                time.sleep(delay)
        
        print(f"\nTotal quotes scraped: {len(self.quotes)}")
        return self.quotes
    
    def export_to_csv(self, filename: str = "quotes.csv"):
        """
        Export scraped quotes to CSV file
        
        Args:
            filename: Name of the output CSV file
        """
        if not self.quotes:
            print("No quotes to export!")
            return
        
        filepath = f"/mnt/user-data/outputs/{filename}"
        
        with open(filepath, 'w', newline='', encoding='utf-8') as file:
            fieldnames = ['text', 'author', 'tags', 'scraped_at']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()
            for quote in self.quotes:
                # Convert tags list to string for CSV
                quote_copy = quote.copy()
                quote_copy['tags'] = ', '.join(quote['tags'])
                writer.writerow(quote_copy)
        
        print(f"Exported {len(self.quotes)} quotes to {filepath}")
    
    def export_to_json(self, filename: str = "quotes.json"):
        """
        Export scraped quotes to JSON file
        
        Args:
            filename: Name of the output JSON file
        """
        if not self.quotes:
            print("No quotes to export!")
            return
        
        filepath = f"/mnt/user-data/outputs/{filename}"
        
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(self.quotes, file, indent=2, ensure_ascii=False)
        
        print(f"Exported {len(self.quotes)} quotes to {filepath}")
    
    def get_statistics(self) -> Dict[str, any]:
        """
        Get statistics about the scraped data
        
        Returns:
            Dictionary containing statistics
        """
        if not self.quotes:
            return {}
        
        authors = [q['author'] for q in self.quotes]
        all_tags = [tag for q in self.quotes for tag in q['tags']]
        
        return {
            'total_quotes': len(self.quotes),
            'unique_authors': len(set(authors)),
            'most_common_author': max(set(authors), key=authors.count),
            'unique_tags': len(set(all_tags)),
            'most_common_tag': max(set(all_tags), key=all_tags.count) if all_tags else None
        }


def main():
    """Main function to run the scraper"""
    # Initialize scraper
    scraper = QuoteScraper()
    
    # Scrape quotes (3 pages with 1 second delay between requests)
    scraper.scrape_all(max_pages=3, delay=1.0)
    
    # Export data
    scraper.export_to_csv()
    scraper.export_to_json()
    
    # Display statistics
    stats = scraper.get_statistics()
    print("\n=== Scraping Statistics ===")
    for key, value in stats.items():
        print(f"{key.replace('_', ' ').title()}: {value}")


if __name__ == "__main__":
    main()
