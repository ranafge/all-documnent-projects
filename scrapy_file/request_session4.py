from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
import requests
import json
headers={
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
}
def scrape(url):
    with requests.Session() as req:
        req.headers.update(headers)
        r = req.get(url)
        mydata =r.json()
        for data in mydata['data']['list']:
            print(data, sep='*')

url =  'https://xueqiu.com/service/v5/stock/screener/quote/list?page=1&size=30&order=desc&orderby=percent&order_by=percent&market=CN&type=sh_sz&_=1606221698728'
scrape(url)
