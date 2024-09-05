# Add comments to this code to explain how it works and predict what it will do.

data = ['Hello World', 'How are you?', '12345']

fileHandler = open('03_Files/newdata.txt', 'w')

for line in data:
  fileHandler.write(line + '\n')

fileHandler.close()