# Data Analysis with Pandas - Make
Write your own code to solve at the tasks following tasks:

## Task 1: Basic DataFrame Operations
Use the movie data stores in the file ```Data/movies.csv``` to solve the following subtasks:
- Load the data and set the column ```title``` as index
- Change the column names to avoid capital letters, white spaces and brackets
- Replace the missing values in all rows with the median of the respective column
- Find all movies that were released between 2005 and 2010
- Find all movies that have a rating above 8.0
- Find all movies that made below the 25th percentile in revenue


## Task 2: Aggregation and Grouping
Under the url in file ```task2.py``` you will find a data set on academic salaries. Use it so solve the following subtasks:
- Find how many records this data frame has, what are the column names?
- Calculate standard deviation for all numeric columns.
- What are the mean values of the first 50 records in the dataset?
- Calculate basic statistics for the salary column
- Determine the correlation between the numeric values – is there an age effect on salary?
- Calculate the average salary by gender, rank and gender+rank
- Write a function that checks if a professor is up for tenure by checking if the time passed since obtaining the phd is at least 6 years. Apply the function to each row of the DataFrame.
- Write a more realistic function that checks if a professor is up for tenure by checking if rank is assistant and the time passed since obtaining the phd is at least 6 years. Apply the function to each row of the DataFrame.
