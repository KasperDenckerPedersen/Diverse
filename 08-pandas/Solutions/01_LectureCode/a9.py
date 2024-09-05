import pandas as pd

# Working with Columns
movies = pd.read_csv('08-pandas/Data/movies.csv')

print(movies.isnull())
print(movies.isnull().sum()) #Sum of missing values in each column

df_clean = movies.dropna() #Remove all rows with missing values.
#print(df_clean.isnull().sum())
print(df_clean.shape)

movies = pd.read_csv('08-pandas/Data/movies.csv')
revenue = movies['Revenue (Millions)']
movies['Revenue (Millions)'].fillna(revenue.mean(), inplace=True) #Replace missing values with the mean value.
print(revenue.mean())
print(movies)