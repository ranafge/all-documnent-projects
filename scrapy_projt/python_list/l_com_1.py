import unicodedata
import re
import os

value = 120
print([value if value % 2==0 else 'odd'])
print(' '.join(['Ha' if i else 'ha' for i in range(3)])+'!')
X = [1.5, 2.3, 4.4, 5.4, 'n', 1.5, 5.1, 'a']

print([i for i in X if isinstance(i, str)])
