#!/bin/env python
import uuid
import csv
import xml.etree.cElementTree as ET

def createCsv(fileName, fieldNames):
	csvfile = open(fileName,'wb')
	wrtr = csv.DictWriter(csvfile, fieldnames=fieldNames)
	return {'Csvfile': csvfile, 'Wrtr': wrtr}

def writePlaces(root):
 	for place in root.iter('Place'):
		identity = place.find('Identity')
		timeStamp = identity.find('TimeStamp').text
		placeId = identity.find('PlaceId').text
		locationId = writeLocation(place.find('LocationList/Location'))
		contactListId = writeContactList(place.find('ContactList'))
		nameId = writeName(place.find('./NameList/Name/TextList/Text/BaseText'))
		categoryListId = writeCategoryList(place.find('CategoryList'))
		placesFile['Wrtr'].writerow({'TimeStamp': timeStamp,'PlaceId': placeId,'LocationId':locationId,
										'NameId': nameId,
										'ContactListId': contactListId,
										'CategoryListId':categoryListId})
def writeCategoryList(categoryList):
	categoryListId = uuid.uuid1()
	for category in categoryList.iter('Category'):
		catListId = writeCategory(category,categoryListId)
	categoryListFile['Wrtr'].writerow({'CategoryListId':categoryListId})
	return categoryListId

def writeContactList(contactList):
	contactListId = uuid.uuid1()
	for contact in contactList.iter('Contact'):
		contacts = writeContact(contact,contactListId)
	contactListFile['Wrtr'].writerow({'ContactListId':contactListId})
	return contactListId

def writeContact(contact,contactListId):
	contactId = uuid.uuid1()
	conType = contact.get('type')
	conString = contact.find('ContactString')
	if conString != None:
		conString = conString.text
	contactFile['Wrtr'].writerow({'ContactId': contactId, 'ContactType':conType, 'ContactString':conString,
									'ContactListId':contactListId})

def writeCategory(category,categoryListId):
	catListId = uuid.uuid1()
	catSys = category.get('categorySystem')
	catId = category.find('CategoryId')
	if catId != None:
		catId = catId.text
	catName = category.find('./CategoryName/Text')
	if catName != None:
		catName = catName.text
	categoryFile['Wrtr'].writerow({'CategoryId':catListId,'CategorySystem':catSys,'Category':catId,
									'CategoryName':catName,'CategoryListId':categoryListId})

def writeStreetName(streetName):
	streetId = uuid.uuid1()
	basName = streetName.find('BaseName').text
	strType = streetName.find('StreetType')
	if strType != None:
		strType = strType.text
	streetNameFile['Wrtr'].writerow({'StreetId':streetId, 'BaseName':basName, 'StreetType':strType})
	return streetId

def writeCountryCode(countryCode):
	countryCodeId = uuid.uuid1()
	couCode = countryCode.find('CountryCode').text
	levels = countryCode.find('./Admin/AdminLevel')
	level1 = levels.find('Level1')
	if level1 != None:
		level1 = level1.text
	level2 = levels.find('Level2')
	if level2 != None:
		level2 = level2.text
	level3 = levels.find('Level3')
	if level3 != None:
		level3 = level3.text
	level4 = levels.find('Level4')
	if level4 != None:
		level4 = level4.text
	countryCodeFile['Wrtr'].writerow({'CountryCodeId':countryCodeId,'CountryCode':couCode,'AdminLevel1':level1,'AdminLevel2':level2,'AdminLevel3':level3,'AdminLevel4':level4})
	return countryCodeId

def writeAdminName(adminName):
	adminNameId = uuid.uuid1()
	lev1 = adminName.find('Level1')
	if lev1 != None:
		lev1 = lev1.text
	lev2 = adminName.find('Level2')
	if lev2 != None:
		lev2 = lev2.text
	lev3 = adminName.find('Level3')
	if lev3 != None:
		lev3 = lev3.text
	lev4 = adminName.find('Level4')
	if lev4 != None:
		lev4 = lev4.text
	adminNameFile['Wrtr'].writerow({'AdminNameId':adminNameId, 'NameLevel1':lev1, 'NameLevel2':lev2, 'NameLevel3':lev3, 'NameLevel4':lev4})
	return adminNameId

def writeGeoPosition(geoPosition):
	geoPositionId = uuid.uuid1()
	lat = geoPosition.find('Latitude').text
	lon = geoPosition.find('Longitude').text
	alt = geoPosition.find('Altitude')
	if alt != None:
		alt = alt.text
	geoPositionFile['Wrtr'].writerow({'GeoPositionId':geoPositionId, 'Latitude':lat, 'Longitude':lon,'Altitude':alt})
	return geoPositionId

