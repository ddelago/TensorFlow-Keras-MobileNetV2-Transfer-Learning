import os
import xml.etree.ElementTree as ET

xml_file = 'IMG_6988.xml'
tree = ET.parse(xml_file)
root = tree.getroot()

# C:\Users\Francis\Desktop\test_pic\IMG_6988.JPG
root[2].text = 'abc'
print(root[2].text)

tree.write('out.xml')