# import requests
# from bs4 import BeautifulSoup
#
# search_url = "https://store.steampowered.com/search/?sort_by=Price_ASC&category1=998%2C996&category2=29"
# category1 = ('998', '996')
# category2 = '29'
#
# params = {
#     'sort_by': 'Price_ASC',
#     'category1': ','.join(category1),
#     'category2': category2,
# }
#
# response = requests.get(
#     search_url,
#     params=params
# )
# # print(response.url)
# soup = BeautifulSoup(response.text, "html.parser")
# prices = soup.select('span[style="color: #888888;"]')
# prcs = soup.find_all("div",{"class": "col search_price discounted responsive_secondrow"})
#
# for p in prcs:
#     print(p.contentssc)

# for d in soup.select_one('span[style="color: #888888;"]'):
#     print(d)
#     print(d.next)

# <div class="col search_price discounted responsive_secondrow">
# <span style="color: #888888;"><strike>$0.90</strike></span><br/>$0.09                    </div>


# elms = soup.find_all("span", {"class": "title"})
# prcs = soup.find_all("div",{"class": "col search_price discounted responsive_secondrow"})
# for elm in elms:
#     print(elm.text)
# for prc in prcs:
#     print(prc.text)

import requests
import json
url = 'https://arizonamedicalmarijuanaclinic.com/wp-admin/admin-ajax.php?action=wp_ajax_ninja_tables_public_action&table_id=42643&target_action=get-all-data&default_sorting=old_first'

import requests

headers = {
    'authority': 'arizonamedicalmarijuanaclinic.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://arizonamedicalmarijuanaclinic.com/dispensaries/',
    'accept-language': 'en-US,en;q=0.9',
}

params = (
    ('action', 'wp_ajax_ninja_tables_public_action'),
    ('table_id', '42643'),
    ('target_action', 'get-all-data'),
    ('default_sorting', 'old_first'),
)

response = requests.get('https://arizonamedicalmarijuanaclinic.com/wp-admin/admin-ajax.php', headers=headers, params=params)

print(response.status_code)

for data in response.json():
    print(data['value']['dispensaryname'])
