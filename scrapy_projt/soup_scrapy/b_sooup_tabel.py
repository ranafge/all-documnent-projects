import csv
import requests
from bs4 import BeautifulSoup

url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

soup = BeautifulSoup(html, 'lxml')
table = soup.find('tbody', attrs={'class': 'stripe'})

total_items = [row.text.strip().split()[:-1] for row in table.find_all('tr')[:-1] ]

outfile = open("inmates.csv", "w")
writer = csv.writer(outfile)

writer.writerow(["Last", "First", "Middle", "Gender", "Race", "Age", "City", "State"])
for row in total_items:
    writer.writerow(row)
