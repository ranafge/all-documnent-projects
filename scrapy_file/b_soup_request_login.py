from bs4 import BeautifulSoup
import requests

url = 'https://www.fool.com/premium/stock-advisor/coverage/tags/buy-recommendation'

payload = {'username': 'xxx@gmail.com', 'password': 'xxx'}
res = requests.post(url, data=payload)
soup = BeautifulSoup(res.text, 'html.parser')
link = soup.findAll("h3", {"class": "content-item-headline"})
print(link)
