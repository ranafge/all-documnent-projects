import re

lines = ['hi!,', 'how', 'are', 'you?']
word_of_symbol = re.compile(r'\w+|\W')
out = [item for string in lines for item in word_of_symbol.findall(string)]

print(out)



