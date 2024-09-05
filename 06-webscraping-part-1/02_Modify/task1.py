import requests
import bs4

url = 'http://www.scrapethissite.com/pages/simple/'

r = requests.get(url)
htmlText = r.text
htmlDocument = bs4.BeautifulSoup(htmlText, 'html.parser')

search = {'class': 'col-md-4 country'}

countries = htmlDocument.find_all('div', search)

searchName = {'class': 'country-name'}
searchCapital = {'class': 'country-capital'}
searchPopulation = {'class': 'country-population'}
searchArea = {'class': 'country-area'}

countryBook = {}

for country in countries:
    countryName = country.find('h3', searchName)
    countryCapital = country.find('span', searchCapital)
    countryPopulation = country.find('span', searchPopulation)
    countryArea = country.find('span', searchArea)
    countryBook[countryName.text.strip()] = {'Country Name': countryName.text.strip(), 
                                             'Country Capital': countryCapital.text.strip(), 
                                             'Country Population': countryPopulation.text.strip(), 
                                             'Country Area': countryArea.text.strip()}

for name in countryBook.keys():
    print(f"Country Name: {countryBook[name]['Country Name']}\nCapital: {countryBook[name]['Country Capital']}\nPopulation: {countryBook[name]['Country Population']}\nArea: {countryBook[name]['Country Area']}\n")
