import requests
from bs4 import BeautifulSoup
import sys

# url = 'https://miqa.nl/woningen/koop/#q1YqqSxIVbJSys7PL1DSUcovSkktSqoECqQklpTmeuaV5acWWaWkFicr1QIA'
# page = requests.get(url)
# soup = BeautifulSoup(page.text, 'html.parser')
#
# title_div = soup.find_all('div', class_='title')
# page = soup.select_one('a.next.page-numbers', href=True).get('href')
# print(page)
# # for streets in title_div :
# #      street = streets.find('h2').text
# #      print(street)

def miqa(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title_div = soup.find_all('div', class_='title')
    for streets in title_div :
        street = streets.find('h2').text
        # print() 'Item ' + street
        print(street)
    try:
        page = soup.select_one('a.next.page-numbers', href=True).get('href')
        print('URL', page)
        miqa(page)
    except AttributeError:
        print('There is no page to extract data. Finished.')


if __name__ == "__main__":
    url = 'https://miqa.nl/woningen/koop/#q1YqqSxIVbJSys7PL1DSUcovSkktSqoECqQklpTmeuaV5acWWaWkFicr1QIA'
    print('starting ...')
    print(url)
    miqa(url)




