from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://webcivic.com/wp/'
url2= 'https://linkin-enc.com/'

response = requests.get(url2)

print(response.status_code)
soup = BeautifulSoup(response.text, 'lxml')

images = soup.find_all('img')
image_list = []
for image in images:
    image_list.append(image.get('src'))

for image in image_list:
    print(image)
