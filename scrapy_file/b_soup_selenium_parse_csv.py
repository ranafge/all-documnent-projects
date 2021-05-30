import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
url = "https://saluddigital.ssch.gob.mx/covid/"

# initiating the webdriver. Parameter includes the path of the webdriver.
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5) # delay for load properly
# # this is just to ensure that the page is loaded
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

table = soup.select_one('div.contenedor-general')

header = [[a.getText(strip=True,separator=' ')][0].split() for a in table.find_all('tr', {'class': 'header-table'})]
text1 = [t.text.strip().split() for t in soup.find_all('tr', {'class': 'ringlon-1'})]
text2 = [t.text.strip().split() for t in soup.find_all('tr', {'class': 'ringlon-2'})]


with open('outz.csv', 'w') as f:
    wr = csv.writer(f, delimiter=',')
    wr.writerow(header[0][1:])
    for row in text1:
        wr.writerow(row)
    for row in text2:
        wr.writerow(row)




