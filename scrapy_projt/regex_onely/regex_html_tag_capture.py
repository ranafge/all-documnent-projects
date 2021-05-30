import re

s = '<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>'
pat = r'</?\s*(\w+).*?>'
tags = re.findall(pat, s)
print(tags)
pattern = r"</?\s*(\w+).*?>"
print(re.findall(pattern, s))
