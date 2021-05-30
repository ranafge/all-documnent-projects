import re

logs = 'cut-this-out \n\n givemethisstring \n\n and-this-out-too'

search_term_start = '''cut-this-out'''
search_term_end = '''and-this-out-too'''

pattern = re.compile(r'\n+\s+(.*?)\s+\n+')
# c = re.compile(search_term_start + r'(.*?)' + search_term_end, re.DOTALL)
# print(c.search(logs).group(1))
print(re.search(pattern, logs).group(1))
print(re.search(pattern, logs).group(0))
print(re.search(pattern, logs).groups())

list = ["ABC", "ABD", "DEF", 'defo23' 'rofs', 'ofeofjw34']

pattern = re.compile(r'\b(ABC | ABD )\b')

print([w for w in list if pattern.search(w)])
