from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

from keras.applications.resnet50 import ResNet50
from keras.applications.vgg16 import VGG16
from keras.applications.vgg19 import VGG19
from keras.applications.inception_v3 import InceptionV3
from keras.applications.xception import Xception
from keras.applications.inception_resnet_v2 import InceptionResNetV2
from keras.applications.mobilenet import MobileNet
from keras.applications.mobilenet_v2 import MobileNetV2
from keras.applications.densenet import DenseNet121, DenseNet169, DenseNet201
from keras.applications.nasnet import NASNetLarge, NASNetMobile
from keras.preprocessing.image import ImageDataGenerator

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, default="VGG16", help='Your pre-trained classification model of choice')
args = parser.parse_args()

image = None
# Prepare the model
if args.model == "VGG16":
    from keras.applications.vgg16 import preprocess_input
    from keras.applications.vgg16 import decode_predictions
    preprocessing_function = preprocess_input
    base_model = VGG16()
    image = load_img('soccer.jpeg', target_size=(224, 224))
elif args.model == "VGG19":
    from keras.applications.vgg19 import preprocess_input
    from keras.applications.vgg19 import decode_predictions
    preprocessing_function = preprocess_input
    base_model = VGG19()
    image = load_img('soccer.jpeg', target_size=(224, 224))
elif args.model == "ResNet50":
    from keras.applications.resnet50 import preprocess_input
    from keras.applications.resnet50 import decode_predictions
    preprocessing_function = preprocess_input
    base_model = ResNet50()
    image = load_img('airplane.jpeg', target_size=(224, 224))
elif args.model == "InceptionV3":
    from keras.applications.inception_v3 import preprocess_input
    from keras.applications.inception_v3 import decode_predictions
    preprocessing_function = preprocess_input
    base_model = InceptionV3()
    image = load_img('soccer.jpeg', target_size=(299, 299))
elif args.model == "Xception":
    from keras.applications.xception import preprocess_input
    from keras.applications.xception import decode_predictions
    preprocessing_function = preprocess_input
    base_model = Xception()
    image = load_img('soccer.jpeg', target_size=(299, 299))
elif args.model == "InceptionResNetV2":
    from keras.applications.inceptionresnetv2 import preprocess_input
    from keras.applications.inceptionresnetv2 import decode_predictions
    preprocessing_function = preprocess_input
    base_model = InceptionResNetV2()
    image = load_img('soccer.jpeg', target_size=(299, 299))
elif args.model == "MobileNet":
    from keras.applications.mobilenet import preprocess_input
    from keras.applications.mobilenet import decode_predictions
    preprocessing_function = preprocess_input
    base_model = MobileNet()
    image = load_img('soccer.jpeg', target_size=(224, 224))
elif args.model == "MobileNetV2":
    from keras.applications.mobilenet_v2 import preprocess_input
    from keras.applications.mobilenet_v2 import decode_predictions
    preprocessing_function = preprocess_input
    base_model = MobileNetV2()
    image = load_img('soccer.jpeg', target_size=(224, 224))
elif args.model == "DenseNet121":
    from keras.applications.densenet import preprocess_input
    from keras.applications.densenet import decode_predictions
    preprocessing_function = preprocess_input
    base_model = DenseNet121()
    image = load_img('soccer.jpeg', target_size=(224, 224))
elif args.model == "DenseNet169":
    from keras.applications.densenet import preprocess_input
    from keras.applications.densenet import decode_predictions
    preprocessing_function = preprocess_input
    base_model = DenseNet169()
    image = load_img('soccer.jpeg', target_size=(224, 224))
elif args.model == "DenseNet201":
    from keras.applications.densenet import preprocess_input
    from keras.applications.densenet import decode_predictions
    preprocessing_function = preprocess_input
    base_model = DenseNet201()
    image = load_img('soccer.jpeg', target_size=(224, 224))
elif args.model == "NASNetLarge":
    from keras.applications.nasnet import preprocess_input
    from keras.applications.nasnet import decode_predictions
    preprocessing_function = preprocess_input
    base_model = NASNetLarge()
    image = load_img('soccer.jpeg', target_size=(224, 224))
elif args.model == "NASNetMobile":
    from keras.applications.nasnet import preprocess_input
    from keras.applications.nasnet import decode_predictions
    preprocessing_function = preprocess_input
    base_model = NASNetMobile()
    image = load_img('soccer.jpeg', target_size=(224, 224))
else:
    ValueError("The model you requested is not supported in Keras")
    
base_model.summary()
    
# convert the image pixels to a numpy array
image = img_to_array(image)
# reshape data for the model
image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
# prepare the image for the VGG model
image = preprocess_input(image)
# predict the probability across all output classes
yhat = base_model.predict(image)
# convert the probabilities to class labels
label = decode_predictions(yhat)
# retrieve the most likely result, e.g. highest probability
label = label[0][0]
# print the classification
print('%s (%.2f%%)' % (label[1], label[2]*100))