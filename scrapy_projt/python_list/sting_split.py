text ="<p>First</p><p>Second</p><p>Third</p>"

print([t.split('<p>') for t in text.split('</p>')])

list1 = [1,2,3,4,5,6,7,8,9,10]
print([(list1[i],list1[i+1]) for i in range(0,len(list1),2)])
