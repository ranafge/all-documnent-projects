from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
import json
import pandas as pd
import numpy as np
import time
import os
import sys
from googletrans import Translator
from selenium.webdriver.chrome.options import Options
translator = Translator()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15"}

from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get('https://www.webofknowledge.com/')
select = Select(driver.find_element_by_id('shibSelect'))
select.select_by_visible_text('AirLiquide')
driver.find_element_by_id('shibSubmit').click()
# wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='select2-shibSelect-container']"))).click()
