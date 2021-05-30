import requests as re
from bs4 import BeautifulSoup as bs
r = re.get("https://skidlamer.github.io/js/Skidfest.user.js")
soup = bs(r.text.encode('utf-8'),"lxml")

with open("script.txt","w") as file:
    file.write(str(soup))
