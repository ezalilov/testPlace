#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from lxml import etree
import csv

class TestPlaceListAndGetStatistics(unittest.TestCase):

    def setUp(self):
        self.tree = etree.parse('sample.xml')

    def tearDown(self):
        self.csvfile.close()


    def testGetStatistics(self):
        self.csvfile = open('Statistics.csv')
        reader = csv.DictReader(self.csvfile, fieldnames = ['PlaceQuantity','CategoryIdQuantity'])
        for row in reader:
            self.countPlace = row['PlaceQuantity']
            self.countCategoryId = row['CategoryIdQuantity']
            self.assertEqual (self.countPlace, '4')
            self.assertEqual(self.countCategoryId, "{'shop': 2, '600-6900-0096': 1, '100-1000-0000': 1, '600-6300-0066': 1, 'food-drink': 1, 'Restaurant': 1, '5400': 1, '9567': 2, '600-6900-0000': 1}")


    def testWriteCategory(self):
        self.csvfile = open('Category.csv')
        reader = csv.DictReader(self.csvfile, fieldnames = ['CategoryId', 'CategorySystem', 'Category', 'CategoryName'])
        nodes = self.tree.xpath('/PlaceList/Place/CategoryList/Category')
        i=0
        for row in reader:
            node = nodes[i]
            catSys = node.get('categorySystem')
            catId = node.find('CategoryId')
            if catId != None:
                catId = catId.text
            catName = node.find('./CategoryName/Text')
            if catName != None:
                catName = catName.text
            else:
                catName = ''
            self.assertTrue(catSys in row['CategorySystem'])
            self.assertTrue(catId in row['Category'])
            self.assertTrue(catName in row['CategoryName'])
            i+=1


    def testWritePlace(self):
        self.csvfile = open('PlaceList.csv')
        reader = csv.DictReader(self.csvfile, fieldnames = ['PlaceId','TimeStamp'])
        nodes = self.tree.xpath('/PlaceList/Place/Identity')
        i=0
        for row in reader:
            node = nodes[i]
            timeStamp = node.find('TimeStamp').text
            placeId = node.find('PlaceId').text
            self.assertTrue(timeStamp in row['TimeStamp'])
            self.assertTrue(placeId in row['PlaceId'])
            i+=1


    def testWriteLocation(self):
        self.csvfile = open('LocationList.csv')
        reader = csv.DictReader(self.csvfile, fieldnames = ['LocationId'])
        nodes = self.tree.xpath('/PlaceList/Place/LocationList/Location')
        i=0
        for row in reader:
            node = nodes[i]
            locationId = node.get('locationId')
            self.assertTrue(locationId in row['LocationId'])
            i+=1


    def testWriteAddress(self):
        self.csvfile = open('Address.csv')
        reader = csv.DictReader(self.csvfile, fieldnames = ['AddressId','StreetId','HouseNumber','CountryCodeId','AdminNameId','PostalCode'])
        nodes = self.tree.xpath('/PlaceList/Place/LocationList/Location/Address/Parsed')
        i=0
        for row in reader:
            node = nodes[i]
            houNumber = node.find('HouseNumber')
            if houNumber != None:
                houNumber = houNumber.text
            else:
                houNumber=''
            self.assertTrue(houNumber in row['HouseNumber'])
            i+=1


    def testWriteCountryCode(self):
        self.csvfile = open('CountryCodes.csv')
        reader = csv.DictReader(self.csvfile, fieldnames = ['CountryCodeId', 'CountryCode', 'AdminLevel1', 'AdminLevel2', 'AdminLevel3', 'AdminLevel4'])
        nodes = self.tree.xpath('/PlaceList/Place/LocationList/Location/Address/Parsed')
        i=0
        for row in reader:
            node = nodes[i]
            couCode = node.find('CountryCode').text
            levels = node.find('./Admin/AdminLevel')
            level1 = levels.find('Level1')
            if level1 != None:
                level1 = level1.text
            else:
                level1=''
            level2 = levels.find('Level2')
            if level2 != None:
                level2 = level2.text
            else:
                level2=''
            level3 = levels.find('Level3')
            if level3 != None:
                level3 = level3.text
            level4 = levels.find('Level4')
            if level4 != None:
                level4 = level4.text
            else:
                level4=''
            self.assertTrue(couCode in row['CountryCode'])
            self.assertTrue(level1 in row['AdminLevel1'])
            self.assertTrue(level2 in row['AdminLevel2'])
            self.assertTrue(level3 in row['AdminLevel3'])
            self.assertTrue(level4 in row['AdminLevel4'])
            i+=1


    def testWriteStreetName(self):
        self.csvfile = open('StreetNames.csv')
        reader = csv.DictReader(self.csvfile, fieldnames = ['StreetId', 'BaseName', 'StreetType'])
        nodes = self.tree.xpath('/PlaceList/Place/LocationList/Location/Address/Parsed/StreetName')
        i=0
        for row in reader:
            node = nodes[i]
            basName = node.find('BaseName').text
            strType = node.find('StreetType')
            if strType != None:
                strType = strType.text
            else:
                strType=''
            self.assertTrue(basName in row['BaseName'])
            self.assertTrue(strType in row['StreetType'])
            i+=1


    def testWriteContact(self):
        self.csvfile = open('Contact.csv')
        reader = csv.DictReader(self.csvfile, fieldnames = ['ContactId', 'ContactType', 'ContactString'])
        nodes = self.tree.xpath('/PlaceList/Place/ContactList/Contact')
        i=0
        for row in reader:
            node = nodes[i]
            conType = node.get('type')
            conString = node.find('ContactString')
            if conString != None:
                conString = conString.text
            self.assertTrue(conType in row['ContactType'])
            self.assertTrue(conString in row['ContactString'])
            i+=1


    def testWriteName(self):
        self.csvfile = open('NameList.csv')
        reader = csv.DictReader(self.csvfile, fieldnames = ['NameId', 'NameType', 'BaseText'])
        nodes = self.tree.xpath('/PlaceList/Place/NameList/Name/TextList/Text/BaseText')
        i = 0
        for row in reader:
            node = nodes[i]
            namType = node.get('type')
            basText = node.text
            self.assertTrue(namType in row['NameType'])
            self.assertTrue(basText in row['BaseText'])
            i+=1


    def testWriteAdminName(self):
        self.csvfile = open('AdminNameList.csv')
        reader = csv.DictReader(self.csvfile, fieldnames = ['AdminNameId', 'NameLevel1', 'NameLevel2', 'NameLevel3', 'NameLevel4'])
        nodes = self.tree.xpath('/PlaceList/Place/LocationList/Location/Address/Parsed/Admin/AdminName')
        i=0
        for row in reader:
            node = nodes[i]
            lev1 = node.find('Level1')
            if lev1 != None:
                lev1 = lev1.text
            else:
                lev1=''
            lev2 = node.find('Level2')
            if lev2 != None:
                lev2 = lev2.text
            else:
                lev2=''
            lev3 = node.find('Level3')
            if lev3 != None:
                lev3 = lev3.text
            lev4 = node.find('Level4')
            if lev4 != None:
                lev4 = lev4.text
            else:
                lev4=''
            self.assertTrue(lev1 in row['NameLevel1'])
            self.assertTrue(lev2 in row['NameLevel2'])
            self.assertTrue(lev3 in row['NameLevel3'])
            self.assertTrue(lev4 in row['NameLevel4'])
            i+=1


    def testWriteGeoPosition(self):
        self.csvfile = open('GeoPositionList.csv')
        reader = csv.DictReader(self.csvfile, fieldnames = ['GeoPositionId', 'Latitude', 'Longitude','Altitude'])
        nodes = self.tree.xpath('/PlaceList/Place/LocationList/Location/GeoPositionList/GeoPosition')
        i=0
        for row in reader:
            node = nodes[i]
            lat = node.find('Latitude').text
            lon = node.find('Longitude').text
            alt = node.find('Altitude')
            if alt != None:
                alt = alt.text
            else:
                alt = ''
            self.assertTrue(lat in row['Latitude'])
            self.assertTrue(lon in row['Longitude'])
            self.assertTrue(alt in row['Altitude'])
            i+=1



if __name__ == '__main__':
    unittest.main(verbosity=2)