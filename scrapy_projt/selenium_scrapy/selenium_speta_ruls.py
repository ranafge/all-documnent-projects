import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import time
urls = []
for i in range(1,5):
    pages = "https://speta.org/home/directory-of-members/?type=companies&category%5B%5D=corporate-member&pg={0}&sort=a-z".format(i)
    urls.append(pages)
Data = []
options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(options=options)
links=[]
for info in urls:
    browser.get(info)
    time.sleep(10)
    elements = browser.find_elements_by_css_selector("div.lf-item.lf-item-default a")
    # elements = browser.find_elements_by_xpath("//*[@id='c27-explore-listings']/section/div/div[2]/div[1]/div/div[1]/a")
    link = [elem.get_attribute('href') for elem in elements]
    links.append(link)
print(links)
print(len(links))
