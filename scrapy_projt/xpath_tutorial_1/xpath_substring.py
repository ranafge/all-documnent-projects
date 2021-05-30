from scrapy.selector import Selector
from bs4 import BeautifulSoup
import requests

html ="""<container>
  <type>01</type>
  <text>one</text>
</container>
<container>
  <type>02</type>
  <text>two</text>
</container>"""

data = Selector(text=html)
# print(data.xpath('//container/following-sibling::container').get())
print(data.xpath('concat(substring(//container[type/text() = "02"]/text,1,string-length(//container[type/text()="02"])*boolean(//container[type/text()="02"]/text())),substring(//container[type/text() = "01"]/text,1,string-length(//container[type/text()="01"])*number(boolean(//container[type/text()="01"]/text())and not(boolean(//container[type/text()="02"]/text())))))').get())