def writeName(nameList):
	nameId = uuid.uuid1()
	namType = nameList.get('type')
	basText = nameList.text
	namesFile['Wrtr'].writerow({'NameId': nameId, 'NameType': namType, 'BaseText': basText})
	return nameId

def writeLocation(location):
	locationId = location.get('locationId')
	addressId = writeAddress(location.find('./Address/Parsed'))
	geoPositionId = writeGeoPosition(location.find('./GeoPositionList/GeoPosition'))
	locationFile['Wrtr'].writerow({'LocationId':locationId,'AddressId':addressId,'GeoPositionId':geoPositionId})
	return locationId

def writeAddress(address):
	addressId = uuid.uuid1()
	houNumber = address.find('HouseNumber')
	if houNumber != None:
		houNumber = houNumber.text
	posCode = address.find('PostalCode')
	if posCode != None:
		posCode = posCode.text
	streetId = writeStreetName(address.find('./StreetName'))
	countryCodeId = writeCountryCode(address)
	adminNameId = writeAdminName(address.find('./Admin/AdminName'))
	addressFile['Wrtr'].writerow({'AddressId':addressId,'StreetId':streetId,'HouseNumber':houNumber,
									'CountryCodeId':countryCodeId,'AdminNameId':adminNameId,'PostalCode':posCode})
	return addressId

def getStatistics(root):
	placeQuantity=0
	for place in root.iter('Place'):
		placeQuantity+=1
	dictCategoryId = countCategoryId(root)
	dictText = countText(root)
	statisticsFile['Wrtr'].writerow({'PlaceQuantity':placeQuantity,'CategoryIdQuantity':dictCategoryId,'TextQuantity':dictText})

def countCategoryId(root):
	dictCategoryId={}
	listCategory=[]
	for categoryId in root.iter('CategoryId'):
		listCategory.append(categoryId.text)
	for elem in listCategory:
		if elem in dictCategoryId:
			dictCategoryId[elem]+=1
		else:
			dictCategoryId[elem]=1
	return dictCategoryId

def countText(root):
	dictText={}
	listText=[]
	for tag in root.iter('BaseText'):
		textAttrb = tag.get('languageCode')
		listText.append(textAttrb)
	for text in listText:
		if text in dictText:
			dictText[text]+=1
		else:
			dictText[text]=1
	return dictText


#main section create all CSV files
placesFile = createCsv('PlaceList.csv',['PlaceId','TimeStamp','LocationId','ContactListId','NameId','CategoryListId'])
locationFile = createCsv('LocationList.csv',['LocationId','AddressId','GeoPositionId'])
geoPositionFile = createCsv('GeoPositionList.csv',['GeoPositionId', 'Latitude', 'Longitude','Altitude'])
addressFile = createCsv('Address.csv',['AddressId','StreetId','HouseNumber','CountryCodeId','AdminNameId','PostalCode'])
streetNameFile = createCsv('StreetNames.csv',['StreetId', 'BaseName', 'StreetType'])
countryCodeFile = createCsv('CountryCodes.csv',['CountryCodeId', 'CountryCode', 'AdminLevel1', 'AdminLevel2', 'AdminLevel3', 'AdminLevel4'])
namesFile = createCsv('NameList.csv',['NameId', 'NameType', 'BaseText'])
contactFile = createCsv('Contact.csv',['ContactId', 'ContactType', 'ContactString','ContactListId'])
contactListFile = createCsv('ContactList.csv',['ContactListId'])
categoryFile = createCsv('Category.csv', ['CategoryId', 'CategorySystem', 'Category', 'CategoryName','CategoryListId'])
categoryListFile = createCsv('CategoryList.csv',['CategoryListId'])
adminNameFile = createCsv('AdminNameList.csv',['AdminNameId', 'NameLevel1', 'NameLevel2', 'NameLevel3', 'NameLevel4'])
statisticsFile=createCsv('Statistics.csv',['PlaceQuantity','CategoryIdQuantity','TextQuantity'])


tree = ET.parse('sample.xml')
root = tree.getroot()

writePlaces(root)
getStatistics(root)

statisticsFile['Csvfile'].close()
placesFile['Csvfile'].close()
namesFile['Csvfile'].close()
contactFile['Csvfile'].close()
categoryListFile['Csvfile'].close()
categoryFile['Csvfile'].close()
adminNameFile['Csvfile'].close()
countryCodeFile['Csvfile'].close()
streetNameFile['Csvfile'].close()
addressFile['Csvfile'].close()
geoPositionFile['Csvfile'].close()
locationFile['Csvfile'].close()

print 'done'