import cv2
Image = cv2.imread('image.jpg')
change_sized_image = cv2.resize(Image, (700, 700))
cv2.imshow('image', change_sized_image)

gb=cv2.GaussianBlur(change_sized_image,(5,5),0)

cv2.imshow('Gaussian blur', gb)

cv2.waitKey(0)
