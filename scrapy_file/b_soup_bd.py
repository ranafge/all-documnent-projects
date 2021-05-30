import requests
from bs4 import BeautifulSoup
request = requests.get("https://corona.gov.bd/")

soup = BeautifulSoup(request.content.decode('utf-8'), "lxml")
my_data = soup.find('div', {'class':'col-md-6 col-sm-6 col-xs-12 slider-button-center xs-mb-15'})
print(my_data.get_text(strip=True, separator='|'))
