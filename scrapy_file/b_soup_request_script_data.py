from bs4 import BeautifulSoup
import requests
import re

url = 'https://bitinfocharts.com/comparison/bitcoin-transactions.html'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml').find_all('script')[4].string
# print(soup)
res = re.search(r'd = new Dygraph\(document.getElementById\(\"container\"\)\,(.*)ylabel',soup).groups(1)
script_4_data = res[0].split('{labels:')[0]

script_4_data = script_4_data[0:len(script_4_data)-2] # str type.
print(script_4_data) # list

# second step script 5

soup = BeautifulSoup(requests.get(url).text, 'lxml').find_all('script')[3].string
data = soup.split('{return',1)
# print(data)
bitcoin_data = data[1].split(';}var',1)[0]  # ok

print(bitcoin_data)
