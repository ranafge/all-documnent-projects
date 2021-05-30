from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
from tabulate import tabulate
#
# url = 'https://www.kff.org/health-reform/state-indicator/total-monthly-medicaid-and-chip-enrollment/?currentTimeframe=0&sortModel=%7B%22colId%22:%22Location%22,%22sort%22:%22asc%22%7D'
# options = Options()
# options.headless = True
#
# driver = webdriver.Chrome(options=options)
# driver.get(url)
# time.sleep(7)
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# rows = soup.find('div', {'class': 'tab-container ngDcCtrl'})


dx= [['Location,Pre-ACA Average Monthly Enrollment,Total Monthly Medicaid/CHIP Enrollment,Percent Change,United States,1,Alabama,2,Alaska,Arizona,Arkansas,California,Colorado,Connecticut,Delaware,District of Columbia,3,Florida,Georgia,Hawaii,Idaho,Illinois,Indiana,Iowa,Kansas,Kentucky,Louisiana,Maine,Maryland,Massachusetts,Michigan,4,Minnesota,5,Mississippi,Missouri,Montana,Nebraska,Nevada,New Hampshire,New Jersey,New Mexico,6,New York,North Carolina,North Dakota,7,Ohio,Oklahoma,Oregon,8,Pennsylvania,Rhode Island,South Carolina,South Dakota,Tennessee,Texas,Utah,9,Vermont,Virginia,Washington,10,West Virginia,11,Wisconsin,12,Wyoming,56,511,799,76,489,912,33%,799,176,972,314,22%,122,334,234,622,92%,1,201,770,1,887,382,57%,556,851,844,592,52%,7,755,381,12,053,848,55%,783,420,1,384,959,77%,N/A,893,114,N/A,223,324,244,351,9%,235,786,251,711,7%,3,695,306,3,977,970,8%,1,535,090,1,976,277,29%,288,357,362,958,26%,238,150,351,597,48%,2,626,943,3,062,183,17%,1,120,674,1,655,712,48%,493,515,716,076,45%,378,160,411,170,9%,606,805,1,494,119,146%,1,019,787,1,629,675,60%,N/A,236,782,N/A,856,297,1,398,124,63%,1,296,359,1,649,211,27%,1,912,009,2,505,315,31%,873,040,1,113,911,28%,615,556,647,721,5%,846,084,959,241,13%,148,974,262,233,76%,244,600,262,715,7%,332,560,709,191,113%,127,082,198,597,56%,1,283,851,1,811,419,41%,457,678,788,718,72%,5,678,417,6,421,226,13%,1,595,952,1,896,445,19%,69,980,103,212,47%,2,130,322,2,851,221,34%,790,051,823,588,4%,626,356,1,078,440,72%,2,386,046,3,135,671,31%,190,833,312,213,64%,889,744,1,074,041,21%,115,501,117,303,2%,1,244,516,1,521,998,22%,4,203,449,4,577,342,9%,294,029,357,531,22%,161,081,164,940,2%,935,434,1,538,513,64%,1,117,576,1,827,322,64%,354,544,535,129,51%,985,531,1,144,492,16%,67,518,61,477,-9%,Data Table,To view data, please select some geographies from the sidebar.']]

# print(data)
data = dx[0][0].split(',')[4:-3]
items = ['1', '2', '3', '4', '5', '6','7', '8', '9', '10', '11', '12']
for item in items:
    if item in data:
        data.remove(item)
# print(data)
# for i, v in enumerate(data):
#     print(i, v)

def four_colusm(l, n):
    return [[l[i:i+n]] for i in range(0, len(l),n)]
mydata = four_colusm(data,52)
print(mydata)
print(len(mydata))
# print(mydata)

print(tabulate(mydata, headers=['Location','Pre-ACA Average Monthly Enrollment','Total Monthly Medicaid/CHIP Enrollment','Percent Change']))

# table = [row.get_text(strip=True, separator=',').split('\n') for row in rows][0]
# print(table)
# print(' '.join(x) for x in table.split(','))
# print(table)
# table_data_as_a_list = [row.get_text(strip=True, separator=',').split(',') for row in rows][0][:-3]

#
# def three_col(l, n):
#     return [l[i:i+n] for i in range(0, len(l), n)]
#
# my_data_list = three_col(data,4)
#
state_list_pd = pd.DataFrame(mydata)
# print(state_list_pd)
# print(my_data_list)
# state_list_pd.to_csv('table.csv')
# driver.close()
