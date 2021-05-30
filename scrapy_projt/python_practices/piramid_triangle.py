results = [[i for i in range(x)] for x in range(0,10)]
for res in results:
    print(*res[1:])

print(*[''.join(str(i) for i in range(1,x)) for x in range(1,10)], sep=' \n')
