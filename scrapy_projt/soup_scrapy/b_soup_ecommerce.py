import requests
from bs4 import BeautifulSoup
headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

link = 'https://www.elcorteingles.es/deportes/search/?s=dunk'

s = requests.session()

response = s.get(link, headers=headers, timeout=4)
print(response.status_code)
soup = BeautifulSoup(response.content, 'html.parser')
iframe_src = soup.select_one("#sec-text-if").attrs['src']
print(iframe_src)
response = s.get(iframe_src, headers=headers, timeout=4)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify())
