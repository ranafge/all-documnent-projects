import requests as re
from bs4 import BeautifulSoup as bs

urls = ["http://vlg.film/ajax/index_films.php?PAGEN_1={}".format(x) for x in range(1,11)]

for url in urls:

    page = re.get(url)
    soup = bs(page.content, 'html.parser')
    wrap = soup.find_all('div', class_="column column--20 column--main")
    print(url)
    for det in wrap:
        link = det.a['href']
        print(link)
