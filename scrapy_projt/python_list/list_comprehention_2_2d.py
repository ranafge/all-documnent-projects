items = (.1, .5, .9)
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

lst_new = [[[.1, 2, 3], [.4, 5, 6], [.7, 8, 9]], [[.5, 2, 3], [2, 5, 6], [3.5, 8, 9]], [[.9, 2, 3], [3.6, 5, 6], [6.3, 8, 9]]]

res = [[[x[0]*items[i] for i in range(len(items))]] for x in lst]
print(res)
print([[[x[0] * i] + x[1:] for x in lst]for i in items])
