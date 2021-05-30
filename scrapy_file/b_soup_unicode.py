from bs4 import BeautifulSoup
import requests

url = 'https://www.hkgem.com/statistics/daily/e_G201201.htm'
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
print("Requesting data from HKGEM...")
url_obj = requests.get(url, headers=header)
print("Status : ", url_obj.status_code)
soup = BeautifulSoup(url_obj.content, "lxml")
file_name = "GEM_stock_data.txt"
file = open(file_name, 'w')
file.write(str(soup))
file.close()
