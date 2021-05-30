from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json
import requests
from selenium import webdriver
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}
webdriver = webdriver.Chrome()
url = 'https://www.quora.com/What-is-it-like-to-live-in-London'
webdriver.get(url)
soup = BeautifulSoup(webdriver.page_source, 'html.parser')
answers = soup.find("script", {"type": "application/ld+json"})
print(answers)
data = json.loads(str(answers))
print(len(data["mainEntity"]["suggestedAnswer"]))
