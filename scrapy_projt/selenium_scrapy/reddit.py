import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests                 # Simpler HTTP requests
from bs4 import BeautifulSoup   # Python package for pulling data out of HTML

##### Web scraper for infinite scrolling page #####
driver = webdriver.Firefox(executable_path=r"/home/rana/Documents/allproject/scrapy_projt/selenium_scrapy/geckodriver")
driver.get("https://www.reddit.com/r/redditdev/")
time.sleep(2)  # Allow 2 seconds for the web page to open
scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
i = 1

while True:
    # scroll one screen height each time
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    # Break the loop when the height we need to scroll to is larger than the total scroll height

    if (screen_height) * i > scroll_height:
        break
# http_headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15'}
# page = requests.get("https://www.reddit.com/r/redditdev/",headers=http_headers, allow_redirects=True, verify=True, timeout=30)
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.close()
flair = soup.find_all("div", class_ ="lrzZ8b0L6AzLkQj5Ww7H1")
print(flair, flush=True)
for link in flair.select('div'):
    print(link.a['href'], '\n')

print(flair)
