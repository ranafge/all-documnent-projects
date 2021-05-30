import requests

def reqeuestApi(url, key):
    return requests.get(url=url).json(key, None)
