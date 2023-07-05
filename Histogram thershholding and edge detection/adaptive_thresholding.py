import cv2
import numpy as np
from matplotlib import pyplot 

image = cv2.imread('image1.jpg')

g=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

a= cv2.adaptiveThreshold(g, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 9)
cv2.imshow('Adaptive Thresholding', a)

cv2.waitKey(0)
cv2.destroyAllWindows()