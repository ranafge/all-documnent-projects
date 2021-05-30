from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(executable_path='./geckodriver')
from selenium.webdriver.common.action_chains import ActionChains
urls =["https://www.youtube.com/",'https://www.google.com', 'https://www.youtube.com/watch?v=MDtEiNkS6f4', 'https://www.youtube.com/watch?v=cnEjFb6uv_o']
driver.get("https://www.google.com")
for i in range(4):
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[i])
    driver.get(urls[i])
    driver.execute_script('''window.open("http://bings.com","_blank");''')
    time.sleep(30)
action = ActionChains(driver)
action.key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()


driver.close()
