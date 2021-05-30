import lxml
import scrapy
from scrapy.selector import Selector
from bs4 import BeautifulSoup
from bs4 import NavigableString

html = """<div class="atag btag" />"""

data = Selector(text=html)
print(data.get())
print(data.xpath('//*[@class="atag"]'))
print(data.xpath('//*[starts-with(@class, "atag")]'))
print(data.xpath('//*[contains(@class, "atag") and contains(@class, "btag")]'))
