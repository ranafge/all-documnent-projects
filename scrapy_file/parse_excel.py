import xlrd

book = xlrd.open_workbook('SOWC 2014 Stat Tables_Table 9.xlsx')

for sheet in book.sheets():
    print(sheet.name)
sheet = book.sheet_names()[1]

print(sheet)

for i in range(sheet.nrows):
    print(i)
