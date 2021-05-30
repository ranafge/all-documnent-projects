import requests
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
    td = soup2.find_all('td', {'class': 'col-md-3'})
    # for dom in range(0, len(td),2):
    #     print(td[dom].get_text(strip=True, separator='\n'))

    mysubdomain = []
    for dom in range( len(td)):
        # print(td[dom].get_text(strip=True, separator='\n'))
        if '.' in td[dom].get_text(strip=True):
            x = td[dom].get_text(strip=True, separator=',').split(',')
            mysubdomain.append(x)
            # print(x)
            # y = td[dom].get_text(strip=True, separator=',').split(',')[1]
            # mysubdomain.append(x)
            # mysubdomain.append(y)
            # mysubdomain.append(td[dom].get_text(strip=True, separator=','))
    print(mysubdomain)
    # print(td)

    # for i in range(len(td)):
        # item = str(td[i])
        # print('\n', item, '\n')
        # subdomain = item[21:37]
        # print(subdomain)
from functools import reduce
flat_list_of_mysubdomain = reduce(lambda x, y: x + y, mysubdomain)
print(flat_list_of_mysubdomain)

print(len(mysubdomain) *2)
print(len(flat_list_of_mysubdomain))
