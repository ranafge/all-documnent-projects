from itertools import chain
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(l[::2])
print(l[1::2])
l[::2], l[1::2] = l[1::2], l[::2]
print(l)
# exclusive or to flip significat bit

res = [l[i^1] for i in range(len(l))]
print(res)

res = list(chain.from_iterable(zip(l[1::2], l[0::2])))
print(res)
