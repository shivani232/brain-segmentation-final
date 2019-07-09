from PIL import Image
import numpy as np
import cv2
from matplotlib import pyplot as plt
import PIL





#-------------------MEDIAN FILTER------------------------------- 



path = "b4.jpg" # Your image pa v th 
img = Image.open(path)
members = [(0,0)] * 9
# print img.width
newimg = Image.new("RGB",(img.width,img.height),"white")
for i in range(1,img.width-1):
    for j in range(1,img.height-1):
        members[0] = img.getpixel((i-1,j-1))
        members[1] = img.getpixel((i-1,j))
        members[2] = img.getpixel((i-1,j+1))
        members[3] = img.getpixel((i,j-1))
        members[4] = img.getpixel((i,j))
        members[5] = img.getpixel((i,j+1))
        members[6] = img.getpixel((i+1,j-1))
        members[7] = img.getpixel((i+1,j))
        members[8] = img.getpixel((i+1,j+1))
        members.sort()
        newimg.putpixel((i,j),(members[4]))
newimg.save('denoised.jpg')



#------------------Segmentation------------


img = cv2.imread('denoised.jpg')
Z = img.reshape((-1,3))

# convert to np.float32
Z = np.float32(Z)


#histogram calculation
hist = cv2.calcHist([img],[0],None,[256],[0,256])


plt.hist(img.ravel(),256,[0,256])
plt.show()

no_clusters = int(raw_input("Enter the no. of clusters: "))



# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = no_clusters
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))
output = PIL.Image.fromarray(res2)
output.save('segmented.jpg')
#segmented_output.save('after_segmentation.jpg')


#cv2.imshow('res2',res2)
#cv2.waitKey(0)


#-----------------thresholding:


img = cv2.imread('segmented.jpg',0)
print "A"
ret,thresh1 = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
print "B"
output = PIL.Image.fromarray(thresh1)
output.save('after_thresholding.jpg')
print "C"
# plt.imshow(thresh1,'gray')
# plt.show()