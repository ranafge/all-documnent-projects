import itertools
first = [1, 3, 6, 8, 9, 9, 12]
second = [1, 2, 3, 2, 1, 0, 3, 3]

res = itertools.product(first, second)
print(res)
ress = [sum(pair) for pair in res]
print(ress)
