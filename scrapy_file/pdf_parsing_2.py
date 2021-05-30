import PyPDF2
import pandas as pd
import csv
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

with open(r'Associate Member.pdf', 'rb') as f:
    pdf = PyPDF2.PdfFileReader(f)
    pages = pdf.getNumPages()
    data = []
    for page in range(pages):
        print(page)
        page = pdf.getPage(page)
        content = page.extractText().strip().split('\n')
        mylist = []
        for word in content:
            if word.endswith('.com') | word.endswith('.org')|word.endswith('.biz') |word.endswith('.net') \
               | word.endswith('mail: ')\
               | word.endswith('.boutique')\
               | word.endswith('.ne')\
               | word.endswith('.bd')\
               | word.endswith('.au')\
               | word.endswith('.tr')\
               | word.endswith('.hk')\
               | word.endswith('.de')\
               | word.endswith('.dk')\
               | word.endswith('.Net')\
               | word.endswith('.cn')\
               | word.endswith('.co')\
               | word.endswith('@run-way.fashrion')\
               | word.endswith('.za'):
                mylist.append(word)
                mylist.append('\n')
            else:
                mylist.append(word)

        print(mylist)
