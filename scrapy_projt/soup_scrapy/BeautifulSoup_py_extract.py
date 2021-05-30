import requests
from bs4 import BeautifulSoup

URL = 'https://dsd.tools/app.riot'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find("div", {"class": "content"})
for data in title:
    print(data.text)

