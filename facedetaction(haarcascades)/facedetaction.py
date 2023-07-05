import cv2
import numpy as np
from matplotlib import pyplot 

image = cv2.imread('image2.jpg')

g=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


haar_cascade = cv2.CascadeClassifier('haarcascades.xml')

faces_rect = haar_cascade.detectMultiScale(g, scaleFactor=1.2, minNeighbors=6)

print("Number of faces :")
print(len(faces_rect))

for (a,b,c,d) in faces_rect:
    cv2.rectangle(image, (a,b), (a+c,b+d), (0,255,0), thickness=2)

cv2.imshow('', image)


cv2.waitKey(0)
cv2.destroyAllWindows()