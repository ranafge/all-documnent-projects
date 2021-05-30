import requests
import bs4
import re
r = requests.get('https://www.elgiganten.dk/catalog/gaming/dk-gaming-laptop/gaming-laptop')
r.raise_for_status()

soup = bs4.BeautifulSoup(r.text, 'html.parser')
price = soup.select('div[class=product-price]')
name = soup.select('a[class=product-name]')
# print(name)
ausus = soup.select('a[class=product-name]')
for a in ausus.find(titile = re.compile('^A')):
    print(a)

print(ausus)
