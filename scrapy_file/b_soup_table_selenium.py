import requests
from bs4 import BeautifulSoup
from selenium import webdriver

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}
URL = "https://fuelkaki.sg/home"
webdriver = webdriver.Chrome()
webdriver = webdriver.get(URL)

soup = BeautifulSoup(webdriver.page, 'html.parser')

for row in soup.select('table', {'class': 'table'}):
    for tr in row.find_all('tr')[1:]:
        tds = tr.find_all('td')
        # for i in tds:
        #     print(i.text)
        # print(len(tds))
        print(tds[0].text,tds[1].text, tds[2].text,tds[3].text,tds[4].text, tds[5].text)

webdriver.quit()

""" 
[<td style="border-color: rgb(39, 102, 173);"><div class="fuel-name">Esso</div><div class="time">2‬‬‬‬0‬‬‬‬ ‬‬‬‬O‬‬‬‬c‬‬‬‬t‬‬‬‬o‬‬‬‬b‬‬‬‬e‬‬‬‬r‬‬‬‬ ‬‬‬‬2‬‬‬‬0‬‬‬‬2‬‬‬‬0‬‬‬‬,‬‬‬‬ ‬‬‬‬0‬‬‬‬4‬‬‬‬:‬‬‬‬5‬‬‬‬2‬‬‬‬p‬‬‬‬m</div></td>, <td><div><div><div><div><div><div><div><div><div><span>S$ </span>1‬.‬7‬0</div></div></div></div></div></div></div></div></div></td>, 
<td><div><div><div><div><div><span>S$ </span>1‬‬‬‬.‬‬‬‬9‬‬‬‬8</div></div></div></div></div><span class="price_subtext">Regular</span></td>,
 <td><div><div><span>S$ </span>2‬.‬0‬2</div></div><span class="price_subtext">Extra</span></td>,
  <td><div><div><div><div><div><div><div><div><div><div><div><div><span>S$ </span>2‬‬‬.‬‬‬4‬‬‬3</div></div></div></div></div></div></div></div></div></div></div></div><span class="price_subtext">(Synergy Supreme+)</span></td>,
   <td>N.A.</td>]
[<td style="border-color: rgb(255, 213, 0);"><div class="fuel-name">Shell</div><div class="time">3‬‬‬0‬‬‬ ‬‬‬O‬‬‬c‬‬‬t‬‬‬o‬‬‬b‬‬‬e‬‬‬r‬‬‬ ‬‬‬2‬‬‬0‬‬‬2‬‬‬0‬‬‬,‬‬‬ ‬‬‬1‬‬‬1‬‬‬:‬‬‬3‬‬‬7‬‬‬a‬‬‬m</div></td>, <td><div><div><div><div><div><div><div><div><span>S$ </span>1‬‬‬.‬‬‬7‬‬‬0</div></div></div></div></div></div></div></div></td>, <td>N.A.</td>, <td><div><div><div><div><div><div><span>S$ </span>2‬‬‬.‬‬‬0‬‬‬2</div></div></div></div></div></div></td>, <td><div><div><div><div><div><div><div><div><div><div><span>S$ </span>2‬‬‬‬‬‬.‬‬‬‬‬‬4‬‬‬‬‬‬7</div></div></div></div></div></div></div></div></div></div></td>, <td><div><div><div><div><div><span>S$ </span>2‬‬‬‬‬‬.‬‬‬‬‬‬6‬‬‬‬‬‬9</div></div></div></div></div><span class="price_subtext">(Shell V-Power)</span></td>]
[<td style="border-color: rgb(0, 0, 0);"><div class="fuel-name">Sinopec</div><div class="time">2‬‬‬6‬‬‬ ‬‬‬O‬‬‬c‬‬‬t‬‬‬o‬‬‬b‬‬‬e‬‬‬r‬‬‬ ‬‬‬2‬‬‬0‬‬‬2‬‬‬0‬‬‬,‬‬‬ ‬‬‬0‬‬‬5‬‬‬:‬‬‬0‬‬‬0‬‬‬p‬‬‬m</div></td>, <td><div><div><div><div><div><div><div><div><div><div><div><div><div><span>S$ </span>1‬‬‬‬.‬‬‬‬7‬‬‬‬0</div></div></div></div></div></div></div></div></div></div></div></div></div></td>, <td>N.A.</td>, <td><div><div><div><div><div><span>S$ </span>2‬.‬0‬2</div></div></div></div></div></td>, <td><div><div><div><div><div><div><div><div><div><div><div><div><div><div><div><span>S$ </span>2‬.‬4‬3</div></div></div></div></div></div></div></div></div></div></div></div></div></div></div></td>, <td><div><div><div><div><div><div><div><div><div><div><div><div><span>S$ </span>2‬‬‬‬‬‬.‬‬‬‬‬‬5‬‬‬‬‬‬9</div></div></div></div></div></div></div></div></div></div></div></div><span class="price_subtext">(SINO X Power)</span></td>]
[<td style="border-color: rgb(228, 145, 52);"><div class="fuel-name">SPC</div><div class="time">1‬‬‬9‬‬‬ ‬‬‬J‬‬‬u‬‬‬n‬‬‬e‬‬‬ ‬‬‬2‬‬‬0‬‬‬2‬‬‬0‬‬‬,‬‬‬ ‬‬‬0‬‬‬9‬‬‬:‬‬‬4‬‬‬1‬‬‬p‬‬‬m</div></td>, <td><div><div><div><div><div><div><div><div><div><div><div><div><div><span>S$ </span>1‬‬‬‬‬‬.‬‬‬‬‬‬6‬‬‬‬‬‬7</div></div></div></div></div></div></div></div></div></div></div></div></div></td>, <td><div><div><div><div><div><div><div><span>S$ </span>1‬‬‬.‬‬‬9‬‬‬5</div></div></div></div></div></div></div></td>, <td><div><div><div><span>S$ </span>1‬‬‬‬.‬‬‬‬9‬‬‬‬9</div></div></div></td>, <td><div><div><div><div><div><div><div><div><div><div><div><span>S$ </span>2‬‬‬‬.‬‬‬‬3‬‬‬‬3</div></div></div></div></div></div></div></div></div></div></div></td>, <td>N.A.</td>]
[<td style="border-color: rgb(39, 102, 173);"><div class="fuel-name">Esso</div><div class="time">2‬0‬ ‬O‬c‬t‬o‬b‬e‬r‬ ‬2‬0‬2‬0‬,‬ ‬0‬4‬:‬5‬2‬p‬m</div></td>, <td><div><div><div><div><div><div><div><div><div><div><div><div><span>S$ </span>1‬‬‬‬.‬‬‬‬7‬‬‬‬0</div></div></div></div></div></div></div></div></div></div></div></div></td>]
[<td style="border-color: rgb(255, 213, 0);"><div class="fuel-name">Shell</div><div class="time">3‬‬‬0‬‬‬ ‬‬‬O‬‬‬c‬‬‬t‬‬‬o‬‬‬b‬‬‬e‬‬‬r‬‬‬ ‬‬‬2‬‬‬0‬‬‬2‬‬‬0‬‬‬,‬‬‬ ‬‬‬1‬‬‬1‬‬‬:‬‬‬3‬‬‬7‬‬‬a‬‬‬m</div></td>, <td><div><div><div><div><div><div><div><span>S$ </span>1‬‬‬‬.‬‬‬‬7‬‬‬‬0</div></div></div></div></div></div></div></td>]
[<td style="border-color: rgb(0, 0, 0);"><div class="fuel-name">Sinopec</div><div class="time">2‬6‬ ‬O‬c‬t‬o‬b‬e‬r‬ ‬2‬0‬2‬0‬,‬ ‬0‬5‬:‬0‬0‬p‬m</div></td>, <td><div><div><div><div><div><div><span>S$ </span>1‬‬‬.‬‬‬7‬‬‬0</div></div></div></div></div></div></td>]
[<td style="border-color: rgb(228, 145, 52);"><div class="fuel-name">SPC</div><div class="time">1‬‬‬‬9‬‬‬‬ ‬‬‬‬J‬‬‬‬u‬‬‬‬n‬‬‬‬e‬‬‬‬ ‬‬‬‬2‬‬‬‬0‬‬‬‬2‬‬‬‬0‬‬‬‬,‬‬‬‬ ‬‬‬‬0‬‬‬‬9‬‬‬‬:‬‬‬‬4‬‬‬‬1‬‬‬‬p‬‬‬‬m</div></td>, <td><div><div><div><div><div><div><div><div><div><div><div><div><div><span>S$ </span>1‬‬‬.‬‬‬6‬‬‬7</div></div></div></div></div></div></div></div></div></div></div></div></div></td>]

"""
