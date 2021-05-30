import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import requests
import requests
import json
a = 'https://tekno.kompas.com/read/2020/11/12/08030087/youtube-down-pagi-ini-tidak-bisa-memutar-video'
b = requests.get("https://apis.kompas.com/api/comment/list?urlpage=https://tekno.kompas.com/read/2020/11/12/08030087/youtube-down-pagi-ini-tidak-bisa-memutar-video&json&limit=10")
print(b)
b = b.json()
b = b['result']["total"]
print(b)
