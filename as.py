import os
import csv
import xml.etree.cElementTree as ET

XML_FILE = os.path.join('sample.xml')
tree = ET.ElementTree(file=XML_FILE)
root = tree.getroot()

csvfile = open("CountryCodes.csv", "wb")
fieldnames = ['id', 'CountryCode', 'AdminLevel1', 'AdminLevel2', 'AdminLevel3', 'AdminLevel4']
wrtr = csv.DictWriter(csvfile, fieldnames=fieldnames)

#for item in root.iter('Place'):
for pars in root.iter('Parsed'):
	couCode = pars.find('CountryCode').text

	print couCode, i
	for admins in pars.iter('AdminLevel'):
		level1 = admins.find('Level1')
		if level1 != None:
			level1 = level1.text
		print level1

		level2 = admins.find('Level2')
		if level2 != None:
			level2 = level2.text
		print level2

		level3 = admins.find('Level3')
		if level3 != None:
			level3 = level3.text
		print level3

		level4 = admins.find('Level4')
		if level4 != None:
			level4 = level4.text
		print level4

		wrtr.writerow({'CountryCode': couCode, 'AdminLevel1': level1, 'AdminLevel2': level2, 'AdminLevel3': level3, 'AdminLevel4': level4})

csvfile.close()

'''		for admins in pars.iter('Admin'):
			print admins

			for admLev in admins.iter('AdminLevel'):
				level1 = admLev.find('Level1')
				if level1 != None:
					level1 = level1.text
				print level1

				level2 = admLev.find('Level2')
				if level2 != None:
					level2 = level2.text
				print level2'''

'''	couCode = item.find('CountryCode')
	if couCode != None:
		couCode = couCode.text
	print couCode
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
'''
#	strType = item.find('StreetType')
#	if strType != None:
#		strType = strType.text
#	print couCode, lev1, lev2, lev3,lev4
'''	wrtr.writerow({'CountryCode': couCode})

for item in root.iter('AdminLevel'):
	lev1 = item.find('Level1')
	if lev1 != None:
		lev1 = lev1.text
	print lev1
	wrtr.writerow({'AdminLevel1': lev1})
csvfile.close()

f = open('CountryCodes.csv', 'r').read()
print f
f = f.replace(',,\n', '')
x = open('ContactList.csv', 'w')
x.write(f)
x.close()'''
