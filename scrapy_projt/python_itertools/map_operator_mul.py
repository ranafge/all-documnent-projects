import operator
import time
import itertools

# define list
l1 = [1, 2, 3]
l2 = [2, 3, 4]

t1 = time.time()
a, b, c = map(operator.mul, l1, l2)

t2 = time.time()
print('Results:', a, b, c)
print('Time taken map function : %.6f' % (t2 - t1))

for i in range(3):
    print(l1[i] * l2[i], end=' ')

# for i in itertools.count(5, 5):  # infinitely running.
#     print(i)
count = 0
for i in itertools.cycle('ab'):
    if count >5:
        break
    else:
        print(i, end=' ')
        count +=1

languages = ['C', 'C++']
x = itertools.cycle(languages)
for i in range(2):
    print(next(x), end=' ')

x = itertools.repeat(23,5)
print(list(x))

#Combinatroc iterator

from itertools import product

print('The cartesian product using repat')

print(list(product([1,2,3], repeat=4)))

print('Cartesian product of the containers:')
print(list(product(['ab'], [3,4],[4,5],[7,9])))
print(list(itertools.permutations(range(3),3)))
print(list(itertools.combinations(range(2),1)))

print(list(itertools.combinations_with_replacement('ab',2)))
print(l1)
print(list(itertools.accumulate(l1, operator.add)))

print(list(itertools.chain.from_iterable([l1,l2])))

print(list(itertools.compress('abcdef',[1,0,0,0,1])))

print(list(itertools.dropwhile(lambda x: x % 2 ==0, [4,6, 8, 10, 22, 24, 1])))

print(*(itertools.zip_longest('gess', 'aessxere', fillvalue='_')))

print(*(itertools.tee([1,2,3],2)))

li = [ (1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10, 1) ]

print(list(itertools.starmap(min, li)))

print(list(itertools.filterfalse(lambda x: x % 2 ==0, [1,2,3,4,5,6,7,87])))
