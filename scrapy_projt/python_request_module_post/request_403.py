import requests
import requests

headers = {
    'authority': 'www.interencheres.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-dest': 'image',
    'referer': 'https://www.interencheres.com/',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': '__cfduid=dc3783a7516d9e83b69ed0a9e2712d2241613991477; __cf_bm=03cd9197cb2a5b18b6edb82811cb1e747cd90211-1613991479-1800-AXfnMb/xhytPCzg11IwYDy4AL3oXSTJCgKQEHz8XSyQI8fVV9BePwvbSwSyMDRZbkDl7RzGrwhJ2+i0JZc48i0AFsRMzn+N50NxoKAGYzYKN; ry_ry-5hfg18fm_realytics=eyJpZCI6InJ5XzFBQjRCRUE5LUY5QzQtNEZFNS04RDFGLUU1QjlCRTczMUM4NiIsImNpZCI6bnVsbCwiZXhwIjoxNjQ1NTI3NDgxMjY3LCJjcyI6bnVsbH0%3D; ry_ry-5hfg18fm_so_realytics=eyJpZCI6InJ5XzFBQjRCRUE5LUY5QzQtNEZFNS04RDFGLUU1QjlCRTczMUM4NiIsImNpZCI6bnVsbCwib3JpZ2luIjp0cnVlLCJyZWYiOm51bGwsImNvbnQiOm51bGwsIm5zIjpmYWxzZX0%3D; datadome=1uPdoUFt3-bS67ui2au09wy2QJcwj.ZZcyB9AJzIAVxRKu5PtE8AIjN1-FxhOskCa-SQQEP5fNNaMry6E_.bNIXUm0LmdyBHRd-Zwp964a; _ga=GA1.2.620286977.1613991484; _gid=GA1.2.133505085.1613991484; _gat_UA-163212-21=1',
}

response = requests.get('https://www.interencheres.com', headers=headers)
print(response.status_code)
