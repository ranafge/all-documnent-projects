from bs4 import BeautifulSoup
import requests
url = 'https://remittanceprices.worldbank.org/en/corridor/Australia/China'
r = requests.get(url,verify=False)
soup = BeautifulSoup(r.text,'lxml')
rows = [i.get_text("|").split("|") for i in soup.select('#tab-1 .corridor-row')]
for row in rows:
    #a,b,c,d,e = row[2],row[15],row[18],row[21],row[25]
    #print(a,b,c,d,e,sep='|')
    print('{0[2]}|{0[15]}|{0[18]}|{0[21]}|{0[25]}'.format(row))
