import urllib2
import json
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Member_state_of_the_European_Union"
page = urllib2.urlopen(url)

soup = BeautifulSoup(page)

EU_countries = []

table = soup.find("table", "wikitable sortable")

for row in table.findAll("tr")[1:]:
    cells = row.findAll("th")
     
    EU_country = cells[0].findAll(text=True)
    #print(EU_country[0])

    EU_countries.append(EU_country[0])
  