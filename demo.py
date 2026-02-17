"""
Web Scraper Demo - With Sample Data
Demonstrates the scraper functionality using simulated data
"""

from quote_scraper import QuoteScraper
from datetime import datetime


def demo_with_sample_data():
    """Run a demo of the scraper using sample data"""
    
    # Create scraper instance
    scraper = QuoteScraper()
    
    # Add sample data (simulating what would be scraped)
    sample_quotes = [
        {
            'text': '"The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking."',
            'author': 'Albert Einstein',
            'tags': ['change', 'deep-thoughts', 'thinking', 'world'],
            'scraped_at': datetime.now().isoformat()
        },
        {
            'text': '"It is our choices, Harry, that show what we truly are, far more than our abilities."',
            'author': 'J.K. Rowling',
            'tags': ['abilities', 'choices'],
            'scraped_at': datetime.now().isoformat()
        },
        {
            'text': '"There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle."',
            'author': 'Albert Einstein',
            'tags': ['inspirational', 'life', 'live', 'miracle', 'miracles'],
            'scraped_at': datetime.now().isoformat()
        },
        {
            'text': '"The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid."',
            'author': 'Jane Austen',
            'tags': ['aliteracy', 'books', 'classic', 'humor'],
            'scraped_at': datetime.now().isoformat()
        },
        {
            'text': '"Imperfection is beauty, madness is genius and it\'s better to be absolutely ridiculous than absolutely boring."',
            'author': 'Marilyn Monroe',
            'tags': ['be-yourself', 'inspirational'],
            'scraped_at': datetime.now().isoformat()
        },
        {
            'text': '"Try not to become a man of success. Rather become a man of value."',
            'author': 'Albert Einstein',
            'tags': ['adulthood', 'success', 'value'],
            'scraped_at': datetime.now().isoformat()
        },
        {
            'text': '"It is better to be hated for what you are than to be loved for what you are not."',
            'author': 'André Gide',
            'tags': ['life', 'love'],
            'scraped_at': datetime.now().isoformat()
        },
        {
            'text': '"I have not failed. I\'ve just found 10,000 ways that won\'t work."',
            'author': 'Thomas A. Edison',
            'tags': ['edison', 'failure', 'inspirational', 'paraphrased'],
            'scraped_at': datetime.now().isoformat()
        },
        {
            'text': '"A woman is like a tea bag; you never know how strong it is until it\'s in hot water."',
            'author': 'Eleanor Roosevelt',
            'tags': ['misattributed-eleanor-roosevelt'],
            'scraped_at': datetime.now().isoformat()
        },
        {
            'text': '"A day without sunshine is like, you know, night."',
            'author': 'Steve Martin',
            'tags': ['humor', 'obvious', 'simile'],
            'scraped_at': datetime.now().isoformat()
        }
    ]
    
    print("=== WEB SCRAPER DEMO ===")
    print("(Using sample data - in production, this would scrape from the web)\n")
    
    # Add sample data to scraper
    scraper.quotes = sample_quotes
    print(f"Loaded {len(sample_quotes)} sample quotes\n")
    
    # Export data
    print("Exporting data...")
    scraper.export_to_csv("demo_quotes.csv")
    scraper.export_to_json("demo_quotes.json")
    
    # Display statistics
    stats = scraper.get_statistics()
    print("\n=== Scraping Statistics ===")
    for key, value in stats.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    print("\n✅ Demo completed successfully!")
    print("Check the output files to see the exported data.")


if __name__ == "__main__":
    demo_with_sample_data()
