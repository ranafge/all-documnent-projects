from bs4 import BeautifulSoup

html = """<countdown current_time="1611585537797" date="1611603000" listing="f446d440-9d45-4e48-bf93-69c5e117fac2" formatted_date="25th January 2021 19:30:00"></countdown>"""

soup = BeautifulSoup(html, 'lxml')

tag = soup.countdown
print(tag.attrs['formatted_date'])
