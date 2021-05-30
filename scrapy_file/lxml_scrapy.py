import requests
from lxml import etree
from bs4 import BeautifulSoup
import lxml
url = "https://www.curseforge.com/minecraft/mc-mods/ae2-extras/files/3120250"

from lxml import html
import requests
import cloudscraper

scraper = cloudscraper.create_scraper()
page = scraper.get(url).text

doc = html.fromstring(page)
divs = doc.xpath("//div[@class='w-full flex justify-between']")
el = divs[0].text_content()
projectID = el.split()[-1]
print(projectID)

