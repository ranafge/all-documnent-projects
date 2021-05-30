from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from scrapy.selector import Selector
import scrapy
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.get('https://www.animeworld.tv/play/sasami-san-ganbaranai.BXHw6')

WebDriverWait(driver, 15)

response = scrapy.Selector(text=driver.page_source)

title = response.css("#anime-title::text").extract_first()

print(title)

