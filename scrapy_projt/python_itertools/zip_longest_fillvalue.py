from itertools import zip_longest
import re
from itertools import chain

dates = ['21/11/2044', '31/12/2018', '23/9/3000', '25/12/2007']
text = ['What are dates? ', ', is an example.\n', ', is another format as well.\n',
        ', also exists, but is a bit ludicrous\n', ', are examples but more commonly used']

print([w for x in zip_longest(text, dates, fillvalue='') for w in x if w])

ls = ['1 Paris-SG 42 20 13 3 4 +33',
      '2 Lille 42 20 12 6 2 +20',
      '3 Lyon 40 20 11 7 2 +20',
      '4 Monaco 36 20 11 3 6 +10']

convert_2d_list = [i.split(maxsplit=2) for i in ls]
print(convert_2d_list)

my_list_dict = {
    'L1': ['a', 'b', 'c', 'd'],
    'L2': ['e', 'f', 'g', 'h']
}


def check_value_return_key(c):
    for k, v in my_list_dict.items():
        if c in v:
            return k
        else:
            return None


print(check_value_return_key('g'))
def find_key(c):
    for k, v in my_list_dict.items():
        if c in v:
            return k
    else:
        raise Exception("value '{}' not found".format(c))

find_key("a")

a = [[[5],[3]],[[4],[5]],[[6],[7]]]

print([list(chain.from_iterable(l)) for l in a])

my_list = [0, 1, 2, 2, 1, 20, 21, 21, 20, 3, 23, 22]
num_map  = {j:i for i, j in enumerate(sorted(set(my_list)))}
print(num_map)

