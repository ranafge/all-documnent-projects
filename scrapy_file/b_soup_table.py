import bs4
import requests
from bs4 import BeautifulSoup

r=requests.get('https://finance.yahoo.com/quote/SAS.ST/?guccounter=1')
soup=BeautifulSoup(r.text,"lxml")
headers = ["Previous Close","Bid","Ask","Day's Range","51 Week Range","Volume","Avg. Volume","Market Cap","Beta (5Y Monthly)","PE Ratio (TTM)","EPS (TTM)","Earnings Date","Forward Dividend & Yield","Ex-Dividend Date","1y Target Est"]
fmt_string = "{:<15} {:<15}{:<15}{:<15}{:<15}{:<15}"
print(fmt_string.format("Previous Close","Open","Bid","Ask","Volume","Avg.Volume","Volume", 'Market Cap', 'Beta'))
print('-' * 100)

for data in soup.find_all('table', class_='W(100%)'):
    for item in  data.find_all("span"):
        print(item.text , sep=' ')


