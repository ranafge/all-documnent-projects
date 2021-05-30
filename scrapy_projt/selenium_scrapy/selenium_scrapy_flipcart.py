import re
import csv
import time
from pathlib import Path

# import details as details
import bs4 as bs4
import os
import copy
import time

from selenium import webdriver
from scrapy.selector import Selector
browser = webdriver.Firefox(executable_path='./geckodriver')
browser.get(url="https://www.flipkart.com/clothing-and-accessories/topwear/pr?sid=clo%2Cash&otracker=categorytree&p%5B%5D=facets.ideal_for%255B%255D%3DMen")
images_urls = []
while True:
    page = browser.page_source
    image_data = Selector(text=page)
    image_data = image_data.css('img._2r_T1I::attr(src)').extract()
    images_urls.append(image_data)
    # print(image_data.xpath('//div[@class="CXW8mj _21_khk"]/img/@src').get())
    browser.find_element_by_css_selector('a._1LKTO3').click()
    time.sleep(5)

print(images_urls)
