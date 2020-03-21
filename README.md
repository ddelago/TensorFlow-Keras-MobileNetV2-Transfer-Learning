# TensorFlow-Keras-MobileNetV2-Transfer-Learning

## Steps
1. Create dataset of images
2. Transform the size of those images by using `1_transform_image_resolution.py`.
    - Move the program to the folder where the images are. 
    - Then run `python 1_transform_image_resolution.py -s 800 600`
3. Divide the images into two folders `test` and `train`.
    - You want to have more train images than test.
4. Use labelImg to annotate the images.
5. If you have cloned or using data that was annotated on a different machine, use `2_xml_directory_fix.py`.
    - `python 2_xml_directory_fix.py train` and `python 2_xml_directory_fix.py test` to fix the file paths in the xml files.
6. Convert the xml annotations into a single file (also create the `label_map.pbtxt` file)
    - `python 3_xml_to_csv.py -i train -o annotations/train_labels.csv -l annotations`
    - `python 3_xml_to_csv.py -i test -o annotations/test_labels.csv`
7. Combine the images and annotations into a single binary tfrecord file.
    - `python 4_generate_tfrecord.py --csv_input=annotations/train_labels.csv --output_path=annotations/train.record --img_path=train --label_map annotations/label_map.pbtxt`
    - `python 4_generate_tfrecord.py --csv_input=annotations/test_labels.csv --output_path=annotations/test.record --img_path=test --label_map annotations/label_map.pbtxt`
