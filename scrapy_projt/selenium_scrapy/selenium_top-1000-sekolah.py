import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url = "https://top-1000-sekolah.ltmpt.ac.id/site/page?id=2001"
options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)

# driver.implicitly_wait(50)
# print(driver.find_elements_by_css_selector(".stack-system.ps-stack").text)
# print(WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.no-div-lines-layout"))).text)
# laptop_data = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.no-div-lines-layout"))).text
# print(laptop_data)
# print(WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.u_cbox_chart_progress.u_cbox_chart_male>div.u_cbox_chart_per"))).text)
# products = driver.find_element_by_css_selector()
# print(products)


# data1 = [wait.until(EC.visibility_of_element_located((By.ID, "tab-1"))).text]
# data2 = [wait.until(EC.visibility_of_element_located((By.ID, "tab-2"))).text]
# data3 = [wait.until(EC.visibility_of_element_located((By.ID, "tab-3"))).text]
# data4 = [wait.until(EC.visibility_of_element_located((By.ID, "tab-4"))).text]
driver.get(url)
wait = WebDriverWait(driver,15)
tab1 = wait.until(lambda driver: driver.find_elements_by_id('tab-1'))
tab2 = wait.until(lambda driver: driver.find_elements_by_id('tab-2'))
tab3 = wait.until(lambda driver: driver.find_elements_by_id('tab-3'))
tab4 = wait.until(lambda driver: driver.find_elements_by_id('tab-4'))
print([ele.text.split('\n') for ele in tab1][0])
print([ele.text for ele in tab2])
print([ele.text for ele in tab3])
print([ele.text for ele in tab4])
# print(tab4.get_attribute('innerHTML').text)
# print(data1)
# print(data2)
# print(data3)
# print(data4)


# print(data)
# find_elements_by_xpath returns a list of selenium objects. You have to access to each object's text attribute
