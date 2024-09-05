import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_csv('Data/movies.csv')

annualRevenuePerGenre = movies.groupby(['Year', 'Genre'])['Revenue (Millions)'].sum()

annualRevenuePerGenre = annualRevenuePerGenre.to_frame()
annualRevenuePerGenre.reset_index(inplace=True)
annualRevenuePerGenre.set_index('Year', inplace=True)

annualRevenuePerGenre.groupby('Genre')['Revenue (Millions)'].plot(legend=True)
# plt.show()
plt.savefig('01_LectureCode/a3.png')