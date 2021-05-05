from PIL import Image
from os import path
import sys

if not path.exists('test_gray.png'):
  if not path.exists('test.jpg'):
    print("privide source image")
    sys.exit()
  img = Image.open('test.jpg').convert('LA')
  img.save('test_gray.png')
  img.show()

