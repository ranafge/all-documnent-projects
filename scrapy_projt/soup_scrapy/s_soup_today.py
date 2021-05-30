from bs4 import BeautifulSoup
html = """<div class="posted-by">
Posted Today by 
<a href="/jobs/nhs-business-services-authority-72549/p72549" class="gtmJobListingPostedBy">NHS Business Services Authority</a> 
<span class=" "> <span data-qa="newMobileLbl" class="label label-new"  > New</span> </span>
</div>"""

soup_obj = BeautifulSoup(html, 'lxml')
print(soup_obj.find('div',{'class': 'posted-by'}).next_element.strip())

favorite_languages = {
   'jen': ['python', 'ruby'],
   'sarah': ['c'],
   'edward': ['ruby', 'go'],
   'phil': ['python', 'haskell'],
   }

for name,languages in favorite_languages.items():
    print("\n" + name.title() + "'s fav lang are:")
    for language in languages:
        print("\t" + language.title())

html = """<span class="grayItalic">
    Received: 01/19/2021
</span>"""

soup = BeautifulSoup(html, 'lxml')
date = soup.find('span', {'class': 'grayItalic'}).get_text()
# converted_date = int(date[13:14])
print(date)
from python_imports import random_user_agent
import requests
headers =random_user_agent.get_header()
print(headers)
url ="https://iapps.courts.state.ny.us/nyscef/DocumentList?docketId=npvulMdOYzFDYIAomW_PLUS_elw==&display=all"
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'lxml')
date = soup.find('span', {'class': 'grayItalic'}).get_text().strip()
converted_date = int(date[13:15])
print(converted_date)
print(date)
