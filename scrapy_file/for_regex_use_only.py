# You can us itertools.groupby to group consecutive non-empty strings usign by bool
from itertools import groupby
lst = ['a', 'b', 'c', '', 'd', 'e', '', 'f']
print([''.join(x) for k, x in groupby(lst,bool) if k])
# print([''.join(g) for k, g in groupby(lst, bool) if k])
