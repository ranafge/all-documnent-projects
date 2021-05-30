from io import StringIO
import csv
import pyexcel
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.options.display.max_columns = 500

with open('soro.csv', 'r') as f:
    reader = csv.reader(f)
    import re
    value = 1
    for line in reader:
        for email in  re.findall(r'Email:\s\w+\.?-?\s?\w+?@\w+-?\w+\.?\w+\.?\w+[2]?', str(line)):
            print(value, email)
            value +=1
