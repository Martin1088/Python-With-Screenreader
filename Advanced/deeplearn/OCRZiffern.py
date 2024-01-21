import numpy as np
import tensorflow as tf
from keras.datasets import mnist
from matplotlib import pyplot
from tensorflow import keras

(x_train, y_train), (x_test, y_test) = mnist.load_data()
print("Shape X_train: ", x_train.shape)
