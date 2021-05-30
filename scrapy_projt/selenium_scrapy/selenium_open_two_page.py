from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get("https://www.justdial.com/Chennai/Hr-Consultancy-Services/nct-10258625/page-2")
# driver.set_page_load_timeout(30)
x = driver.find_element_by_xpath('//*[@id="srchpagination"]/a[12]')
print(x.text)
driver.get("https://www.justdial.com/Chennai/Hr-Consultancy-Services/nct-10258625/page-3")
