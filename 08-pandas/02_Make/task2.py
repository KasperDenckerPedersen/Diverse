import pandas as pd
url = 'https://raw.githubusercontent.com/Apress/data-analysis-and-visualization-using-python/master/Ch07/Salaries.csv'
persons = pd.read_csv(url)

#print(persons)

# Write your code here
#Find how many records this data frame has, what are the column names?
#print(persons.shape[0])
#print(persons.columns)

#Calculate standard deviation for all numeric columns.
std = persons.std(numeric_only=True)
#print(std)

#What are the mean values of the first 50 records in the dataset?
persons50 = persons.head(50)
meanPerson = persons50.mean(numeric_only=True)
#print(meanPerson)

#Calculate basic statistics for the salary column
mean_salary = persons['salary'].mean()
median_salary = persons['salary'].median()
std_salary = persons['salary'].std()
min_salary = persons['salary'].min()
max_salary = persons['salary'].max()

#print(f"Mean Salary: {mean_salary}")
#print(f"Median Salary: {median_salary}")
#print(f"Standard Deviation: {std_salary}")
#print(f"Minimum Salary: {min_salary}")
#print(f"Maximum Salary: {max_salary}")

#Determine the correlation between the numeric values – is there an age effect on salary?
#correlation_matrix = persons.corr(numeric_only=True)
#age_salary_correlation = correlation_matrix.loc['age', 'salary']
#print(f"\nCorrelation between age and salary: {age_salary_correlation}")

# Calculate the average salary by gender
avg_salary_by_gender = persons.groupby('sex')['salary'].mean()

# Calculate the average salary by rank
avg_salary_by_rank = persons.groupby('rank')['salary'].mean()

# Calculate the average salary by gender and rank
avg_salary_by_gender_rank = persons.groupby(['sex', 'rank'])['salary'].mean()

#print(f"Average salary by gender: {avg_salary_by_gender}\n")

#print(f"Average salary by rank: {avg_salary_by_rank}\n")

#print(f"Average salary by gender and rank: {avg_salary_by_gender_rank}")

#Write a function that checks if a professor is up for tenure by checking if the time passed since obtaining the phd is at least 6 years. Apply the function to each row of the DataFrame.

def is_up_for_tenure(row):
    current_year = 2024
    years_since_phd = current_year - row['phd']
    return years_since_phd >= 6

persons['up_for_tenure'] = persons.apply(is_up_for_tenure, axis=1)

#print(persons[persons['up_for_tenure']])

#Write a more realistic function that checks if a professor is up for tenure by checking if rank is assistant and the time passed since obtaining the phd is at least 6 years. Apply the function to each row of the DataFrame.
def is_up_for_tenure_realistic(row):
    current_year = 2024
    years_since_phd = current_year - row['phd']
    return row['rank'] == 'AsstProf' and years_since_phd >= 6

persons['up_for_tenure'] = persons.apply(is_up_for_tenure_realistic, axis=1)

#print(persons[persons['up_for_tenure']])