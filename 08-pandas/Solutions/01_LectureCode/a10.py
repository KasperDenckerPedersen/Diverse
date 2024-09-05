import pandas as pd

# Slicing, Selection, Extraction
movies = pd.read_csv('08-pandas/Data/movies.csv')

# Slicing by column
genre_col = movies['Genre']
print(genre_col)
print(type(genre_col))

# genre_col = movies[['Genre']]
# print(genre_col)
# print(type(genre_col))

genre_col = movies[['Genre', 'Description', 'Rating']]
print(genre_col)
print(type(genre_col))

# Slicing by row
movies.set_index('Title', inplace=True) #Set index to be a specific column

prom = movies.loc["Prometheus"]
print(prom)

prom = movies.iloc[1]
print(prom)

# Conditional Selection
movies[movies['Director'] == "Ridley Scott"]

selector1 = movies['Director'] == 'Christopher Nolan'
selector2 = movies['Director'] == 'Ridley Scott'
print(movies[selector1 | selector2])

selection = ['Christopher Nolan', 'Ridley Scott']
print(movies[movies['Director'].isin(selection)])
