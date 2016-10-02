import os
import csv
import xml.etree.cElementTree as ET

XML_FILE = os.path.join('sample.xml')
tree = ET.ElementTree(file=XML_FILE)
root = tree.getroot()

csvfile = open("AdminNames.csv", "wb")
fieldnames = ['id', 'NameLevel1', 'NameLevel2', 'NameLevel3', 'NameLevel4']
wrtr = csv.DictWriter(csvfile, fieldnames=fieldnames)

for item in root.iter('AdminName'):
	lev1 = item.find('Level1')
	if lev1 != None:
		lev1 = lev1.text

	lev2 = item.find('Level2')
	if lev2 != None:
		lev2 = lev2.text

	lev3 = item.find('Level3')
	if lev3 != None:
		lev3 = lev3.text

	lev4 = item.find('Level4')
	if lev4 != None:
		lev4 = lev4.text


	print lev1,'\n', lev2,'\n',lev3,'\n',lev4
	wrtr.writerow({'NameLevel1': lev1, 'NameLevel2': lev2, 'NameLevel3': lev3, 'NameLevel4': lev4})

csvfile.close()

#	print '%s' % item.attrib
#for Longitude in root.iter('Longitude'):
#	lon = Longitude.text
#	print lon

#for child_of_root, lon in root.iter():
#	if child_of_root.tag == "Latitude" and lon.tag == "Longitube":
#		print '%s,%s' % (child_of_root.text, lon.text)
#		wrtr.writerow({'Latitube': child_of_root.text, 'Longitube': lon.text})

