import re
import requests
from urllib.request import urlopen
from urllib.parse import urljoin
import urllib.request

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"




#
# def downalod(url):
#     return requests(url,headers={'User-Agent': 'XYZ/3.0'}).read()
#
def extract_links(response):
    link_regex = re.compile('<img[^>]+src=["\'](.*?)["\']',
re.IGNORECASE)
    return link_regex.findall(response)
#
#
#
# urls=[
#
#  'https://www.example.com/about-us/',
#  'https://www.example.com/our-projects/',
#  'https://www.example.com/3c-metal-group/',
#  'https://www.example.com/installation/',
#  'https://www.example.com/inspection/',
#  'https://www.example.com/contact-us/',
# ]
#
# print([i for i in urls if 'about-us' in i or 'contact-us' in i])
#
if __name__ == "__main__":
    target_url = 'https://www.rokomari.com/book'
    # download_page = downalod(target_url)


    opener = AppURLopener()
    response = opener.open('https://www.rokomari.com/book')
    links = extract_links(response)
    print(links)

