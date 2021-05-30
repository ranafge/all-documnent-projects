import scrapy
import requests
import pprint

req = requests.get("https://www.animeworld.tv/play/sasami-san-ganbaranai.BXHw6")
print(req.status_code)
response = scrapy.Selector(text=req.text)
print(response.xpath(''))
