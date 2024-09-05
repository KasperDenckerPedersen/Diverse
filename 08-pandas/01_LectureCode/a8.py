import pandas as pd

# Working with Columns
movies = pd.read_csv('Data/movies.csv')

#print(movies.columns)
movies.rename(columns={
    'Runtime (Minutes)': 'Runtime',
    'Revenue (Millions)': 'Revenue_millions'
},
              inplace=True)
#print(movies.columns)

movies.columns = [
    'rank', 'title', 'genre', 'description', 'director', 'actors', 'year',
    'runtime', 'rating', 'votes', 'revenue_millions', 'metascore'
]
print(movies.columns)

movies = pd.read_csv('Data/movies.csv')
#print(movies.columns)
movies.columns = [col.lower() for col in movies.columns]

columns = []
for col in movies.columns:
    columns.append(col.lower())
movies.columns = columns

#print(movies.columns)
