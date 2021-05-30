amount=['1-100000','2000-60000','10-20000000','50000-800000']
print([x.split('-') for x in amount])
res = [f'{int(x.split("-")[0]):,}-{int(x.split("-")[1]):,}' for x in amount]

print(res)

lst = ['order','orderNumber']
lst = [f'"{elt}"' if elt == 'order' else elt for elt in lst]
print(lst)
print([f'"{elt}"' if elt== 'order' else elt for elt in lst])
