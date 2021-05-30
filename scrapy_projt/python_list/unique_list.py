sequence = ['1', '2', '3', '3', '6', '4', '5', '6']
unique = []

[unique.append(x) for x in sequence if x not in unique]

print(unique)

