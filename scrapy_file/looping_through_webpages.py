import requests
from requests import get
from bs4 import BeautifulSoup
import numpy as np
from time import sleep
from random import randint

headers = {"Accept-Language": "en-US, en;q=0.5"}

pages = range(1,6)

for page in pages:

    page = requests.get("https://www.myhome.ie/rentals/ireland/property-to-rent?page=" + str(page), headers=headers)

    soup = BeautifulSoup(page.text, "html.parser")

    rent_div = soup.find_all('div', class_='PropertyListingCard__Content MhHelper__Flex--spaced')

    sleep(randint(5,10))

rent = []

for container in rent_div:
    name = container.find('div', class_='PropertyListingCard__Price').text
    rent.append(name)

print(len(rent))
