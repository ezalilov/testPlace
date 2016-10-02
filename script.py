import os
import csv
import fileinput
import xml.etree.cElementTree as ET

def setNumberLine(fileName):
	for line in fileinput.input(fileName, inplace=True):
		print "%d%s" % (fileinput.filelineno(), line)

XML_FILE = os.path.join('sample.xml')
tree = ET.ElementTree(file=XML_FILE)
root = tree.getroot()

csvfile = open("Address.csv", "wb")
fieldnames = ['id', 'StreeId', 'HouseNumber', 'CountryCodeId', 'AdminNameId', 'PostalCode']
wrtr = csv.DictWriter(csvfile, fieldnames=fieldnames)

for item in root.iter('Parsed'):
	houNumber = item.find('HouseNumber')
	if houNumber != None:
		houNumber = houNumber.text
	print houNumber


