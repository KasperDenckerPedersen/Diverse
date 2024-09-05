##Importrimg data:
import pandas as pd
import matplotlib.pyplot as plt
import requests

## 1) Import from csv:
# movies = pd.read_csv('Data/movies.csv')
# print(movies)

## 2) #Import from url (only online)
# url = 'https://raw.githubusercontent.com/wi3jmu/PDS1920/master/Lecture/data/IMDB-Movie-Data.csv'
# movies = pd.read_csv(url)
# print(movies)

## 3) Import from url (locally)
##Make it to a csv file and then read it as 1)

# url = 'https://raw.githubusercontent.com/wi3jmu/PDS1920/master/Lecture/data/IMDB-Movie-Data.csv'
# response = requests.get(url)

# if response.status_code == 200:
#     with open('08-pandas/Data/output.csv', 'w', newline='') as csvfile:
#         csvfile.write(response.text)

movies = pd.read_csv('08-pandas/Data/output.csv')
print(movies)

##Print data about a specific row:
#print(movies.loc[100])

##View operations:
#print(movies.columns) #See the names of all columns
#print(movies.head()) #First 5 bu default
#print(movies.tail()) #First 5 by default
#print(movies.sample(5, axis=0)) #5 random rows, 1 by default, axis = 1 to get a random column.

#print(movies.shape[0]) #Number of Rows
#print(movies.shape[1]) #Number of Columns

#print(movies['Director'].value_counts()[:10]) #Print the top n directors with most movies. 

##View info (count, mean, std, min, max, quantiles):
#print(movies.describe()) #If not all counts is the same, there is missing values
#print(movies['Genre'].describe()) #See for only one column
#print(movies['Genre'].unique()) #Prints a list with all the unique values/names in a column
#print(movies['Genre'].value_counts()) #Counts how many times each unique value appears. 

##Sorting:
#print(movies.sort_values(by=['Year'])) #Ascending by default
#print(movies.sort_values(by=['Year'], ascending = False)) #Ascending
#print(movies.sort_values(by=['Year', 'Revenue (Millions)'], ascending = False)) #First by Year and then by revenue

##Dublicates:
#tmpDF = pd.concat([movies, movies]) #Creating a new DataFrame with movies twice in a row.

#tmpDF = tmpDF.drop_duplicates() #Remove all dublicates
#tmpDF.drop_duplicates(inplace=True) #Remove the dublicates in place.

##Rename columns
# movies.rename(columns={
#     'Runtime (Minutes)': 'Runtime',
#     'Revenue (Millions)': 'Revenue_millions'
# },
#               inplace=True) #Renaming and replacing them directly in place. Will not work if inplace = False.

#Manual write the column names:
# movies.columns = [
#     'rank', 'title', 'genre', 'description', 'director', 'actors', 'year',
#     'runtime', 'rating', 'votes', 'revenue_millions', 'metascore'
# ]

##Make all columns lower case:
#movies.columns = [col.lower() for col in movies.columns]

#Or
# columns = []
# for col in movies.columns:
#     columns.append(col.lower())
# movies.columns = columns

#Or change it by one type at a time:
# movies.columns = movies.columns.str.lower()
# movies.columns = movies.columns.str.replace(' ', '_')
# movies.columns = movies.columns.str.replace('(', '')
# movies.columns = movies.columns.str.replace(')', '')

##Missing values:
#print(movies.isnull().sum()) #Sum of missing values in each column
#df_clean = movies.dropna() #Remove all rows with missing values.
#movies['Revenue (Millions)'].fillna(revenue.mean(), inplace=True) #Replace missing values with the mean value.
#movies.fillna(movies.median(numeric_only= True), inplace=True) #Replace the missing values in all rows with the median of the respective column

##Set index to a specific column:
# movies.set_index('Title', inplace=True) #Set index to be a specific column

# prom = movies.loc["Prometheus"] #Searching in index rows by the name
# prom = movies.iloc[1] #Searching in index by index number

