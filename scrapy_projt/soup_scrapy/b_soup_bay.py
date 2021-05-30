from bs4 import BeautifulSoup
import requests
import csv


my_url ="https://www.thebay.com/product/fjallraven-classic-kanken-backpack-0600090077437.html?&site_refer=CSE_GGLPLA:GSE+-+Shopping+-+Now+On+Sale:5-20%25+Discount&gclid=CjwKCAiAjeSABhAPEiwAqfxURbzZMRhc-ZJ4Cd-Ofa5uKGy8BMGJqOXWY30mjqIyMYCnEwGIqgazQxoCk_oQAvD_BwE&gclsrc=aw.ds"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
   }
r = requests.get(my_url, headers=headers)
print(r.status_code)
soup = BeautifulSoup(r.content, 'lxml')

all = soup.find("span",{"class":"value bfx-price"}).find('span', {'class': 'formatted_sale_price'})
print(all.text)


