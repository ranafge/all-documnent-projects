import time

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(
    requests.get("https://www.bayt.com/en/international/jobs/executive-chef-jobs/").content,"lxml")

links = soup.select('h2.m0.t-regular')
for link in links:
    print(link.a['href'])

print(soup.find_all("h2", class_="m0 t-regular")[0])
follow_links = [
     a.find_next('a') for a in
     soup.find_all("h2", class_="m0 t-regular")
     # if "#" not in a.find_next.a["href"]
 ]
print(follow_links)
