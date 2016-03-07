import csv
from EUCountries import EU_countries

#print len(EU_countries)


def pruning(filename):
	data = []
	with open(filename, 'rb') as csvfile:
		csvreader = csv.reader(csvfile)
		header = next(csvreader)
		data.append(header)
		for row in csvreader:
			if(row[1] in EU_countries):
				data.append(row)
				#print(row)
	return data
    

def writeToCSV(data, filename):
	with open(filename, 'w') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerows(data)

data = pruning('unemployment_rate.csv')
#newData = data.insert(0, "Arsenal")

print data
writeToCSV(data, 'EU_unemployment_rate.csv')

