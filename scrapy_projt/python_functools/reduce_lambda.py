from functools import reduce

l = [[1,2,3], [4,5,6], [7], [8,9]]

res = reduce(lambda x, y: x+y, l)
print(res)
