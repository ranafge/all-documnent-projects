import requests as ureq
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}

#opening up connection, grabbing url
url = "https://www.etsy.com/sg-en/search/bath-and-beauty/soaps?q=green+beauty&explicit=1&ref=pagination&page=1"
uclient = ureq.get(url, headers=headers)
# page_html = uclient.read()
#html parsing
soup = BeautifulSoup(uclient.text, 'lxml')

listings = soup.findAll("div", {"class":"content bg-white col-md-12 pl-xs-1 pr-xs-0 pr-md-1 pl-lg-0 pr-lg-0 bb-xs-1"})
# print(listings)

for d in listings:

    print(d.h3)
    print()
    print()
    break

#html parsing
# page_soup = soup(page_html, 'lxml')
# print(page_soup.p)
#
# #grabs each product
# listings = page_soup.findAll("li", {"class":"wt-list-unstyled wt-grid__item-xs-6 wt-grid__item-md-4 wt-grid__item-lg-3 wt-order-xs-0 wt-order-sm-0 wt-order-md-0 wt-order-lg-0 wt-order-xl-0 wt-order-tv-0 grid__item-xl-fifth tab-reorder"})
# len(listings)
