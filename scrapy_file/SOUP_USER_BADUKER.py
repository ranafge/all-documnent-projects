from bs4 import BeautifulSoup
import requests
from scrapy.selector import Selector

html = """<div class="Item-Details">
    <p class="Product-title">
        <a href="/link_i_need">
            text here that i need to grab
            more text here that i would like to grab
        </a>
    </p>"""

soup = BeautifulSoup(html, 'lxml')

for div in soup.findAll('p', {'class': 'Product-title'}):
    print(div.find('a')['href'])
    print(div.find('a').getText(strip=True))

