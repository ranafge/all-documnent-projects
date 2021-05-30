from operator import itemgetter
list_to_be_sorted =[{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]
newlist = sorted(list_to_be_sorted, key=lambda k: k['name'], reverse=True)
print(newlist)
new2list = sorted(list_to_be_sorted, key=lambda k: k['age'])
print(new2list)

new3list = sorted(list_to_be_sorted, key=itemgetter('name'))
print(new3list)
