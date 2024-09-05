# Add comments to this code to explain how it works and predict what it will do.

grades = {'Mike': -3, 'Sandra': 12, 'Josh': 10, 'Anna': 7} # Create a dictionary of grades 

for key, value in grades.items(): # Iterate over the key, value pairs of the dictionary (the variable key iterates over the names and the variable value over the grades)
    print(f'{key}: {value}') # Print out the names and the according grades

print(sum(grades.values()) / len(grades.values())) # Calculate and print the average grade