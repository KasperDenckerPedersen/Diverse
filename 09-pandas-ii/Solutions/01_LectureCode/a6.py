import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_csv('Data/movies.csv')

movies['Rating'].plot(
    kind='hist', 
    title='Rating'
    )


# plt.show()
plt.savefig('01_LectureCode/a6.png')

