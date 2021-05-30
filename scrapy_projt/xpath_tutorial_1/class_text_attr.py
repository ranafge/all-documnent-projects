from scrapy.selector import Selector
from bs4 import BeautifulSoup
html = """<a href = "www.example1.com" class = "example-class" Example Text 1 />
<a href = "www.example2.com" class = "example-class" Example Text 2 />
<a href = "www.example3.com" class = "example-class" Example Text 3 />"""

data = Selector(text=html)
# print(data.xpath("descendant-or-self::a[@class and contains(concat(' ', normalize-space(@class), ' '), ' example-class ')]").extract())

p = [r.re(r"Example Text \d") for r in data.css('a')]
print(p)
import re
print(re.findall(r"Example Text \d", html))


