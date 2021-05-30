import re
from bs4 import BeautifulSoup
html= """<div style="text-align: center;">
            <img src="https://documents.google.com/" alt="" width="60" height="30" />
            <br />
            Pick me please.

        <p> Do not pick me please! </p>

        <br />
        <br />
    </div>"""

soup = BeautifulSoup(html, 'lxml')
print(soup.find(text=re.compile("Pick me please.")).strip())



