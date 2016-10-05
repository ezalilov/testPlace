import csv
import fileinput
import xml.etree.cElementTree as ET

def setNumberLine(fileName):
	for line in fileinput.input(fileName, inplace=True):
		print "%d%s" % (fileinput.filelineno(), line)

def getGeoPositions(root):
	csvfile = open("GeoPositions.csv", "wb")
	fieldnames = ['id', 'Latitude', 'Longitude','Altitude']
	wrtr = csv.DictWriter(csvfile, fieldnames=fieldnames)

	for item in root.iter('GeoPosition'):

		lat = item.find('Latitude').text
		lon = item.find('Longitude').text
		alt = item.find('Altitude')
		if alt != None:
			alt = alt.text

		wrtr.writerow({'Latitude': lat, 'Longitude': lon, 'Altitude': alt})

	csvfile.close()
	setNumberLine('GeoPositions.csv')

def getAdminNames(roto):
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

		wrtr.writerow({'NameLevel1': lev1, 'NameLevel2': lev2, 'NameLevel3': lev3, 'NameLevel4': lev4})

	csvfile.close()
	setNumberLine('AdminNames.csv')

def getCategoryList(root):
	csvfile = open("CategoryList.csv", "wb")
	fieldnames = ['id', 'CategorySystem', 'CategoryId', 'CategoryName']
	wrtr = csv.DictWriter(csvfile, fieldnames=fieldnames)

	for item in root.iter('Category'):
		print item.tag
		catSys = item.get('categorySystem')
		print catSys,'after'

		catId = item.find('CategoryId')
		if catId != None:
			catId = catId.text

		catName = item.find('Text')
		if catName != None:
			catName = catName.text
			
		wrtr.writerow({'CategorySystem': catSys, 'CategoryId': catId, 'CategoryName': catName})

	csvfile.close()

	f = open('CategoryList.csv', 'r').read()
	f = f.replace('\n,,,\n,,,', '')
	f = f.replace(',,,\n', '')
	x = open('CategoryList.csv', 'w')
	x.write(f)
	x.close()
	setNumberLine('CategoryList.csv')

def getContactList(root):

	csvfile = open("ContactList.csv", "wb")
	fieldnames = ['id', 'ContactType', 'ContactString']
	wrtr = csv.DictWriter(csvfile, fieldnames=fieldnames)

	for item in root.iterfind('./Place/ContactList//'):
		conType = item.get('type')

		conString = item.find('ContactString')
		if conString != None:
			conString = conString.text

		wrtr.writerow({'ContactType': conType, 'ContactString': conString})

	csvfile.close()

	f = open('ContactList.csv', 'r').read()
	f = f.replace(',,\n', '')
	x = open('ContactList.csv', 'w')
	x.write(f)
	x.close()
	setNumberLine('ContactList.csv')

def getNameList(root):
	csvfile = open("NameList.csv", "wb")
	fieldnames = ['id', 'NameType', 'BaseText']
	wrtr = csv.DictWriter(csvfile, fieldnames=fieldnames)

	for item in root.iter('BaseText'):
		namType = item.get('type')
		basText = item.text

		wrtr.writerow({'NameType': namType, 'BaseText': basText})

	csvfile.close()
	setNumberLine('NameList.csv')

def getStreetName(root):
	csvfile = open("StreetName.csv", "wb")
	fieldnames = ['id', 'BaseName', 'StreetType']
	wrtr = csv.DictWriter(csvfile, fieldnames=fieldnames)

	for item in root.iter('StreetName'):
		basName = item.find('BaseName').text

		strType = item.find('StreetType')
		if strType != None:
			strType = strType.text

		wrtr.writerow({'BaseName': basName, 'StreetType': strType})

	csvfile.close()
	setNumberLine('StreetName.csv')

def getCountryCodes(root):
	csvfile = open("CountryCodes.csv", "wb")
	fieldnames = ['id', 'CountryCode', 'AdminLevel1', 'AdminLevel2', 'AdminLevel3', 'AdminLevel4']
	wrtr = csv.DictWriter(csvfile, fieldnames=fieldnames)

	for pars in root.iter('Parsed'):
		couCode = pars.find('CountryCode').text

		for admins in pars.iter('AdminLevel'):
			level1 = admins.find('Level1')
			if level1 != None:
				level1 = level1.text

			level2 = admins.find('Level2')
			if level2 != None:
				level2 = level2.text

			level3 = admins.find('Level3')
			if level3 != None:
				level3 = level3.text

			level4 = admins.find('Level4')
			if level4 != None:
				level4 = level4.text

			wrtr.writerow({'CountryCode': couCode, 'AdminLevel1': level1, 'AdminLevel2': level2, 'AdminLevel3': level3, 'AdminLevel4': level4})

	csvfile.close()
	setNumberLine('CountryCodes.csv')


tree = ET.parse('sample.xml')
root = tree.getroot()

#getGeoPositions(root)
#getAdminNames(root)
getCategoryList(root)
#getNameList(root)
#getStreetName(root)
#getCountryCodes(root)