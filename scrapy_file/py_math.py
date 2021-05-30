import requests
from bs4 import BeautifulSoup

URL = "https://www.centrepointstores.com/sa/en/Women/Fashion-Accessories/Watches/CENTREPOINT-Citizen-Women%27s-Rose-Gold-Analog-Metal-Strap-Watch-EU-6039-86A/p/EU603986AGold"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}
r = requests.get("http://www.gentedellarete.it/?pg=news&tf=G&page={}/".format(1), headers=HEADERS)
soup = BeautifulSoup(r.content, 'html.parser')

for x in soup.findAll('div', {'class',"text py-5 pl-md-5"}):
    print('\n',x.select_one("div > a:nth-child(2) h3").text, sep='\n') #heading ok
    print('\n', x.select_one('p').text) #under h3 ok
    print('\n', x.select('p')[1].text) # body ok
    print('\n', x.select('p')[1].text.split('(')[1].strip(')')) # date ok?




