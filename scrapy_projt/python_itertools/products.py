from itertools import product
input_x = ['1', ['2', '2x'], '3', '4', ['5', '5x']]

re_formated_input_x = [i  if isinstance(i,list) else [i] for i in input_x]
print(re_formated_input_x)

res = list(product(*re_formated_input_x))

print(res)

a = [8,9,4,7,5,6,1,4,8]

b = [6,4,7,1,5,8,3,6,4,4]

diff = [x-y for x, y in zip(a,b)]
print(diff)
