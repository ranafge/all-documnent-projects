import requests
from bs4 import BeautifulSoup
import time
import json
import pandas as pd
import numpy as np
import time
import os
import sys
from time import sleep
from random import randint

import pandas as pd
import requests
from bs4 import BeautifulSoup
from googletrans import Translator


traslator = Translator()
partynames = []


for page in range(11, 12):
    page = requests.get("https://www.cvk.gov.ua/pls/vnd2019/wp304pt001f01=919pf7331=" + str(page) + ".html",
                        verify=False)
    page.encoding = page.apparent_encoding

    soup = BeautifulSoup(page.text, 'html.parser')
    ukraine_tr = soup.find_all('tr')
    sleep(randint(2, 10))

    for container in ukraine_tr:
        partyn = container.find('a', class_='a2')
        if partyn is not None:
            name = traslator.translate(partyn.get_text()).text
        else:
            name = "N/A"
        partynames.append(name)

ukraine = pd.DataFrame({
    'pty_n': partynames
})

ukraine.to_csv('ukraine.csv')









