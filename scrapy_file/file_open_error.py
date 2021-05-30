import csv

with open('my_csv_file.txt.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_file:
        print(line)
