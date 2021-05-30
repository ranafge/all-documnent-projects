from bs4 import BeautifulSoup
import requests
import csv


my_url = "https://www.billboard.com/charts/hot-100"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
   }
r = requests.get(my_url)
page_soup = BeautifulSoup(r.content, 'lxml')

filename = "Billboard100.csv"
csv_writer = csv.writer(open(filename, 'w'))

Chart = page_soup.find_all('li', {'class': 'chart-list__element display--flex'})

BB = []
for item in Chart:
   Song = item.find('span', class_='chart-element__information__song text--truncate color--primary').text.strip()
   Artist = item.find('span', class_='chart-element__information__artist text--truncate color--secondary').text.strip()
   Rank = item.find('span', class_='chart-element__rank__number').text.strip()
   Billboard = {
         'Song': Song,
         'Artist': Artist,
         'Rank': Rank,
}
   BB.append(Billboard)

   print(BB)

with open("Billboard100.csv", "w", newline="") as infile:
   writer = csv.writer(infile)
   for row in BB:
      writer.writerow([row])
