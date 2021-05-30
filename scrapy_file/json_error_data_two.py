import re
import json
import codecs
import requests
from bs4 import BeautifulSoup
from pandas.io.json import json_normalize 
r = requests.get('https://understat.com/league/EPL')
soup = BeautifulSoup(r.content, 'lxml')
# print(soup.prettify())
scripts = soup.find_all('script')[1]
# print(scripts)

pattern = re.compile(r"JSON.parse\((.*)\),")
data = pattern.findall(r.text)[0]
# print(data)
mydata = codecs.getdecoder('unicode-escape')(data)[0]
print(mydata)
jsonStr = json.loads(mydata[1:-1])

df = json_normalize(jsonStr)
print(df)


















