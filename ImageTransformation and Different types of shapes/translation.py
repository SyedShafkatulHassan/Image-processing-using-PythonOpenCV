import cv2
import numpy as np

image = cv2.imread('image.jpg')

change_sized_image = cv2.resize(image, (500, 500))

image_traslated = cv2.warpAffine(change_sized_image, np.float32([[1, 0, 400], [0, 1, 200]]), (image.shape[1], image.shape[0]))

cv2.imshow('image_traslated',image_traslated)

cv2.waitKey(0)