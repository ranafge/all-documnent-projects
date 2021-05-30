import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver =webdriver.Chrome('chromedriver')

products=[]
prices=[]
images=[]

driver.get('https://shopee.co.id/search?keyword=laptop')

time.sleep(5)
for i in range(10):
    driver.execute_script("window.scrollBy(0, 350)")
    time.sleep(1)

content=driver.page_source
soup=BeautifulSoup(content, 'lxml')

for item in soup.select('div[data-sqe="item"]'):
    dataImg=item.img
    name=item.find('div',class_="_1Sxpvs")
    price=item.find('div',class_="QmqjGn")

    if dataImg is not None:
        products.append(name.get_text())
        prices.append(price.get_text())
        images.append(dataImg['src'])

df=pd.DataFrame({'Product Name':products,'Price':prices,'Images':images})
print(df.head)
