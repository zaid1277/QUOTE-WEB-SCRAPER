# Quote Web Scraper

A clean, professional web scraper built with Python that extracts quotes from [quotes.toscrape.com](http://quotes.toscrape.com) and exports them in multiple formats.

## Features

- 🔍 **Automatic Pagination**: Scrapes multiple pages automatically
- 📊 **Multiple Export Formats**: Exports data to both CSV and JSON
- 🛡️ **Error Handling**: Robust error handling for network issues
- 📈 **Statistics**: Generates insights about scraped data
- ⏱️ **Rate Limiting**: Respectful delays between requests
- 🎯 **Clean Code**: Well-structured, documented, and following best practices

## Technologies Used

- **Python 3.x**
- **BeautifulSoup4**: HTML parsing
- **Requests**: HTTP requests
- **CSV & JSON**: Data export formats

## Installation

1. Clone or download this repository
2. Install required dependencies:

```bash
pip install requests beautifulsoup4
```

## Usage

Run the scraper:

```bash
python quote_scraper.py
```

The scraper will:
1. Scrape 3 pages of quotes (configurable)
2. Export data to `quotes.csv` and `quotes.json`
3. Display statistics about the scraped data

### Customization

You can modify the scraper behavior in the `main()` function:

```python
# Change number of pages to scrape
scraper.scrape_all(max_pages=5, delay=1.0)

# Change output filenames
scraper.export_to_csv("my_quotes.csv")
scraper.export_to_json("my_quotes.json")
```

## Code Structure

```
quote_scraper.py
├── QuoteScraper (class)
│   ├── __init__()          # Initialize scraper
│   ├── scrape_page()       # Scrape single page
│   ├── scrape_all()        # Scrape multiple pages
│   ├── export_to_csv()     # Export to CSV
│   ├── export_to_json()    # Export to JSON
│   └── get_statistics()    # Get data statistics
└── main()                  # Entry point
```

## Example Output

### Console Output
```
Starting to scrape 3 pages...
Scraping page 1...
Found 10 quotes on page 1
Scraping page 2...
Found 10 quotes on page 2
Scraping page 3...
Found 10 quotes on page 3

Total quotes scraped: 30
Exported 30 quotes to quotes.csv
Exported 30 quotes to quotes.json

=== Scraping Statistics ===
Total Quotes: 30
Unique Authors: 15
Most Common Author: Albert Einstein
Unique Tags: 25
Most Common Tag: inspirational
```

### CSV Output
```csv
text,author,tags,scraped_at
"The world as we have...",Albert Einstein,"change, deep-thoughts, thinking",2024-02-16T10:30:00
```

### JSON Output
```json
[
  {
    "text": "The world as we have created it...",
    "author": "Albert Einstein",
    "tags": ["change", "deep-thoughts", "thinking"],
    "scraped_at": "2024-02-16T10:30:00"
  }
]
```

## Best Practices Demonstrated

✅ **Object-Oriented Design**: Clean class structure
✅ **Type Hints**: Function signatures include type annotations
✅ **Error Handling**: Try-catch blocks for network errors
✅ **Documentation**: Comprehensive docstrings
✅ **Respectful Scraping**: Rate limiting with delays
✅ **Data Validation**: Checks for empty data
✅ **Multiple Formats**: CSV and JSON export options

## Legal & Ethical Considerations

- This scraper uses [quotes.toscrape.com](http://quotes.toscrape.com), a site specifically designed for practicing web scraping
- Always respect `robots.txt` when scraping real websites
- Include rate limiting to avoid overwhelming servers
- Only scrape publicly available data
- Check the website's Terms of Service before scraping

## Future Enhancements

- Add support for more websites
- Implement database storage
- Add command-line arguments
- Create data visualization
- Add unit tests

## License

This is a learning project and is free to use and modify.

## Author

[Your Name]
- GitHub: [Your GitHub]
- LinkedIn: [Your LinkedIn]

---

**Note**: This project demonstrates fundamental web scraping skills including HTTP requests, HTML parsing, data extraction, and file I/O operations.
