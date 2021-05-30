import PyPDF2
import pandas as pd
import csv
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
import re

with open(r'Associate Member.pdf', 'rb') as f:
    pdf = PyPDF2.PdfFileReader(f)
    pages = pdf.getNumPages()
    with open('sorowar_vaixx.csv', 'w') as f:
        for page in range(pages):
            print(page)
            page = pdf.getPage(page)
            content = page.extractText().strip().split('\n')
            content = content[1:len(content)-1:]
            wr = csv.writer(f)
            wr.writerow(content)






