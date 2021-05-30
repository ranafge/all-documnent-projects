import lxml
import scrapy
from scrapy.selector import Selector
from bs4 import BeautifulSoup
from bs4 import NavigableString

html = """<bookstore>
 <category>
  <book location="US">A1</book>
  <book location="FIN">A2</book>
 </category>
 <category>
  <book location="FIN">B1</book>
  <book location="US">B2</book>
 </category>

</bookstore> """

data = Selector(text=html)
print(data.get())
print(data.xpath("//category/book[@location='US']").getall())
