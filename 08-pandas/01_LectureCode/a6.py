import pandas as pd

# Sorting Data
movies = pd.read_csv('Data/movies.csv')

print(movies.sort_values(by=['Year'])) #Default is ascending order

print(movies.sort_values(by=['Year'], ascending = False))

print(movies.sort_values(by=['Year', 'Revenue (Millions)'], ascending = False))
