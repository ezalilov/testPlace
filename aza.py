import csv
import xml.etree.cElementTree as ET

def getGeoPositions(root):
	csvfile = open("AdminNames.csv", "wb")
	fieldnames = ['id', 'NameLevel1', 'NameLevel2', 'NameLevel3', 'NameLevel4']
	wrtr = csv.DictWriter(csvfile, fieldnames=fieldnames)

	for item in root.iter('AdminName'):
		lev1 = item.find('Level1').text
		lev2 = item.find('Level2').text
		lev3 = item.find('Level3').text
		lev4 = item.find('Level4').text
		wrtr.writerow({'NameLevel1': lev1, 'NameLevel2': lev2, 'NameLevel3': lev3, 'NameLevel4': lev4})

	csvfile.close()


tree = ET.parse('sample.xml')
root = tree.getroot()