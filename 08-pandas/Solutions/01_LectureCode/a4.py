import pandas as pd

# Getting Info
movies = pd.read_csv('08-pandas/Data/movies.csv')
print(movies.info())
print(movies.shape) #To get number of rows(1000) and columns(12)
