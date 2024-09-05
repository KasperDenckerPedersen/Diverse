# Add comments to this code to explain how it works and predict what it will do.

grades = [] # Create an empty list

nGrades = int(input('How many grades do you want to enter:\n>')) # Get input from user and convert to integer

for i in range(0, nGrades): # Ask the user for to enter a new grade and append it to the list grades for each student
    grade = int(input("Please enter the next grade:\n>"))
    grades.append(grade)

print(grades) # Print the list