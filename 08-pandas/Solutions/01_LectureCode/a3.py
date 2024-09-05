import pandas as pd

# View Operations
movies = pd.read_csv('08-pandas/Data/movies.csv')
print(movies.head()) #First 5 bu default
print(movies.tail()) #First 5 by default
print(movies.sample(5, axis=0)) #5 random rows, 1 by default, axis = 1 to get a random column.