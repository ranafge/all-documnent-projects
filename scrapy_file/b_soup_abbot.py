from bs4 import BeautifulSoup
import requests

url = "http://www.stravaiging.com/history/castle/abbot-house-dunfermline"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')


mydiv = soup.find('div', {'class': 'c8'})

print(mydiv.find_all('p')[2].text)
print(mydiv.find_all('p')[2].text.split(':')[1])



