import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}

def bestbuty(url):
    request = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(request.content, 'lxml')
    return soup.prettify()

# def bestbuy():
#     result = requests.get(bburl)
#     soup = BeautifulSoup(result.content, 'lxml')
#
#     price = soup.find('a',attrs={'class': 'megaButton buyTier3 cartAddNoRadio'})
#
#     print(price.get_text(strip=True, separator=' '))

bburl = "https://www.ebgames.ca/SearchResult/QuickSearch?q=animal+crossing"

print(bestbuty(bburl))
