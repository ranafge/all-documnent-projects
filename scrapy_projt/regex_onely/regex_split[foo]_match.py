import re
s = 'Hello [foo] world!'
print(re.split(r'(\[[^][]*])', s))
print(re.split(r"(\[[^][]+])",s))
