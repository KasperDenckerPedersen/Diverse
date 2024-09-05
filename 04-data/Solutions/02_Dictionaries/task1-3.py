# Add comments to this code to explain how it works and predict what it will do.

favoriteFoods = {} # Create an empty dictionary

while True: # Iterate until the loop breaks
    name = input('Enter your name:\n>') # Get input and store it as name
    food = input('Enter your favorite food:\n>') # Get input and store it as food
    favoriteFoods[name] = food # Add an entry to the dictionary with name as key and food as value
    again = input('Do you want to add another person?\n>') # Ask it the user wants to stop
    if again == 'no':
        break

for key in favoriteFoods: # Print out all the favorite foods
    print(f'{key} loves {favoriteFoods[key]}')