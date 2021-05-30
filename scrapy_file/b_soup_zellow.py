import requests as s
from bs4 import BeautifulSoup

req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

all_data = []

url = 'https://www.zillow.com/austin-tx/home-values/:formatted/'
r = s.get(url, headers=req_headers)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())
print(soup.find('li.legend-value'))

for ul in soup.find_all('ul'):
    lis=ul.find_all('li')
    for elem in lis:
        all_data.append(elem.text.strip())

print(all_data)
