# Day 69 — Web Scraping

## Key syntax
```python
from bs4 import BeautifulSoup
import requests

r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(r.text, 'html.parser')

# CSS selectors
soup.select('div.class')           # class selector
soup.select('table tr td')         # nested
soup.select_one('h1')              # first match
soup.find('tag', {'attr':'val'})   # find by attr
soup.find_all('a', href=True)      # all links

# Extract data
tag.text                           # visible text
tag.get_text(strip=True)           # strip whitespace
tag['href']                        # attribute value
tag.get('href', '')                # safe attribute
```

## Be respectful
- Check `robots.txt` before scraping
- Add delays between requests (`time.sleep`)
- Set a descriptive User-Agent
- Don't scrape what you shouldn't

## Gotchas
- Dynamic content (JavaScript) → BeautifulSoup won't see it — use Playwright/Selenium
- Always decode bytes: `r.content.decode('utf-8')` if encoding issues
- `soup.get_text()` includes all nested text — use `.strings` for finer control
