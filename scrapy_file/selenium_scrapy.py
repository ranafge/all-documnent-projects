from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
driver = webdriver.Chrome()
eachLink=[]
authors = []
baseurl='https://meetinglibrary.asco.org'
for x in range (1,2):
  driver.get(f'https://meetinglibrary.asco.org/results?meetingView=2020%20ASCO%20Virtual%20Scientific%20Program&page={x}')
  time.sleep(120)
  page_source = driver.page_source

  soup = BeautifulSoup(page_source,'html.parser')
  productlist=soup.find_all('a',class_='ng-star-inserted')
  for auth in soup.find_all('div', {'class':'record__ellipsis'}):
      authors.append(auth.text)

  for item in productlist:
     for link in item.find_all('a',href=True):
         eachLink.append(baseurl+link['href'])
print(eachLink)
print('\n', authors, '\n')

driver.quit()
