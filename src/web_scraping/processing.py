import csv

# used to generate "early_leaver_truncate.csv" file
def prune(filename):
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
		csvwriter = csv.writer(csvfile)
		csvwriter.writerows(data)

# used to generate "unemployment_youth_truncated.csv" file
def truncate(filename):
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
			if(row[2] == "Total" and row[4] == "From 15 to 24 years" and row[-3] == "Total"):
				if("Germany" in row[1]):
					row[1] = "Germany"
				tmp.append(row[0])
				tmp.append(row[1])
				tmp.append(row[-2])
				data.append(tmp)
	return data

def modify(filename):
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
			if("Euro" not in row[1] and row[2] == "Current prices, million euro"):
				if("Germany" in row[1]):
					row[1] = "Germany"
				tmp.append(row[0])
				tmp.append(row[1])
				tmp.append(row[-2])
				data.append(tmp)
	return data
data = truncate('../../data/unemployment_youth.csv')
#data = prune('../../data/early_leaver.csv')
#data = modify('../../data/gdp.csv')
print data
writeToCSV(data, '../../data/unemployment_youth_truncated.csv')