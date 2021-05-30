import requests
from bs4 import BeautifulSoup
import ssl
url = "https://www.bloomberg.com/quote/SPX:IND"
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")

text = soup.find('div', text=True)
print(text)
