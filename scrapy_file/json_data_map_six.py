import requests
from bs4 import BeautifulSoup
import json
import re
import random
from fake_useragent import UserAgent
ua = UserAgent()

url = 'https://www.usnewsdeserts.com/states/california/#1536357227283-a4a9d6e4-ccf9'

r = requests.get(url)
r.status_code == 200
post_url = 'https://public.tableau.com/vizql/w/TopOwnersCalifornia/v/Owners/sessions/7432358EAD6040C7BA9476D07DAC603B-0:0/commands/tabdoc/select'
prams = {"worksheet": "Income",
"dashboard": "Owners",
"selection": {"objectIds":[212],"selectionType":"tuples"},
"selectOptions": "select-options-simple",
"zoneId": "4",
"zoneSelectionType": "replace"}
prams = json.dumps(prams)
post_data = requests.post(post_url, prams=prams, headers={'User-Agent': ua.random})
print(post_data)
soup = BeautifulSoup(r.content, 'lxml')
print(soup.prettify())





