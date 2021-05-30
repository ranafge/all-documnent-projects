import requests
from selenium import webdriver
from bs4 import BeautifulSoup
webdriver.Chrome()
url = 'http://110.74.207.107:8080/livedata/collection.jsf?template=weather&node=596&view=statistic&year=2019&units=metric'
webdriver = webdriver.Chrome()
webdriver.get(url)
soup = BeautifulSoup(webdriver.page_source, 'html.parser')
table = soup.find(id='statistic-table')

print(table)
