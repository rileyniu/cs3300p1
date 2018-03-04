import csv
hs = open("at.txt","a")
with open('crypto-markets.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['symbol']=="BTC":
			hs.write(row['date']+","+row['close']+'\n')
hs.close()