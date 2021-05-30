import re

tests = ['(USED ON P/N D511835AAB503)', '(USED ON PN D511835AAB503)']

pattern = re.compile(r"\(USED ON P\/?N ([^\)]+)")

for test in tests:
    m = pattern.search(test)
    if m:
        print(test, '==>', m.group(1))
