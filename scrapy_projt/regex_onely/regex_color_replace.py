import re

d = "01:22:33:22"
print(';'.join(d.rsplit(':',1) ))