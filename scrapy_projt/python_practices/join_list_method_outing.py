string = 'stack overflow, ask question , keep remove'

res = ' '.join([i.split()[0] for i in string.split(',')])
print(res)
