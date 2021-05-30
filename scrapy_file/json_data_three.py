import requests
import json
import codecs
from pandas.io.json import json_normalize
from bs4 import BeautifulSoup

import unicodedata

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQaftrT4JJh6dqfFHaUuxiOE5CiFDTt2YIbiJe9sATHQrBILnfUVpSnDTKg26yTgmZKci4NVxtsByD7/pubchart?oid=1258306542&format=interactive"
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.text, features="html.parser")
scripts = soup.find_all('script')[1]
# print(scripts)
for script in scripts:
    if 'chartJson' in script:
        encoded_string = script
        # print(encoded_string, end='\n\n*****************88')
        encoded_string = encoded_string.split("'chartJson': '",1)[-1]
        # print(encoded_string)
        encoded_string = encoded_string.split("parsedNumHeaders",1)[0]
        # print(encoded_string[0])
        # print(codecs.getdecoder('unicode-escape')(encoded_string[1]))
        # print(codecs.getdecoder('unicode-escape')(encoded_string)[0])
        jsonStr = codecs.getdecoder('unicode-escape')(encoded_string)[0]
        print(jsonStr)
        # jsonStr = jsonStr.split(',\\"parsedNumHeaders\\":1',1)[0]
        # jsonStr = jsonStr.split('"rows":',1)[1]
        # jsonStr = jsonStr.split('"cols":',1)[0].rstrip(',')
        # jsonStr = jsonStr.encode('utf8').decode('unicode_escape')
        # jsonObj = json.loads(jsonStr)
