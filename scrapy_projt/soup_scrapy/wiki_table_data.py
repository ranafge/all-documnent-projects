import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from itertools import zip_longest

soup = bs(requests.get('https://en.wikipedia.org/wiki/Districts_of_Warsaw').content, 'lxml')
table = soup.select_one('h2:contains("Localities") ~ .wikitable') #isolate table of interest
results = []

for row in table.select('tr')[0::2]: #walk the odd rows
    for i in row.select('th'):
        r = list(zip_longest([i.text.strip()] , [i.text for i in row.findNext('tr').select('li')], fillvalue=i.text.strip())) # zip the current district to the list of neighbourhoods. Fill with District name to get lists of equal length
        results.append(r)

results = [i for j in results for i in j] #flatten list of lists
df = pd.DataFrame(results, columns= ['District','Neighbourhood'])
print(df)
