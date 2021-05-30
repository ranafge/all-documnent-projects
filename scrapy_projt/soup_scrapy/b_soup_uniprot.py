from bs4 import BeautifulSoup
html = """<a href="/watch/36242552" class="thumbnail video vod-show play-video-trigger user-can-watch" data-video-id="36242552" data-video-type="show">"""

# html_content = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
# print(soup.select('a href[data-video-id]'))
ids = [tag['data-video-id'] for tag in soup.select('a') if tag['data-video-id']]
print(ids)
