from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import requests
import csv
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get("https://www.haze.gov.sg/resources/pollutant-concentrations")#use selenium for dynamic websites
content = driver.page_source
soup = BeautifulSoup(content, "lxml") #parse the html

data = {}
nea_table = soup.find("table", attrs={"class": "table table-striped table-bordered surveillance-table"})

for table in nea_table.find_all("tbody") :
    #Get the headers
    t_headers = []
    for th in table.find_all("th"):
        t_headers.append(th.text.replace('\n', ' ').strip())

    #Get all rows
    table_data = []
    for tr in table.find_all("tr"): # find all tr's from table's tbody
        t_row = {}

        # find all td in tr and zip it with t_header
        for td, th in zip(tr.find_all("td"), t_headerss):
           t_row[th] = td.text.replace('\n', '').strip()
        table_data.append(t_row)


keys = table_data[1].keys()
with open('../soup_scrapy/NEA.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(table_data)
