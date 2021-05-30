
import time
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome()

driver.get('http://www.tsetmc.com/loader.aspx?ParTree=151311&i=42354736493447489')
time.sleep(5) # delay 5 sec
page_source = driver.page_source

soup = BeautifulSoup(page_source,'html.parser')
# print(soup.prettify())
prices = soup.find('div', {'class': 'box6 h80'}).find('table')

for td in prices.find_all('tr')[1]:
    print(td.getText()) # all td text garbed.

driver.quit()
