from lxml import etree
import sc



#    def setUp(self):
#        self.getStatistics = sc.getStatistics(sc.root)
#        self.countCategoryId = sc.countCategoryId(sc.root)
 #       self.tree = etree.parse('sample.xml')

def testCountText():
    getStatistics = sc.getStatistics(sc.root)
    assert getStatistics==4

def testCountCategoryId():
    countCategoryId = sc.countCategoryId(sc.root)
    assert countCategoryId == {'shop': 2, '600-6900-0096': 1, '100-1000-0000': 1, '600-6300-0066': 1, 'food-drink': 1, 'Restaurant': 1, '5400': 1, '9567': 2, '600-6900-0000': 1}
'''
    def testWriteCategiry(self):
        nodes = self.tree.xpath('/PlaceList/Place/CategoryList')
        for node in nodes:
'''

