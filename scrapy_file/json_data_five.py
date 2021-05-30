from bs4 import BeautifulSoup as soup
import requests
import json

page_link = 'https://www.lazada.com.my/catalog/?_keyori=ss&from=input&page=1&q=h370m&sort=priceasc'
page_response = requests.get(page_link, timeout=5)
page_content = soup(page_response.text, "html.parser")

json_tags = page_content.find_all('script',{'type':'application/ld+json'})

for jtag in json_tags:
    print(jtag.get_text)

# for jtag in json_tags:
#     json_text = jtag.get_text()
#     print(json_text)
    # json_dict = json.loads(json_text)
    # print(json_dict)
