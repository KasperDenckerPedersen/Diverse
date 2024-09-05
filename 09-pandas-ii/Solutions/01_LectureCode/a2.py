import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_csv('Data/movies.csv')
movies.groupby(['Year'])['Revenue (Millions)'].sum().plot()

# plt.show()
plt.savefig('01_LectureCode/a2.png')
