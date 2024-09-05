# Variable Assignment - Modify

name1 = "Axl"
name2 = "Slash"

# Add 2 more variables to store 'Duff' and 'Izzy'
name3 = "Duff"
name4 = "Izzy"


# This line uses concatenation to join the variables together with the string 'and' to make a sentence. Complete the line to output all of the variables 
print(name1 + " and " + name2 + " and " + name3 + " and " + name4) # Option 1
print(f'{name1} and {name2} and {name3} and {name4}') # Option 2
print(name1, name2, name3, name4, sep=" and ") # Option 3