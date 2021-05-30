import lxml
import scrapy
from scrapy.selector import Selector
from bs4 import BeautifulSoup
from bs4 import NavigableString

html = "<p>Whatever you want type <strong>here is great</strong></p>"

data = Selector(text=html)
# print(data.get())
# print(data.xpath('//node/text()[1]'))
# print(data.xpath('//node/text()[2]').get())
# print(data.xpath('//node/text()[position()=1]'))
print(data.get())
print(data.xpath("string(//p/text())").getall())
