import requests
from bs4 import BeautifulSoup

source = requests.get('https://www.svpboston.com/').text

soup = BeautifulSoup(source, features="html.parser")

title = soup.find("meta", property="og:title")

print(title["content"] if title else "No meta title given")

