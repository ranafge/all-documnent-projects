from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

browser = webdriver.Chrome()

## Link to the movie as an example
url = "https://vw.ffmovies.sc/film/fatman-2020/watching/?server_id=3"
browser.get(url)
element = WebDriverWait(browser,10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='player']"))
)
clickable = browser.find_element_by_id("player")
clickable.find_element_by_xpath('.//*').click()
browser.switch_to.frame("iframe-embed")
time.sleep(5)
