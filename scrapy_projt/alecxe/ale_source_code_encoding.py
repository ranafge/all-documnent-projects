import sys
import csv
print(sys.getdefaultencoding())

def read_file():
    with open('t.txt', 'r') as f:
        data = [row for row in csv.reader(f.read().splitlines()) ]
    return data
print(read_file())
