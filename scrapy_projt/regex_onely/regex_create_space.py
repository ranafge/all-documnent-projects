import re
test = "example(test)"
test2 = "example(test)example"
test3 = "(test)example"
test4 = "example (test) example"

for i in [test, test2, test3, test4]:
    res = re.sub(r"[^\S]?(\([^\)]+\))[^\S]?", r' \1 ',i)
    print(res)
print()
for i in [test, test2, test3, test4]:
    print(re.sub(r"[^\S]?(\(.*?\))[^\S]?", r' \1 ', i))
