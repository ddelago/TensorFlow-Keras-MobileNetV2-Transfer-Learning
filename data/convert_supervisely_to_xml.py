import os
import xml.etree.ElementTree as ET
import json
import sys
import shutil

# Create new train and test directories
os.mkdir('annotations/train')
os.mkdir('annotations/test')
os.mkdir('images/train')
os.mkdir('images/test')

for json_file in os.listdir('annotations'):
    # Skip directories
    if not json_file.endswith('.json'):
        continue

    data = json.load(open(f'annotations/{json_file}'))
    
    # Get image filename
    filename = json_file[0:json_file.index('.jpg.json')]

    # Get the image resolution
    width = data['size']['width']
    height = data['size']['height']

    # Check if training or validation image
    data_type = 'test'
    if data['tags'][0]['name'] == 'train':
        data_type = 'train'
    
    # Move image to the correct directory
    shutil.move(f'images/{filename}.jpg', f'images/{data_type}/{filename}.jpg')

    # Get the bounding boxes
    objects = []
    for box in data['objects']:
        # Get classname
        classname = data['objects'][0]['classTitle']

        # Get bounding box
        bbox = data['objects'][0]['points']['exterior']
        bbox_min = bbox[0]
        bbox_max = bbox[1]

        objects.append([bbox_min[0], bbox_min[1], bbox_max[0], bbox_max[1], classname])

    # Now remove file
    os.remove(f'annotations/{json_file}')

    """ Now create the xml file """
    tree = ET.ElementTree()
    data = ET.Element('annotation')
    ET.SubElement(data, 'folder').text = f'data/images/{data_type}'
    ET.SubElement(data, 'filename').text = f'{filename}.jpg'
    ET.SubElement(data, 'path').text = f'{os.getcwd()}\\images\\{data_type}\\{filename}.jpg'

    xml_source = ET.SubElement(data, 'source')
    ET.SubElement(xml_source, 'database').text = 'Unknown'
    
    xml_size = ET.SubElement(data, 'size')
    ET.SubElement(xml_size, 'width').text = str(width)
    ET.SubElement(xml_size, 'height').text = str(height)
    ET.SubElement(xml_size, 'depth').text = '3'

    ET.SubElement(data, 'segmented').text = '0'

    for box in objects:
        xml_object = ET.SubElement(data, 'object')
        ET.SubElement(xml_object, 'name').text = box[4]
        ET.SubElement(xml_object, 'pose').text = 'Unspecified'
        ET.SubElement(xml_object, 'truncated').text = '0'
        ET.SubElement(xml_object, 'difficult').text = '0'

        xml_bndbox = ET.SubElement(xml_object, 'bndbox')
        ET.SubElement(xml_bndbox, 'xmin').text = str(box[0])
        ET.SubElement(xml_bndbox, 'ymin').text = str(box[1])
        ET.SubElement(xml_bndbox, 'xmax').text = str(box[2])
        ET.SubElement(xml_bndbox, 'ymax').text = str(box[3])

    tree._setroot(data)
    tree.write(f'annotations/{data_type}/{filename}.xml')
