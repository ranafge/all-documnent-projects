import requests
from bs4 import BeautifulSoup
from PIL import Image

url ="https://www.nike.com/gb/w/new-mens-shoes-3n82yznik1zy7ok"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

images = soup.find_all('img', {'class':'css-1fxh5tw product-card__hero-image'},src=True)
count = 1
for i in images:
    if 'data:image' not in i['src']:
        image_url = i['src']
        print(image_url)
        name = image_url.split('/')[-1].split('.')[0]

        img = Image.open(requests.get(image_url, stream=True).raw)
        img.save(f'{name}.jpg')




