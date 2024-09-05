# Add comments to this code to explain how it works and predict what it will do.

data = ['Hello World', 'How are you?', '12345'] # Create a list of data

fileHandler = open('03_Files/newdata.txt', 'w') # Open connection to the file with a write permission

for line in data: # Iterate over the list data
  fileHandler.write(line + '\n') # Write the list items line by line to the file

fileHandler.close() # Close the connection