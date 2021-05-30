from bs4 import BeautifulSoup
import json
import re
import requests
import js2xml

base_url = 'https://www.tripadvisor.in/Restaurants-g494941-Indore_Indore_District_Madhya_Pradesh.html'

r = requests.get(base_url)
# print(r.status_code)
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
all_scripts = soup.find_all('script')

result=all_scripts[85]
print(result)
print('*'*10)
print(js2xml.parse(result))
