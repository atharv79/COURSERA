'''Extracting Data from XML

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. 
The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract 
the comment counts from the XML data, compute the sum of the numbers in the file.

Actual data: http://py4e-data.dr-chuck.net/comments_509117.xml (Sum ends with 99)
NOTE : Each student will have a distinct data url for the assignment - so only use your own data url for analysis.'''

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('ENTER URL : ')

uh = urllib.request.urlopen(url)
data = uh.read()

tree = ET.fromstring(data)

lst = tree.findall('comments/comment/count')

counts = tree.findall('.//count')
Sum = 0
Count = 0
for each in counts:
    Count = Count + 1
    z = int(each.text)
    Sum = Sum + z
print('Retrieving: ', url)
print('Count: ', Count)
print('Sum: ', Sum)
