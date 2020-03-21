#python transform_image_resolution.py -s 800 600
from PIL import Image
import os
import argparse

def rescale_images(size):
    # Get current directory
    cur_path = os.getcwd() + '\\\\'

    # Loop over images in folder
    for img in os.listdir():
        if img.endswith('.jpg') or img.endswith('.JPG'):
            im = Image.open(cur_path + img)
            im_resized = im.resize(size, Image.ANTIALIAS)
            im_resized.save(cur_path + img)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Rescale images")
    parser.add_argument('-s', '--size', type=int, nargs=2, required=True, metavar=('width', 'height'), help='Image size')
    args = parser.parse_args()
    rescale_images(args.size)