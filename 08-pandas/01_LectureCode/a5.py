import pandas as pd

# Getting Info
movies = pd.read_csv('Data/movies.csv')
print(movies.describe())

print(movies['Genre'].describe())
#print(movies['Genre'].unique())
print(movies['Genre'].value_counts())
