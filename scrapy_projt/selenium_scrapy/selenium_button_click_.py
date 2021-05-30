
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

wd = webdriver.Chrome()
wd.get('https://allegro.pl/oferta/zageszczarka-6-5km-90kg-higher-briggs-gratisy-9003885105#aboutSeller')

wd.maximize_window()
wd.find_element_by_xpath("/html/body/div[2]/div[5]/div/div[2]/div[2]/button[1]").click()

click_on_button = wd.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[10]/div/div/div/div/div[7]/div[2]/div/div/div[2]/div/div[2]/section/div/div/div/div[2]/div/div/div[2]/section[2]/div/div/div[1]/ul/li[2]/div/button')
click_on_button.click()
click_on_button = wd.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[10]/div/div/div/div/div[7]/div[2]/div/div/div[2]/div/div[2]/section/div/div/div/div[2]/div/div/div[2]/section[2]/div/div/div[2]/ul/li[1]/div/button')
click_on_button.click()
click_on_button = wd.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[10]/div/div/div/div/div[7]/div[2]/div/div/div[2]/div/div[2]/section/div/div/div/div[2]/div/div/div[2]/section[2]/div/div/div[2]/ul/li[2]/div/button')
click_on_button.click()
