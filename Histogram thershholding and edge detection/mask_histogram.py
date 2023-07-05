import cv2
import numpy as np
from matplotlib import pyplot 

image = cv2.imread('image1.jpg')

b=np.zeros(image.shape[:2],dtype=np.uint8)

m=cv2.rectangle(b, (244, 244), (444, 444), 255, -1)

image=cv2.bitwise_and(image,image,mask=m)

rc= image[:, :,2]
gc = image[:, :,1]
bc = image[:, :,0]

rh, p = np.histogram(rc.flatten(), bins=256,)
gh, p = np.histogram(gc.flatten(), bins=256, )
bh, p = np.histogram(bc.flatten(), bins=256,)

pyplot.xlabel('Intensity')
pyplot.ylabel('pixels')
pyplot.plot(bh ,color='blue')
pyplot.plot(rh, color='red' )
pyplot.plot(gh, color='green')
pyplot.show()
