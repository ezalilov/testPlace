from lxml import etree
import csv


tree = etree.parse('sample.xml')

csvfile = open('AdminNameList.csv')
reader = csv.DictReader(csvfile, fieldnames = ['AdminNameId', 'NameLevel1', 'NameLevel2', 'NameLevel3', 'NameLevel4'])
for row in reader:
 #   print row['NameLevel1']

    nodes = tree.xpath('/PlaceList/Place/LocationList/Location/Address/Parsed/Admin/AdminName')
    for node in nodes:
        lev1 = node.find('Level1')

        if lev1 != None:
            lev1 = lev1.text
            print lev1
        lev2 = node.find('Level2')
        if lev2 != None:
            lev2 = lev2.text
        lev3 = node.find('Level3')
        if lev3 != None:
            lev3 = lev3.text
        lev4 = node.find('Level4')
        if lev4 != None:
            lev4 = lev4.text
        else:
            lev4 = ''

        if lev1 == row['NameLevel1']:# and catId == row['Category'] and catName == row['CategoryName']:
            print lev1,row['NameLevel1'],'true'#, catId, row['Category'],catName,row['CategoryName'], 'true'
            break