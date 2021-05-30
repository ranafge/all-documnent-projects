import requests
from bs4 import BeautifulSoup
# r = requests.get(url)
soup = BeautifulSoup("""<span class="imgInner">
<img src="https://cdn.cloudflare.com/image.jpg" alt="image" title="image">
</span>""", 'lxml')
image = soup.select_one('span.imgInner img')['src']
print(image)
