import requests
from bs4 import BeautifulSoup

url = "http://buchholterberg.ch/de/Gemeinde/Information/News/Newsmeldung?filterCategory=22&newsid=911"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

date = soup.find_all('div',{'id':'middle'})
for each in date:
    print(each.find('h1').nextSibling.split(':'))
    print(each.find('h1').nextSibling.split(':',1)[-1].strip())

