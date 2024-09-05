import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_csv('Data/movies.csv')

n=10
directors = movies['Director'].value_counts()[:n].index.tolist()
movies[movies['Director'].isin(directors)].boxplot(column=['Rating'], by="Director", vert=False)

# plt.show()
plt.tight_layout()
plt.savefig('01_LectureCode/a7.png')

