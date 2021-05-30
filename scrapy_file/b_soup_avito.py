from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen, Request
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
reg_url = 'https://www.avito.ru/rossiya/avtomobili?cd=1'
req = requests.get(reg_url, headers=headers, stream=True)
soup = BeautifulSoup(req.content, 'lxml')

print(soup.find('div', "index-content-2lnSO"))
