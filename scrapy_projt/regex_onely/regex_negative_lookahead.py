import re
text="""hello 123
hello 1234
hello 12 world 123
hello 123 world 1234
h3ll0 123
h3ll0 1234"""

print(re.findall(r"^(?!(.*\d){4})[A-Za-z ,.!?\d]+$", text))
