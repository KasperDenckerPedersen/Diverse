import pandas as pd

# View Operations
movies = pd.read_csv('Data/movies.csv')
print(movies.head())
print(movies.tail())
print(movies.sample())