from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
import requests

headers={
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
}
def scrape(url):
    with requests.Session() as req:
        req.headers.update(headers)
        r = req.get(url).text
        soup = bs(r, 'lxml')
        info = soup.find_all('td', {'class': 'first'})
        res = [[b.text, b.a['href']] for b in info]
  
        print(res)


url =  'https://www.muddywatersresearch.com/research/'
scrape(url)
