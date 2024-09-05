# Add comments to this code to explain how it works and predict what it will do.

names = ["Alex","Anita","Patrick", "Atif","Sue"] # Create a list of names

print("Enter a number for your choice.")
print("1. Show all")
print("2. Add name")
print("3. Show name")
print("4. Exit")
choice = int(input()) # Get user input

if choice == 1:
  print(names) # Print all names
elif choice == 2:
  name = input("Enter the name:\n>")
  names.append(name) # Add the new name
elif choice == 3:
  print("Enter the index of the name") # Ask for the list index of a name
  index = int(input())
  print(names[index]) # Print the name stored at the index position from the list
else:
  print("Goodbye")


# What would happen if you choose option “3” and entered index “0”? 
  # The program will print Alex

# What would happen if you choose option “3” and entered index “7”?
  # The program will throw an error as index 7 does not exist in the list

# What would happen if you choose option “2” and entered the name “Stuart”?
  # The name Stuart would be added to the list names