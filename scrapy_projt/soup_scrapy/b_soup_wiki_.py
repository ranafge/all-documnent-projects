from bs4 import BeautifulSoup
import requests

URL = 'https://en.m.wikipedia.org/wiki/List_of_methods_of_torture'
page = requests.get(URL)

html_soup = BeautifulSoup(page.content, 'html.parser')
print(html_soup.prettify())


print ([x.text for x in html_soup.find("section", class_="mf-section-1").find_all('a')])


