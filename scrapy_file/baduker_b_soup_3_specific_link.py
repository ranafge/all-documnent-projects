import requests
import csv
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as BS

my_protein_list = ["ArthCp002"]
for protein in my_protein_list:
    text = requests.get('https://www.genome.jp/dbget-bin/www_bget?ath:' + protein).text
    soup = BS(text,'html.parser')
    # print(soup.prettify())
    AGI = soup.find_all("a",href=True)
    for a in AGI:
        if 'Tair' in a.get('href'):
            print(a.get('href'))

