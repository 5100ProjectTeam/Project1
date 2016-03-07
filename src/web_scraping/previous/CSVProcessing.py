import csv
from EUCountries import EU_countries

#print len(EU_countries)


def pruning(filename):
	data = []
	with open(filename, 'rb') as csvfile:
		csvreader = csv.reader(csvfile)
		
        header = next(csvreader)
        tmpList = []
        tmpList.append(header[0])
        tmpList.append(header[1])
        tmpList.append(header[-2])
        data.append(tmpList)

        for row in csvreader:
	        tmp = []
	        if("Euro" in row[1] or row[2] == "Males" or row[2] == "Females"):
	        	continue
	        else:
	        	if("Germany" in row[1]):
	        		row[1] = "Germany"
	        	tmp.append(row[0])
	        	tmp.append(row[1])
	        	tmp.append(row[-2])
	        	data.append(tmp)
	        return data

    

def writeToCSV(data, filename):
	with open(filename, 'w') as csvfile:
		csvwriter = csv.writer(csvfile, delimiter=',')
		csvwriter.writerows(data)

data = pruning('early_leaver.csv')
#newData = data.insert(0, "Arsenal")

print data
#writeToCSV(data, 'early_leaver_truncated.csv')

