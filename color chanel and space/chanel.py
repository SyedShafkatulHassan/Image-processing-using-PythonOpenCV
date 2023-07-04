import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread('image.jpg')

change_sized_image = cv2.resize(image, (700, 700))

blue,green,read=cv2.split(change_sized_image)

cv2.imshow('image Blue',blue)
cv2.imshow('image green',green)
cv2.imshow('image red',read)

a=a = np.zeros_like(blue)  
blueish=cv2.merge((blue,a,a))
cv2.imshow('Blueish',blueish)

b=b = np.zeros_like(read)  
readish=cv2.merge((b,b,read))
cv2.imshow('readish',readish)

cv2.waitKey(0)