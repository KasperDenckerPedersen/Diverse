import pandas as pd

# Reading and Writing Data Frames
movies = pd.read_csv('08-pandas/Data/movies.csv')
print(movies)

# url = 'https://raw.githubusercontent.com/wi3jmu/PDS1920/master/Lecture/data/IMDB-Movie-Data.csv'
# movies = pd.read_csv(url)
# print(movies)
#Can only be done in github, when you are online. Dosn't work when working locally.

movies.to_csv('08-pandas/Data/movies_modified.csv', index='Year')

movies = pd.read_csv('08-pandas/Data/movies_modified.csv')
print(movies)
