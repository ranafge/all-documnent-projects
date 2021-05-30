import pandas
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
url = 'https://www.realtor.com/realestateandhomes-search/Orlando_FL/dom-1'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
linklist = []
urls = soup.find_all('div', class_ = 'jsx-4195823209 photo-wrap')
for url in urls:
    for link in url.find_all('a', href=True):
        linklist.append('https://www.realtor.com' + link['href'])
#print(linklist)

testurl = 'https://www.realtor.com/realestateandhomes-detail/127-W-Wallace-St_Orlando_FL_32809_M62756-65861'

r = requests.get(testurl, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
address = soup.find('div', class_='jsx-1959108432 address-section').h1.text
print(address)
name = soup.find('a', class_ = 'jsx-725757796 agent-name').text.strip()
print(name)
