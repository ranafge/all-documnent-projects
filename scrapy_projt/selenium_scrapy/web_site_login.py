# from selenium import webdriver
# # from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
#
#
# driver = webdriver.Chrome()
#
# url = "https://portal.spryngsms.com/login?redirect=%2F"
# username = "cosmos"
# password = "12345"
#
# driver.get(url)
#
# driver.get('https://portal.spryngsms.com/login?redirect=%2F')
#
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
# "//span[text()='Gebruikersnaam']//following::div[1]//input"))).send_keys("cosmos")
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
# "//span[text()='Wachtwoord']//following::div[1]//input"))).send_keys("12345")
# driver.find_element_by_css_selector("#app > div.application--wrap > div.tw-flex.tw-w-full.tw-pr-8 > div > div > div > div > div > section > form > footer > div.form__footer-bottom.form__footer-bottom--login > div > button").click()

'//*[@id="content"]/div[1]/div[2]/a[3]'
# urls =["https://nj.zu.ke.com/zufang/caochangmendajie/pg{}/#contentList".format(x) for x in range(1,10)]
# url = "https://nj.zu.ke.com/zufang/caochangmendajie/"
# from lxml import etree
# from lxml im
# page=etree.HTML(Download.downloadPage(url))            #download page
# nums = page.xpath('/html/body/div[3]/div[1]/div[5]/div[1]/div[2]/a[2]/text()')
# print(nums)
# print(urls)
