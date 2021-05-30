from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup
import pandas as pd

driver = webdriver.Chrome()
urls = ["https://racing.hkjc.com/racing/information/English/Racing/LocalResults.aspx?RaceDate=2021/02/06&Racecourse=ST&RaceNo=1","https://racing.hkjc.com/racing/information/English/Racing/LocalResults.aspx?RaceDate=2021/02/06&Racecourse=ST&RaceNo=2"]

for url in urls:
    driver.get(url)
    time.sleep(5)
    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "f_fs13")))
    htmlStr = driver.page_source

    soup_level1 = soup(htmlStr, 'html.parser')

    race_soup = soup_level1.find('tbody',{'class':'f_fs13'}).find_parent('table')
    results_soup = soup_level1.find('tbody',{'class':'f_fs12'}).find_parent('table')

    df1 = pd.read_html(str(race_soup))[0]
    print(df1)


    df2 = pd.read_html(str(results_soup))[0]
    print(df2)


    print('good')


    driver.close()
