import requests
from bs4 import BeautifulSoup
text = """<a>   
   "1447 Acres &nbsp; Council, Adams County, ID"
    <br>
    "1,190,000" 
</a>"""                                                                                                                                  

soup = BeautifulSoup(text, 'lxml')

print(''.join(soup.get_text(strip=True, separator='\n').replace('"', '')))


