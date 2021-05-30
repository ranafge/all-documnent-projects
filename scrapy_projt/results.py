text = "this is line one . this is line two . this is line three ."

expectedoutput = [['this', 'is', 'line', 'one', '.'],
                   ['this', 'is', 'line', 'two', '.'],
                   ['this', 'is', 'line', 'three', '.']]

myoutput =[['this', 'is', 'line', 'one', '.'],
           ['this', 'is', 'line', 'two', '.'],
           ['this', 'is', 'line', 'three', '.']]


print([text.split()[i:i+5] for i in range(0,len(text.split()),5) ])
