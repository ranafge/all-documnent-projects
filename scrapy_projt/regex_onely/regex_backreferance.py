import re

pattern = re.compile(r'(\d+)-(\w+)')

print(pattern.sub(r'\2-\1', "1-a\n20-baer\n34-afcr"))

pattern = re.compile(r'(?P<first>\w+) (?P<second>\w+)')

print(pattern.search('Hello world').groupdict())

pattern = re.compile(r'(?P<country>\d+)-(?P<id>\w+)')
print(pattern.sub(r'\2-\1',"1-a\n20-baer\n34-afcr"))
print(pattern.sub(r'\1-\2',"1-a\n20-baer\n34-afcr"))
string = " After so many requests, this is Bretagne. She was the last surviving 9/11 search dog, and our second ever 14/10. RIP* "
print(re.split(r"(\d+/\d+)", string)[-2])
