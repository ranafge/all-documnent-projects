import bs4
from bs4 import BeautifulSoup

soup = bs4.BeautifulSoup("<td id='1'>This is text</td>", 'lxml')
td = soup.find(attrs={'id': '1'})
print(td)
