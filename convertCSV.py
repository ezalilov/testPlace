import csv
import sys
import xml.etree.ElementTree as etree

f = open('CategoryList.csv', 'r').read()
f = f.replace('\n,,,\n,,,', '')
f = f.replace(',,,\n', '')

x = open('CategoryList.csv', 'w')
x.write(f)
x.close()
