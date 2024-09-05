# Add comments to this code to explain how it works and predict what it will do.

names = ['Sara', 'Mike', 'Julia', 'Sven'] # Create a list of names
attending = [True, False, False, True] # Create a list of attendance

classAttendance = {} # Create an empty dictionary to store the attendance of the students
for i in range(0, len(names)): # Iterate over the indices of the list names
  classAttendance[names[i]] = attending[i] # Assign each name as the key and the attendance as the value to the dictionary

print(classAttendance) # Print the attendance

# What does the program do?
  # Combine both list to one dictionary

# What will happen if we have two students with the same name?
  # The attendance of the first name will be overwritten