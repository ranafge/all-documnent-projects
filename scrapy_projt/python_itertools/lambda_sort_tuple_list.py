lst = [('candy','30','100'), ('apple','10','200'), ('baby','20','300')]
sorted_list = sorted(lst, key=lambda x: x[0])
print(sorted_list)

l=[('303', '30'), ('343', '34'), ('999', '9')]
l = sorted(l, lambda x:int(x))
print(l)

def multiply(x):
    return x* 2
l = map(lambda x: multiply(x), [1,2,3])
print(list(l))

