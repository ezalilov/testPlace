import unittest
from lxml import etree
import sc
import csv

class TestPlaceListAndGetStatistics(unittest.TestCase):

    def setUp(self):
#        self.getStatistics = sc.getStatistics(sc.root)
#        self.countCategoryId = sc.countCategoryId(sc.root)
        self.root = sc.parseFile('sample.xml')
        self.tree = etree.parse('sample.xml')

    def testCountText(self):
        self.getStatistics = sc.getStatistics(self.root)
        self.assertEqual(self.getStatistics, 4)

    def testCountCategoryId(self):
        self.countCategoryId = sc.countCategoryId(self.root)
        self.assertDictContainsSubset(self.countCategoryId, {'shop': 2, '600-6900-0096': 1, '100-1000-0000': 1, '600-6300-0066': 1, 'food-drink': 1, 'Restaurant': 1, '5400': 1, '9567': 2, '600-6900-0000': 1})

    def testWriteCategory(self):
        csvfile = open('Category.csv')
        reader = csv.DictReader(csvfile, fieldnames = ['CategoryId', 'CategorySystem', 'Category', 'CategoryName'])
        for row in reader:
            nodes = self.tree.xpath('/PlaceList/Place/CategoryList')
            for node in nodes:
                catSys = node.get('categorySystem')
                catId = node.find('CategoryId')
                if catId != None:
                    catId = catId.text
                else:
                    catId = ''
                catName = node.find('./CategoryName/Text')
                if catName != None:
                    catName = catName.text
                else:
                    catName = ''
                self.assertTrue(catSys in row['CategorySystem'])
                self.assertTrue(catId in row['Category'])
                self.assertTrue(catName in row['CategoryName'])

    def testWritePlace(self):
        csvfile = open('PlaceList.csv')
        reader = csv.DictReader(csvfile, fieldnames = ['PlaceId','TimeStamp'])
        for row in reader:
            nodes = self.tree.xpath('/PlaceList/Place/Identity')
            for node in nodes:
                timeStamp = node.find('TimeStamp').text
                placeId = node.find('PlaceId').text
                self.assertTrue(timeStamp in row['TimeStamp'])
                self.assertTrue(placeId in row['PlaceId'])

    def testWriteLocation(self):
        csvfile = open('Adress.csv')
        reader = csv.DictReader(csvfile, fieldnames = ['LocationId'])
        for row in reader:
            nodes = self.tree.xpath('/PlaceList/Place/LocationList')
            for node in nodes:
                locationId = node.get('locationId')
                self.assertTrue(locationId in row['LocationId'])

    def testWriteAddress(self):
        csvfile = open('Adress.csv')
        reader = csv.DictReader(csvfile, fieldnames = ['AddressId','StreetId','HouseNumber','CountryCodeId','AdminNameId','PostalCode'])
        for row in reader:
            nodes = self.tree.xpath('/PlaceList/Place/LocationList/Location/Address/Parsed')
            for node in nodes:
                houNumber = node.find('HouseNumber')
                if houNumber != None:
                    houNumber = houNumber.text
                posCode = node.find('PostalCode')
                if posCode != None:
                    posCode = posCode.text
                self.assertTrue(houNumber in row['HouseNumber'])
                self.assertTrue(posCode in row['PostalCode'])

    def testWriteCountryCode(self):
        csvfile = open('CountryCodes.csv')
        reader = csv.DictReader(csvfile, fieldnames = ['CountryCodeId', 'CountryCode', 'AdminLevel1', 'AdminLevel2', 'AdminLevel3', 'AdminLevel4'])
        for row in reader:
            nodes = self.tree.xpath('/PlaceList/Place/LocationList/Location/Address/Parsed')
            for node in nodes:
                couCode = node.find('CountryCode').text
                levels = node.find('./Admin/AdminLevel')
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
                self.assertTrue(couCode in row['CountryCode'])
                self.assertTrue(level1 in row['AdminLevel1'])
                self.assertTrue(level2 in row['AdminLevel2'])
                self.assertTrue(level3 in row['AdminLevel3'])
                self.assertTrue(level4 in row['AdminLevel4'])

    def testWriteStreetName(self):
        csvfile = open('StreetNames.csv')
        reader = csv.DictReader(csvfile, fieldnames = ['StreetId', 'BaseName', 'StreetType'])
        for row in reader:
            nodes = self.tree.xpath('/PlaceList/Place/LocationList/Location/Address/Parsed/StreetName')
            for node in nodes:
                basName = node.find('BaseName').text
                strType = node.find('StreetType')
                if strType != None:
                    strType = strType.text
                self.assertTrue(basName in row['BaseName'])
                self.assertTrue(strType in row['StreetType'])

    def testWriteContact(self):
        csvfile = open('Contact.csv')
        reader = csv.DictReader(csvfile, fieldnames = ['ContactId', 'ContactType', 'ContactString'])
        for row in reader:
            nodes = self.tree.xpath('/PlaceList/Place/ContactList')
            for node in nodes:
                conType = node.get('type')
                conString = node.find('ContactString')
                if conString != None:
                    conString = conString.text
                self.assertTrue(conType in row['ContactType'])
                self.assertTrue(conString in row['ContactString'])

    def testWriteName(self):
        csvfile = open('NameList.csv')
        reader = csv.DictReader(csvfile, fieldnames = ['NameId', 'NameType', 'BaseText'])
        for row in reader:
            nodes = self.tree.xpath('/PlaceList/Place/NameList/Name/TextList/Text/BaseText')
            for node in nodes:
                namType = node.get('type')
                basText = node.text
                self.assertTrue(namType in row['NameType'])
                self.assertTrue(basText in row['BaseText'])

    def testWriteAdminName(self):
        csvfile = open('AdminNameList.csv')
        reader = csv.DictReader(csvfile, fieldnames = ['AdminNameId', 'NameLevel1', 'NameLevel2', 'NameLevel3', 'NameLevel4'])
        for row in reader:
            nodes = self.tree.xpath('/PlaceList/Place/LocationList/Location/Address/Parsed/Admin/AdminName')
            for node in nodes:
                lev1 = node.find('Level1')
                if lev1 != None:
                    lev1 = lev1.text
                lev2 = node.find('Level2')
                if lev2 != None:
                    lev2 = lev2.text
                lev3 = node.find('Level3')
                if lev3 != None:
                    lev3 = lev3.text
                lev4 = node.find('Level4')
                if lev4 != None:
                    lev4 = lev4.text
                self.assertTrue(lev1 in row['NameLevel1'])
                self.assertTrue(lev2 in row['NameLevel2'])
                self.assertTrue(lev3 in row['NameLevel3'])
                self.assertTrue(lev4 in row['NameLevel4'])

    def testWriteGeoPosition(self):
        csvfile = open('GeoPositionList.csv')
        reader = csv.DictReader(csvfile, fieldnames = ['GeoPositionId', 'Latitude', 'Longitude','Altitude'])
        for row in reader:
            nodes = self.tree.xpath('/PlaceList/Place/GeoPositionList/GeoPosition')
            for node in nodes:
                lat = node.find('Latitude').text
                lon = node.find('Longitude').text
                alt = node.find('Altitude')
                if alt != None:
                    alt = alt.text
                self.assertTrue(lat in row['Latitude'])
                self.assertTrue(lon in row['Longitude'])
                self.assertTrue(alt in row['Altitude'])


if __name__ == '__main__':
    unittest.main(verbosity=2)