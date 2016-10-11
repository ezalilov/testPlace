from lxml import etree
import csv

def timer(reps, func, *args):
    import time
    start = time.clock()
    for i in range(reps):
        apply(func, args)
    return time.clock() - start

tree = etree.parse('sample.xml')

csvfile = open('Category.csv')
reader = csv.DictReader(csvfile, fieldnames = ['CategoryId', 'CategorySystem', 'Category', 'CategoryName'])
for row in reader:
#	print row['Category']
	nodes = tree.xpath('/PlaceList/Place/CategoryList/Category')
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

		if catSys == row['CategorySystem'] and catId == row['Category'] and catName == row['CategoryName']:
			print catSys,row['CategorySystem'], catId, row['Category'],catName,row['CategoryName'], 'true'
			break
#		else:
#			print 'false'
#			break

	#	print catSys,catId,catName
	#	self.assertTrue(catSys in node.get('categorySystem'))
#		print {'catSys':catSys,'catId':catId,'catName':catName}

#with open('Category.csv') as csvfile:
#	reader = csv.DictReader(csvfile, fieldnames = ['CategoryId', 'CategorySystem', 'Category', 'CategoryName'])
#	for row in reader:
#		print row['CategorySystem'], row['Category'], row['CategoryName']
