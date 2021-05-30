import requests
from bs4 import BeautifulSoup as bs

resultdata = {
'sr': '3',
'et': '2',
'exam': 'ssc',
'year': "2012",
'board': 'chittagong',
'roll': "102275",
'reg': "626948",

 }
headers ={
    'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
    'cookie': 'PHPSESSID=24vp2g7ll9utu1p2ob5bniq263; tcount_unique_eb_log=1',
    'Origin': 'http://www.educationboardresults.gov.bd',
    'Referer': 'http://www.educationboardresults.gov.bd/',
    'Request URL': 'http://www.educationboardresults.gov.bd/result.php'


}
with requests.Session() as s:
    url = 'http://www.educationboardresults.gov.bd/index.php'
    r = s.get(url, headers=headers)
    soup = bs(r.content,'lxml')
    # print(soup.prettify())
#Scraping  and by passing Captcha

    alltable =soup.findAll('td')
    captcha = alltable[56].text.split('+')
    print(captcha)
    value_one, value_two = int(captcha[0]), int(captcha[1])
    print(value_one, value_one)

    resultdata['value_s'] = value_one+value_two

    resultdata['button2'] = 'Submit'
    print(resultdata)
    r=s.post("http://www.educationboardresults.gov.bd/result.php", data=resultdata, headers= headers)
    soup = bs(r.content, 'lxml')
    print(soup.prettify())
