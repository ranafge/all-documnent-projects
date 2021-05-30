import requests
from bs4 import BeautifulSoup

headers={
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    "Referer" : "https://www.yelp.ie/biz/tesla-san-francisco?osq=Tesla=Dealership"
}
def main(url):
    with requests.Session() as req:
        req.headers.update(headers)
        r = req.get(url).text

        soup = BeautifulSoup(r, 'lxml')

        divs = soup.find_all('div',class_="lemon--div__373c0__1mboc border-color--default__373c0__3-ifU")
        print(divs)

url = 'https://www.yelp.ie/biz/tesla-san-francisco?osq=Tesla=Dealership'
main(url)

["https://www.yelp.ie/biz/y0pllLqKVUQi2IkhYYf9ug/review_feed?hrid=WqGBt4VQfr1vvGzie-QjLw&rh_type=phrase&rh_ident=oliver&rl=en",
"https://www.yelp.ie/biz/y0pllLqKVUQi2IkhYYf9ug/review_feed?hrid=nlmFH44VXXAmqnKAnm0P1A&rh_type=phrase&rh_ident=dublin",
"https://www.yelp.ie/biz/y0pllLqKVUQi2IkhYYf9ug/review_feed?hrid=OD-NXvs88PBfRaLgXPZrRQ&rh_type=phrase&rh_ident=model_s"]
