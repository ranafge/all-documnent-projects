from bs4 import BeautifulSoup
import requests
import re
url = 'https://www.sec.gov/Archives/edgar/data/1321502/000143774910004615/andain_10k-123106.htm'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
# print(soup.prettify())
# soup = BeautifulSoup(page.text.replace("\xa0"," "), 'html.parser')
res = soup.find_all(text=re.compile("\w+(.+)RISK FACTORS?", re.IGNORECASE))
print(res[0].replace('\xa0', ''))
<div style="text-align: center;">
            <img src="https://documents.google.com/" alt="" width="60" height="30" />
            <br />
            Pick me please.

        <p> Do not pick me please! </p>

        <br />
        <br />
    </div>
