
import requests
import bs4


response = requests.get("http://scans.bgs.ac.uk/sobi_scans/boreholes/795279/images/10306199.html")

soup = bs4.BeautifulSoup(response.content,'lxml')

NextPg = soup.select('a[title="Next page"]')[0]
print(NextPg['href'])

print('Done.')