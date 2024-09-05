import pandas as pd
import requests
from io import StringIO

url = 'https://raw.githubusercontent.com/Apress/data-analysis-and-visualization-using-python/master/Ch07/Salaries.csv'
response = requests.get(url, verify=False)
data = StringIO(response.text)
salaries = pd.read_csv(data)

# url = 'https://raw.githubusercontent.com/Apress/data-analysis-and-visualization-using-python/master/Ch07/Salaries.csv'

# salaries = pd.read_csv(url)

# Number of records and column names
print(f'Number of records: {salaries.shape[0]}')
print(f'Columns: {salaries.columns}')

# Standard deviation
print(salaries.describe().loc['std'])

# Mean values for first 50 values
print(salaries.iloc[0:50]['salary'].mean())

# Basic statistics for salary column
print(salaries.describe()['salary'])

# Correlation
print(salaries.corr(numeric_only=True))

# Average salary by gender, rand and salary + rank
print(salaries.groupby('sex')['salary'].mean())
print(salaries.groupby('rank')['salary'].mean())
print(salaries.groupby(['sex', 'rank'])['salary'].mean())

# Check for tenure
def up_for_tenure(x):
    if x >= 6:
        return True
    else:
        return False

salaries['up_for_tenure'] = salaries['phd'].apply(up_for_tenure)

# Cbeck for tenure advanced
def up_for_tenure_advanced(x):
    if x['rank'] == 'AsstProf':
        if x['phd'] >= 6:
            return True
        else:
            return False
    else:
        return False
    
salaries['up_for_tenure_advanced'] = salaries.apply(up_for_tenure_advanced, axis=1)
print(salaries[salaries['rank'] == 'AsstProf'])