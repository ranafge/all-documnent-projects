import re
import csv
import pandas as pd

with open('sorowar_vaixx.csv', 'r') as f:
    reader = csv.reader(f)

    with open('xxx.csv', 'w') as fi:
        w = csv.writer(fi,lineterminator='\n')
        for line in reader:
            w.writerow(line)


