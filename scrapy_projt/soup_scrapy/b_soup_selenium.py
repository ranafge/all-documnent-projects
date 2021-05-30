
import re
import csv
import time
from pathlib import Path

# import details as details
from selenium import webdriver
import bs4 as bs4
import os
import copy
import time
option = webdriver.ChromeOptions()
option.add_argument(" - incognito")
option.add_argument("headless")
exec_path = '/Users/Downloads/MUR_scraping-master/Libraries/chromedriver'
browser = webdriver.Chrome( options=option)
browser.get(url="https://www.flipkart.com/search?q=sofa")

page = browser.page_source

soup = bs4.BeautifulSoup(page, 'lxml')

desc_div = soup.find('div', class_='t-content t-state-active')
desc_list = []

if desc_div:
    desc_p_list = desc_div.find_all(class_='display-row')
    if desc_p_list:
        for p in desc_p_list:
            desc_list.append(p.get_text(strip=True, separator=' '))
        # desc_list = ' '.join(desc_list)
# print(desc_list)

table = soup.find('table')
table_rows = table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)
