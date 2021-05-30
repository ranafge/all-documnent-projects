from bs4 import BeautifulSoup
import requests
import pandas as pd
def Get_Top_List_BR(url):
    response = requests.get(url)
    page = response.text
    soup = BeautifulSoup(page, 'lxml')
    table = soup.find(id='table')
    rows = [row for row in table.find_all('tr')]
    movies = {}
    for row in rows[1:]:
        items = row.find_all('td')
        link = items[1].find('a')
        title, url_string = link.text, link['href']
        #split url string into unique movie serial number
        url = url_string.split('?', 1)[0].split('t', 4)[-1].split('/', 1)[0]
        #set serial number as key to avoid duplication in any other category-especially title
        movies[url] = [url_string] +[i.text for i in items]

    movie_page = pd.DataFrame(movies).T  #transpose
    print(movie_page)
    movie_page.columns = ['URL', 'Rank', 'Title', 'Genre', 'Budget', 'Running Time','Gross',
                    'Theaters', 'Total_Gross', 'Release_Date', 'Distributor', 'Estimated']
    return movie_page

df_test_BR = Get_Top_List_BR('https://www.boxofficemojo.com/year/2019/?grossesOption=calendarGrosses&area=BR/')

df_test_BR.head(10)
