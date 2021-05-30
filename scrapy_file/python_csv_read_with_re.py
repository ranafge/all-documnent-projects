import re
import csv
# (?=")(.*)\,(?="?Tel)
with open('xxx.csv', 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        print(row)
        sent = ""
        for d in row:
            sent +=d
        print(sent)
        res =re.search(r'(?=")(.*)\,(?="?Tel)', sent)
        print(res)
        break
