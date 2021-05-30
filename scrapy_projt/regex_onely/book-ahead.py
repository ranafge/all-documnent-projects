import re

string = "12457,9998547,2598714,22541,32154,999321,4578554,999147,9995478,9993124"

print(re.findall(r"(?![9]+)(?:\d{1,18})",string)) #dont match 9+before
import re

strings = ['LINESTRING (-3.1 2.42, 5.21 6.1, -1.17 -2.23)',
           'LINESTRING (1.83 9.5, 3.33 2.87)']

for string in strings:
    st = re.findall('(?<=[(,]).*?(?=[,)])', string)
    print([tuple(s.split()) for s in st])
    print(st)


