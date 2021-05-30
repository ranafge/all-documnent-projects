import requests
from bs4 import BeautifulSoup

url = 'https://divar.ir/s/tehran/auto'
response = requests.get(url)
print(response)
print('\n')
print(response.text)
print('Finished')
