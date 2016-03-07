import urllib2
import json
from bs4 import BeautifulSoup
from EuropeanCountries import countries
from EUCountries import EU_countries

file = open('../../data/EU_english.json', 'w')

url = "https://en.wikipedia.org/wiki/List_of_countries_by_English-speaking_population"
page = urllib2.urlopen(url)

soup = BeautifulSoup(page)

country = ""
english_speakers = ""
European_data = []
EU_data = []

table = soup.find("table", "wikitable sortable")

for row in table.findAll("tr")[1:]:
    
    tmpDict = {}

    cells = row.findAll("td")

    country = cells[0].findAll(text=True)
    eng_speakers = cells[1].findAll(text=True)
    
    country_value = country[1]
    eng_speakers_value = eng_speakers[0]

    """
    if(country_value in countries):
        tmpDict['country'] = country_value
        tmpDict['percentage of english speakers'] = eng_speakers_value
        European_data.append(tmpDict)
        print country_value, eng_speakers_value
    """
    
    if(country_value in EU_countries):
        tmpDict['country'] = country_value
        tmpDict['percentage of engilsh speakers'] = eng_speakers_value
        EU_data.append(tmpDict)
        #print country_value, eng_speakers_value

# the data of Ireland is missing from the wiki website
EU_data.append({"country": "Ireland", "percentage of engilsh speakers": "94"})
   
file.write(json.dumps(EU_data))
    