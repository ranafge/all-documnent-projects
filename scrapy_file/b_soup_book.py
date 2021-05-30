import requests
from bs4 import BeautifulSoup
import re

html = """<html>
<body>
<div class="ecopyramid">
<ul id="producers">
<li class="producerlist">
<div class="name">plants</div>
<div class="number">100000</div>
</li>
<li class="producerlist">
<div class="name">algae</div>
<div class="number">100000</div>
</li>
</ul>
<ul id="primaryconsumers">
<li class="primaryconsumerlist">
<div class="name">deer</div>
<div class="number">1000</div>
</li>
<li class="primaryconsumerlist">
<div class="name">rabbit</div>
<div class="number">2000</div>
</li>
</ul>
<ul id="secondaryconsumers">
<li class="secondaryconsumerlist">
<div class="name">fox</div>
<div class="number">100</div>
</li>
<li class="secondaryconsumerlist">
<div class="name">bear</div>

<div class="number">100</div>
</li>
</ul>
<ul id="tertiaryconsumers">
<li class="tertiaryconsumerlist">
<div class="name">lion</div>
<div class="number">80</div>
</li>
<li class="tertiaryconsumerlist">
<div class="name">tiger</div>
<div class="number">50</div>
</li>
</ul>
</body>
</html> """

soup = BeautifulSoup(html, 'lxml')
all_div = soup.div
all_ul = soup.find('ul', { 'id': "secondaryconsumers"})
# print(all_ul.find_previous('li')) #find previous li for ul tag
# print(all_div.find_all_next('li')) # next all li tag.
# print(soup.find('li', {'class': "producerlist"}).text)
#print(soup.find('ul', {'id': "producers"}).get_text(strip=True))
# print([i.text for i in soup.find('ul', {'id': "producers"})])
#print(soup.find(text='50')) #case sensitive.
# print(re.search(r'50', soup.text).group())
# print(soup.text)

# print(soup.find_all('div')) # list of div

# for item in soup.find_all('div'):
# print([item.get_text(strip=True) for item in soup.find_all('div')[1:]])# list of div
#
# print(soup.find_all(['div'], recursive=False))

# print(soup.find_next_sibling('li', {'class':"producerlist"}))
