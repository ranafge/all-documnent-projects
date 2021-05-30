import re
bad_letters = "AKS"
word = "Sanctuary"

if re.search(f"[{bad_letters}]", word, re.IGNORECASE):
    print('MATCH')

strings = ['LINESTRING (-3.1 2.42, 5.21 6.1, -1.17 -2.23)',
           'LINESTRING (1.83 9.5, 3.33 2.87)']

