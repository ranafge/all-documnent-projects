import requests
from bs4 import BeautifulSoup
import pandas as pd

url ='https://www.klsescreener.com/v2/stocks/view/5292'

klseLink = requests.get(url)

klseParser = BeautifulSoup(klseLink.text, 'html.parser')

currentQuarterReportTables = klseParser.find('table', {'class': 'financial_reports table table-hover table-sm table-theme'}).findAll('tr')


output = []
for row in currentQuarterReportTables[1:]:
    res = [td.text.strip() for td in row.findAll("td")]
    output.append(res)

df = pd.DataFrame(output, columns=['col'+str(i) for i in range(1,12)])
print(df.loc[:3,['col1', 'col2', 'col3', 'col4','col5']])

print(df.loc[1,['col1']])
res =df.loc[1][0]
res2 =df.loc[3][0]
print()
print(res)
print(res2)

