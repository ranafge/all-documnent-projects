from functools import reduce
from operator import mul, add

def product(xs):
    return reduce(add, xs, 1)

print(product([2,2,3]))

print(max(len(i) for i in [[1],[1,2],[1,2,3]]))
