import pandas as pd
import requests
from io import StringIO

url = 'https://raw.githubusercontent.com/Apress/data-analysis-and-visualization-using-python/master/Ch07/Salaries.csv'
response = requests.get(url, verify=False)
data = StringIO(response.text)
salaries = pd.read_csv(data)

print(salaries)