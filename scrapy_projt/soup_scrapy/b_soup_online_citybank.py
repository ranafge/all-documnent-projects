from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import requests
x = 'https://www.online.citibank.co.in/credit-card/rewards/citi-rewards-credit-card?eOfferCode=INCCCCTWAFCTRELM'
# wb = webdriver.Chrome()
# wb.get(x)
headers = {
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'Referer': '',
    'Origin': 'https://www.online.citibank.co.in',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
}

params = (
    ('_bust', '2021-01-21T05-05-29-195Z'),
)

import requests

headers = {
    'Connection': 'keep-alive',
    'Content-Length': '1822',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Origin': 'https://www.online.citibank.co.in',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Language': 'en-US,en;q=0.9',
}

session = requests.Session()
session.headers.update(headers)
r = session.post('https://684d0d3b.akstat.io/', params=params)

r = session.get(x)


print(r.status_code)

soup = BeautifulSoup(r.content, 'lxml')

print(soup.find('div', class_ = "m-top-sm block-hero-art-2 display-image"))
print(soup.find('div', class_ = "m-top-sm block-hero-art-2 display-image").find('img').get('src'))
