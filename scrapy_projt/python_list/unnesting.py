L = [1, [2, 3, [4, 5, [6]]], [7, 8], 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
def get_first(seq):
    if isinstance(seq,  list):
        return get_first(seq[0])
    return seq

print(get_first(L))
print([get_first(i) for i in L])
