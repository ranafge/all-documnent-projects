from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

html_page = urlopen('https://francechansons.net/alain-souchon-liste-de-chansons/')
soup = bs(html_page, 'lxml')

entry_content_div=soup.find("div", class_="entry-content")
ul = entry_content_div.find("ul").find_all_next('li')
for link in ul:
    url = link.find_next('a')['href']
    # ('a')['href']
    if 'francechansons' not in url:
        print("https://francechansons.net/"+url)
    else:
        print(url)
# print('liesssssss', ul)
# li = ul.find('li')
# children = ul.findChildren("a")
# for child in children:
#     print(child)
#     print("https://francechansons.net/" + child['href'])
