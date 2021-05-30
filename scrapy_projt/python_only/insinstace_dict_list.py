from bs4 import BeautifulSoup
import requests
import pandas as pd
page = requests.get("https://www.morele.net/pralka-candy-cs4-1062d3-950636/?sekcja=reviews-all")

soup = BeautifulSoup(page.content, "html.parser",
).find_all("div", {"class":"reviews-item"}) 
# print(soup)
morele = [div.getText(strip=True) for div in soup]

print(morele)
csv_table = pd.DataFrame(morele)
csv_table = csv_table.reset_index(drop=True)
csv_table.insert(0,'No.',csv_table.index)