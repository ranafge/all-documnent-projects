import requests
from bs4 import BeautifulSoup
import re
keys = ['XLU', 'XLRE']
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"
}

def main(url):
    with requests.Session() as req:
        req.headers.update(headers)
        for key in keys:
            r = req.get(url.format(key))

            #
            symbols = re.findall(r'etf\\/(.*?)\\', r.text)
            print(symbols)
main("https://www.zacks.com/funds/etf/{}/holding")














