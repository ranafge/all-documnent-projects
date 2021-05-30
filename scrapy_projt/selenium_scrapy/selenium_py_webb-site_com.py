from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




driver = webdriver.Chrome()
driver.get('https://webb-site.com/')

search = driver.find_element_by_name('code')

search.click()

search.send_keys("1830")

search.send_keys(Keys.RETURN)


element = driver.find_element_by_link_text('Financials')

element.click()


element = driver.find_elements_by_link_text('Annual Report')
# print(element)
# print(len(element))
# element.click()
for c in element:
    c.click()
