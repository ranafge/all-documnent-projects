import re
# a = str("  assets, (a) Property, (b) Capital, (d) Goodwil, (i) Investments (A), (iv) Loans (A)")
a ="  assets, (a) Property, (b) Capital, (d) Goodwil, (i) Investments (A), (iv) Loans (A)"
print(re.sub(r"\s*\(\w+\)\s*",' ', a).strip())


list=[['a'],['b'],['cc']]

print([i for subl in list for i in subl])
