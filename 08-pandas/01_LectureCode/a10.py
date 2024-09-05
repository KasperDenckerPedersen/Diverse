import pandas as pd

# Slicing, Selection, Extraction
movies = pd.read_csv('Data/movies.csv')

# Slicing by column
genre_col = movies['Genre']
#print(genre_col)
#print(type(genre_col))

genre_col = movies[['Genre']]
#print(genre_col)
#print(type(genre_col))

genre_col = movies[['Title', 'Genre', 'Description', 'Rating']]
#print(genre_col)
#print(type(genre_col))

# Slicing by row
movies.set_index('Title', inplace=True)

prom = movies.loc["Prometheus"] #Finding something based in a index and searching in that index
#print(prom)

prom = movies.iloc[1] #Using index number and it will always give the index where as before it would always return the title no matter where on the list is is
#print(prom)

# Conditional Selection
test = movies['Director'] == "Ridley Scott" #test is all rows with true and false statements for each movie
#print(test)

condition = movies['Director'] == "Ridley Scott"
#print(movies[condition]) #This prints all the movies where conditions is True

selector1 = movies['Director'] == 'Christopher Nolan'
selector2 = movies['Director'] == 'Ridley Scott'
#print(movies[selector1 | selector2]) #Print movies with either of the directors

selection = ['Christopher Nolan', 'Ridley Scott']
print(movies[movies['Director'].isin(selection)]) #Prints the movies where the director matches a name in the selection list.
#movies[movies] make it print all the movies and not true / false statements, see above