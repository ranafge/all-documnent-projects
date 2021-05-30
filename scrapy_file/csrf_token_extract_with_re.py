from bs4 import BeautifulSoup
import requests
import json 
url= ["https://www.premierleague.com/stats/top/clubs/wins?se={}".format(x) for x in range(1,100)]
print(url)
for url in url:
    data= requests.get(url).text

    soup=BeautifulSoup(data,"html.parser")

    PLtable = soup.find_all('table')[0]

    data = []
    for td in PLtable.find_all("td"):
          data.append(td.text.replace('\n', ' ').strip())
    print(data)
