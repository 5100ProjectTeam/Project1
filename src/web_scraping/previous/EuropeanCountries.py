import urllib2
import json
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_European_countries_by_area"
page = urllib2.urlopen(url)

soup = BeautifulSoup(page)

countries = []

table = soup.find("table", "wikitable sortable")

for row in table.findAll("tr")[1:]:
    cells = row.findAll("td")
     
    country = cells[1].findAll(text=True)
    countries.append(country[0])
  