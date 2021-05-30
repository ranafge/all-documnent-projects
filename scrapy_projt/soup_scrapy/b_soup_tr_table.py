from bs4 import BeautifulSoup
import requests

url = 'https://www.yugiohcardguide.com/archetype/abyss-actor.html'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

print([t for sub in tr.find_all('tr') in soup.find('tbody').find_all('tr') for t in sub])
