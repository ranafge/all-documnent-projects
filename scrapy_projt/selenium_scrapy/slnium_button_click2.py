import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
options = Options()
options.headless = True

url = "https://www.carousell.sg/categories/men-s-fashion-3/"
driver = webdriver.Chrome()
driver.get(url)

how_many_page=15
for i in range(how_many_page):
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button._3dxOPpKVs8._2Hl0nzGgOH._3KEDnFP0dp._3AGrhxH5DS._2UF39lBLOv.yYAF4gRW1m"))).click()
urls= []
soup = BeautifulSoup(driver.page_source,"lxml")
for ln in soup.findAll("a"):
    urls.append(ln.get('href'))

print(len(urls))
print(urls)

driver.quit()
