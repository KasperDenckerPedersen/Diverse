# Add comments to this code to explain how it works and predict what it will do.

grades = []

nGrades = int(input('How many grades do you want to enter:\n>'))

for i in range(0, nGrades):
    grade = int(input("Please enter the next grade:\n>"))
    grades.append(grade)

print(grades)
