a = [0, 4, 10, 100]

print([a[x] - a[x-1] for x in range(1, len(a))])
