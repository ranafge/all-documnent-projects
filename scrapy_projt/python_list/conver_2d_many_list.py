ls =[[1, 2, 3, 4, 5],[10, 20, 30, 40, 50]]

res = [list(x) for x in zip(*ls)]

new_list = []
for i in res:
    item = ''.join(str(i).split(','))
    new_list.append(item)
print(new_list) #['[1 10]', '[2 20]', '[3 30]', '[4 40]', '[5 50]']

print([''.join(new_list)]) #['[1 10][2 20][3 30][4 40][5 50]']
