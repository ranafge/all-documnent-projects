from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

product_links = []
baseurl = "https://www.technodom.kz/"
options = Options()
options.headless = True

driver = webdriver.Chrome( options=options)


for x in range(1, 5):
    driver.get(
        f"https://www.technodom.kz/bytovaja-tehnika/uhod-za-odezhdoj/stiral-nye-mashiny/f/brands/lg/brands/samsung?page={x}"
    )
    # Wait for the page to fully render
    sleep(3)
    soup = BeautifulSoup(driver.page_source, "lxml")
    product_list = soup.find_all("li", class_="ProductCard")
    for item in product_list:
        for link in item.find_all("a", href=True):
            product_links.append(baseurl + link["href"])
    print(product_links)

wmlist = []
for link in productlinks:
    driver.get(link)
    soup = BeautifulSoup(driver.page_source, "lxml")
    print(link)
    name = soup.find('h1', class_='ProductHeader-Title').text.strip()
    price = soup.find('p', class_='ProductPrice ProductInformation-Price').text.strip()

    wm = {
        'Model':name,
        'Price': price
    }
    wmlist.append(wm)
    print('Saving:', wm['Model'])
df = pd.DataFrame(wmlist)

df.to_excel("TD pricesTEST.xlsx", sheet_name='TEW', index=False)
