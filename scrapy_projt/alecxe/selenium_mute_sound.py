import re
from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path='../selenium_scrapy/geckodriver')
driver.get("https://pay.google.com/gp/w/home/signup")
driver.find_element_by_id("identifierId").send_keys('ranafge@gmail.com')
time.sleep(3)
driver.find_element_by_css_selector("div.VfPpkd-RLmnJb").click()
time.sleep(3)
# driver.close()
driver.find_element_by_name("password").send_keys('Rana9911@')
driver.find_element_by_id("passwordNext").click()

# get_web_element_attribute_names(search_element)
