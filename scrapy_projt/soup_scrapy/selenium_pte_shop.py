from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = "https://www.petshop.co.uk/Dog"
driver = webdriver.Firefox(executable_path="/home/rana/Documents/allproject/scrapy_projt/selenium_scrapy/geckodriver")
driver.get(url)
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
for old_price in soup.find_all("small", class_ = "product-views-price-old"):
    print(old_price)

driver.quit()
