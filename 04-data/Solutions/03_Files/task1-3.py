import csv

file = open('03_Files/mydata2.csv', 'r',) # Open connection to the file with read permission
reader = csv.DictReader(file) # Parse the connection to the csv dict reader function
for row in reader: # Iterate over the file row by row
    print(row) # Print the rows