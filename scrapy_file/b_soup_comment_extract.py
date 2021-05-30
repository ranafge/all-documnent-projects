from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

page=urlopen('https://catalog.data.gov/dataset')
soup=BeautifulSoup(page,'lxml')

dataset_number=soup.select('div .new-results')
print(dataset_number)

 # Snippet snippets/search_result_text.html start
 # Snippet snippets/search_result_text.html end
