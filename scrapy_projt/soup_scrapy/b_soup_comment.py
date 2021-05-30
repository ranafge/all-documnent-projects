from urllib.request import urlopen
from bs4 import BeautifulSoup, Comment

url = 'https://www.pro-football-reference.com/years/2020/draft.htm'
html = urlopen(url)

soup = BeautifulSoup(html, "lxml")

comment = soup.find(text=lambda text: isinstance(text, Comment) and 'class="table_outer_container"' in text) #THIS RETURNS NONE
print(comment)
# stats_page = BeautifulSoup(comment, "lxml")
