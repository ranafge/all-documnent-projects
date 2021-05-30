from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/events/777016513046446')
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

date_time = soup.find('div', class_=['_1oa6'])
print(date_time.text)

driver.close()
