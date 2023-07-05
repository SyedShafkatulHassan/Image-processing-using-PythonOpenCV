import cv2
import numpy as np
from matplotlib import pyplot 

image = cv2.imread('image1.jpg')

g=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

l = cv2.Laplacian(g, cv2.CV_64F)
l = np.uint8(np.absolute(l))
cv2.imshow('', l)



cv2.waitKey(0)
cv2.destroyAllWindows()