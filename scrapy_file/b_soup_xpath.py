from bs4 import BeautifulSoup

with open('my_html.html', 'rb') as html:
    text = html.read()
    soup = BeautifulSoup(text, 'lxml')

# "//td[div='1203']/following-sibling::td/input[@type='checkbox']"

