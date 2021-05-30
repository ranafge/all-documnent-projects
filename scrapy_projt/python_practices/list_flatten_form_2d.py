from functools import reduce
import operator
import itertools

l = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
print(reduce(lambda x,y: x +y, l))
print([i for subl in l for i in subl])
print(reduce(operator.concat,l))
print(sum(l, []))
print(list(itertools.chain(*l)))
print(list(itertools.chain.from_iterable(l)))

last_two_items = l[-2:]
print(last_two_items)
# You can also use slice assignment to remove one or more lelement form a list

r= [1, 'blah', 9,8,2,3, 1, 4]
r2=['dd','cc', 'dddd']
print(r)
print('index', r.index('blah'))
print([ix for ix, e in enumerate(r) if e == 1])
print(list(itertools.chain(r, r2)))
res = operator.add(r,r2)
print(res)

map_res = map(str,(x for x in range(10)))
print(list(map_res))
del map_res[-1]

print(map_res)
