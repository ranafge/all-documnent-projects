def collision(tab, tab1):
    for i in range(len(tab)):
        for j in range(len(tab1)):
            if tab[i] == tab1[j]:
                return i,j
    return -1,-1

x,y = collision([1,2,3],[3,4,5])
x, y = collision([1, 2, 3], [10, 10, 10])
print(x,y)
