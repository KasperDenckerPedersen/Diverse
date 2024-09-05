import pandas as pd

# Reading and Writing Data Frames
movies = pd.read_csv('Data/movies.csv')
print(movies)

url = 'https://raw.githubusercontent.com/wi3jmu/PDS1920/master/Lecture/data/IMDB-Movie-Data.csv'
movies = pd.read_csv(url)
print(movies)

movies.to_csv('Data/movies_modified.csv', index=False)

movies = pd.read_csv('Data/movies_modified.csv')
