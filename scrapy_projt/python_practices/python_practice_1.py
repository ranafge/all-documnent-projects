from collections import Counter

stuff = ["cow", "apple", "pig", "cow", "cow"]
print(Counter(stuff).items())
print(' and '.join([f"{k} and {v + 's' if int(k) > 1 else v}" for v, k in Counter(stuff).items()]))
print(' '.join([f"{v} {k + 's' if v > 1 else k}" for k, v in Counter(stuff).items()]))
