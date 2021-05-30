import requests
from bs4 import BeautifulSoup
import csv

pages = [ 0 , 25 , 50 , 75]
for page in pages:

    source = requests.get('https://finance.yahoo.com/screener/predefined/day_gainers?count=25&offset={}'.format(page)).text


    soup = BeautifulSoup(source , 'lxml')


    for link in soup.find_all("a"):
        table = soup.find("table",{"class":"W(100%)"})
        thead = table.find("thead").find_all("th")
        table_head = [th.text for th in thead]
        #print(table_head)

        table_body = table.find ("tbody").find_all("tr")

        with open("report.csv" , "a" , newline="") as csv_file:
                csv_write = csv.writer(csv_file)
                csv_write.writerow(table_head)

                for tr in table_body:
                    table_data = [td.text.strip() for td in tr.find_all('td') ]
                    csv_write.writerow(table_data)
