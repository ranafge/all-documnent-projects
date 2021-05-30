import csv
import pandas as pd
#
# with open('my_csv_file.txt.csv', 'r') as f:
#     lines = f.readlines()
#     new_list = []
#     for line in lines:
#         for word in line.splitlines():
#             new_list.append(word)
# print(new_list)

# o/p
"""['Sally Whittaker,2018,McCarren House,312,3.75', 'Belinda Jameson,2017,Cushing House,148,3.52', 'Jeff Smith,2018,Prescott House,17-D,3.20', 'Sandy Allen,2019,Oliver House,108,3.48']"""

# with open('numbers_csv.csv', 'r') as f:
#     lines = f.readlines()
#     new_list = []
#     for line in lines:
#         for word in line.split(','):
#             if not word == '\n':
#                 new_list.append(int(word))
# print(new_list)

# csv_file = pd.read_csv('numbers_csv.csv', 'encoding=UTF-8')
# print(csv_file)
# {'valido': 'válido', 'nao e': 'não é', 'invalidos': 'inválidos', 'avaliacao': 'avaliação'}
# final = {}
# with open("fich_teste.txt", 'r') as file:
#     lines = file.readlines()
#     for i,word in enumerate(lines):
#         k,v = word.split(';')
#         final[k] = v.split('\n')[0]
# print(final)
# 
final = {}
with open("fich_teste.txt", 'r') as file:
    for line in file:
        key, value = line.strip().split(';')
        final[key] = value

print(final)
