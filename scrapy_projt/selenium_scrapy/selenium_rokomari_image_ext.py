from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url='https://www.rokomari.com/book/117698/mosnobie-rumi-5'

driver = webdriver.Chrome()
driver.get(url)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.pagesArea')))
img =driver.find_elements_by_xpath("/html/body/div[4]/div[1]/div[2]/ul/li")


