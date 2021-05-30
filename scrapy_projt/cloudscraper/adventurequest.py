import cloudscraper
import cloudscraper
from bs4 import BeautifulSoup as soup


url = "http://adventurequest.life/"
import cfscrape

scraper = cfscrape.create_scraper()
html = scraper.get(url).content
page_soup = soup(html, "html.parser")
print(page_soup)
