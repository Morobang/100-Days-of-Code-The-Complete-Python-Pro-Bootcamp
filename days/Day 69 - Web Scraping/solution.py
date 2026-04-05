# Day 69 — Web Scraping — SOLUTIONS
from bs4 import BeautifulSoup
import requests, re, time

def get_soup(url):
    try:
        r=requests.get(url,headers={'User-Agent':'Mozilla/5.0'},timeout=10)
        r.raise_for_status(); return BeautifulSoup(r.text,'html.parser')
    except Exception: return None

def extract_links(html,base_url=''):
    soup=BeautifulSoup(html,'html.parser')
    links=[]
    for a in soup.find_all('a',href=True):
        href=a['href']
        if href.startswith('http'): links.append(href)
        elif href.startswith('/') and base_url: links.append(base_url.rstrip('/')+href)
    return links

def scrape_table(html):
    soup=BeautifulSoup(html,'html.parser'); table=soup.find('table')
    if not table: return []
    headers=[th.get_text(strip=True) for th in table.find_all('th')]
    rows=[]
    for tr in table.find_all('tr')[1:]:
        tds=[td.get_text(strip=True) for td in tr.find_all('td')]
        if tds: rows.append(dict(zip(headers,tds)))
    return rows

def clean_text(html):
    soup=BeautifulSoup(html,'html.parser')
    return re.sub(r'\s+',' ',soup.get_text()).strip()

def polite_scraper(urls,delay=1):
    results=[]
    for url in urls:
        results.append((url,get_soup(url)))
        time.sleep(delay)
    return results
