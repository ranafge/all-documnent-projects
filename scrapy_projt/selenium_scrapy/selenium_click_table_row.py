from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://aaaai.planion.com/Web.User/SearchSessions?ACCOUNT=AAAAI&CONF=AM2021&USERPID=PUBLIC&ssoOverride=OFF')

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'clickdiv')))
eachRow = driver.find_elements_by_class_name('clickdiv')

wait = WebDriverWait(driver, 5)

for item in eachRow:
    item.click() #opens the new window per each row
    faculty=wait.until(EC.presence_of_element_located((By.XPATH, "//td[@valign='MIDDLE']/b")))
    print(faculty.text)
    driver.find_element_by_class_name('XX').click()
