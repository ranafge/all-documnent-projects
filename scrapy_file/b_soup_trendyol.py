from bs4 import BeautifulSoup
import requests

def trendyol(url):
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
    page = requests.get(url, headers=headers).text
    soup = BeautifulSoup(page, "html.parser")

    list= soup.find("div", {'class':'prdct-cntnr-wrppr'})
    for link in list.find_all('div',{'class': 'p-card-chldrn-cntnr'}):
        print("https://www.trendyol.com" + link.find('a', href=True)['href'])
        print(link.find('div',{'class':'image-container'}).img['alt'])
        print(link.find('span',{'class':'prdct-desc-cntnr-ttl'}).text)

url = "https://www.trendyol.com/erkek+kazak--hirka?filtreler=22%7C175&pi=3"
trendyol(url)
