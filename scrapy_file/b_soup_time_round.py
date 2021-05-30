from bs4 import BeautifulSoup

html_doc = """<td data-timestamp="4.5833333333333" class="hide-on-hover fill-space relative">
              <div class="col border-box text-center nowrap row large-up-text-right padding-horz-small push">```"""

soup = BeautifulSoup(html_doc, 'html.parser')
out = soup.select_one('td')['data-timestamp']
print(round(float(out)))

print(soup.prettify())
