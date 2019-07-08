import cv2
from skimage import io
import skimage.draw


image = skimage.io.imread("/home/jhwang/Documents/test/10.JPG")
#image = skimage.io.imread("/home/jhwang/Documents/dataset/val/4.JPG")
print(image.shape)
print(image.size)

