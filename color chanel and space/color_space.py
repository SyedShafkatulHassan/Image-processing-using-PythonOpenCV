import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread('image.jpg')

change_sized_image = cv2.resize(image, (700, 700))

cv2.imshow('change_sized_image',change_sized_image)
cv2.waitKey(0)

hsv_color=cv2.cvtColor(change_sized_image,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV',hsv_color)
cv2.waitKey(0)

grey_color=cv2.cvtColor(change_sized_image,cv2.COLOR_BGR2GRAY)
cv2.imshow('grey',grey_color)
cv2.waitKey(0)

lab_color=cv2.cvtColor(change_sized_image ,cv2.COLOR_BGR2Lab)
cv2.imshow('Lab',lab_color)
cv2.waitKey(0)


rgb_color=cv2.cvtColor(change_sized_image,cv2.COLOR_BGR2RGB)
plt.imshow(rgb_color)
plt.show() 
cv2.waitKey(0)
