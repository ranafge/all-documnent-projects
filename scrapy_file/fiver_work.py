from bs4 import BeautifulSoup
import requests


url ="https://www.displayspecifications.com/en"
url2 ="https://www.displayspecifications.com/en/brand/f652d"

page =requests.get(url2).content

soup = BeautifulSoup(page, 'lxml')
data = soup.find_all('div', {'class':'model-listing-container-80'})
p = []
for div in data:
    p.extend([(x.get('href'),y['data-src']) for x in div.find_all('a') for y in div.find_all('img') ])
    p.extend([(z.text, p.text) for z in div.find_all('h3') for p in div.find_all('p')])

print('*'*30)

print(p)
print(len(p))


#
# divs = soup.find_all('div', {'class':'article-listing-container'})
# print(divs)
# for div in divs:
#     links = div.find_all('a', href=True)
#     for link in links:
#         print(link['href'])
#     dates = div.find_all('p')
#     for date in dates:
#         print(date.text)
#
