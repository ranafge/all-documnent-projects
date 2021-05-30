from bs4 import BeautifulSoup
import requests
headers = {
"origin": "https://www.reddit.com",
"referer": "https://www.reddit.com/r/programmingmemes/",
# "sec-ch-ua": '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
# "sec-ch-ua-mobile": "?0",
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-origin",
"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}
source = requests.get('https://www.reddit.com/r/programmingmemes/', headers=headers)
print(source.status_code)
soup = BeautifulSoup(source.text, 'lxml')

img = soup.find('div', class_='_3JgI-GOrkmyIeDeyzXdyUD _2CSlKHjH7lsjx0IpjORx14')
link = img.a["href"]
print(link)
image = img.img["src"]
print(image)

img = soup.find('div', class_='_3Oa0THmZ3f5iZXAQ0hBJ0k')

image = img.img["src"]
print(image)
