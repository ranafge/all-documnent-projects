from bs4 import BeautifulSoup
import requests

url = "https://finance.yahoo.com/quote/fb?p=FB"

content = requests.get(url).text

soup = BeautifulSoup(content, 'lxml')

output = soup.find('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span')
print(output)
print(output.text)


