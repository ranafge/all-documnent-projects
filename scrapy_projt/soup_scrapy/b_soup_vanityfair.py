import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")
html = url.text
page = BeautifulSoup(html, 'html.parser')
match = page.find('div', {'class': 'article__chunks'})

page_list = [[k.get_text() for k in i.find_all('p')] for i in match]

for i in page_list[:-2]:
   for k in i:
     print(k + '\n')
