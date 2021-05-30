import re

import requests

from bs4 import BeautifulSoup
from shutil import copyfileobj

url = "https://ganjoor.net/hafez/ghazal/sh1/"
page = requests.get(url).text

text = BeautifulSoup(page, "html.parser").find_all("div", {"class": "m2"})
print([t.text.replace("\u200c", "") for t in text])

pattern = re.compile(r"https://i\.ganjoor\.net/a2?/\d+[-a-z]+?\.mp3")
audio_tracks = re.findall(pattern, page)
print(audio_tracks)

for track in audio_tracks:
    print(f"Fetching track: {track}...")
    with requests.get(track, stream=True) as t, \
            open(track.split("/")[-1], "wb") as a:
        copyfileobj(t.raw, a)
