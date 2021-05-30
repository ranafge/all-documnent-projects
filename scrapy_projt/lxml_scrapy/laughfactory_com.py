from lxml import html
import requests


url='http://www.laughfactory.com/jokes/popular-jokes'

r=requests.get(url)
tree = html.fromstring(r.content)
print(tree.text)
