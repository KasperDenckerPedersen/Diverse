import pandas as pd

# Handling Duplicates
movies = pd.read_csv('Data/movies.csv')

tmpDF = pd.concat([movies, movies])
#print(tmpDF.shape)

tmpDF = tmpDF.drop_duplicates()
#print(tmpDF.shape)

tmpDF = pd.concat([movies, movies])
tmpDF = tmpDF.drop_duplicates(keep=False)
#print(tmpDF.shape)

tmpDF = pd.concat([movies, movies])
tmpDF.drop_duplicates(inplace=True) #Inplace overwrites the tmpDF without naming it before and overwrite it like that. 
print(tmpDF.shape)