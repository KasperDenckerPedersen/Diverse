import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_csv('Data/movies.csv')

movies.plot(kind='scatter',
            x='Rating',
            y='Revenue (Millions)',
            title='Revenue vs Rating',
            )

# plt.show()
plt.savefig('01_LectureCode/a5.png')