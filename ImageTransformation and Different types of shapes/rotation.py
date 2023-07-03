import cv2
import numpy as np

image = cv2.imread('image.jpg')

change_sized_image = cv2.resize(image, (500, 500))

# image. shape[:2] By using 2 I am only taking width and height from here and avoiding channel

height,width = change_sized_image.shape[:2] 

# rotation from center

rotated_image = cv2.warpAffine(change_sized_image, cv2.getRotationMatrix2D((width/2, height/2), 90, 1), (width, height))

cv2.imshow('image_traslated',rotated_image)

cv2.waitKey(0)