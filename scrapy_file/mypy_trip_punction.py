import string

# def clean(item):
#     return ''.join(char for char in item if char in string.ascii_letters)

ls = ["'Foo'", 'Foo', 'Bar']
# ls = list(set(clean(item) for item in ls))
# print(ls)
ls = ["'Foo'", 'Foo', 'Bar']

def clean(item):
    return ''.join(char for char in item if char in string.ascii_letters)

print(list(clean(x) for x in ls))
