# The following code checks if a student has already collected enough ECTS points to write the Bachelor thesis

minPoints = 120
points = int(input("How many ECTS points do you already have?\n"))

print(f'Allowed to write thesis: {points >= minPoints}')

# Modify the code to print if a student is allowed to write the thesis or not