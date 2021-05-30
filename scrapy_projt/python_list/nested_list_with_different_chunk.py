ls = list(range(1,101))
# print(ls)
# [20, 30,40]

print(
   [ls[i:i+n] for i in range(0, len(ls)) for n in [2,5,8]]
)
