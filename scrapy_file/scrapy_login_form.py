import time
import scrapy
from scrapy.http import FormRequest
from bs4 import BeautifulSoup
import urllib

html_atag = """<html><body><div class = "article">
  <div class = "news">
    <p>text 1</p>
    <p>text 2</p>
    <p>text 3</p>
    <p>text 4</p>
    <p>text 5</p>
    <p>text 6</p>
  </div>
</div>
</body>
</html>"""
soup = BeautifulSoup(html_atag, 'lxml')

p = soup.find("div",{'class':'news'}).findAll('p')[1:3]

for i in p:
    print(i.text)


