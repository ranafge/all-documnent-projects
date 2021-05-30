import requests
from bs4 import BeautifulSoup
import json
import codecs
from pandas.io.json import json_normalize

url = 'https://understat.com/player/2097'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
scripts = soup.find_all('script')
# print(scripts)
    # I noticed the data was imbedded in the script tag that started with `var shotsData`
for script in scripts[3]:
    if 'player_info' in script:
        encoded_string = script
        encoded_string = encoded_string.split("JSON.parse('",1)[-1]

        jsonStr = codecs.getdecoder('unicode-escape')(encoded_string)[0].split("]'),")[0]
        print(jsonStr)
        codecs.getdecoder('unicode-escape')(encoded_string)

        # I store that text, then trim off the string on the ends so that
        # it's in a valid json format
        # encoded_string = script
        # print(encoded_string)
        # encoded_string  = encoded_string .split("JSON.parse('", 1)[-1]
        # print(encoded_string)
        # encoded_string = encoded_string.rsplit("player_info =",1)[0]
        # encoded_string = encoded_string.rsplit("'),",1)[0]
        # # Have it ignore the escape characters so it can decode the ascii
        # # and be able to use json.loads
        # jsonStr = codecs.getdecoder('unicode-escape')(encoded_string)[0]
        # print(jsonStr)
        # jsonObj = json.loads(jsonStr)
        # print(jsonObj)
        #
        # df = json_normalize(jsonObj)
        # print(df)
