import requests
from bs4 import BeautifulSoup

url = "https://www.programmableweb.com/category/all/apis"  # url to be scraped.
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', {'class':'views-table cols-5 table'})
table_body = table.find('tbody')
master_list = []
for row in table_body.find_all('tr'):
    master_list.append(row)

print(len(master_list))
for a in master_list:
    print(a, end='\n\n\n\n')
