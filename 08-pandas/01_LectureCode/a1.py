import pandas as pd

# Creating and Indexing Data Frames
data = {'ordered': [3, 2, 7, 3], 'delivered': [0, 2, 4, 2]}
purchases = pd.DataFrame(data)
print(purchases)

names = ['June', 'Robert', 'Lily', 'David']
purchases = pd.DataFrame(data, index = names)

print(purchases)
print('\n')
print(purchases.loc['June'])

