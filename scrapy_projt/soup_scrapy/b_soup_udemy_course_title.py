import requests
from bs4 import BeautifulSoup
from selenium import webdriver
url ="https://www.udemy.com/courses/search/?src=ukw&q=veri+bilimi"
import time
webdriver =webdriver.Chrome()

webdriver.get(url)
time.sleep(6) # delay 6 sec

soup = BeautifulSoup(webdriver.page_source, "lxml")

course_titles = soup.find_all("div", attrs={"class":"udlite-focus-visible-target udlite-heading-md course-card--course-title--2f7tE"})
for title in course_titles:
    print(title.get_text())
