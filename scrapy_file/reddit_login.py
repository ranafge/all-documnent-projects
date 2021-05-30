import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"
}
def main(url):
    with requests.Session() as req:
        req.headers.update(headers)
        response = req.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        csrf = soup.find('div',{"class": "App m-desktop"}).find(attrs={'name':'csrf_token'}).get('value')
        payload = {'username':'username','password':'password',"csrf_token":csrf}
        username = 'username'
        login_url = f"https://www.reddit.com/user/{username}"
        data = req.get(login_url, data=payload)
        print(data.content)
        print(data.status_code)

url = 'https://www.reddit.com/login/'
main(url=url)
