my_list = [[[(2,3,4,5)]],[[8,2,4,2]],[[9,0,0,0]]]
res = [my_list[0][0][0][0]] +[x[0] for subl in my_list[1:] for x in subl]
# print(res)

def get_first(seq):
    if isinstance(seq, (tuple, list)):
        return get_first(seq[0])
    return seq

print(get_first(my_list))
print([get_first(i) for i in my_list]) # very good answer


import re
h = "173.4k net worth blabla "

match = re.search('([-+]?\d*\.\d+|\d+)k net worth', h)
if match:
    f = float(match.group(1))*1000
    print(f)
