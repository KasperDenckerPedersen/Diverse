# Add comments to this code to explain how it works and predict what it will do.

names = ['Sara', 'Mike', 'Julia', 'Sven']
attending = [True, False, False, True]

classAttendance = {}
for i in range(0, len(names)):
  classAttendance[names[i]] = attending[i]

print(classAttendance)

# What does the program do?
  # Answer
  #Prints the name and if they attended class

# What will happen if we have two students with the same name?
  # Answer
  #Since we use dictionary, it will overwrite the values if we have two of the same name. 

