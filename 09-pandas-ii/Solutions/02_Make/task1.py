import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Data/StudentsPerformance.csv')


# Task 1
## Task 1.1
parentEducation = df.groupby(['parental_education'])[['math_score', 'reading_score', 'writing_score']].mean()
parentEducation.plot(kind='bar')
plt.savefig('02_Make/subtask1.png')

## Task 1.2
df.groupby('gender').boxplot()
plt.savefig('02_Make/subtask2.png')

## Task 1.3
colors = df['reading_score'] > 80
df.plot(kind='scatter', x='math_score', y='reading_score', color = colors)
plt.xlabel('Reading Score')
plt.ylabel('Math Score')
plt.title('Scatter Plot of Math Scores vs. Reading Scores')
plt.savefig('02_Make/subtask3.png')