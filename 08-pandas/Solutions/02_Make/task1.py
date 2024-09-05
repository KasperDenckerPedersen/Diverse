import pandas as pd

# Load data
movies = pd.read_csv('08-pandas/Data/movies.csv')

# Set index
movies.set_index('Title', inplace=True)

# Rename columns
movies.columns = [x.lower() for x in movies.columns] #Lower case all column names
movies.rename(columns={
    'runtime (minutes)': 'runtime_minutes',
    'revenue (millions)': 'revenue_millions'
    }, inplace=True)

# Replace missing values
movies['revenue_millions'].fillna(movies['revenue_millions'].mean(), inplace=True)
movies['metascore'].fillna(movies['metascore'].mean(), inplace=True)

# Find all movies released between 2005 and 2010
print(movies[(movies['year'] >= 2005) & (movies['year'] <= 2010)])

# Find all movies with a rating above 8.0
print(movies[movies['rating'] > 8].sort_values('rating', ascending=False))

# Find all movies that made below the 25th percentile in revenue
print(movies[movies['revenue_millions'] < movies['revenue_millions'].quantile(0.25)])

