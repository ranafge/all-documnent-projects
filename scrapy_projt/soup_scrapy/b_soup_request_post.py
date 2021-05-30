import requests
from bs4 import BeautifulSoup
import requests
prodlink=[]

cookies = {
    'ESOLVE': '537507d0d2226637df7896bac091d648',
    '_ga': 'GA1.3.677450556.1613230295',
    '_gid': 'GA1.3.1046474275.1613230295',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://www.storeandmore.co.za',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary57WatmxVwMPvJzr4',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www.storeandmore.co.za/subcategory/crates_and_food_bins',
    'Accept-Language': 'en-US,en;q=0.9',
}

data = {
  '$------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name': '"MAX_FILE_SIZE"\\r\\n\\r\\n5000000\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="dowhat"\\r\\n\\r\\n\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="menu_id"\\r\\n\\r\\n107\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="id"\\r\\n\\r\\n487\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="host"\\r\\n\\r\\nhttps://www.storeandmore.co.za/\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="module"\\r\\n\\r\\nbin/storeandmore.geckonet.co.za/\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="process_step"\\r\\n\\r\\n0\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="user_conversion_rate"\\r\\n\\r\\n1\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="user_currency_symbol"\\r\\n\\r\\nR\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="itemindex"\\r\\n\\r\\n\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="discount_system"\\r\\n\\r\\nqty\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="store_location_id"\\r\\n\\r\\n\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="temp_latitude"\\r\\n\\r\\n\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="temp_longitude"\\r\\n\\r\\n\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="temp_fulltext_user_address"\\r\\n\\r\\n\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="searchphrase"\\r\\n\\r\\n\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="dowhat_search"\\r\\n\\r\\n\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="basket_total_items"\\r\\n\\r\\n0\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="Submit_Inc"\\r\\n\\r\\n\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="Email_Inc"\\r\\n\\r\\n\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="Password_Inc"\\r\\n\\r\\n\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="sorting_order"\\r\\n\\r\\n0\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="code_0"\\r\\n\\r\\n101-2-00526\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="code_1"\\r\\n\\r\\n101-2-00527\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="code_2"\\r\\n\\r\\n101-2-00528\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="code_3"\\r\\n\\r\\n101-2-00534\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="code_4"\\r\\n\\r\\n101-2-00535\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="code_5"\\r\\n\\r\\n101-2-00536\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="code_6"\\r\\n\\r\\n101-2-00532\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="code_7"\\r\\n\\r\\n101-2-00531\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="code_8"\\r\\n\\r\\n101-2-00533\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="code_9"\\r\\n\\r\\n103-4-00040\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="code_10"\\r\\n\\r\\n107-2-00065\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="code_11"\\r\\n\\r\\n107-2-00036\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="code_12"\\r\\n\\r\\n107-2-00054\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="code_13"\\r\\n\\r\\n107-2-00024\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="code_14"\\r\\n\\r\\n107-2-00025\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="code_15"\\r\\n\\r\\n107-2-00066\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="code_16"\\r\\n\\r\\n107-2-00067\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="code_17"\\r\\n\\r\\n107-2-00047\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="code_18"\\r\\n\\r\\n107-2-00046\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="code_19"\\r\\n\\r\\n107-2-00006\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="code_20"\\r\\n\\r\\n107-2-00026\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="code_21"\\r\\n\\r\\n107-2-00027\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="code_22"\\r\\n\\r\\n107-2-00028\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="code_23"\\r\\n\\r\\n107-2-00029\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="23c2cf7139e4775f5f4b9fe5deb183c70cae0e3c"\\r\\n\\r\\n2\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4\\r\\nContent-Disposition: form-data; name="sort"\\r\\n\\r\\nt1.`name`\\r\\n------WebKitFormBoundary57WatmxVwMPvJzr4--\\r\\n'
}

url='https://www.storeandmore.co.za/subcategory/crates_and_food_bins'
response1 = requests.get(url)

response2 = requests.post('https://www.storeandmore.co.za/sef/form_handler.php', headers=headers, cookies=cookies, data=data)
responses = [response1, response2]
for response in responses:

    soup = BeautifulSoup(response.text, 'html.parser')
    prodlink.append(response.url)
    for i in soup.find_all('a', class_='product_link'):
        prodlink.append(i['href'])

print(prodlink)
print(len(prodlink))
