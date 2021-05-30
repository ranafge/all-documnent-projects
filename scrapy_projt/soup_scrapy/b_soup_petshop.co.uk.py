from bs4 import BeautifulSoup
import requests
url = "https://www.petshop.co.uk/Dog"
r = requests.get(url)
print(r.status_code)
soup = BeautifulSoup(r.content,  'lxml')
alldata = []
for old_price in soup.find_all("div", {"class": "product-views-price"}):
    data = [price.getText(strip=True) for price in old_price.find_all('span',{'class':'product-views-price-lead'})]
    alldata.append(data[0])
print(alldata)
