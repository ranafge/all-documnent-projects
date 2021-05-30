from itertools import permutations

a = ['2', '3', '4']
x = []
for i in permutations(a,2):
    print(i
          )
    print(''.join(i))
    x.append(''.join(i))

print(a + x)

