# Add comments to this code to explain how it works and predict what it will do.

meals = ['Pasta', 'Pizza', 'Kebab', 'Pasta', 'Salad', 'Burger', 'Burger', 'Pizza', 'Pasta']

# Counts how many times all meals appears in a list by storing it in a dictionary and count + 1 every time it appears
counts = {}
for meal in meals:
  counts[meal] = counts.get(meal, 0) + 1

print(counts)