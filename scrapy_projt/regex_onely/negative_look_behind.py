import re

String  = "foobar barbar beachbar crowbar bar ";

print(re.findall(r'(?!foobar).{6}\w+', String))
