import requests
from bs4 import BeautifulSoup
search = input("Search for:")

url = f'https://www.bing.com/search?q={search}&qs=n&form=QBRE&sp=-1&pq={search}&sc=8-2&sk=&cvid=6DB4EB34420C49ACB66D5B78B163F2E8'

print(url)

r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})#does not return search results

# print(results)
links = results.findAll("li")
# print(links)
for item in links:
    print(item)

