from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

URL = 'website'
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get(URL)
wait = WebDriverWait(driver, 10)
#-------------------------------------------------------------------

wait.until(EC.presence_of_element_located((By.ID,"username"))).send_keys("nocsud")
wait.until(EC.presence_of_element_located((By.ID,"value"))).send_keys("noc_sud10")
driver.find_element_by_id("submitDataverify").click()


#-------------------------------------------------------------------
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()
root = soup.find(id='root')
print(root)
