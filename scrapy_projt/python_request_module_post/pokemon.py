import requests

import requests

headers = {
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'Referer': 'https://pokedex.org/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
}

response = requests.get('https://pokedex.org/js/main.js', headers=headers)

print(response.status_code)
# print(response.json())
print(response.text)
