import requests
from bs4 import BeautifulSoup
import re
cookie_url = "https://www.unilevernotices.com/cookie-notice/notice.html"
response = requests.get(cookie_url)
soup = BeautifulSoup(response.content, 'html.parser')

market = soup.findAll('div', class_=re.compile('richText-content'))

market_linkd = soup.findAll('a', text=re.compile(("Spain - Spanish"),re.IGNORECASE))
print(" extracted remaining country data ", market_linkd)   # result works fine
print('xxxxxxxxxxxxxxx')
market_linkd = soup.findAll('a', title=re.compile("South Africa - English  "), href=True) #.replace('<br>','')
print(" South aftrica data ", market_linkd)  # result []
for link in market_linkd:
    print()
    print(link.text)
    print(link.get('href'))
print('xxxxxxxxxxxx')
for ml in market_linkd:
    print("*********************", ml)
    response = requests.get('https://www.unilevernotices.com'+ml['href'])
    soup = BeautifulSoup(response.content, "html.parser")
    cookie_title = soup.find('h1', class_=re.compile('title-heading'))
    cookie_link = 'https://www.unilevernotices.com'+ml['href']
    print(cookie_link)
    print(cookie_title)
