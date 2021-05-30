from bs4 import BeautifulSoup
import requests

count = 1
link = 'https://www.panafoto.com/categorias/'
data = requests.get(link).text

soup = BeautifulSoup(data, 'lxml')
test = soup.find_all('li', {'class': 'item product product-item'})
test = soup.find_all('div', {'class': 'result-content'}) # no ok
test = soup.find_all('id', {'class': 'instant-search-results-container'})# no ok
test = soup.find_all('div', {'id': 'algolia-right-container'})# no ok
test = soup.find_all('div', {'class': 'result-title text-ellipsis'})# no ok
test = soup.find_all('div', {'class': 'infos'})# no ok
test = soup.find_all('h3', {'class': 'result-title text-ellipsis'})# no ok
test = soup.select('div.price')# no ok
print(test)
print(len(test))

for  a in test:
    print(a.text)
    print(a.h3)
    print()
