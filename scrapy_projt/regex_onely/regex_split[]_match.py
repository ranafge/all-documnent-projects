import re
tests = ['john', 'john[doe]']

pattern = re.compile(r'^([^\[\]]+)(?:\[([^\]]+)])?')

for test in tests:
    m = pattern.match(test)
    if m:
        print(test, ' ->', m[1], m[2])
