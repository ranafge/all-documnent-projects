import requests
from bs4 import BeautifulSoup

# Send GET request
r = requests.get('https://tiki.vn/dien-thoai-may-tinh-bang/c1789?src=c.1789.hamburger_menu_fly_out_banner&_lc=Vk4wMzkwMTUwMDk=')

# Parse HTML text
soup = BeautifulSoup(r.text, 'html.parser')
# def scrape_tiki(url="https://tiki.vn/dien-thoai-may-tinh-bang/c1789?src=c.1789.hamburger_menu_fly_out_banner&_lc=Vk4wMzkwMTUwMDk="):

# Get parsed HTML
#     soup = get_url(url)

cnt = 1
product = soup.find_all('div',{'class','product-item'})
# print(product)

for i in product:
    # print(i)
    rating = i.find('span', class_="rating-content")
    print(rating)
