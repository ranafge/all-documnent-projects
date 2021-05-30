import re

hand = open('member.txt')

for line in hand:
    line = line.rstrip()
    if re.search(r'Email:.+@', line):
        print(line)


