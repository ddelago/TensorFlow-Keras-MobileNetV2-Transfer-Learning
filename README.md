# TensorFlow-Keras-MobileNetV2-Transfer-Learning
Followed this tutorial https://mc.ai/training-your-object-detection-model-on-tensorflow-part-2/. Using TensorFlow version 1.15.0

## Steps
1. Create dataset of images
2. Transform the size of those images by using `1_transform_image_resolution.py`.
    - Move the program to the folder where the images are. 
    - Then run `python 1_transform_image_resolution.py -s 800 600`
3. Divide the images into two folders `test` and `train`.
    - You want to have more train images than test.
4. Use labelImg to annotate the images. Or you can use Supervisely.
    - Have the annotations and the images in the correct train/test directory. Filepaths do not matter in the annotations file, only the image filenames. 
    - If used Supervisely, combine all annotations and images in the respective folders, then run the `convert_supervisely_to_xml.py` program to move them into train/test folders.
5. If you have cloned or using data that was annotated on a different machine, use `2_xml_directory_fix.py`.
    - `python 2_xml_directory_fix.py data/annotations/train` and `python 2_xml_directory_fix.py data/annotations/test` to fix the file paths in the xml files.
6. Convert the xml annotations into a single file (also create the `label_map.pbtxt` file)
    - `python 3_xml_to_csv.py -i data/annotations/train -o data/annotations/train_labels.csv -l data/annotations`
    - `python 3_xml_to_csv.py -i data/annotations/test -o data/annotations/test_labels.csv`
7. Combine the images and annotations into a single binary tfrecord file.
    - `python 4_generate_tfrecord.py --csv_input=data/annotations/train_labels.csv --output_path=data/train.record --img_path=data/images/train --label_map data/label_map.pbtxt`
    - `python 4_generate_tfrecord.py --csv_input=data/annotations/test_labels.csv --output_path=data/test.record --img_path=data/images/test --label_map data/label_map.pbtxt`
8. Download a model from the TensorFlow Model Zoo such as MobileNetV2 SSD. 
9. Get the config for the model from the `object_detection/samples/config/` directory.
10. A few lines need to be changed in the config file before you can begin training. 
    - Line 9: Change the number of classes to the number of classes in your dataset.
    ```
    num_classes: 1
    ```
    - line 156: Update fine_tune_checkpoint to the path of model.ckpt in the downloaded model directory.
    ```
    fine_tune_checkpoint: "C:/Users/ddela/Desktop/Projects/Machine-Learning/TensorFlow-Keras-MobileNetV2-Transfer-Learning/ssd_mobilenet_v2_coco_2018_03_29/model.ckpt"
    ```
    - Line 175: Update the path of the train.record file.
    ```
    input_path: "C:/Users/ddela/Desktop/Projects/Machine-Learning/TensorFlow-Keras-MobileNetV2-Transfer-Learning/data/train*.record"
    ```
    - Line 177 and 191: Update the path to the path of labelmap.pbtxt
    ```
    label_map_path: "C:/Users/ddela/Desktop/Projects/Machine-Learning/TensorFlow-Keras-MobileNetV2-Transfer-Learning/data/label_map.pbtxt"
    ```
    - Line 189: Update the path of the test.record file.
    ```
    input_path: "C:/Users/ddela/Desktop/Projects/Machine-Learning/TensorFlow-Keras-MobileNetV2-Transfer-Learning/data/test*.record"
    ```
    - Line 181: Update the number of examples to the number of images in your test directory.
    ```
    num_examples: 15
    ```
    - Line 141 and 162: Edit batch_size and num_steps to increase the performance of your training.
11. Train the model with the updated parameters of your model in the file.
    - `python 5_train_model.py`
    - You may have to run this multiples times to completely finish training.
    - You can use tensorboard to see how well training went.
    - `tensorboard --logdir=.`
12. Create an inference graph to use for training.
    - `python 6_export_graph.py`
