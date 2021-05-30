import os
from selenium import webdriver
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import requests

url = requests.get('https://www.fiverr.com')
print(url.text)
print(url.status_code)
bs = BeautifulSoup(url.text,'html.parser')
print(bs.text)
for x in bs.find_all['img']:
        print(x['src'])
