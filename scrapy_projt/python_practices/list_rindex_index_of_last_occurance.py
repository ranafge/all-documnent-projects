li = ["a", "b", "a", "c", "x", "d", "a", "6"]


print(''.join(li).rindex('a'))
print(max(loc for loc, v in enumerate(li) if v =='a'))
