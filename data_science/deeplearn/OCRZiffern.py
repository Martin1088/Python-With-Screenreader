import numpy as np
import tensorflow as tf
from keras.datasets import mnist
from matplotlib import pyplot
from tensorflow import keras

(x_train, y_train), (x_test, y_test) = mnist.load_data()
print("Shape X_train: ", x_train.shape)

pyplot.imshow(x_test[1], cmap='gray_r')
## pyplot.show()

# Konvertiere die Pixelwerte in ASCII-Art
ascii_art = ''
for row in x_test[1]:
    for pixel in row:
        ascii_art += '#' if pixel > 127 else ' '
    ascii_art += '\n'

# Anzeigen der ASCII-Art
print(ascii_art)

## flatting
image_size=28*28
x_train = x_train.reshape(x_train.shape[0], image_size)
x_train = x_train.astype('float32')
x_train /= 255
print("Shape X_train: ", x_train.shape)
x_test = x_test.reshape(x_test.shape[0], image_size)
x_test = x_test.astype('float32')
x_test /= 255
print("Shape X_test: ", x_test.shape)

## Labels
print("Labes: ", x_train[0])
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)
print("Labes: ", x_train[0])
from keras.models import Sequential
model = Sequential()
from keras.layers import Dense
model.add(Dense(units=512, activation='relu',input_shape=(image_size,)))
model.add(Dense(units=512, activation='relu'))
model.add(Dense(units=10, activation='softmax'))
model.summary()

## trainieren des Modells
model.compile(loss='categorical_crossentropy', 
              optimizer='sgd', 
              metrics=['accuracy'])

training = model.fit(x_train,
                    y_train,
                    epochs=10,
                    verbose=True,
                    validation_split=.01)
## Evaluieren 
model.evaluate(x=x_test, y=y_test)

model.save('OCR_Ziffern')