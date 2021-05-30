from bs4 import BeautifulSoup
import requests

url = 'https://www.eurekalert.org/'
login = 'login'

headers = {'origin': url,
           'referer': url+login}

s = requests.session()

login_payload = {'login': 'xxx',
                 'password': 'xxx'}

# i have read that it should be .post here, but I do not have anywhere .post on the website
login_req = s.post(url+login, headers=headers, data = login_payload)
print(login_req) # returns 200, if i try .get it also returns 200


login_response = s.get(url+'reporter/embargoed.php')
print(login_response) # returns 200
soup = BeautifulSoup(login_response.content, 'html.parser')
print(soup) # prints HTML but not the HTML that I want
