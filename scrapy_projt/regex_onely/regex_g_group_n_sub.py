import re
pound_links = re.compile(r'#<a href=".*?">(.*?)</a>')
output = pound_links.sub(r'#\g<1>', '#<a href="stuff1">stuff1</a>')

print(output)




