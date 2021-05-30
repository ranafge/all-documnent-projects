from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from scrapy.selector import Selector
import scrapy
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
# Links
links = ['https://www.energymadeeasy.gov.au/plan?id=1ST82937MRE&postcode=2000', 'https://www.energymadeeasy.gov.au/plan?id=1ST82959MRE&postcode=2000', 'https://www.energymadeeasy.gov.au/plan?id=1ST82961MRE&postcode=2000']

# Empty List
distributor = []
browser = webdriver.Firefox(executable_path='./geckodriver')
browser.maximize_window()

for ind_lnk in links:
    browser.get(ind_lnk)
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/section/div/div[1]/div[6]/div/button'))).click()
    time.sleep(3)
    try:
        distributor.append(browser.find_element_by_xpath("//*[@id='content']/div/section/div/div[1]/div[6]/div/div/div[1]/section/div[5]/span").text)
    except:
        distributor.append("")
    browser.close()

print(distributor)

