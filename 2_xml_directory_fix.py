import os
import xml.etree.ElementTree as ET
import sys

if len(sys.argv) < 2:
    print('Specify folder where xml files are.')
os.chdir(sys.argv[1])

for xml_file in os.listdir():
    # Skip images and programs
    if xml_file.endswith('.jpg') or xml_file.endswith('.JPG') or xml_file.endswith('.py'):
        continue

    # Parse xml
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Get filename and new path
    filename = root[1].text
    cur_path = os.getcwd()
    cur_path = cur_path.replace('\\\\', '\\')
    cur_dir = cur_path.split('\\')[-1]

    # Update paths
    root[0].text = cur_dir
    root[2].text = f'{cur_path}\{filename}'
    tree.write(xml_file)