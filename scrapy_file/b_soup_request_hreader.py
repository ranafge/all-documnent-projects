import requests
url = 'https://yts.mx/api/v2/list_movies.json'
# headers ={
#
# "Host": "yts.mx",
# "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
# "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
# "Accept-Language": "en-US,en;q=0.5",
# "Accept-Encoding": "gzip, deflate, br",
# "Connection": "keep-alive",
# "Cookie": "__cfduid=dc7c362f485cca2fe8a95d47804e05a4a1608557390; PHPSESSID=fma859uj26g18sifi23l10kvhc",
# "Upgrade-Insecure-Requests": "1",
# "Cache-Control": "max-age=0",
# "TE": "Trailers",
# }
res = requests.get(url)
print(res.json())
