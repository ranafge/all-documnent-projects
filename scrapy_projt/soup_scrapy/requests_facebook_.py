import requests
from bs4 import BeautifulSoup

import requests

headers = {
    'authority': 'www.papara.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '__cfruid=64370d0d06d80a1e1a701ae8bee5a4b85c1de1af-1610296629',
}

response = requests.get('https://www.papara.com/', headers=headers)

print(response.status_code)
print(response.text)
