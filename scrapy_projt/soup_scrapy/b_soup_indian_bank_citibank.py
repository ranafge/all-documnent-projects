from urllib.request import urlopen
from bs4 import BeautifulSoup
import json,requests

details = []

url = ['https://www.online.citibank.co.in/credit-card/rewards/citi-rewards-credit-card?eOfferCode=INCCCCTWAFCTRELM']
html = requests.get(url[0])
print(html.status_code)
soup = BeautifulSoup(html.content, 'lxml')
x = soup.select('span.m-bottom-0')

addr= soup.select('span.m-bottom-0')[12:20] # number of span
for d in addr:
    print(d.get_text())

addr= soup.select('span.m-bottom-0')[58:70]
for d in addr:
    print(d.get_text()) # get_text() method for inner tag text
