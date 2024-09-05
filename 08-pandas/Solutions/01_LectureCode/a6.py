import pandas as pd

# Sorting Data
movies = pd.read_csv('08-pandas/Data/movies.csv')

#print(movies.sort_values(by=['Year'])) #Ascending by default

#print(movies.sort_values(by=['Year'], ascending = False))

#print(movies.sort_values(by=['Year', 'Revenue (Millions)'], ascending = False))
