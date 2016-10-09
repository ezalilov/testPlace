#!/bin/env python2.7.11
import uuid
import csv
import xml.etree.cElementTree as ET

class Files:
    """docstring for PlaceList"""
    def __init__(self,fileName, fieldNames):
#        self.name = name
        wrtr = self.createCsv(fileName, fieldNames)
        print wrtr
#        self.closeFile()

    def createCsv(self, fileName, fieldNames):
        csvfile = open(fileName,'wb')
        wrtr = csv.DictWriter(csvfile, fieldnames=fieldNames)
        return wrtr

    def getStatistics(self,root):
        placeQuantity=0
        for place in root.iter('Place'):
            placeQuantity+=1
#        dictCategoryId = countCategoryId(root)
#        dictText = countText(root)
        self.wrtr.writerow({'PlaceQuantity':placeQuantity})

    def countCategoryId(self, root):
        dictCategoryId={}
        listCategory=[]
        for categoryId in root.iter('CategoryId'):
            listCategory.append(categoryId.text)
        for elem in listCategory:
            if elem in dictCategoryId:
                dictCategoryId[elem]+=1
            else:
                dictCategoryId[elem]=1
        return self.dictCategoryId

    def countText(self, root):
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
        return self.dictText


#main section
tree = ET.parse('sample.xml')
root = tree.getroot()

statisticsFile = Files('Statistics.csv',['PlaceQuantity','CategoryIdQuantity','TextQuantity'])
statisticsFile.getStatistics(root)