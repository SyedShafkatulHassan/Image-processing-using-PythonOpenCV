import cv2
import numpy as np
from matplotlib import pyplot 

image = cv2.imread('image1.jpg')

g=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
h=cv2.calcHist([g],[0],None,[256],[0,256])

pyplot.xlabel('Intensity')
pyplot.ylabel('pixels')
pyplot.plot(h)
pyplot.show()

# cv2.imshow('',g)
# cv2.waitKey(0)
