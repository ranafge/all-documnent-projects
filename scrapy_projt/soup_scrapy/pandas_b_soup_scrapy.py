import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
    
baseurl = "https://www.technodom.kz"
options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)

productlinks = []

for x in range(1,2):
    driver.get(
        f"https://www.technodom.kz/bytovaja-tehnika/uhod-za-odezhdoj/stiral-nye-mashiny/f/brands/lg/brands/samsung?page={x}"
    )
    # Wait for the page to fully render
    sleep(5)
    soup = BeautifulSoup(driver.page_source, "lxml")
    product_list = soup.find_all("a", class_="ProductCard-Content")

    for item in product_list:
        link = baseurl + item["href"]
        if link not in product_list:
            productlinks.append(link)


wmlist = []
for link in productlinks[1:10]:
    driver.get(link)
    sleep(5)
    soup = BeautifulSoup(driver.page_source, "lxml")
    print(link)
    name = soup.find('h1', class_='ProductHeader-Title').text.strip()
    price = soup.find('p', class_='ProductPrice ProductInformation-Price').text.strip()

    wm = {
        'link': link,
        'Model':name,
        'Price': price
    }
    wmlist.append(wm)
    print('Saving:', wm['Model'])

df = pd.DataFrame(wmlist)
df.to_excel("TD_pricesTEST.xlsx", sheet_name='TEW', index=False)
