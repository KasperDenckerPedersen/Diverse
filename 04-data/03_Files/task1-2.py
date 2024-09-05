# Add comments to this code to explain how it works and predict what it will do.

import csv

file = open('03_Files/mydata.csv', 'r',)
reader = csv.reader(file, delimiter = ',')
for row in reader:
    # print(row)
    print(row[0])
    print(row[1])