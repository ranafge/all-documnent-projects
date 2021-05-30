import re
from bs4 import BeautifulSoup

pattern = r'\{\w+\s*:,*\s*\w+\}'
s='[{abc:, xyz}, {abcd: 890}, {a :908}]' # s string.
# res = re.findall(pattern, s)
# print(res[0]) # output {abc:, xyz}
#
# print(re.findall('(\{[a-z0-9, :]+\})', s)[0])
print(re.findall(r'\{\w+:,\s*\w+\}',s)[0])


cell_text = """\
#%%sql
q = \"\"\"
select 
name, breed, sum(weight) over (partition by breed order by name) as running_total_weight
from cats 
order by breed, name
\"\"\"

f(q)
"""
res = re.findall(r'(?s)"""(.*?)"""', cell_text)[0]
print(res)


s = 'hello how are you? {{foo;;[[1;;2;;3]];;bar;;[[0;;2;;3]]}} im okay {{ABC;;DEF;;[[10;;11]]}}'
for m in re.findall(r'{{(.*?)}}', s):
    print(re.split(r';;(?![^[]*])', m))

print(re.split(r';;(?![^[]*])','foo;;[[1;;2;;3]];;bar;;[[0;;2;;3]]'))
