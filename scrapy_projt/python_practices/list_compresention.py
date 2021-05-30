testList = [[30.0, "?", 910.0, 120.],[11.0, 25.4, 330.3, 340.0], [1.6, 23.4, 23.0, 46.0], [7.0,14.0,"?",2.0], ["*", "*", 8.9, 6.4]]
newList = [[11.0, 25.4, 330.3, 340.0], [1.6, 23.4, 23.0, 46.0]] # expected output

res =[subl for subl in testList if not any(isinstance(val , str) for val in subl) ]
print(res)

res2 = [subl for subl in testList if not any(type(val) !=float for val in subl)]
print(res2)
