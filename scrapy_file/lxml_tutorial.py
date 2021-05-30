import requests
from lxml import etree
from bs4 import BeautifulSoup

url = "https://www.westernunion.com/us/en/web/send-money/start?SrcCode=12345&ReceiveCountry=IN&SendAmount=100&ISOCurrency=CNY&FundsOut=BA&FundsIn=CreditCard"

page = requests.get(url).text
# soup = BeautifulSoup(page.content, 'html.parser')
# doc = etree.xmlfile(soup.prettify())
root = etree.fromstring(page)
for tx in root.xpath('//span'):
    print(tx.text)