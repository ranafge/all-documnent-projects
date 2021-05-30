from bs4 import BeautifulSoup
import json
import re
import requests
from datetime import datetime, timedelta
# import js2xml
from datetime import datetime
base_url = 'https://eqmindexes.com/risk-parity-index-summary/'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')
all_scripts = soup.find_all('script')
script_7 = all_scripts[7].string
result = re.search(r"(?<=var data = )([^$]*);", script_7).group()[:-1]

result = json.loads(result)
for d in result:
    date = datetime.fromtimestamp(d[0]/1000)-timedelta(days=1)
    date = date.strftime('%A,%b %d, %Y ')
    print(f"{date}, {d[1]}")

