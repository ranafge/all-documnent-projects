import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

wd = webdriver.Chrome()
html_file = os.getcwd() + '//' + 'selenium_local_file.html'
print(html_file)
wd.get('file:///'+html_file)
wd.maximize_window()

d = wd.find_element_by_css_selector('span.ui-button-text')
print(d)

for i in range(1,105):
    time.sleep(.5)
    d.click()
    time.sleep(.5)
