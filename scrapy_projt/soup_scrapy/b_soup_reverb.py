import requests
from bs4 import BeautifulSoup as Soup

url = 'https://reverb.com/marketplace?query=jackson+guitars'

response = requests.get(url)
soup = Soup(response.text, 'html.parser')
# for item in soup.select('h3.csp-square-card__title.csp-square-card__title--limit-height'):
#     print(item)
for item in soup.select('li.tiles__tile'):
    print(item)
# for item in soup.select('h3.csp-square-card__title.csp-square-card__title--limit-height'):
#     print(item)
# for item in soup.find_all('h4', class_='grid-card__title'):
#     print(item.text)
