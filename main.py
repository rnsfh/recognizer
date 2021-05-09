from PIL import Image
from os import path
import sys
import numpy as np

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


# pushing some garbage lol
# roflmao