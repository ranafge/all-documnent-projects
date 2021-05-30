
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

page=urlopen('https://catalog.data.gov/dataset')
soup=BeautifulSoup(page,'lxml')

dataset_number=soup.select('div .new-results')
result = re.findall('<!--(.*)-->', str(dataset_number))
print(result)
