# post_url = "https://www.pdfyeah.com/remove-pdf-metadata/"
from bs4 import BeautifulSoup
import requests
headers={
"authority": 'www.pdfyeah.com',
"method": 'POST',
"path": '/remove-pdf-metadata/',
"scheme": 'https',
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US,en;q=0.9",
"cache-control": "max-age=0",
"content-length": "7417836",
"content-type": "multipart/form-data; boundary=----WebKitFormBoundaryLrj8CSAWQunyHjuH",
"cookie": "__gads=ID=a55bd4cd30934aa2-22638084dbc50088:T=1611840370:RT=1611840370:S=ALNI_MZ3rGRB8kMPyngQoZ8ubdqAlE-Cbw; cookiebanner-accepted=1",
"origin": "https://www.pdfyeah.com",
"referer": "https://www.pdfyeah.com/remove-pdf-metadata/",
"sec-ch-ua-mobile": "?0",
"sec-fetch-dest":"document",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "same-origin",
"sec-fetch-user": "?1",
"upgrade-insecure-requests": "1",
}

url = 'https://www.pdfyeah.com/remove-pdf-metadata/'
files = {'upfile': open('/home/rana/Downloads/PyWebScrapingBook.pdf', 'rb')}
session = requests.Session()
session.headers.update(headers)
r = session.post(url, files=files)

print(r.status_code)
soup = BeautifulSoup(r.content, 'lxml')
print(soup.prettify())
search = soup.find(text=True)
print(search)
# session = requests.session()
# session.get(url)
# r = session.post(url, files=files)
# print(r.status_code)
# print(r.text)
# search = r.text.find("Completed")
# print(r.text+"\n")
# print(search)

#
# def scrape(url):
#     with requests.Session() as req:
#         req.headers.update(headers)
#         r = req.get(url).text
#         soup = bs(r, 'lxml')
#         info = soup.find_all('td', {'class': 'first'})
#         res = [[b.text, b.a['href']] for b in info]
#
#         print(res)
