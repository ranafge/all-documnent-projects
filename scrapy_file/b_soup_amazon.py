#My CODE
import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.de/Neues-Apple-iPhone-Pro-128-GB/dp/B08L5SNWD2/ref=sr_1_1_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3UH87RWLLO40E&dchild=1&keywords=iphone+12+pro&qid=1605603669&sprefix=Iphone+12%2Caps%2C175&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzRjAxN0xWNTk0TVpYJmVuY3J5cHRlZElkPUEwNzE4ODIxMktCWlhJMVlHWDFNMyZlbmNyeXB0ZWRBZElkPUExMDMwODk2Tk5OVkdZRTJISDVMJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'lxml')
#I tried other parsing methods too: 'html.parser', 'html5lib'. Not helpful
title = soup.find(id="productTitle").get_text().strip()
price = soup.find(id='priceblock_ourprice').get_text().strip()[:5]
print(title) #returns correct string from the URL above
print(price)
