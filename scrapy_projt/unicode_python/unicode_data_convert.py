import unicodedata
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
 'Host': 'www.lieferando.de',
 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0',
 'Upgrade-Insecure-Requests': 1}
url = 'https://www.lieferando.de/speisekarte/dreamburger-pizza'
email = 'info&commat;lieferando&period;de'
res = unicodedata.normalize('NFKD', email).encode('ascii', 'ignore').decode('ascii')
print(res)

