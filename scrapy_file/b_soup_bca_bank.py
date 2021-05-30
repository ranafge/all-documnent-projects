import requests
from bs4 import BeautifulSoup
import pandas as pd
url="https://www.bca.co.id/webapi/webapilocation?status=3&locationtype=Branch&type=All&lat=-6.1967113&lng=106.8227216&distance=2000"

payload = {
    "status": "3",
    "locationtype": "Branch",
    "type": "All",
    "lat": "-6.1967113",
    "lng":"106.8227216",
    "distance":"2000"
}

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}

response = requests.get(url, data=payload, headers=headers,verify = False)
import json
result = json.loads(response.text)
result1=pd.DataFrame(result)
result1.to_csv("x.csv")
