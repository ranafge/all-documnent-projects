import requests
from bs4 import BeautifulSoup
# specify the URL of the archive here
url = 'https://cdn-cf-east.streamable.com/video/mp4/g6f986.mp4?Expires=1621994280&Signature=IqySuJxyVi9pCmC~JUhl-iyp-LmG6OiAFfQeu-~-a55osCfu9VrksEhzaQzJlMxAHcSt1R4j9Pt-G8sblQeFt3UtGqY-neHJkC4mUxuHjxGWAWdksyiAxkMb8DYRLkvIseUfkbKbeO6Dt807QwMkspFmXYdzljm8DLho6nMQfC--jtfy8B2gONhA9YUmK2o~fUHwTHzTXXqNGct2hQl-B9cFLDBdj8LXWTj-75YInwWxLwtoenKK~qLahGtJXKXvxTVltxMvUYXXvP9F~WfhNIhNqns1JKrrrqJ~N1XunZHCv~IVJyzOEvrn2G4J5LMIn~dcEZ9frV3APHsE4D~HQA__&Key-Pair-Id=APKAIEYUVEN4EVB2OKEQ'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

with open('video.mp4', 'wb') as f_out:
    r = requests.get(url, headers=headers, stream=True)
    print(r)
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            f_out.write(chunk)
