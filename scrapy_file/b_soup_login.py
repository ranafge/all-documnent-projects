import requests
import re
import json

sites = [
    "https://steamcommunity.com/market/listings/730/AK-47%20%7C%20Redline%20%28Field-Tested%29"
]
for url in sites:
    r = requests.get(url)
    page_source = r.text
    # print(page_source)
    results = re.search(r'var line1=(\[.*\])',page_source).group(1)
    list_of_list = json.loads(results)
    # print(list_of_list)
    for list in list_of_list:
        for data in list:
            print(data)
        # print(list[0], '\n')


