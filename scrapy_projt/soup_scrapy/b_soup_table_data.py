import requests
from bs4 import BeautifulSoup
import csv
import re
import pandas as pd

url = "https://www.kpaa.or.kr/kpaa/eng/list.do?"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

data_list = [td.getText(strip=True, separator=',').split(',') for td in  soup.find('div', {'class':'cont_box2'}).find_all('tr')[:-1]]

df = pd.DataFrame(data_list)

df.to_excel('x.xlsx')
