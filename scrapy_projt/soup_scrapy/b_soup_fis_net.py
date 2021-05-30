import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}

url ="http://www.fis-net.com/fis/companies/details.asp?l=e&filterby=companies&letter=a&page=1&company_id=66937&country_id="

res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')
address = soup.select_one('div#description_details')
for data in address:
    print(data)
