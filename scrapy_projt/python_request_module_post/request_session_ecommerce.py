import requests
from lxml import html

def main():
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    session = requests.session()
    session.headers.update({'user_agent':user_agent})
    initial_url = 'https://www.ligloo.fr/annonce-immobiliere/{0}.html#!/?page={1}&tri=pertinance'
    categories = ('STUDIO', 'LOFTS', 'MAISON', 'APPART-2-PIECES-MOINS-DE-40-M2')
    for category in categories:
        dictionary_of_links = {}
        for page in range(1, 6):
            url = initial_url.format(category, page)
            print(url)
            result = session.get(url)
            tree = html.fromstring(result.text) #why tree is the same every time?

print(main())
