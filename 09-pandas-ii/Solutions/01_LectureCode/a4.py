import pandas as pd
import matplotlib.pyplot as plt


def is_action_or_comedy(x):
    if 'Action' in x:
        if 'Comedy' in x:
            return "both"
        else:
            return "action"
    else:
        if 'Comedy' in x:
            return "comedy"
        else:
            return "neither"


movies = pd.read_csv('Data/movies.csv')

movies["action_comedy"] = movies["Genre"].apply(is_action_or_comedy)

annualRevenuePerGenre = movies.groupby(['Year', 'action_comedy'])['Revenue (Millions)'].sum()

annualRevenuePerGenre = annualRevenuePerGenre.to_frame()
annualRevenuePerGenre.reset_index(inplace=True)
annualRevenuePerGenre.set_index('Year', inplace=True)

annualRevenuePerGenre.groupby('action_comedy')['Revenue (Millions)'].plot(legend=True)

# plt.show()
plt.savefig('01_LectureCode/a4.png')