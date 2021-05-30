import requests
from bs4 import BeautifulSoup
from selenium import webdriver

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}
URL = "https://www.mydays.de/magicbox/kurzurlaub"
webdriver = webdriver.Chrome()
webdriver = webdriver.get(URL)

soup = BeautifulSoup(webdriver.page_source, 'html.parser')
Price = soup.find('div',{"class":"c-mbvoucher__pricebox"})
print(Price)

webdriver.quit()
