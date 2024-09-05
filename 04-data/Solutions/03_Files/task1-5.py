# Add comments to this code to explain how it works and predict what it will do.

import csv # Import the csv library

data = [              # Create a list of dictionaries
  {'name': 'John', 'age': 25}, 
  {'name': 'Sara', 'age': 27},
  {'name': 'Mike', 'age': 29}
]

keys = ['name', 'age'] # Set the keys

fileHandler = open('03_Files/newdata.csv', 'w') # Open a write connection to the file
writer = csv.DictWriter(fileHandler, fieldnames=keys) # Parse the connection to the dict write function
writer.writeheader() # Write the keys as header row to the file
for entry in data: # Iterate over the dictionaries in the list
    writer.writerow(entry) # Add the values in the dictionary to the file

fileHandler.close() # Close the connection