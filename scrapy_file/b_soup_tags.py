# https://stackoverflow.com/questions/64870372/how-can-i-get-text-without-specific-tags-in-beautifulsoup
from bs4 import BeautifulSoup
html = '''<span class="head">A
</span>Explanation <span style="color: red;">1</span>
<span class="head">B</span>
Explanation <span style="color: red;">2</span>'''
soup = BeautifulSoup(html, 'lxml')
print([i.get_text() for i in soup.find_all('span')])
print(soup.findChild('span', {'class': 'head'}).text)
# for i in soup.findAll('span'):
#     for x in i.find_next():
#         print(x.text)

"""    
<span class="head">A</span>
Explanation 
<span style="color: red;">1</span>

<span class="head">B</span>
Explanation 

<span style="color: red;">2</span>

"""
