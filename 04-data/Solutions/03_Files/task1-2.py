# Add comments to this code to explain how it works and predict what it will do.

import csv # Import the csv library

file = open('03_Files/mydata.csv', 'r',) # Open connection to the file with read permission
reader = csv.reader(file, delimiter = ',') # Parse the connection to the csv reader function specifying the delimiter
for row in reader: # Iterate over the file row by row
    print(row) # Print the rows