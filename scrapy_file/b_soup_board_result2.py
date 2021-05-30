import requests
from bs4 import BeautifulSoup

link = 'http://www.educationboardresults.gov.bd/'
result_url = 'http://www.educationboardresults.gov.bd/result.php'

resultdata = {
    'sr': '3',
    'et': '2',
    'exam': 'ssc',
    'year': 2012,
    'board': 'chittagong',
    'roll': 102275,
    'reg': 626948,
    'button2': 'Submit',
 }

def get_number(s,link):
    r = s.get(link)
    soup = BeautifulSoup(r.text,"lxml")
    num = 0
    captcha_numbers = soup.select_one("tr:has(> td > #value_s) > td + td").text.split("+")
    for i in captcha_numbers:
        num+=int(i)
    return num

with requests.Session() as s:
    s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    resultdata['value_s'] = get_number(s,link)
    r = s.post(result_url, data=resultdata)
    print(r.text)
