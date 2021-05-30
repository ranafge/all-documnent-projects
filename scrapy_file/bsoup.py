import requests
from bs4 import BeautifulSoup
import json
import re

URL="https://www.bankmega.com/en/about-us/bank-mega-network/"

r = requests.get(URL)
soup = BeautifulSoup(r.content, 'lxml')

for element in soup.find_all('script',type="text/javascript"):
    print(element.get_text)

    if "$('#table_data_atm').hide();" in element.get_text:
        print('yes', end='\n\n')
        print("-"*10)
    #     string_raw = element.get_text()
    #     first_bracket_open = string_raw.find("[")
    #     first_bracket_close = string_raw.find("]")
    #     cleaned_string = string_raw[first_bracket_open:first_bracket_close+1].replace('city:', '"city":').replace('lokasi:', '"lokasi":').replace('alamat:', '"alamat":').replace("\n", "")
    #     cleaned_string = re.sub("\s\s+", " ", cleaned_string)
    #     cleaned_string = cleaned_string.replace(", },", "},").replace(", ]", "]").replace("\t", " ")
    #     parsed = json.loads(cleaned_string)
    #     print(parsed)