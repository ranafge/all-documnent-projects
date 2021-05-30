import requests
import json
from bs4 import BeautifulSoup

url = 'https://preply.com/en/skype/english-tutoring-jobs'

r= requests.get(url)
print(r.status_code)

soup = BeautifulSoup(r.content, 'html.parser')

script = soup.find_all('script')[6].string

data = json.loads(script)

for urls in data['itemListElement']:
    print(urls['url'])
    print(urls['name'])
    print(urls['position'])
