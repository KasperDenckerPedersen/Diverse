# Write your code here
import pandas as pd

# Load data
movies = pd.read_csv('Data/movies.csv')

#Load the data and set the column ```title``` as index
movies.set_index('Title', inplace=True)
#print(movies)

#Change the column names to avoid capital letters, white spaces and brackets
movies.columns = movies.columns.str.lower()
movies.columns = movies.columns.str.replace(' ', '_')
movies.columns = movies.columns.str.replace('(', '')
movies.columns = movies.columns.str.replace(')', '')
#print(movies.columns)

#Replace the missing values in all rows with the median of the respective column
movies.fillna(movies.median(numeric_only= True), inplace=True)
#print(movies)

#Find all movies that were released between 2005 and 2010
selector1 = movies['year'] > 2005
selector2 = movies['year'] < 2010
#print(movies[selector1 & selector2])

#Find all movies that have a rating above 8.0
condition1 = movies['rating'] > 8.0
#print(movies[condition1])

#Find all movies that made below the 25th percentile in revenue
revenuePercentile = movies['revenue_millions'].quantile(0.25)
condition2 = movies['revenue_millions'] < revenuePercentile
#print(movies[condition2])

#Print all conditions in one
print(movies[selector1 & selector2 & condition1 & condition2])