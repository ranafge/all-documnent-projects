from bs4 import BeautifulSoup
import requests
import re

# html = "<p>text <span>more text</span> additional text</p>"
# soup = BeautifulSoup(html,'html.parser')
# for match in soup.findAll('span'):
#     match.unwrap()
# myindend_text = ''
# for string in soup.strings:
#
#     myindend_text += string.strip()+' '
#
# print(myindend_text)

soup = BeautifulSoup(requests.get("https://rotogrinders.com/team-stats/nfl-allowed?sport=nfl&position=QB&site=draftkings&range=season").content, 'lxml')

scripts = soup.find_all('script')
print(scripts[14].string)
script_14 = scripts[14].string
# print(len(scripts))
script_data = re.search(r"data = (.*)",script_14).group(1)
print(script_data)
import json

print(json.loads(script_data))
print('Shoul dok')
print([(d['att'], d['team']) for d in json.loads(script_data) ])
