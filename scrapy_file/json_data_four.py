from bs4 import BeautifulSoup as bs
from selenium import webdriver

driver = webdriver.Chrome()
site = 'https://evolving-hockey.com/stats/team_standard/?_inputs_&std_tm_str=%225v5%22&std_tm_table=%22On-Ice%22&std_tm_team=%22All%22&std_tm_range=%22Seasons%22&std_tm_adj=%22Score%20%26%20Venue%22&std_tm_span=%22Regular%22&dir_ttbl=%22Stats%22&std_tm_type=%22Rates%22&std_tm_group=%22Season%22'

r = driver.get(site)
import time
time.sleep(5)
soup = bs(driver.page_source, 'html.parser')
data = soup.find_all('tr')[1]
for d in data:
    print(d.get_text(strip=True), end='   ')

data2 = soup.find_all('tr')[1:33]

for x in data2:
    print(x.get_text(strip=True,separator='  '), end='\n')

driver.quit()
