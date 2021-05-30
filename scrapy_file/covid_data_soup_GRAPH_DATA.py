from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from bs4 import BeautifulSoup
from datetime import datetime
import locale
import requests

locale.setlocale( locale.LC_ALL, '' )

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

url = "https://www.zillow.com/austin-tx/home-values/"
api_url = "https://www.zillow.com/ajax/homevalues/data/timeseries.json?r=10221&m=zhvi_plus_forecast&dt=111"


graph = requests.get(api_url, headers=headers).json()
print(graph['10221;zhvi_plus_forecast;111']['data'][0])
for v in graph['10221;zhvi_plus_forecast;111']['data']:
    print(datetime.fromtimestamp(v['x']//1000).date())
    print('$'+"{:,}K".format(float(v['y'])/1000))
    print(locale.currency(v['y'], grouping=True))





