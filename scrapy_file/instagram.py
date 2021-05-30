from bs4 import BeautifulSoup
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.instagram.com/p/B5LeHK2h4p0/')
time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

datetime = soup.select('time._1o9PC.Nzb55')[0]['datetime']
title = soup.select('time._1o9PC.Nzb55')[0]['title']
print(datetime)
print(title)
driver.quit()
