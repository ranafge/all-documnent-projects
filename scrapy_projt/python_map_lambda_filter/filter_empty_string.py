mylist=['rana', '', 'sharmin', '', 'hafiz', '']

filter_mylist = list(filter(None,mylist))
print(filter_mylist)

mylist_with_digit = ['rana', 22, 'alveen', 33, 'sharmin', 44]

filter_mylist_with_digit = [x for x in mylist_with_digit if isinstance(x, int)]
print(filter_mylist_with_digit)

print(list(filter(lambda x: isinstance(x,int), filter_mylist_with_digit)))
mylist_digit = [['rana', 22], ['alveen', 33], ['sharmin', 44]]
print(' '.join([str(x[1]) for x in mylist_digit]).join(['{','}']))
