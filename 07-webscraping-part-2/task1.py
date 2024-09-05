import requests
import json

def get_data(year):

    url = "http://www.scrapethissite.com/pages/ajax-javascript"

    querystring = {"ajax":"true","year": year}

    payload = ""
    response = requests.request("GET", url, data=payload, params=querystring)

    data = json.loads(response.text)
    return data

movies = []
for i in range(2010, 2016):
    data = get_data(i)
    movies = movies + data

for movie in movies:
    print(f"Title: {movie['title']}")
    print(f"Year: {movie['year']}")
    print(f"Number of awards: {movie['awards']}")
    print(f"Number of nominations: {movie['nominations']}\n")