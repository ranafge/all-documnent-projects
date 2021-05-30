from functools import reduce

list_of_str = ['hix ' , 'ceb']

print(reduce(str.join, list_of_str))
