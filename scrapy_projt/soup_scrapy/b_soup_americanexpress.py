
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import requests
import re
import json
AMEXurl = ['https://www.americanexpress.com/in/credit-cards/all-cards/?sourcecode=A0000FCRAA&cpid=100370494&dsparms=dc_pcrid_408453063287_kword_american%20express%20credit%20card_match_e&gclid=Cj0KCQiApY6BBhCsARIsAOI_GjaRsrXTdkvQeJWvKzFy_9BhDeBe2L2N668733FSHTHm96wrPGxkv7YaAl6qEALw_wcB&gclsrc=aw.ds']

identity = ['filmstrip_container']

r = requests.get(AMEXurl[0])

html_1 = urlopen(AMEXurl[0])

soup_1 = BeautifulSoup(r.content,'lxml')

# Extracting All Images

# images = soup_1.find_all('img', src=True)
#
# for img in images:
#     print(img['src'])
#
#
# # all image tags that display png files.
# platinum_card_image=soup_1.find_all('img', src=re.compile('\.svg$'))
#
# for img in platinum_card_image:
#     print(img.get('src'))
import pprint
images_7 = soup_1.select('script')[8].string.split('__REDUX_STATE__ = ')
data = images_7[1]

for d in json.loads(data)["modelData"]['componentFeaturedCards']['cards']:
    print(d['imgurl'])

