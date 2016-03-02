import urllib2
import json
from bs4 import BeautifulSoup
from EuropeanCountries import countries

file = open('List_of_countries_by_English-speaking_population.txt', 'w')

url = "https://en.wikipedia.org/wiki/List_of_countries_by_English-speaking_population"
page = urllib2.urlopen(url)

soup = BeautifulSoup(page)

country = ""
english_speakers = ""
data = []

table = soup.find("table", "wikitable sortable")

for row in table.findAll("tr")[1:]:
    
    tmpDict = {}
    cells = row.findAll("td")

    country = cells[0].findAll(text=True)
    eng_speakers = cells[1].findAll(text=True)
    
    country_value = country[1]
    eng_speakers_value = eng_speakers[0]

    if(country_value in countries):
        tmpDict['country'] = country_value
        tmpDict['percentage of english speakers'] = eng_speakers_value
        data.append(tmpDict)
        print country_value, eng_speakers_value

file.write(json.dumps(data))
    