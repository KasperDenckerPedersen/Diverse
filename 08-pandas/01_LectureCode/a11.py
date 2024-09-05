import pandas as pd

# Group By
movies = pd.read_csv('08-pandas/Data/movies.csv')

movies.dropna(inplace=True)
print(movies.groupby('Genre'))
print(movies.groupby('Genre')['Revenue (Millions)'])
print(movies.groupby('Genre')['Revenue (Millions)'].median().sort_values(
        ascending=False))


def rating_fun(x):
    if x >= 8.0:
        return "good"
    else:
        return "bad"


movies["rating_verbal"] = movies['Rating'].apply(rating_fun)


def complicated_function(x):
    if x['Rating'] >= 8.0 and x['Revenue (Millions)'] <= 100:
        return True
    else:
        return False

movies['rating_complicated'] = movies.apply(complicated_function, axis=1)
print(movies)
