
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from tensorflow.keras.applications import imagenet_utils
import os
import tensorflowjs as tfjs
#import keras
#%matplotlib inline

mobile = tf.keras.applications.mobilenet.MobileNet()
tf.saved_model.save(mobile, "MobileNet_Saved_Model/")

##convert to tensorflowjs on command line
##(mainEnv) C:\Users\bclar>tensorflowjs_converter --input_format=tf_saved_model projects\TensorFlowJS\MobileNet_Saved_Model projects\TensorFlowJS\



