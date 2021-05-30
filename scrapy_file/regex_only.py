import re

mylist = [{ "id":"12345", "table":"mytable",'id': '22'}]

print([k[v] for k in mylist for v in k if v=='id'])
# print(mylist[0])
# print(mylist[0].items())
# print('-'*10)
# for v in mylist[0].items():
#     print(v)

print(mylist[0])
print()
print(mylist[0].items())
