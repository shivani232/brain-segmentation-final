import cv2
import PIL
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('after_segmentation.jpg',0)
ret,thresh1 = cv2.threshold(img,150,255,cv2.THRESH_BINARY)

output = PIL.Image.fromarray(thresh1)
output.save('after_thresholding.jpg')
plt.imshow(thresh1,'gray')
plt.show()