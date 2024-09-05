import pandas as pd

# Working with Columns
movies = pd.read_csv('Data/movies.csv')

#print(movies.isnull()) #Is the number 0 then True, else false
#print(movies.isnull().sum())

df_clean = movies.dropna()
print(df_clean.shape)

movies = pd.read_csv('Data/movies.csv')

revenue = movies['Revenue (Millions)']
movies['Revenue (Millions)'].fillna(revenue.mean(), inplace=True) #Replaces the missing values with something else
print(movies.isnull().sum())
