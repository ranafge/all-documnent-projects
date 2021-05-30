from bs4 import BeautifulSoup
import time
import requests
import datetime

url = "http://bigpara.hurriyet.com.tr/doviz/dolar/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml-xml")
old_value = soup.find("span" ,attrs={"class":"value up"}).text
first_value = soup.find("span" ,attrs={"class":"value up"}).text


# while True:
time.sleep(1)
url = "http://bigpara.hurriyet.com.tr/doviz/dolar/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml-xml")
new_value = soup.find("span" ,attrs={"class":"value up"}).text

for data in soup.find_all('div', {'class': 'kurDetail mBot20'}):
    print([i.get_text(':', strip=True) for i in data.find_all('div', {'class': 'kurBox'})])
    print(data.get_text("|", strip=True))


