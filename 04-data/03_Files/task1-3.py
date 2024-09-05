# Add comments to this code to explain how it works and predict what it will do.

#DictReader knows first row in the mydata2 is the headers. 

import csv

file = open('03_Files/mydata2.csv', 'r',)
reader = csv.DictReader(file)
for row in reader:
    print(row)