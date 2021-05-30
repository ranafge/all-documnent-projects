from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}
driver = webdriver.Chrome()
url = 'https://steamdb.info/app/730/graphs/'
driver.get(url)
WebDriverWait(driver, 15).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div#chart-month-breakdown.table-responsive')))
soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup.prettify())
# select_tobdy = soup.select('div.span8')[0]
# for td in select_tobdy.find_all('tr'):
#     print(td.text.strip())
# print(select_tobdy)
#
# mydata_table = soup.select('table.table.table-hover')[9]
# # print(mydata_table)
# print('*'*10)
print(soup.select('div#chart-month-breakdown.table-responsive'))
driver.quit()












