from bs4 import BeautifulSoup
import requests

headers = {"User-Agent": 'UserAgent'}

URL = 'https://www.centrepointstores.com/sa/en/Women/Fashion-Accessories/Watches/CENTREPOINT-Citizen-Women%27s-Rose-Gold-Analog-Metal-Strap-Watch-EU-6039-86A/p/EU603986AGold'

page = requests.get(URL, headers=headers)
# print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.text)
# title = soup.find(id="product-details-name").text
# price = soup.find(id="products-details-price-current-01").text
#
# print (title)
# print (price)
