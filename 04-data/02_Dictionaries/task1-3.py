# Add comments to this code to explain how it works and predict what it will do.
# In a dictionary we overwrite the key if the same name is used more than once. In a list it will just be added to the end. 

favoriteFoods = {}

while True:
    name = input('Enter your name:\n>')
    food = input('Enter your favorite food:\n>')
    favoriteFoods[name] = food
    again = input('Do you want to add another person?\n>')
    if again == 'no':
        break

for key in favoriteFoods:
    print(f'{key} loves {favoriteFoods[key]}')
