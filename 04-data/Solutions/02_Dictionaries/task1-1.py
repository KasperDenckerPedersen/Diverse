# Add comments to this code to explain how it works and predict what it will do.

meals = ['Pasta', 'Pizza', 'Kebab', 'Pasta', 'Salad', 'Burger', 'Burger', 'Pizza', 'Pasta'] # Create a list of meals

counts = {} # Create an empty dictionary
for meal in meals: # Iterate over the list of meal
  counts[meal] = counts.get(meal, 0) + 1 # Use the name of the meal as key in the dictionary counts and check if it is already there. If so increase the value by one, if not set it to 1

print(counts) # print out the dictionary showing all meals as keys and the count how often they are in the list as values