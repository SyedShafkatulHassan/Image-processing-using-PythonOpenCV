import cv2
import numpy as np
from matplotlib import pyplot 

image = cv2.imread('image1.jpg')

g=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# here p will be 150
p, t = cv2.threshold(g, 150, 205, cv2.THRESH_BINARY)
cv2.imshow('', t)

cv2.waitKey(0)
cv2.destroyAllWindows()