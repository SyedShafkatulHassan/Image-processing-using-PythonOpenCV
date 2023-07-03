import cv2
import numpy as np

image = cv2.imread('image.jpg')

change_sized_image = cv2.resize(image, (500, 500))

cv2.imshow('image_traslated',cv2.flip(change_sized_image,1))

cv2.waitKey(0)