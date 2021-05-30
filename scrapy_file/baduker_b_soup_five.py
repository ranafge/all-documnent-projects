from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests
site = "http://www.voltwo.webd.pl/1-indexy/index-5-opracowania/01-maturalne-KINEMATYKA.html"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = requests.get(site).text
print(req)

soup = BeautifulSoup(req, "lxml").find_all('td')

print(soup)
print([a.find('a')['href'] for a in soup if a.find('a') and '.pdf' in a.find('a')['href']])
