from lxml import etree


tree = etree.parse('sample.xml')

nodes = tree.xpath('/PlaceList/Place/CategoryList/Category')
for node in nodes:
	catSys = node.get('categorySystem')
	catId = node.find('CategoryId')
	if catId != None:
		catId = catId.text
	catName = node.find('./CategoryName/Text')
	if catName != None:
		catName = catName.text
	print {'catSys':catSys,'catId':catId,'catName':catName}


