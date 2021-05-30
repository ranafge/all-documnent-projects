
from bs4 import BeautifulSoup

page = """<ul id="name1">
            <li>li1</li>
            <li>li2</li>
            <li>li3</li>
            <li>li4</li>
        </ul>
        <ul id="name2">
             <li>li5</li>
             <li>li6</li>
             <li>li7</li>
         </ul>"""

soup = BeautifulSoup(page,'lxml')
ul_tag = soup.find_all('ul', {"id": ["name1", "name2"]})

for i in ul_tag:
    print(i.text)
