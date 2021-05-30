import re
from string import printable

# your invisibles are in the string...

s='''<@961483653468439706> Text to remove, this text is useless, that's why i want it gone!
Type `keep the letters and spaces` and `this too`'''

print(re.findall(r"`(.*?)`", s))

# for m in re.findall(r'`([^`]*)`', s):
#     print(repr(m))
#     print(''.join([c for c in m if c in printable]))
#     print()

