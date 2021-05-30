from bs4 import BeautifulSoup
import requests
url = "https://en.wikipedia.org/wiki/Carlow%E2%80%93Kilkenny_(D%C3%A1il_constituency)"
res = requests.get(url)
soup = BeautifulSoup(res.content,'lxml')
my_tables = soup.find_all("table", {"class":"wikitable"})
# print(my_tables)
for table in my_tables:
    rows = table.find_all('tr')
    print([row.get_text(strip=True) for row in rows])
