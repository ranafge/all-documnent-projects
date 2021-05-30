import requests
from bs4 import BeautifulSoup

sub_url = "https://labtestsonline.org/tests/17-hydroxyprogesterone"
response = requests.get(sub_url)

soup = BeautifulSoup(response.content, 'html.parser')
other_names =[
    tag.next.next.get_text(strip=True,  separator=',').split(',') for tag in soup.find('div', class_='field-label')
][0]
print(other_names)
