list_of_lists = [[1,8],[2,9],[3,0]]

res = [j for i in zip(*list_of_lists) for j in i]
print(res)
print(list(zip(*list_of_lists)))
