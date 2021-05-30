import requests
from bs4 import BeautifulSoup

BASE = 'https://kith.com/collections/mens-footwear-sneakers'

content = requests.get(BASE)

soup = BeautifulSoup(content.text, 'html.parser')

# for i in soup.find_all('div', {'class':'product-card__information'}):
#     print('https://kith.com' + i.a['href'])

# print(soup.prettify())
out = soup.find_all('div', {'class':'product-card__information'})[0]
print(out.a['href'])
