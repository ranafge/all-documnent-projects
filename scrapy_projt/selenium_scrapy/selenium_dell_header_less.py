import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
url = "https://www.dell.com/en-us/shop/dell-laptops/sr/laptops/11th-gen-intel-core?appliedRefinements=23775"
options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)
driver.get(url)
# driver.implicitly_wait(50)
# print(driver.find_elements_by_css_selector(".stack-system.ps-stack").text)
# print(WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.no-div-lines-layout"))).text)
laptop_data = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.no-div-lines-layout"))).text
print(laptop_data)
# print(WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.u_cbox_chart_progress.u_cbox_chart_male>div.u_cbox_chart_per"))).text)
# products = driver.find_element_by_css_selector()
# print(products)

# productlinks = []
#
# for x in range(1,2):
#     driver.get(
#         f"https://www.technodom.kz/bytovaja-tehnika/uhod-za-odezhdoj/stiral-nye-mashiny/f/brands/lg/brands/samsung?page={x}"
#     )
#     # Wait for the page to fully render
#     sleep(5)
#     soup = BeautifulSoup(driver.page_source, "lxml")
#     product_list = soup.find_all("a", class_="ProductCard-Content")
#
#     for item in product_list:
#         link = baseurl + item["href"]
#         if link not in product_list:
#             productlinks.append(link)
#
#
# wmlist = []
# for link in productlinks[1:10]:
#     driver.get(link)
#     sleep(5)
#     soup = BeautifulSoup(driver.page_source, "lxml")
#     print(link)
#     name = soup.find('h1', class_='ProductHeader-Title').text.strip()
#     price = soup.find('p', class_='ProductPrice ProductInformation-Price').text.strip()
#
#     wm = {
#         'link': link,
#         'Model':name,
#         'Price': price
#     }
#     wmlist.append(wm)
#     print('Saving:', wm['Model'])
#
# df = pd.DataFrame(wmlist)
# df.to_excel("TD_pricesTEST.xlsx", sheet_name='TEW', index=False)
