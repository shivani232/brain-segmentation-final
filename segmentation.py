import numpy as np
import cv2
from matplotlib import pyplot as plt
import PIL

img = cv2.imread('brain2.jpg')
Z = img.reshape((-1,3))

# convert to np.float32
Z = np.float32(Z)


#histogram calculation
hist = cv2.calcHist([img],[0],None,[256],[0,256])


plt.hist(img.ravel(),256,[0,256])
# plt.show()


# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 4
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))
output = PIL.Image.fromarray(res2)
output.save('after_segmentation.jpg')
#segmented_output.save('after_segmentation.jpg')


cv2.imshow('res2',res2)
cv2.waitKey(0)
#cv2.destroyAllWindows()


#thresholding:

# ret,thresh1 = cv2.threshold(res2,127,255,cv2.THRESH_BINARY)
# print "1"
# plt.imshow(thresh1,'gray')
# print "2"
# plt.show()

