d = {'invoice_date': '2021-02-12T15:48:52+05:30',
     'no_of_bill_files': '3',
     'amount': '12', 'gst': '12',
     'bill0': 123, 'bill1': 456, 'bill2': 789, 'owner': 2}

import re
# print(d.items())
# for i in d.keys():
#     if i in re.findall('bill\d+'):
#       print(i)
# print(re.findall('bill\d+'), d.items())
cond = {'invoice_date': '2021-02-12T15:48:52+05:30',
'no_of_bill_files': '3',
'amount': '12', 'gst': '12',
'bill0': 123, 'bill1': 456, 'bill2': 789, 'owner': 2}
li = bill = [{'document': cond[f'bill{i}']} for i in range(int(cond['no_of_bill_files']))]
print(li)
# First convert list of dictionary of 3 bill like
print([{'document':d[f'bill{i}']}for i in range(3)])
# Then use range function as
print([{'document':d[f'bill{i}']}for i in range(int(d['no_of_bill_files']))])
print(list(d.items()))
print([i for i in list(d.items())])
