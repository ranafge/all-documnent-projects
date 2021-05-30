import requests
import json
import pandas as pd
#
# link = "http://123.253.36.205:8051/API/Member/GetMembersList?searchString=&zone=0&blacklisted=false"
# r = requests.get(link)
#
# for item in r.json():
#     print(item['NameOfOrganization'])
#     print(item['Phone'])
#     print(item['MobileNo'])
#     print(item['Email'])




# ok, its work.
# convert sting to a file object using
#io.StringIo and pass to the csv module

from io import StringIO
import csv

scsv = """text,with,Polish,non-Latin,letters
1,2,3,4,5,6
a,b,c,d,e,f
gęś,zółty,wąż,idzie,wąską,dróżką,
"""

f = StringIO(scsv)
# print(f)
# print(type(f))
# reader = csv.reader(scsv.split('\n'), delimiter=',')
# print(reader)
# for row in reader:
#     print('\t'.join(row))

# print('alveen')
#
# class Myobject:
#     pass

# initalize Myobject class.
# mo = Myobject()
# mo.name = 'rana'
# print(mo.name)
from lxml import etree
txt = '''<span _ngcontent-his-c101="" id="driveValue" class="ng-binding ng-scope"> 1.00 TK = 779.8<span _ngcontent-his-c101="">Disk Drive Value</span>(DDV) </span>'''

root = etree.fromstring(txt)
for td in root.xpath('//span[contains(@id, "driveValue")]'):
    print(td.text)
