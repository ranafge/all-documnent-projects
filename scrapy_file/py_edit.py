import requests
from bs4 import  BeautifulSoup

# res_item = requests.get('https://www.jetsetter.com/magazine/cool-tech-gadgets-on-amazon/')
# bs_item = BeautifulSoup(res_item.text,'html.parser')
# list_item = bs_item.find_all('h2',class_ ="heading")
#
# for item_print in list_item:
#     print(item_print.get_text(strip=True))


next_page_url = ['https://web.archive.org/web/20150630111618/https://www.zalando.co.uk/womens-clothing/?p={0}'.format(x) for x in range(2,5)]
# print(next_page_url)
# ('https://example.com/page-{}'.format(i) for i in range(1,total_pages))
base_url = ['https://web.archive.org/web/20150906222155mp_/https://www.zalando.co.uk/womens-clothing/']
star_urls = base_url + ['https://web.archive.org/web/20150630111618/https://www.zalando.co.uk/womens-clothing/?p={0}'.format(x) for x in range(2,6)]
print(star_urls)
