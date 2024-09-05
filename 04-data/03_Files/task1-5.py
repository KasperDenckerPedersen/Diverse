# Add comments to this code to explain how it works and predict what it will do.

import csv

data = [
  {'name': 'John', 'age': 25}, 
  {'name': 'Sara', 'age': 27},
  {'name': 'Mike', 'age': 29}
]

keys = ['name', 'age']

fileHandler = open('03_Files/newdata.csv', 'w')
writer = csv.DictWriter(fileHandler, fieldnames=keys)
writer.writeheader()
for entry in data:
    writer.writerow(entry)

fileHandler.close()