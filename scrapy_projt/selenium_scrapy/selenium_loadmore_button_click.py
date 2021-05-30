from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

options = webdriver.FirefoxOptions()
options.add_argument('start-maximized')

browser = webdriver.Firefox(executable_path='./geckodriver')
browser.maximize_window()

url = 'https://www.instagram.com/p/CKCVIu2gDgn'
browser.get(url)
browser.implicitly_wait(10) #wait for 10 sec
load_more = browser.find_element(By.XPATH,'/html/body/div[1]/section/main/div/div[1]/article/div[3]/div[1]/ul/li/div/button/span').click()
time.sleep(2)

# browser.close()
