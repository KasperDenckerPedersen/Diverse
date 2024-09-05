# Add comments to this code to explain how it works and predict what it will do. 

letters = ['a', 'z', 'd', 'x', 'g', 'f'] # Create a list with multiple letters

letters.sort() # Sort the list alphabetically 

output = '' # Create an empty string
for letter in letters: # Concatenate all the strings in the ordered list
  output += letter
print(output)

# What will be the output of the code?
  # adfgxz

# What happens in line 5? Why might the result be different than we expect?
  # The list is sorted and the result is stored. We might expect the sorting to be lost as we do not catch a return value anywhere. However, in Python this is not required (but also not forbidden) as lists are manipulated inplace.