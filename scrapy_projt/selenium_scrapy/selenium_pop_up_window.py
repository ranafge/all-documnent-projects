from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from time import sleep
from selenium.webdriver.chrome.options import Options

url = 'https://www.bloomingdales.com/shop/product/kobi-halperin-eden-soft-blazer?ID=3857556&CategoryID=1005879'


options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Firefox(executable_path='./geckodriver')
driver.get(url)
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, './/*[@class="sc-link"]'))).click()
