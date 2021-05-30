from bs4 import BeautifulSoup
import requests

import json

url = 'https://footballapi.pulselive.com/football/stats/ranked/teams/wins?page=0&pageSize=20&compSeasons=79&comps=1&altIds=true'

headers = {
    "Host": "footballapi.pulselive.com",
"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
"Accept": "*/*",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate, br",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"Origin": "https://www.premierleague.com",
"Connection": "keep-alive",
"Referer": "https://www.premierleague.com/stats/top/clubs/wins?se=79",
"If-None-Match": "083bcdbc679be42363d2eaefe7e90df5b",
"TE": "Trailers",


}

results = requests.get(url, headers=headers).json()

for data in results['stats']['content']:
    print(data['owner']['name'], data['value'])



