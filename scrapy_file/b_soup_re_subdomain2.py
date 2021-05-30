import requests
import re
from bs4 import BeautifulSoup

headers = {
    'Host' : 'dnsdumpster.com',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language' : 'en-US,en;q=0.5',
    'Accept-Encoding' : 'gzip, deflate',
    'DNT' : '1',
    'Upgrade-Insecure-Requests' : '1',
    'Referer' : 'https://dnsdumpster.com/',
    'Connection' : 'close'
}

proxies = {
    'http' : 'http://127.0.0.1:8080'
}

domain = 'google.com'

with requests.Session() as s:
    url = 'https://dnsdumpster.com'
    response = s.get(url, headers=headers, proxies=proxies)
    response.encoding = 'utf-8' # Optional: requests infers this internally
    soup1 = BeautifulSoup(response.text, 'html.parser')
    input = soup1.find_all('input')
    csrfmiddlewaretoken_raw = str(input[0])
    csrfmiddlewaretoken = csrfmiddlewaretoken_raw[55:119]
    data = {
        'csrfmiddlewaretoken' : csrfmiddlewaretoken,
        'targetip' : domain
    }
    send_data = s.post(url, data=data, proxies=proxies, headers=headers)
    print(send_data.status_code)
    soup2 = BeautifulSoup(send_data.text, 'html.parser')
    td = soup2.find_all('td', {"class": "col-md-4"})
    mydomain = []
    for i in range(len(td)):
        subdomain = td[i].text.strip()
        mydomain.append(subdomain)

# filter_mydomain
filtered_subdomain = []
for sub in mydomain:
    if sub.endswith('.'):
        res = sub[:len(sub)-1]
        filtered_subdomain.append(res)
    else:
        filtered_subdomain.append(sub)

print(filtered_subdomain)
