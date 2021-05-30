import re

para = '''good start
 project you always wanted
 stars are shining brightly
 Start working on that
 hi there
 start and try to
 finish the book
 bye'''
word = re.compile(r'start')
for line in para.split('\n'):
    if not word.search(line):
        print(line)
