import json

import requests

url = 'https://explorer.flitsnode.app/get_address_transactions?address=fiexp1irjkvmwuiqv18afddzd8bgwvfric'

req = requests.get(url)
print('\n'.join('|'.join(i) for i in json.loads(req.text)['data']))

# soup = BeautifulSoup(json.loads(req.text), 'html.parser')
# print(soup)
# print(type(soup))
# print(soup['data'])

