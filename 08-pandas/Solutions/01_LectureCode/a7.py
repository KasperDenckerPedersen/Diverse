import pandas as pd

# Handling Duplicates
movies = pd.read_csv('08-pandas/Data/movies.csv')

tmpDF = pd.concat([movies, movies])
print(tmpDF.shape)

tmpDF = tmpDF.drop_duplicates()
print(tmpDF.shape)

tmpDF = pd.concat([movies, movies])
tmpDF = tmpDF.drop_duplicates(keep=False) #'first' to keep the first movies, and 'last' to keep the last movies
print(tmpDF.shape)

tmpDF = pd.concat([movies, movies])
tmpDF.drop_duplicates(inplace=True)
print(tmpDF.shape)