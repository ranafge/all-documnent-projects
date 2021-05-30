import requests
import bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
url = 'https://pages.daraz.com.bd/'
offers = url + 'wow/gcp/daraz/megascenario/bd/ramadan_eidcampaign_april21/grocery_free_shipping'
driver = webdriver.Firefox(executable_path=r'/home/rana/Documents/allproject/scrapy_projt/selenium_scrapy/geckodriver')
driver.get(offers)

wait = WebDriverWait(driver, 30)
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product2-in-a-row-item")))
scrolls = 7
while True:
    scrolls -= 1
    print(scrolls)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(5)
    if scrolls < 0:
        break
html = driver.page_source
output = []
driver.close()
soup = bs4.BeautifulSoup(html, 'html.parser')
for product in soup.find_all("div", {"class": "product2-in-a-row-item"}):
    image = product.find("img", {"class": "rax-image"})
    title = product.find("span", {"class": "product-item-bottom-title"})
    price = product.find_all("div", {"class": "lzd-price"})
    discount = product.find_all("span", {"class": "text"})

    links = product.select('img.rax-image[src]')[0]['src']
    print(links)
    if links.startswith(" https"):
        print('link : ', links)

    image = image['src']
    productName = title.text
    price = price[0].text if len(price) else 0
    discount = discount[0].text if len(discount) else 0

