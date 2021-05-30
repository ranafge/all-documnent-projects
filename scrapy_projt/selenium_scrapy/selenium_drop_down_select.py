from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from shutil import which
from selenium.webdriver.support.ui import Select
import time
chrome_options = Options()
chrome_options.add_argument("--headless")

# PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://www.kvwl.de/earzt/index.htm")
print(driver.title)

search_input = driver.find_element_by_id("doc-search-search-location")
search_input.send_keys("Bielefeld, Germany")

search_input.send_keys(Keys.ENTER)
time.sleep(5)

driver.find_element_by_id('ul.dropdown-menu.inner')


# select.select_by_visible_text(' Hausärzte')
# select.options
# # select by visible text
# select.select_by_value('12001_SID')


# print(driver.page_source)

driver.close()
