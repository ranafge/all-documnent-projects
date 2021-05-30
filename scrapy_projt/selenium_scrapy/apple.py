from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

driver = webdriver.Firefox(executable_path='./geckodriver')
url = "https://developer.apple.com/documentation/technologies"

driver.get(url)
sleep(2)

soup = BeautifulSoup(driver.page_source, 'lxml')


for a in soup.find_all('a', href=True):
    print(a)

driver.close()
