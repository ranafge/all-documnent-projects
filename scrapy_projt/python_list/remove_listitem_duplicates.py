list1 = ['AAB', 'CAA', 'ADA']
result = sorted(list1, key=lambda x: x[1])
print(result)

from collections import OrderedDict

list1 = ['AAB', 'CAA', 'ADA']
list1 = [''.join(OrderedDict.fromkeys(l).keys()) for l in list1]
print(list1)
new_list = []
for word in list1:
    new_list.append(''.join(set(word)))
print(new_list)
