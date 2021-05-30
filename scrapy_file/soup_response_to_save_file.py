import requests

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
}

url = "https://www.uob.co.id/wsm/stayinformed.do?path=lokasicabangatm"

response = requests.get(url, headers=headers).text

with open('response_data.csv', 'w') as f:
    f.write(response)