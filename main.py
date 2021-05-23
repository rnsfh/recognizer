from PIL import Image
from os import path
import sys
import numpy as np
import keras

if not path.exists('test_gray.png'):
  if not path.exists('test.jpg'):
    print("privide source image")
    sys.exit()
  img = Image.open('test.jpg').convert('L')
  img.save('test_gray.png')
  img.show()


from matplotlib import image, pyplot
image = image.imread('test_gray.png')
print(image.dtype)
print(image.shape)

pyplot.imshow(image, cmap='gray')#, interpolation='lanczos')
pyplot.show()

## 2 (Conv + MaxPooling) -> 3 Hidden layers -- loss 0.1406 accuracy 0.9720

## resize image to width, height constant size
## maybe do some interpolation ((maybe))

## convolution + maxpooling
## convolution + maxpooling

## some hidden layers idk how many

## output in multiple nodes ((?))


# still doing scripts lOl
# still...DOING...gargagsaewqwцйцqwdqwdqwdqwdqwdqdq

model = keras.Sequential(
        [
            ## convolutional layer
            layers.Conv2D(16, (3, 3), activation="relu", input_shape = (30, 30, 3), name = "conv1"),
            layers.MaxPooling2D(pool_size = (2, 2), name = "maxpol1"),
            layers.Conv2D(64, (3, 3), activation="relu", name = "conv2"),
            layers.MaxPooling2D(pool_size = (2, 2), name = "maxpol2"),
            layers.Conv2D(64, (3, 3), activation="relu", name = "conv3"),
            layers.MaxPooling2D((2, 2), name = "maxpol3"),

            ## flatten dimensions
            layers.Flatten(),

            ## dense 1-D layers
            layers.Dense(1028, activation = "relu", name = "layer1"),
            layers.Dropout(0.3),
            layers.Dense(512, activation = "relu", name = "layer2"),
            layers.Dropout(0.2),
            layers.Dense(256, activation = "relu", name = "layer3"),

            ## output layer
            layers.Dense(NUM_CATEGORIES, activation = "softmax", name = "output")
            #layers.Dense(NUM_CATEGORIES, activation = "relu", name = "outputlayer")
        ]
    )
model.compile(optimizer='adam',
    loss="categorical_crossentropy", #use this because get some error "logits and labels must have the same first
                                    # dimension, got logits shape [32,3] and labels shape [96]"
    #loss = keras.losses.SparseCategoricalCrossentropy(),
    metrics=['accuracy']
)
# model.compile(
#     optimizer=keras.optimizers.RMSprop(),  # Optimizer
#     # Loss function to minimize
#     loss=keras.losses.SparseCategoricalCrossentropy(),
#     # List of metrics to monitor
#     metrics=[keras.metrics.SparseCategoricalAccuracy()],
# )

