import requests

with requests.Session() as req:
    headers = {
        'authority': 'login.mbc.net',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'origin': 'https://shahid.mbc.net',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://shahid.mbc.net/',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': '_gcl_au=1.1.1199633606.1614921781; WZRK_G=38c72e930fdb4b74837aa643dc47b107; _ga=GA1.1.1880367528.1614921781; _scid=a233719a-6581-477a-a7db-7111775ad5d2; gmid=gmid.ver4.AcbHoSuw-Q.WFFC0rz1YY3Z8Jkf3PSY2-d85Q20q4ngU541yDeCdCPz9Jb4_6zdRw9_rHKK7NHL.4vpNb7p4gJcxVMMRVoaPaKM774BnYDXqsNqgEqF8-DNz6t5OzbeAT9DpKFeAh6cnMbi_rbYE-mVIQT7isOAPIg.sc3; ucid=ctWpLfyUS5YIrftLu6u8-w; hasGmid=ver4; gig_bootstrap_3_Pm0x4fe9XSy6gv04PewESwqZ_HLgUCbXwWWPHCbGmUGFbW1xyHa42dFt0XTVay0T=login_ver4; _fbp=fb.1.1614921782478.439841241; _sctr=1|1614880800000; PAPVisitorId=JL2A8d7cVVZ64SlP4IkRS6AFl9t5nmdv; _ga_9ZLGVMG0QJ=GS1.1.1614921780.1.1.1614924710.2; WZRK_S_65W-567-675Z=%7B%22p%22%3A12%2C%22s%22%3A1614921781%2C%22t%22%3A1614924710%7D',
    }

    data = {
      'loginID': 'ranafge@gmail.com', # registered Email
      'password': 'pass1478',
      'sessionExpiration': '0',
      'targetEnv': 'jssdk',
      'include': 'profile,data',
      'includeUserInfo': 'true',
      'lang': 'en',
      'APIKey': '3_Pm0x4fe9XSy6gv04PewESwqZ_HLgUCbXwWWPHCbGmUGFbW1xyHa42dFt0XTVay0T',
      'sdk': 'js_latest',
      'authMode': 'cookie',
      'pageURL': 'https://login.mbc.net/accounts.login',
      'sdkBuild': '11903',
      'format': 'json'
    }
    req.headers.update(headers)
    r = req.post('https://login.mbc.net/accounts.login',data=data)
    print(r.json()['statusCode']) # 200
    print(r.json()['isRegistered']) # True
    print(r.json()['profile']) # {'email': 'XXX@yyyy.com'}
    r = req.get('https://shahid.mbc.net/en/home')
    print(r.status_code)
    print(r.text)


    # statusCode= 200
    # isRegistered= True
    # profile= {'email': 'XXX@yyyy.com'}


    # print(r.status_code)
    # r = req.get("https://shahid.mbc.net/en/home")
    #
    # soup = BeautifulSoup(r.content, 'lxml')
    # for div in soup.find_all('div'):
    #     print(div, end='\n\n\n')