# Conditional Selection
# movies[movies['Director'] == "Ridley Scott"]

# selector1 = movies['Director'] == 'Christopher Nolan'
# selector2 = movies['Director'] == 'Ridley Scott'
# print(movies[selector1 | selector2])

# selection = ['Christopher Nolan', 'Ridley Scott'] #Selection is a list
# print(movies[movies['Director'].isin(selection)])

##Group by:
# movies.dropna(inplace=True)
# print(movies.groupby('Genre')['Revenue (Millions)'].max().sort_values(
#         ascending=False))

##Create a new column based on other existing columns
# def succesAndgood(row):
#     rating = row['Rating']
#     revenue = row['Revenue (Millions)']
#     if rating >= 8.0 and revenue >= 300:
#         return "Succes and good"
#     elif rating >= 8.0 and revenue < 300:
#         return "Unsuccesfull but good"
#     elif rating < 8.0 and revenue >= 300:
#         return "Succesfull but bad"
#     else:
#         return "Unsuccesfull and bad"
# movies["Succes & Good"] = movies.apply(succesAndgood, axis=1)
# print(movies['Succes & Good'])
##Or
# def is_action_or_comedy(x):
#     if 'Action' in x:
#         if 'Comedy' in x:
#             return "both"
#         else:
#             return "action"
#     else:
#         if 'Comedy' in x:
#             return "comedy"
#         else:
#             return "neither"

# movies["action_comedy"] = movies["Genre"].apply(is_action_or_comedy)
# print(movies["action_comedy"])

##Or
# def Succes_movies(row):
#     if row['Revenue (Millions)'] >= 300 and row['Metascore'] >= 70:
#         return True
#     else:
#         return False

# movies['Succes_Movies'] = movies.apply(Succes_movies, axis=1) #Axis 1 applying it on each row, default is 0 and it apply to columns.
# selector1 = movies['Succes_Movies'] == True
# print(movies[selector1])

##Plotting:
# 'hist', 'bar', 'box', 'line', 'scatter'
# legend=True gives each line a title
# movies.groupby('Year')['Revenue (Millions)'].sum().plot(kind="line", legend=True) #Plot directly, () is the x-axis, [] is the y-axis
# plt.show()

##Plot with more group by: remember to unmark the function is_action_or_comedy + line below
# annualRevenuePerGenre = movies.groupby(['Year', 'action_comedy'])['Revenue (Millions)'].sum()

# annualRevenuePerGenre = annualRevenuePerGenre.to_frame()
# annualRevenuePerGenre.reset_index(inplace=True)
# annualRevenuePerGenre.set_index('Year', inplace=True)

# annualRevenuePerGenre.groupby('action_comedy')['Revenue (Millions)'].plot(legend=True)

##Plot scatter:
# movies.plot(kind='scatter',
#             x='Rating',
#             y='Revenue (Millions)',
#             title='Revenue vs Rating',
#             )

# plt.show()

##Ensures that the titles of the subplots do not overlap with each other and that all subplots fit nicely within the figure window.
#plt.tight_layout()

#print(movies['Revenue (Millions)'])

##Correlation matrix:
# moviesDataFrame = pd.DataFrame(movies)
# correlationMatrix = moviesDataFrame[['Rating', 'Revenue (Millions)', 'Metascore']].corr()
# print(correlationMatrix)

# print("")
# print(correlationMatrix['Rating'])

# print("")
# print(correlationMatrix['Rating']['Metascore'])

##Loop through correlation matrix:
# for column1 in correlationMatrix.columns:
#     for column2 in correlationMatrix.columns:
#         if correlationMatrix[column1][column2] < 1:
#             if correlationMatrix[column1][column2] >= 0.5:
#                 print(f"The correlation of {correlationMatrix[column1][column2]} between {column1} and {column2} is significant\n")
#             else:
#                 print(f"No significant correlation between {column1} and {column2}\n")