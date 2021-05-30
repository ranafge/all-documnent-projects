mydict = {}
mydict['name'] = 'Rana'
mydict['age'] = 23
mydict['email'] = 'ranafge@gmail.com'
mydict['ranaf'] = 'email'
print(mydict)
for k, v in mydict.items():
    if 'email' not in v:
        del mydict[k]
print(mydict)
