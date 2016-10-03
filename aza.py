import uuid
import csv
import xml.etree.cElementTree as ET

def openPlaceCsvForWrite(fileName):
	csvfile = open(fileName,'wb')
	fieldNames = ['TimeStamp', 'PlaceId', 'LocationId', 'ContactId', 'NameId', 'CategoryListId']
	wrtr = csv.DictWriter(csvfile, fieldnames=fieldNames)
	writePlace(root,wrtr)
	csvfile.close()

def writePlace(root,wrtr):
 	for item in root.iter('Place'):
		for identity in item.iter('Identity'):
			timeStamp = identity.find('TimeStamp').text
			placeId = identity.find('PlaceId').text
#			print timeStamp, placeId
			print  'in writePlace'
			nameId = openNamesCsvForWrite('Names.csv')
			wrtr.writerow({'TimeStamp': timeStamp, 'PlaceId': placeId, 'NameId': nameId})

def openNamesCsvForWrite(fileName):
	csvfile = open(fileName, "wb")
	fieldNames = ['NameId', 'NameType', 'BaseText']
	wrtr = csv.DictWriter(csvfile, fieldnames=fieldNames)
	print 'in openNamesCsvForWrite'
	return writeNames(root,wrtr)
	csvfile.close()

def writeNames(root,wrtr):
	for item in root.iter('BaseText'):
		nameId = uuid.uuid1()
		namType = item.get('type')
		basText = item.text
#		print basName, strType
		wrtr.writerow({'NameId': nameId, 'NameType': namType, 'BaseText': basText})
		print nameId, 'in writeNames'
		return nameId

tree = ET.parse('sample.xml')
root = tree.getroot()

openPlaceCsvForWrite('Place.csv')
#writePlace(root,wrtr)