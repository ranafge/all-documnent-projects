from bs4 import BeautifulSoup
from bs4 import element

s = '''
<div class="block">aaa
 <p> bbb</p>
 <p> ccc</p>
 <h1>ddd</h1>
</div>
'''

soup = BeautifulSoup(s, "lxml")
for e in soup.find('div', {"class": "block"}):
    # print(e)
    print(e.strip())
    print(type(e))
    # if type(e) == element.NavigableString and e.strip():
    #     print(e.strip())
# aaa
