from bs4 import BeautifulSoup
import requests

name = '1QB Information technologies HQ'
province = 'BC'

url = 'https://www.yellowpages.ca/search/si/1/' + name + '/' + province
url = url
print(url)
print('https://www.yellowpages.ca/search/si/1/1QB+Information+technologies+HQ/British+Columbia+BC')
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
address = soup.find_all('span', {'class': 'jsMapBubbleAddress'})
# https://www.yellowpages.ca/search/si/1/1QB Information technologies HQ/BC
# print(address.text)
print(address)
print([d.text for d in address if d.text == '7-3318 Oak St'])
