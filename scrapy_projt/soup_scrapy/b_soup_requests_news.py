import requests as rq
from bs4 import BeautifulSoup as bs

url = "https://news.guidants.com/#Ticker/Profil/?i=133962&e=74"

response = rq.get(url)
soup = bs(response.text, "lxml")
print(soup.find_all(text=True))
price = soup.find_all("span", {"class":"quote quote_standard"})

print(price)
10.0000
