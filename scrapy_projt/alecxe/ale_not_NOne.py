from collections import ChainMap
a = [None, None, None, 1, 2, 3, 4, 5]
b = [None, None, None]

print(next(item for item in a if item is not None))
print(next((item for item in b if item is not  None), 'All are Nones'))

a = [{'a':1},{'b':2},{'c':1},{'d':2}]

print(dict(ChainMap(*a)))
