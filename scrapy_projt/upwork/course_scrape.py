import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys

headers = {
    'authority': 'www.dicoding.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'origin': 'https://www.dicoding.com',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.dicoding.com/login',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '_ga=GA1.2.1006077084.1615991519; _gid=GA1.2.267423529.1615991519; _fbp=fb.1.1615991521540.542130134; _hjTLDTest=1; _hjid=70b39f11-b3b0-43c8-92df-bbc2e0ca9d3a; _hjFirstSeen=1; _hjAbsoluteSessionInProgress=1; _fw_crm_v=41bf4697-1941-4d21-dc9e-6f38b7608b04; _gcl_au=1.1.728612000.1615992100; laravel_session=eyJpdiI6ImxcL2JPNWZodk1JcUZ6TXNkMjhMTnpnPT0iLCJ2YWx1ZSI6InNubm40clRXaFZiUUZuSUUrQnBaVXRtTTNPT2JLMW1IeVwvQnN3SnpSXC81NmMrZ3k4RU1ZZkVqR2M5aXBCMzJONElCXC9iczhTekxQZDdrczNvOFVjZU1RPT0iLCJtYWMiOiI0OTMyMjMyNDE3OTM4YWQ1OTJiYTRjODIwZTcxODFmNTNhM2U4ZjBmOTk5MmFkMjUzNzlhZWM0ZDUwMDJmNGZkIn0%3D',
}

data = {
  'captcha': '03AGdBq24zyOwD8xM8-cc6uASbhiLXp5wrSKpYSyWMUBV2rwheV4xbjBAtBEyOA2OG3lUoRoCEjxCoPI8BDINOw-lssOcbQH_W9YMz8duvT3UonLZHVj1crObfVByhFx41th-lCEgOZabRTSMmOu7Az0fo0s9uBS6Ip18h93FOxb_ueJdzJswFUgf-1K6t15LJgHNCUBeZGrp_dPOYMGRQClYwALrHCLUHRwaNi5FMBImkHdZ3fHzJj0_FtSj0XmR39er6WHyLCQvhU_gMuGE9Mfy6TMvO3p43GtXnAXimabOIWz0hXR56NWDK0x_PQjQoaMhpnX9U4HpMzs4VN2-apKaMaySIveHW7e00oKDA1iB0RERiSn9A5QAmm4_KKS91P9byHnaPzUlWAMFJZguFBZnun1_H3xY1Ag8c9R4zLFzHQ1ABIuUFwDAPFxszupfmV_PsPDg8_7cX',

  '_token': '9ab8VYPPRA0gejE5E46DPJkbDJhtLfWRbjMZoes6',
  'credits': '',
  'login_email': 'mybudipepe01@gmail.com',
  'login_password': 'duasatu'
}
login_email= 'mybudipepe01@gmail.com',
login_password= 'duasatu'
url = 'https://www.dicoding.com/login'
driver = webdriver.Chrome()
driver.get(url)

driver.find_element_by_css_selector("#login_email").send_keys(login_email)
# driver.find_element_by_id("identifierNext").click()
time.sleep(5)
driver.find_element_by_css_selector("#login_password").send_keys(login_password)
# driver.find_element_by_id("passwordNext").click()
driver.find_element_by_name("Masuk").send_keys(Keys.RETURN)
# driver.find_element_by_css_selector('#login-modal > div > div > div.modal-body.p-4 > form > div:nth-child(5) > button').click()

time.sleep(5)


driver.close()


# response = requests.post('https://www.dicoding.com/login', headers=headers, data=data)
