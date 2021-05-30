import pandas as pd
from pandas import json_normalize
data = [
  {
    "trend": {
      "id": "387",
      "radio_id": "149",
      "count": "6075"
    },
    "radio": {
      "id": "149",
      "name": "Bayern 1 Munchen",
      "radio_url": "https:\/\/br-edge-30aa-fra-ts-cdn.cast.addradio.de\/br\/br1\/franken\/mp3\/mid",
      "image_url": "https:\/\/www.radiosbackend.com\/radiogermany\/uploads\/bayern-1-munchen.png",
      "added": "2020-12-14 18:13:41",
      "cat_id": "91",
      "image_file": "bayern-1-munchen.png"
    }
  },
  {
    "trend": {
      "id": "218",
      "radio_id": "764",
      "count": "2648"
    },
    "radio": {
      "id": "",
      "name": "",
      "radio_url": "",
      "image_url": "",
      "added": "",
      "cat_id": "",
      "image_file": ""
    }
  },
  {
    "trend": {
      "id": "6862",
      "radio_id": "1843",
      "count": "1"
    },
    "radio": {
      "id": "1843",
      "name": "Radio Musik-Train",
      "radio_url": "http:\/\/streamplus53.leonex.de:11112\/;",
      "image_url": "https:\/\/www.radiosbackend.com\/radiogermany\/uploads\/2e630aed01a46e22f43afde7440b2d8c.jpg",
      "added": "2020-12-12 21:49:05",
      "cat_id": "111",
      "image_file": "2e630aed01a46e22f43afde7440b2d8c.jpg"
    }
  }
]

data = json_normalize(data)
print(data.head())
