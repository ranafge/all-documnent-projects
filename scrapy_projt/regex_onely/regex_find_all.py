import re

x = re.findall(r'CAT.+?END', 'Cat \n eND', flags = re.I | re.DOTALL)

x = re.findall(r'(?si)CAT.+?END', 'Cat \n eND')

print(x)
