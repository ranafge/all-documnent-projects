import requests
headers = {"User-Agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Mobile Safari/537.36'}
mvideo_requests =requests.get('https://www.mvideo.ru/smartfony-i-svyaz-10/smartfony-205/f/category=iphone-914', headers = headers)
print(mvideo_requests.status_code)
